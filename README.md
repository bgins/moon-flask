# Moon Flask

Moon Flask is a simple portfolio web app built on Flask. 

The app comes with standard 'about' and 'contact' pages. All of the other pages and their navigation links are generated dynamically from a database. The database is managed with SQLAlchemy.

Moon Flask uses [Skeleton CSS](http://getskeleton.com/) for layout and [Font-Awesome](https://fortawesome.github.io/Font-Awesome/) for social icons.

The app comes with a sample set of content, styles and a sample user; namely, the Early Renaissance painter [Paolo Uccello](https://en.wikipedia.org/wiki/Paolo_Uccello).

<h2>Deploy</h2>
<h4>Clone the Repository</h4>
Make a folder for Moon Flask, then clone the repository into it:
```
$ git clone https://github.com/thuselem/moon-flask
```

<h4>Set up a Virtual Environment</h4>
Setting up a virtual environment has a number of inconsistencies among operating systems and versions of Python. This app has been tested with Python 3.4.

The following will set up a Python 3.4 virtual environment on Mac OS X or Linux:
```
$ virtualenv -p python3.4 moon-flask
```
If you do not have `virtualenv`, install it with your package manager. For example, on Ubuntu:
```
$ sudo apt-get install python-virtualenv
```
On Mac OS X:
```
$ sudo easy_install virtualenv
```
For virtual environment setup on other systems, check out [Miguel Grinberg's Flask Mega-Tutorial Part I] (http://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world). Create the virtual environmental in the `moon-flask` directory, then stop where the tutorial instructs you to install Flask and the other extensions. These are installed next.

<h4>Install the Requirements</h4>
```
$ cd moon-flask
$ source bin/activate
$ pip install -r requirements.txt
```

<h4>Build the Sample Database</h4>
```
$ python build_db.py
```

<h4>Set the Environment Variables</h4>
Environment variables must be set for `SECRET_KEY`, `MAIL_USERNAME` and `MAIL_PASSWORD`. Even though a default is included for `SECRET_KEY`, please make up your own and store it as an environment variable for effective CSRF protection. If you are running Moon Flask locally, the variables can be set at the command line. On Linux:
```
$ export SECRET_KEY='Crazy, long string'
$ export MAIL_USERNAME='email username'
$ export MAIL_PASSWORD='email password'
```
The flask-mail settings are configured for a Yahoo account. I tried using Gmail, but could not get it to work. The email settings can be changed in `config.py`.

<h2>Run Moon Flask Locally</h2>
<h4>Activate the virtual environment</h4>
```
$ source bin/activate
```
<h4>Start the Development Server</h4>
```
$ python run.py runserver
```
<h4>Debug Mode</h4>
```
$ python run.py runserver -d
```
Once you have started the development server, navigate to `localhost:5000` in a web browser to view the app. To stop the development server, press Ctrl-C at the command line.

<h2>Configure a Web Server</h2>
This is a large topic. When I find a reliable set of instructions, I will provide a link.

<h2>Data Models and How They are Rendered</h2>
`ERD.png` details the database model. A User can have many Pages and Posts. Each Page can have many Posts. A User can have many Social Icons. Although the database model is contructed with multiple users in mind, at this point the app will only work for one user.

Each Page has a 'name' and a 'description'. Both are displayed in the header, 'name' as the page heading and 'description' as a subheading. The 'image' field is a boolean value. If `True`, the 'page' template will display a properly named image above the page heading. See the section below on naming images.

Each Post has a 'title' and 'body'. The 'title' and 'body' are displayed as post headings and bodies respectively. As with Pages, 'image' is a boolean test for an image associated with the Post. Each Post can render an 'image' <i>or</i> an 'embed'. Not both. The 'embed' is an iframe tag, including all html elements.

All Post fields are optional. This allows for modular construction of a Post. For example, longer posts could be built from multiple posts stitched together leaving out the 'title' field where appropriate. Posts could be just a 'title' and 'image'. To skip a field assign it an empty string or set 'image' to `False`.

The Social Icons are displayed at the bottom of the contact page and each dynamically generated page. The fields for the social icons are the 'href' link of the social media profile and the Font-Awesome 'css_value' for the icon. The [Font-Awesome cheatsheet](https://fortawesome.github.io/Font-Awesome/cheatsheet/) lists the possible icons and their css values. See the Font-Awesome documentation for details on resizing and manipulating icons.

<h4>Naming Images</h4>
Images must be placed in the `app/static/img/` folder. They must be .jpg files. Their name must match the 'name' field of their corresponding 'Page' or 'title' field for 'Post' images. Remove spaces and keep the capitalization scheme intact. For example, a Post with the title "The Bridges of Portland" would have a corresponding image named "TheBridgesofPortland.jpg".

<h2>Manage Content</h2>
Moon-Flask does not have an Admin panel for managing content at this point. It will be better when it does. For now, the content must be managed manually.

Use the commands in `build_db.py` as a model for items you wish to add. Lines can be replaced in this script, but make sure to include your additions in `db.session.add_all()` before the commit statement. 

Items can also be added, deleted or modified in the shell by running:
```
$ python run.py shell
```
The primary key 'id' field is automatically generated and need not be assigned.

The app uses SQLAlchemy and SQLite by default. Change `SQLALCHEMY_DATABASE_URI` in `config.py` to use another database. The script `build_db.py` builds the SQLite database file `data.sqlite`.

The best way to update the database file is to delete `data.sqlite` and build the database from scratch. Note that SQLite cannot overwrite existing database entries. If you want to to add entries without deleting `data.sqlite`, you must remove any existing database entries.

<h2>To do</h2>
This app can be improved. Here are my top improvements:<br/>
1. Admin panel for managing content<br/>
2. Proper error handling in contact.py<br/>
3. Chronological display of posts<br/>
4. Async email<br/>
5. Support for multiple users

Being a neophyte Flask developer, I welcome any suggestions and best practice recommendations. Thank you!
