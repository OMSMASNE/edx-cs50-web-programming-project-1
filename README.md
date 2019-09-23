# Project 1 : BOOKS!

## Web Programming with Python and JavaScript

# This project has been created by ***OM SANTOSHKUMAR MASNE*** .

### Created on 15/01/2019.
### All dates mentioned in this project are in the format: DD/MM/YYYY.

### This website is a project website created for EDX course, Web Programming with Python and JavaScript.

### This is a web application for book's reviews.
---

### USAGE:

#### Requirements:
* Install the necessary requirements: `pip install -r requirements.txt`.

#### DATABASE AND API:
* Setup the database (Instructions in 'database.sql' in project root).

* Create an environment variable `DATABASE_URL` and set its value to your DATABASE's URL.

* Create an environment variable `GOODREADS_KEY` and set its value to your GOODREADS API KEY.

#### Import the books:
* Goto import books directory.
* Type `python import.py` in the terminal.

#### Type the following commands in the terminal:

For windows:
`> set FLASK_APP=application.py`

For Linux:
`$ export FLASK_APP=application.py`

Then: `flask run`

---

### The website's structure is as follows:

* The '/' route lands the user at the homepage. The website's homepage gives the user 2 options. The user can choose to create a new account or the user may login to the website.

    * The user has to fill the username and the password fields to create a new account. If account is created succesfully the user is redirected to the account successfully created page. If there is any error, then the user is shown that error.

    * The user may use 'guest' as username and password to login if the user does not want to create account. The website's features will be limited if the guest login is used.

    * If the user has an account, then that accounts login credentials can be used to login.

* Once logged in, the user is sent to the books search page. This page helps the user to find the required book by using any one of the attributes of the book (ISBN, TITLE, AUTHOR, YEAR). Alternatively the user can select any book from the table shown below.

* If the user searched for some book, then a search result page will be rendered showing all the search results (if any).

* When a book is selected, the book's information is shown. Here, the book's ISBN, TITLE, AUTHOR and YEAR are shown. If the server is able to contact GOODREADS website (API), then, the GOODREADS's rating count and average rating are shown. Any previous reviews of the book are also shown here.

* The user also has an option to leave a review of the selected book. If the user has used to guest login, then the submit review option is disabled. Security measures are taken on the server side to prevent any intentional or unintentional malicious act of the user.

* An API is also available with the website, which can be used to get information of a particular book in JSON format.

* The API is used as follows: `/api/<string:isbn>`, where `<string:isbn>` is the ISBN (number) of a book.

A footer is also shown on index (homepage) page, displaying the name of the creator of this project, short information about the project and 'guest' login information.

Many other HTML and CSS properties are used in this project website to enhance its appearance.
This project website is also compatible with devices with small screens (screen resolution).

---

### This project uses [FLASK](https://palletsprojects.com/p/flask/).

### This project uses [BOOTSTRAP](https://getbootstrap.com).

### This project uses [GOODREADS](https://www.goodreads.com/) for book's reviews.
### Link to [GOODREADS API](https://www.goodreads.com/api).

### The background image on website's homepage is licensed under the Creative Commons Zero [CC0] License. [LICENSE LINK](https://creativecommons.org/publicdomain/zero/1.0/). 
### [IMAGE LINK](https://www.pexels.com/photo/bay-beach-blue-cliff-373409/).
### Photograph by [Pixabay](https://www.pexels.com/@pixabay).

---

## License:
### Licensed under the GNU Affero General Public License v3.0 only (AGPL-3.0-only) license.
### Copyright (c) 2019 OM SANTOSHKUMAR MASNE. All Rights Reserved.
