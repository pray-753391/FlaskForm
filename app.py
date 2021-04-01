from flask import Flask, render_template, flash, redirect, url_for, send_from_directory
from flask import Markup
from flask_ckeditor import random_filename

from form import LoginForm,UploadForm
import os
app = Flask(__name__)
app.secret_key = 'secret string'
#要在项目根目录下手动创建uploads文件夹，用于保存上传后的文件
app.config['UPLOAD_PATH'] = os.path.join(app.root_path,'uploads')
user = {
	'username': 'Grey Li',
	'bio': 'A boy who loves movies and music.',
}
movies = [
	{'name': 'My Neighbor Totoro', 'year': '1988'},
	{'name': 'Three Colours trilogy', 'year': '1993'},
	{'name': 'Forrest Gump', 'year': '1994'},
	{'name': 'Perfect Blue', 'year': '1997'},
	{'name': 'The Matrix', 'year': '1999'},
	{'name': 'Memento', 'year': '2000'},
	{'name': 'The Bucket list', 'year': '2007'},
	{'name': 'Black Swan', 'year': '2010'},
	{'name': 'Gone Girl', 'year': '2014'},
	{'name': 'CoCo', 'year': '2017'},
]

def baz(n):
    if n == 'baz':
        return True
    return False
app.jinja_env.tests['baz'] = baz

def bar():
	return 'I am bar.'
foo = 'I am foo.'
app.jinja_env.globals['bar'] = bar
app.jinja_env.globals['foo'] = foo

@app.template_filter()
def musical(s):
    return s+Markup(' &#9835; ')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/watchlist')
def watchlist():
    return render_template('watchlist.html',user=user,movies=movies)

@app.route('/flash')
def just_flash():
	flash('I am flash,who is looking for me')
	return 'aaaa'

@app.route('/html')
def pure():
	return render_template('pure.html')

@app.route('/basic',methods=['GET','POST'])
def basic():
	form = LoginForm()
	if form.validate_on_submit():
		username = form.username.data
		flash('Welcome %s' %username)
		return redirect(url_for('index'))
	return render_template('basic.html',form=form)

@app.route('/bootstrap')
def bootstrapForm():
	form = LoginForm()
	return render_template('bootstrap.html',form=form)

@app.route('/upload', methods=['GET','POST'])
def upload():
	form = UploadForm()
	if form.validate_on_submit():
		f = form.photo.data
		#生成随机文件名 我们调用这个函数来获取随机文件名，传入原文 件名作为参数
		filename = random_filename(f.filename)
		#保存文件
		f.save(os.path.join(app.config['UPLOAD_PATH'],filename))
		flash('Upload success')
		#session['filenames'] = [filename]
		#return redirect(url_for('show_images'))
		return redirect(url_for('watchlist'))
	return  render_template('upload.html',form=form)
@app.route('/uploads/<path:filename>')
#传入参数filename
def showfile(filename):
	return send_from_directory(app.config['UPLOAD_PATH'], filename)
@app.errorhandler(404)
def page_not_found(e):
	return render_template('errors/404.html'),404


if __name__ == '__main__':
    app.run()
