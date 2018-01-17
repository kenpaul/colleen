# RThis is te workhorse code for this app. We import some tools and then
# set up some functions to handle specific URL's. These functions are also
# know as "view functions"


from flask import render_template, flash, redirect, url_for
from app_pkg import app
from app_pkg.forms import LoginForm

# If the web URL matches either of these two then we'll set up
# some variables and pass them as args to the index.html URL to
# be processed and rendered back to users browser.
#
# Note that although we could have written the HTML in these view functions it
# is easier to manage if we state that externally in its own index.html file
# otherwise referred to as a template (and processed by render_template)
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

# Here's another view function with some extra logic.
@app.route('/login', methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(form.username.data, form.remember_me.data))
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)
