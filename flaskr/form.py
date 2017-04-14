from wtforms import Form, StringField, SubmitField, PasswordField, BooleanField
from wtforms.validators import Email, Length, DataRequired


class LoginForm(Form):
    email = StringField(u'邮箱', validators=[DataRequired(), Email(), Length(1, 64)])
    password = PasswordField(u'密码', validators=[DataRequired()])
    remember_me = BooleanField(u"记住")
    submit = SubmitField(u'登录')
