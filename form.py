from wtforms import Form, StringField,PasswordField,BooleanField,SubmitField
from wtforms.validators import DataRequired,Length
#表单可以由一个python类表示
class LoginForm(Form):
    username = StringField('Username',validators=[DataRequired()])
    password = PasswordField('Password',validators=[DataRequired(),Length(8,128)])
    remember = BooleanField('Remember me')
    submit = SubmitField('Log in')