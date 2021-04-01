from flask_wtf import  FlaskForm
from wtforms import Form, StringField,PasswordField,BooleanField,SubmitField,IntegerField
from wtforms.validators import DataRequired,Length,ValidationError
from flask_wtf.file import FileField, FileRequired, FileAllowed
#表单可以由一个python类表示
class LoginForm(FlaskForm):
    username = StringField('Username',validators=[DataRequired()])
    password = PasswordField('Password',validators=[DataRequired(),Length(8,128)])
    remember = BooleanField('Remember me')
    submit = SubmitField('Log in')
#针对特定字段的验证器
class FortyTowForm(FlaskForm):
    answer = IntegerField('The Number')
    submit = SubmitField()
    def validate_answer(form,field):
        if field.data != 42:
            #raise用来引发异常
            raise  ValidationError('Must be 42')
#上传文件的表单
class UploadForm(FlaskForm):
    #FileRequired是验证是否包含文件对象 FileAllowed用来验证文件类型
    photo = FileField('Upload Image',validators=[FileRequired(),FileAllowed(['jpg','jpeg','png','gif'])])
    submit = SubmitField()
