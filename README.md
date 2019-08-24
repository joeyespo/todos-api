TODOs API
=========

[![Deploy to Heroku](https://www.herokucdn.com/deploy/button.png)](https://heroku.com/deploy)


Setup
-----

Initialize the database

```console
$ python manage.py migrate
```

*Optional* Enable `DEBUG` mode

```console
$ echo DEBUG=True > .env
```

*Optional* Create a superuser for admin access

```console
$ python manage.py createsuperuser
```


Run
---

```console
$ python manage.py runserver
```

Now visit [http://localhost:8000/](http://localhost:8000/) to see the app.

Note: If you created a superuser above, you can also access the admin pages
at [http://localhost:8000/admin](http://localhost:8000/admin).


Test
----

```console
$ python manage.py test
```


Deploy
------

```console
$ git push heroku origin
```
