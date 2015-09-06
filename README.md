# moon-flask

Moon-Flask is a simple portfolio web app built on Flask. The app comes with a base set of styles and a sample user; namely, the Early Renaissance painter [Paolo Uccello](https://en.wikipedia.org/wiki/Paolo_Uccello). Paolo is a great sample user because his paintings are fantastic and in the public domain.

The app comes with standard 'about' and 'contact' page. All of the other 'pages' and their navigation links are generated dynamically from a database. The database is managed with SQLAlchemy.

Moon-Flask uses [Skeleton CSS](http://getskeleton.com/) for layout and [Font-Awesome](https://fortawesome.github.io/Font-Awesome/) for social icons. 

<h2>Deploy</h2>
<h4>Clone the repository</h4>
Navigate to the folder where you want Moon-Flask to live, then clone the repository:
```
git clone https://github.com/thuselem/moon-flask
```

<h4>Set up a virtual envinronment</h4>
Setting up a virtual environment has an unfortunate number of inconsistencies among operating systems and versions of Python. The following works on Ubuntu Linux. This will set up a Python 3.4 virtual environment.
```
virtualenv -p /usr/bin/python3.4 moon-flask
```
If you do not have virtualenv installed:
```
sudo apt-get install python-virtualenv
```
For virtual environment setup on other systems, check out [Miguel Grinberg's Flask Mega-Tutorial Part I] (http://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world). Install the virtualenv to the moon-flask directory, then stop where the tutorial instructs you to install Flask and the other extensions. These are installed next.

<h4>Install the requirements</h4>
```
cd moon-flask
source bin/activate
pip install -r requirements.txt
```

<h4>Build the sample database</h4>
```
python build_db.py
```

<h4>Set the Environment Variables</h4>
Environment variables must be set for `SECRET_KEY`, `MAIL_USERNAME` and `MAIL_PASSWORD`. Even though a default is included for `SECRET_KEY`, please make up your own and keep it in the environment for the best CSRF protection. The variables can be set at the command line. Replace with the appropriate strings. On Linux:
```
export SECRET_KEY='Crazy, long string'
export MAIL_USERNAME='email username'
export MAIL_PASSWORD='email password'
```
The current flask-mail settings are configured for a Yahoo account. I tried using Gmail, but simply could not get it to work. If you wish to try Gmail, change the email settings in `config.py`.

<h2>Run Moon-Flask Locally</h2>
<h4>Activate the virtual environment</h4>
```
source bin/activate
```
<h4>Start the Development Server</h4>
```
python run.py runserver
```
<h4>Run the Application in Debug Mode</h4>
```
python run.py runserver -d
```

<h2>Configure a Web Server</h2>
This is a large topic. I will link to a good set of instructions after testing server deployment.

<h2>Data Models and How They are Rendered</h2>
`ERD.png` details the database models and their fields. A User can have many Pages and Posts, and each Page can have many Posts. A User can also have many Social Icons. Although the database models are built with multiple users in mind, at this point the app will only work for one user.

Each Page has a 'name' and a 'description'. Both are displayed in the header, 'name' as the page heading and 'description' as a subheading. The 'image' field is a boolean value. If `True`, the 'page' template will display a properly named image above the page heading. See the note below on the naming images.

Each Post has a 'title' and 'body'. The 'title' and 'body' are displayed post headings and bodies respectively. As with Pages, 'image' is a boolean test for an image associated with the Post. Each Post can render an 'image' <i>or</i> an 'embed'. The 'embed' is an iframe tag, including all html elements.

All of the Post fields are optional. This allows for modular construction of a Post. For example, longer posts could be built from multiple posts stiched together leaving out the 'title' field where appropriate. Posts could be just a 'title' and 'image'. To skip a field assign it an empty string or set 'image' to `False`.

The Social Icons are displayed at the bottom of the 'contact' and each 'page' template. The fields for the social icons are the 'href' link for you social media profile page and the 'css_value' for the icon using Font-Awesome. Here is the [Font-Awesome cheatsheet](https://fortawesome.github.io/Font-Awesome/cheatsheet/). See the Font-Awesome documentation for details on resizing and manipulating icons.

<h4>Naming Images</h4>
Images must be placed in the `app/static/img/ folder`. They must be .jpg files. Their name must match the 'name' field of their corresponding 'Page' or 'title' for 'Post' images. Remove spaces and keep caps the same. For example, a Post with the title "The Bridges of Portland" would have a corresponding image named "TheBridgesofPortland.jpg".

<h2>Manage Content</h2>
Moon-Flask does not have an Admin panel for managing content at this point. It will be better when it does. 

For now, the content must be managed manually.

Use the commands in `build_db.py` as a model for items you wish to add. Lines can be replaced in this script, but make sure include you include your additions in `db.session.add_all()` before the commit. Note that you cannot write over existing database entries. Delete the lines for existing entries before making your additions, or delete `data.sqlite` and build the database from scratch.

Items can also be added, deleted or modified in the shell by running:
```
python run.py shell
```
The primary key 'id' field is automatic and need not be assigned.

The app uses SQLAlchemy and SQLite by default. Change `SQLALCHEMY_DATABASE_URI` in `config.py` to use another database. The script `build_db.py` creates the sample user SQLite database `data.sqlite`.

<h2>To do</h2>
This app can be improved. Here is my list of the top improvements:<br/>
1. Admin panel for managing content<br/>
2. Proper error handling in contact.py<br/>
3. Chronological display of posts<br/>
4. Aync email<br/>
5. Support for multiple users

Being real, I am neophyte Flask developer. I am welcome to any suggestions or best practice recommendations. Thank you!
