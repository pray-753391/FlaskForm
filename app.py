from flask import Flask, render_template, flash, redirect, url_for
from flask import Markup
app = Flask(__name__)
app.secret_key = 'secret string'
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

@app.errorhandler(404)
def page_not_found(e):
	return render_template('errors/404.html'),404


if __name__ == '__main__':
    app.run()
