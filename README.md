# Moon Flask

Moon Flask is a simple portfolio web app built on [Flask](http://flask.pocoo.org/). 

The app comes with 'about' and 'contact' pages, and generates additional pages and their navigation links from a database. Moon Flask uses [SQLAlchemy](http://www.sqlalchemy.org/) for database management, [Skeleton CSS](http://getskeleton.com/) for page layout and [Font-Awesome](https://fortawesome.github.io/Font-Awesome/) for social icons.

The app comes with a sample set of content, styles and a sample user, the Early Renaissance painter [Paolo Uccello](https://en.wikipedia.org/wiki/Paolo_Uccello).

<h2>Deploy</h2>
<h4>Clone the Repository</h4>
Make a folder for Moon Flask, then clone the repository into it:

```
$ git clone https://github.com/thuselem/moon-flask
```

<h4>Install Python</h4>
Moon Flask was developed in Python 3.4. I recommend Python 3.4, but the app will also work in Python 2.7.

On Mac OS X and Windows, you may need to install Python 3.4. Ubuntu Linux 14.04 and later come with Python 3.4 installed. 

Check if Python 3.4 is installed. On Mac OS X or Linux:

```
$ python3
```

On Windows, enter the full path of the Python 3.4 executable. This should be:

```
$ C:\Python34\python.exe
```

If Python 3.4 is installed, an interactive shell will open and report Python 3.4. (`exit()` returns you to your command prompt.)

If you do not have Python 3.4, install it now. Installers are available for [Mac OS X](https://www.python.org/downloads/release/python-343/) and [Windows](https://www.python.org/downloads/release/python-343/). Make sure to select the "Add python.exe to Path" on Windows.

<h4>Install Virtualenv</h4>
A virtual environment is a sandbox for a Python application. Any extensions and packages you install to it are isolated, preventing conflicts with your system environment and other virtual environments.

We will use `virtualenv` to create our virtual environment. You can also create your virtual environment using `pyvenv` or `venv` if you prefer.

To install `virtualenv` on Mac OS X:

```
$ sudo easy_install virtualenv
```

On Windows:

```
$ pip install virtualenv
```

Use your package manager on Linux distributions. For example, on Ubuntu:

```
$ sudo apt-get install python-virtualenv
```

<h4>Set up the Virtual Environment</h4>
If Python 3.4 is your only Python installation:

```
$ virtualenv moon-flask
```

If you have more than one version of Python on your system, specify Python 3.4:

```
$ virtualenv -p python3.4 moon-flask
```

On Windows, specify the full path of the executable. With the default Python installation, this will be:

```
$ virtualenv -p C:\Python34\python.exe moon-flask
```

<h4>Install Flask, SQLAlchemy and Flask Extensions</h4>
Next we will install the required packages in the virtual environment. First, activate the virtual environment:

```
$ cd moon-flask
$ source bin/activate
```

On Windows:

```
$ cd moon-flask
$ Scripts\activate
```

Your command line prompt will now start with (moon-flask), indicating the virtual environment is active. Now install the required packages using pip:

```
$ pip install -r requirements.txt
```

<h4>Build the Sample Database</h4>
The `build_db.py` script will build a database for our sample user Paolo Uccello:

```
$ python build_db.py
```

<h4>Set the Environment Variables</h4>
Environment variables must be set for `SECRET_KEY`, `MAIL_USERNAME` and `MAIL_PASSWORD`. These variables can be temporarily set at the command line.

Flask uses `SECRET_KEY` to prevent [cross-site request forgery](https://en.wikipedia.org/wiki/Cross-site_request_forgery). A hard-coded default is included for `SECRET_KEY`, but please make up your own key and store it as an environment variable for effective CSRF protection. To set the `SECRET_KEY` on Mac OS X or Linux:

```
$ export SECRET_KEY='Crazy,long_string'
```

On Windows:

```
$ set SECRET_KEY=Crazy,long_string
```

The `MAIL_USERNAME` and `MAIL_PASSWORD` environment variables are used by the flask-mail extension. When a user submits the form on the contact page, Moon Flask sends an outgoing mail request to an email server. The message is sent from and delivered to the email address specified in `MAIL_USERNAME`. `MAIL_PASSWORD` authenticates the send request.

To set these on Mac OS X or Linux:

```
$ export MAIL_USERNAME='email_user@example.com'
$ export MAIL_PASSWORD='email_password'
```

On Windows:

```
$ set MAIL_USERNAME=email_user@example.com
$ set MAIL_PASSWORD=email_password
```

The email server name, port, SSL and TLS are specified in `config.py`. The defaults are set for a Yahoo account for testing purposes. Change these defaults to use your preferred email provider. (A warning, gmail will not work.)

<h2>Run Moon Flask Locally</h2>
<h4>Start the Development Server</h4>
Make sure your virtual environment is still active, then start the local development server:

```
$ python run.py runserver
```

<h4>Debug Mode</h4>
Debug mode provides you with an interactive debugger in the browser. Do not use in production.

```
$ python run.py runserver -d
```

<h4>Deactivate the virtual environment</h4>
When you have finished working with Moon Flask, deactivate the virtual environment:

```
$ deactivate
```

<h2>Data Models and How They are Rendered</h2>
`ERD.png` details the database model. A User can have many Pages and Posts. Each Page can have many Posts. A User can have many Social Icons. Although the database model is constructed with multiple users in mind, at this point the app will only work for one user.

Each Page has a 'name' and a 'description'. Both are displayed in the header, 'name' as the page heading and 'description' as a subheading. The 'image' field is a boolean value. If `True`, the 'page' template will display a properly named image above the page heading. See the section below on naming images.

Each Post has a 'title' and a 'body'. The 'title' and 'body' are displayed as post headings and bodies respectively. As with Pages, 'image' is a boolean test for an image associated with the Post. Each Post can render an 'image' <i>or</i> an 'embed'. Not both. The 'embed' is an iframe tag, including all HTML elements.

All Post fields are optional. This allows for modular construction of a Post. For example, longer posts could be built from multiple posts stitched together leaving out the 'title' field where appropriate. Posts could be just a 'title' and 'image'. To skip a field, assign it an empty string or set 'image' to `False`.

The Social Icons are displayed at the bottom of the contact page and each dynamically generated page. The fields for social icons are the 'href' link to the social media profile and the Font-Awesome 'css_value' of the desired icon. The [Font-Awesome cheatsheet](https://fortawesome.github.io/Font-Awesome/cheatsheet/) lists all possible icons and their css values. See the [Font-Awesome documentation](http://fontawesome.io/examples/) for details on resizing and manipulating icons.

<h4>Naming Images</h4>
Images must be placed in the `app/static/img/` folder. They must be .jpg files. Their name must match the 'name' field of their corresponding 'Page' or 'title' field for 'Post' images. Remove spaces and keep the capitalization scheme intact. For example, a Post with the title "The Bridges of Portland" would have a corresponding image named "TheBridgesofPortland.jpg".

<h2>Manage Content</h2>
Moon-Flask does not have an Admin panel for managing content at this point. It will be better when it does. For now, the content must be managed manually.

Use the commands in `build_db.py` as a model for items you wish to add. Lines can be replaced in this script, but make sure to include your additions in the `db.session.add_all()` before the commit statement. 

Items can also be added, deleted or modified in the shell by running:

```
$ python run.py shell
```
The primary key 'id' field is automatically generated and need not be assigned.

The app uses SQLAlchemy and SQLite by default. Change `SQLALCHEMY_DATABASE_URI` in `config.py` to use another database. The script `build_db.py` builds the SQLite database file `data.sqlite`.

The best way to update the database file is to delete `data.sqlite` and build the database from scratch. Note that SQLite cannot overwrite existing database entries. If you want to to add entries without deleting `data.sqlite`, you must remove any existing database entries from `build_db.py`.

<h2>To do</h2>
This app can be improved. Here are my top improvements:<br/>
1. Flexible image names and types<br/> 
2. Better error handling in contact.py<br/>
3. Chronological display of posts<br/>
4. Async email<br/>
5. Admin panel for managing content<br/>
6. Support for multiple users

Being a neophyte Flask developer, I welcome any suggestions and best practice recommendations. Thank you!
