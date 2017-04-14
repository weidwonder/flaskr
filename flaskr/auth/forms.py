from flask_wtf import Form
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import Email, Length, DataRequired, ValidationError

from flaskr.auth.services import user_service


class LoginForm(Form):
    """
    登陆Form
    """
    username = StringField('邮箱', validators=[DataRequired(), Length(1, 64)])
    password = PasswordField('密码', validators=[DataRequired()])
    submit = SubmitField('登录')

    def validate(self):
        self.user = user_service.authenticate(self._fields['username'], self._fields['password'])
        if self.user:
            return super(LoginForm, self).validate()
        else:
            raise ValidationError('用户名密码错误')

    def get_user(self):
        return self.user


class RegisterForm(Form):
    """
    注册form
    """
    username = StringField('用户名', validators=[DataRequired(), Length(1, 32)])
    password = PasswordField('密码', validators=[DataRequired()])
    email = StringField('邮箱', validators=[DataRequired(), Email(), Length(1, 64)])
    describe = StringField('自我陈述', default='')
    submit = SubmitField('登录')

    def validate_username(self, field):
        conflicted_user = user_service.get_by_username(field.data)
        if conflicted_user:
            raise ValidationError('该用户名已经被注册')

    def validate_email(self, field):
        conflicted_user = user_service.get_by_email(field.data)
        if conflicted_user:
            raise ValidationError('该邮箱已经被注册')
