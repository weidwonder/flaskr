import string

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import Email, Length, DataRequired, ValidationError

from flaskr.auth.services import user_service


class LoginForm(FlaskForm):
    """
    登陆Form
    """
    username = StringField('邮箱', validators=[DataRequired(), Length(1, 64)])
    password = PasswordField('密码', validators=[DataRequired()])
    submit = SubmitField('登录')

    def validate(self):
        rv = FlaskForm.validate(self)
        if not rv:
            return False
        self.user = user_service.authenticate(self._fields['username'].data, self._fields['password'].data)
        if self.user:
            return True
        else:
            self.password.errors.append('用户名密码错误')
            return False

    def get_user(self):
        return self.user


class RegisterForm(FlaskForm):
    """
    注册form
    """
    username = StringField('用户名', validators=[DataRequired(), Length(1, 32)])
    password = PasswordField('密码', validators=[DataRequired()])
    email = StringField('邮箱', validators=[DataRequired(), Email(), Length(1, 64)])
    description = StringField('自我陈述', default='', validators=[Length(0, 1024)])
    submit = SubmitField('注册')

    def validate_username(self, field):
        conflicted_user = user_service.get_by_username(field.data)
        if conflicted_user:
            raise ValidationError('该用户名已经被注册')

    def validate_email(self, field):
        conflicted_user = user_service.get_by_email(field.data)
        if conflicted_user:
            raise ValidationError('该邮箱已经被注册')

    def validate_password(self, field):
        password = field.data
        contain_lowercase = False
        contain_uppercase = False
        contain_numbers = False
        for char in password:
            if char in string.ascii_lowercase:
                contain_lowercase = True
            if char in string.ascii_uppercase:
                contain_uppercase = True
            if char in string.digits:
                contain_numbers = True
        if not all((contain_numbers, contain_uppercase, contain_lowercase)):
            raise ValidationError('密码必须包含大写字母， 小写字母和数字')
