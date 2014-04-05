Calculator
==========

Ascentio test

Requirements:
------------

Requirements were not clearly defined. Several assumptions were made in order to keep things simple, extendable, easy to maintain and easy to use.
I did not make requirements refinement because it will take us longer than expected and it was consider outside the scope of this exercise.

Architecture:
------------

Languaje: Python
Web framework: Django
Math parser/engine: sympy
Rest API framework: django-tastypie

Development methodology: TDD (Test Driven Development)
Code style: PEP-8

I try to use libraries as much as possible instead of developing custom code for problem like this. Math parsing is not a minor problem and is really important to keep a maintainable code.


Installation
------------

 Requirements:
  - pip
  - Virtualenv wrapper
  - git

 1. Clone repository
     $ cd calculator
 2. Create virtual environments
     $ mkvirtualenv calculator
 3. Load requirements
     $ pip install -r requirements.txt
 4. Create sqlite3 database and a superuser with:
     $ python manage.py syncdb
 5. Run tests:
     $ python manage.py test solve
 6. Run server
     $ python manage.py runserver
 7. Visit page with your browser:
     http://localhost:8000/


Using the calculator:
---------------------

 To use the calculator you should be logged in.

 Commands:
  * help (will list the list of available commands)
  * load <session_name> (will list all the commands stored in a session)
  * save <session_name> (will save all the commands not saved in a session)
  * Enter a equation to be solved

Operations supported:
 * addition ( <exp> + <exp> )
 * subtraction ( <exp> - <exp> )
 * multiplication ( <exp> * <exp> )
 * division  ( <exp> / <exp> )
 * logarithm ( log(<exp>)  )


Next Steps:
-----------

 * Add functional tests
 * Add code and general documentation
 * Manual tests
 * Bug fixing
 * Client Demo
