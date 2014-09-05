# Alamo City Python Group Intro&nbsp;to&nbsp;Django

---

# About Me

Douglas Mendizabal

* GitHub - [https://github.com/dmend](https://github.com/dmend)

* CloudKeep - [https://github.com/cloudkeep](https://github.com/cloudkeep)

---

# Web Development

HTML + CSS + JavaScript = Magic!

## Tools

* Chrome Developer Tools
* Firebug for Firefox - [http://getfirebug.com/](http://getfirebug.com/)

---

# Django

“Django is a high-level Python Web Framework that encourages rapid development and clean, pragmatic design.”

* [https://www.djangoproject.com/](https://www.djangoproject.com/)

## It’s not MVC, it’s…
![MTV](http://i.imgur.com/sOr5T5w.png)

* Models
* Templates (Views)
* Views (Controllers)

---

# Django

## “Elegant URL design”
*  Uses regular expressions for url matching

## Built-in ORM
* SQL: Postgres, MySQL, SQLite, etc.

## Everything AND the Kitchen Sink!
* Admin Interface
* Authentication
* Development Web Server

---

# Request Handling

![Django Flow](http://i.imgur.com/Lh1H9tZ.jpg)

---

# Request Handling

* Request is handled by the server
* Django URL configuration routes the request to the view
* View renders the response

Can be extended with Middleware

* Authentication/Authorization
* Caching
* CSRF protection

---

# URLConf

* [Cool URIs don’t change!](http://www.w3.org/Provider/Style/URI.html)
* Uses Regular Expressions for URL matching
* You can pass regex groups as parameters to your view

		!python
		urlpatterns = patterns('',
		    url(r'^home/$', 'app.views.home'),
		    (r'^book/(?P<book_id>\d{5})/$', 
		     'books.views.book_detail'),
		)

---

# Models

* Each model is a Python class that subclasses django.db.models.Model
* Each attribute of the model represents a database field

        !python
		from django.db import models

		class Book(models.Model):
		    title = models.CharField(max_length=256)
		    release_date = models.DateField()

---

# Django ORM

* Using ORM

        !python
        >>> b = Book(title='How to Avoid Huge Ships.')
        >>> b.save()
		>>> Book.objects.create(title=foo)
		>>> Book.objects.all()
		[<Book: Book object>, <Book: Book object>]

		>>> Book.objects.get(pk=1)
		<Book: Book object>

		>>> Book.objects.filter(title__contains='query')

---

# Security - SQL Injection

* By using the Django ORM you get protection from SQL Injection for free!
* Values sent to the ORM are escaped based on your database backend
* You can execute raw SQL if you need to

		!python
		>>> Book.objects.raw('SELECT * FROM myapp_book')

---

# View Functions

* A view is a Python function that takes a Web request and returns a Web response

		!python
		def my_view(request):
		    # ...
		    if foo:
		        return HttpResponse('<h1>Page found!</h1>')
		    else:
		        return HttpResponseNotFound('<h1>Page not found</h1>')

---

# View Functions

* Views define which data you see, not how you see it

		!python
		def book_detail(request, book_id):
		    try:
		        p = Book.objects.get(pk=book_id)
		    except Book.DoesNotExist:
		        raise Http404
		    return render_to_response('detail.html', 
		                              {'book': b})

---

# Templates

* Django’s template engine provides a powerful mini-language for defining the user-facing layer of your application

		!html
		<!DOCTYPE html>
		<html>
		<head>
			<title>Future time</title>
		</head>
		<body>
		    <h1>{{ book.title }}</h1>
		    <p>Released on  {{ book.release_date }}.</p>
		</body>
		</html> 
Not limited to HTML

---

# Templates

* Templates are reusable

		!python
		{% extends "base.html" %} 

		{% block title %}
		The current time
		{% endblock %} 

		{% block content %} 
		<p>It is now {{ current_date }}.</p> 
		{% endblock %}

---

# Security - Cross Site Scripting (XSS)

* All variables output by the template engine are escaped 
* Django provides a ‘safe’ filter to bypass protection if you need to

		!python
		{{ name|safe }}

![XSS](http://i.imgur.com/iJ3Er.jpg)

---

# Security - Cross Site Request Forgery

* Easy to use
* Not on by default
* Add the middleware

		!python
		'django.middleware.csrf.CsrfViewMiddleware'

* In any template that uses a POST form use 
		
		!python
		<form action="." method="post">
			{% csrf_token %}

* In the corresponding view functions, ensure that the csrf context processor is being used.  One way of doing this is using RequestContext
		
		!python
		def view(request):
		    #...
		    return render_to_response('book.html', {'book': book},
		                            context_instance=RequestContext(request))

---

# Questions?