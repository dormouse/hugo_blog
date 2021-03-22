---
title: "Make a blog with Flask"
date: 2017-02-09
lastmod: 2017-02-09
tags: ["flask","blog"]
categories: ["development"]
slug: "make-a-blog-with-flask"
description: "let start a blog with Flask."
---



Init
----

Fisst create a new repository which name "flask\_site" on github. Then
git clone to loacl. Init the env:

    $ cd flask_site
    $ mkvirtualenv -p python3 flask_site 
    $ pip install flask
    $ pip install flask-login
    $ pip install flask-openid
    $ pip install flask-mail
    $ pip install flask-sqlalchemy
    $ pip install sqlalchemy-migrate
    $ pip install flask-whooshalchemy
    $ pip install flask-wtf
    $ pip install flask-babel
    $ pip install guess_language
    $ pip install flipflop
    $ pip install coverage

Hello World
-----------

    $ mkdir blog
    $ cd blog
    $ mkdir app
    $ mkdir app/static
    $ mkdir app/templates
    $ mkdir tmp

`blog/app/__init__.py`:

    from flask import Flask

    app = Flask(__name__)
    from app import views

`blog/app/views.py`:

    from app import app

    @app.route('/')
    @app.route('/index')
    def index():
        return "Hello, World!"

`blog/run.py`:

    from app import app
    app.run(debug=True)

Get into blog path, use `python run.py` to run the dev serve. "Hello
world" with show in `127.0.0.1:5000`.

Use template
------------

Change views.py:

    from flask import render_template
    from app import app

    @app.route('/')
    @app.route('/index')
    def index():
        blog_title = 'Awsome Blog'  # fake blog title
        posts = [  # fake array of posts
            { 
                'title': 'First blog', 
                'content': 'This is my first blog!' 
            },
            { 
                'title': 'Second blog', 
                'content': 'Second blog for flask blog.' 
            }
        ]
        return render_template("index.html",
                               blog_title=blog_title,
                               posts=posts)                               

Create `blog/app/templates/base.html`:

    <html>

    <head>
    {% if blog_title %}
        <title>{{ blog_title }} - flaskblog</title>
    {% else %}
        <title>Welcome to flaskblog</title>
    {% endif %}
    </head>

    <body>
    {% block body %}{% endblock %}
    </body>

    </html>

Create `blog/app/templates/index.html`:

    {% extends "base.html" %}
    {% block body%}
        {% for post in posts %}
        <div>
            <h1>{{ post.title}}</h1>
            <p>{{ post.content}}</p>
        </div>
        {% endfor %}
    {% endblock %}
