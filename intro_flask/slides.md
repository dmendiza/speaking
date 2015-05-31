# Intro to Flask

---

# Flask

* Web microframework
* Uses jinja for templating
* Built-in development server

---

# Webdev Primer

* Request/Response model
* Parsing URLs
    * https://www.example.com/path/to/some/file.html

---

# Hello World

    !python
    from flask import Flask
    app = Flask(__name__)

    @app.route('/')
    def hello_world():
        return 'Hello World!'

    if __name__ == '__main__':
        app.run()

---

# Flask app
* WSGI app
* Debugger

        !python
        app.debug = True
        app.run()

        app.run(debug=True)

---

# Simple Routing

    !python
    @app.route('/')
    def index():
        return 'Index Page'

    @app.route('/hello')
    def hello():
        return 'Hello World'

---

# Routing with Variables

    !python
    @app.route('/user/<username>')
    def show_user_profile(username):
        # show the user profile for that user
        return 'User %s' % username

---

# Routing with Converters

    !python
    @app.route('/post/<int:post_id>')
    def show_post(post_id):
        # show the post with the given id, the id is an integer
        return 'Post %d' % post_id

* int
* float
* path

---

# Routing Gotcha: Redirection

    !python
    @app.route('/projects/')
    def projects():
        return 'The project page'

    @app.route('/about')
    def about():
        return 'The about page'

* Trailing slash redirects
* Non-trailing slash 404s

---

# URL Building

    !python
    >>> from Flask import url_for

    >>> print url_for('show_user_profile', username='John Doe')
    /user/John%20Doe

---

# HTTP Methods

* GET
    - request a page
* POST
    - submit a form

* HEAD, PUT, DELETE, HEAD, OPTIONS

---

# Static Files

    !python
    url_for('static', filename='style.css')


---

# Rendering Templates

    !python
    from flask import render_template

    @app.route('/hello/')
    @app.route('/hello/<name>')
    def hello(name=None):
        return render_template('hello.html', name=name)
---

# Jinja

    !html
    <!doctype html>
    <html>
    <head>
        <title>Hello from Flask</title>
    </head>
    <body>
    {% if name %}
      <h1>Hello {{ name }}!</h1>
    {% else %}
      <h1>Hello World!</h1>
    {% endif %}
    </body>
    </html>

---

# Template Inheritance

    !html
    <!doctype html>
    <html>
    <head>
    {% block head %}
        <link rel="stylesheet" 
              href="{{ url_for('static', filename='style.css') }}">
        <title>{% block title %}{% endblock %} - My Webpage</title>
    {% endblock %}
    </head>
    <body>
        <div id="content">{% block content %}{% endblock %}</div>
        <div id="footer">
        {% block footer %}
        &copy; Copyright 2010 by <a href="http://domain.invalid/">you</a>.
        {% endblock %}
        </div>
    </body>
    </html>

---

# Template Inheritance

    !html
    {% extends "layout.html" %}
    {% block title %}Index{% endblock %}
    {% block head %}
        {{ super() }}
        <style type="text/css">
            .important { color: #336699; }
        </style>
    {% endblock %}
    {% block content %}
    <h1>Index</h1>
    <p class="important">
        Welcome on my awesome homepage.
    {% endblock %}

---

# Request Object

    !python
    @app.route('/login', methods=['POST', 'GET'])
    def login():
        error = None
        if request.method == 'POST':
            if valid_login(request.form['username'],
                           request.form['password']):
                return log_the_user_in(request.form['username'])
            else:
                error = 'Invalid username/password'
        # the code below is executed if the request method
        # was GET or the credentials were invalid
        return render_template('login.html', error=error)

---

# Fake request

    !python
    from flask import request

    with app.test_request_context('/hello', method='POST'):
        # now you can do something with the request until the
        # end of the with block, such as basic assertions:
        assert request.path == '/hello'
        assert request.method == 'POST'

---

# Response Object

    !python
    @app.errorhandler(404)
    def not_found(error):
        resp = make_response(render_template('error.html'), 404)
        resp.headers['X-Something'] = 'A value'
        return resp

---

# Redirection and Errors

    !python
    from flask import abort, redirect, url_for

    @app.route('/')
    def index():
        return redirect(url_for('login'))

    @app.route('/login')
    def login():
        abort(401)
        this_is_never_executed()

---

# Customizing Error Pages

    !python
    from flask import render_template

    @app.errorhandler(404)
    def page_not_found(error):
        return render_template('page_not_found.html'), 404

---

# Sessions

    !python
    from flask import Flask, session, redirect, url_for, escape, request

    app = Flask(__name__)

    @app.route('/')
    def index():
        if 'username' in session:
            return 'Logged in as %s' % escape(session['username'])
        return 'You are not logged in'

    @app.route('/login', methods=['GET', 'POST'])
    def login():
        if request.method == 'POST':
            session['username'] = request.form['username']
            return redirect(url_for('index'))
        return '''<form action="" method="post">
                  <p><input type=text name=username>
                  <p><input type=submit value=Login>
                  </form>'''
---

# Sessions

    !python
    @app.route('/logout')
    def logout():
        # remove the username from the session if it's there
        session.pop('username', None)
        return redirect(url_for('index'))

    # set the secret key.  keep this really secret:
    app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'

---

# What's next?

* Database Storage
* File Uploads
* Testing
* Deployment
