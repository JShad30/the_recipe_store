# Recipes - Data Centric Milestone Project

This is my Milestone Project for the Data Centric Module of the Full Stack Development Course. This site has been developed to allow users to find, upload and share menus with like minded people. There is an option for the user to become a member of the site, although they do not need to to be able to find and use recipes.

I have designed the site to have a good presentation and consistent feel throughout. The home page has an introduction with scrolling images for visual effect. Cursive writing fonts have been used on the recipes and a post it note look for recipe titles, to give the website a personal feel.

## User Experience

Every page has the same Navbar, Footer and Social Icons (displayed on the left of the screen in desktop views, and within the navbar in mobile views), which are styled depending on the screen size the user is viewing the site in.

### Example uses of site

A user can use theRecipeStore to look for recipes for different meal types. These are recipes that have been uploaded by other users. Recipes can only be uploaded by users that have become a member of the site, and they can do this by signing up for an account (accessible from the home page by clicking either the sign up or login buttons in the navbar). Log in or signing in takes the user to their personal page, from where they can upload the recipes.

### Home Page

The homepage has a large scrolling image at the top of the page. This contains an intro message to the site. Underneath there is a grid showing different meal types. When the user selects one of these, they are taken to the page of that particular meal type. Underneath this, also in a grid form, but in the structure of postit notes are a list of recipes that have been uploaded.

### Sign in and Log in pages

This website gives the user the option to become a member. They can sign up for this by going to the 'Sign Up' page. This can be accessed throughout the site from the navbar. They are then asked to submit their first name, last name, and their chosen username to create the account. From then on, if they revisit the site they will be able to go to the 'Log in' page and supply their username to be taken into their account. This will enable them to upload their own recipes.

### About and Contact pages

In the bottom right of the footer on every page, you will find links to the 'About' and 'Contact' pages. If the user has any questions about the site or their account, they are able to visit the 'Contact' page and send a message. The 'About' page has been created for those users that would like more information about the site, maybe before they create and account. In the text, they are able to find links to the 'Contact' and 'Sign Up' pages.

### Individual Meal Pages

If the user is looking for a meal of a particular type, they can either click the navbar menu, or, from the home page, the meal type options. This then takes them through to the individual pages for these options. They are then presented with recipes which they can click for meals of this type. 

## Features

## Technology Used

This project was built using different languages, libraries and frameworks. 

### Frontend

The template pages have been written with HTML5 (http://www.html5.com/) and styled with CSS3 (www.css3.com) in the style.css file. CSS3 was used to create the mobile responsiveness seen across the whole site. It has also been used to create the hover effects for the buttons and icons. On each of the pages, you will find the jinja template engine used. A 'base.html' page has been created to contain the HTML code that is to be used on each of the pages i.e. the head, header and the footer.

jQuery (https://jquery.com/) has been used in the navbar to control the dropdown menus. It is also used in the home page to allow the user to scroll between meal type, preferences or allergen, and switch the post it notes section between the most popular recipes on the site and the most recently uploaded recipes on the site. ------Javascrpt (https://www.javascript.com/) was used for the form in the contact page.------

The contact form on the 'contact.html' page was created using HTML forms. An account and template for the data submitted was created on Emailjs, and this was connected with Javascrpt in the 'contact.js' file.

### Python

The site has been built using the Python based Flask framework (http://flask.pocoo.org/) and is run from the 'run.py' file. All the pages are routed from here, and contain the fuctions and logic. Python has been used to create the logic within the 'run.py' file (https://www.python.org/). The 'jinja template engine' (http://jinja.pocoo.org/) has been used within the html template pages already described.

### Data Storage

To reduce the amount of code in the index.html page, the 'meal-type-homepage.json' file was created. I then ran a for statement in the 'index.html' template that called each of the objects.

### Version Control

Git was used throughout the project for version control.

### Contact Form

I was having an issue with the redirects when the submit button was pressed on the contact form. I created a form that when filled in sent an email to the users email address. While this was working, there was no feedback to the user that a message had been sent. Therefore I built a new template (messagereceived.html) that I wanted to redirect the user to when the submit button was pressed. At first the only way I could do this was to give the form a method of 'POST'. Although feedback was then being given to the user, the emails were not being sent.

To solve this ..................................

## Testing

The CSS was run through a CSS validator and errors were corrected. It now shows no errors. The javascript/jquery code was validated using jshint and showed no errors.

The site has been tested manually by clicking the links to the pages and checking all of the jQuery options. It has also been tested in different browsers.

Accounts have been created and I have created recipes to ensure that all functionality works well for new members. 

### Contact

A number of test emails were sent from the contact page to check that the form was set up correctly......... (Now running in python in Flask).

## Further Considerations

### Navbar

The navbar on all pages works well generally. However, on screen sizes such as mobile phone devices turned horizontally the screen is not high enough for all the links to fit on the screen. It is currently difficult to scroll this, and therefore this would be a priority as a further consideration.

### Database and displaying recipes

There are many ways in which the database can be used to give the user more options. Currently the database is used on the home page to allow the user to select meal types, preference or allergen. More functionality can be provided through sql and a search form to allow the user to search for desserts for people who are lactose intolerent, or nut free snacks etc.

### Sign Up and Log in

To make becomming a member of the site more secure the sign up page will have a 'confirm password'. This password will then also be encrypted.

## Deployment

This project has been deployed to both Github and Heroku by using the push command in the terminal.

If you would like to contribute to the project can be cloned or downloaded from the Github link provided below. 

The individual files on Github can be found via https://github.com/JShad30/solar-system-quiz, and the website can be viewed via https://solar-system-quiz.herokuapp.com/.

## Credits

### Media

The images used on the front page for the scrolling header and the meal type pictures are taken from Pixabay.

The image used for the gluten free page was found from https://www.verywellhealth.com/five-different-types-of-gluten-allergy-562305

The image for the lactose free page image was found from https://www.medicalnewstoday.com/articles/317496.php

The image for the nut free meal was found at https://www.onegreenplanet.org/vegan-food/these-vegan-recipes-are-nut-free-and-delicious/

### Acknowledgements

Throughout the project I received support from the mentor and the tutors. For individual coding tips, I would search online. These include:

UX Rating Youtube Channel, https://www.youtube.com/watch?v=z05L-y6GAAY - Hamburger menu to a cross in the navbar when selected in mobile views.

Slideshow on the homepage - https://www.the-art-of-web.com/css/fading-slideshow-no-jquery/

The following link was a guide I used to help create the membership areas and implement user authentication - https://pythonspot.com/login-authentication-with-flask/ and from youtube I used https://www.youtube.com/watch?v=d04xxdrc7Yw

Sticky Social links on all pages when viewed on desktop - https://www.w3schools.com/howto/howto_css_sticky_social_bar.asp

To send the email from the contact form - https://code.tutsplus.com/tutorials/intro-to-flask-adding-a-contact-page--net-28982