from flask import render_template, flash, redirect, url_for
from app_pkg import app
from app_pkg.forms import LoginForm

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Kenneth',
            'group':'EA'}
    posts = [
        {
            'author': {'username': 'Srini'},
            'body': 'New release of ScaleIO'
        },
        {
            'author': {'username': 'Dave'},
            'body': 'vSAN 6.3 has bugs'
        }
    ]
    return render_template('index.html', user=user, posts=posts)

@app.route('/login', methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(form.username.data, form.remember_me.data))
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)
