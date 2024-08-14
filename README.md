## Services

Below is the list of exposed services by this application that can be used

#### Base

Base url: http://127.0.0.1:8000/

#### Categories

[AUTH][GET] -> BaseURL/api/categories/get-list-of-categories <br />

#### Products

[AUTH][GET] -> BaseURL/api/products/get-all-products <br />
[AUTH][POST] -> BaseURL/api/products/create <br />
[AUTH][GET] -> BaseURL/api/products/<int:pk> <br />
[AUTH][PUT] -> BaseURL/api/products/<int:pk>/update <br />
[AUTH][DELETE] -> BaseURL/api/products/<int:pk>/delete <br />

Where <int:pk> is the id of the product <br />

#### Orders

[AUTH][GET] -> BaseURL/api/orders/get-order-list/ <br />
[AUTH][POST] -> BaseURL/api/orders/create-order/ <br />
[AUTH][GET] -> BaseURL/api/orders/user-orders/<int:user_id>/ <br />
[AUTH][POST] -> BaseURL/api/orders/cancel-order/<int:order_id>/ <br />
[AUTH][POST] -> BaseURL/api/orders/pay-order/<int:order_id>/ <br />

#### Auth

[POST] -> BaseURL/api/user-login/ <br />
[POST] -> BaseURL/api/register/ <br />
[AUTH][POST] -> BaseURL/api/update-profile/<int:pk>/ <br />

# Usage

To use this template to start your own project:

### Existing virtualenv

If your project is already in an existing python3 virtualenv first install django by running

    $ pip install django
    
And then run the `django-admin.py` command to start the new project
      
### No virtualenv

This assumes that `python3` is linked to valid installation of python 3 and that `pip` is installed and `pip3`is valid
for installing python 3 packages.

Installing inside virtualenv is recommended, however you can start your project without virtualenv too.

If you don't have django installed for python 3 then run:

    $ pip3 install django restframework django-cors-headers Pillow mysqlclient
        
After that just install the local dependencies, run migrations, and start the server.

# Getting Started

First clone the repository from Github and switch to the new directory:

    $ git clone git@github.com/USERNAME/{{ project_name }}.git
    $ cd {{ project_name }}
    
Activate the virtualenv for your project.

Then simply apply the migrations:

    $ python manage.py makemigrations
    $ python manage.py migrate
    

You can now run the development server:

    $ python manage.py runserver