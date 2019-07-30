# Recipes - Data Centric Milestone Project

## User Experience and features

Every page has the same Navbar, Footer and Social Icons (displayed on the left of the screen in desktop views, and within the navbar in mobile views), which are styled depending on the screen size the user is viewing the site in.

### Example uses of site

A user can use theRecipeStore to look for recipes for different meal types. These are recipes that have been uploaded by other users. Recipes can only be uploaded by users that have become a member of the site, and they can do this by signing up for an account (accessible from the home page by clicking either the sign up or login buttons in the navbar). Logging in or signing in takes the user to their personal page, from where they can upload the recipes.

### Home Page

The homepage has a large scrolling image at the top of the page. This contains an intro message to the site. Underneath there is a grid showing different meal types (they can also scroll between recipe preference and allergen). When the user selects one of these, they are taken to the page of that particular meal type. Underneath this, also in a grid form, but in the structure of post it notes are a list of recipes that have been uploaded.

### Sign in and Log in pages

This website gives the user the option to become a member. They can sign up for this by going to the 'Sign Up' page. This can be accessed throughout the site from the navbar. They are then asked to submit their first name, last name, and their chosen username to create the account. From then on, if they revisit the site they will be able to go to the 'Log in' page and supply their username to be taken into their account. This will enable them to upload their own recipes.

### About and Contact pages

In the bottom right of the footer on every page, you will find links to the 'About' and 'Contact' pages. If the user has any questions about the site or their account, they are able to visit the 'Contact' page and send a message. The 'About' page has been created for those users that would like more information about the site, maybe before they create and account. In the text, they are able to find links to the 'Contact' and 'Sign Up' pages.

### Personal page

When the user has logged in they are taken to their personal home page. At the top they are presented with their information, which they can change if they wish. If they press the update button underneath the information is permanently updated in the database.

At the bottom of the page they will see the list of the recipes they have created, in post it note format. They also have the option to create a new recipe, and if they click the button are taken to the create recipe page. 

### Create Recipe Page

The create recipe page is only accessible by users that are logged in. When a user goes here they are provided with a form that uses textfields, radio buttons and check boxes to create the recipe and assign it a meal type, preferences and allergens. When the recipe is submitted it is stored in the database.

### Individual Recipe Pages

If the user is looking for a meal of a particular type, they can either click the navbar menu, or, from the home page, the meal type options. This then takes them through to the individual pages for these options. They are then presented with recipes which they can click for meals of this type. 

If the user is signed in and they are on the page of a recipe they have created, they are presented with two buttons: update and delete. If they press the delete button the recipe is removed from the database. If they press update, they are redirected to the create recipe page but with the initial information pre filled out.

## Technology Used

This project was built using different languages, libraries and frameworks. 

### Frontend

The template pages have been written with HTML5 (http://www.html5.com/) and styled with CSS3 (www.css3.com) in the style.css file. CSS3 was used to create the mobile responsiveness seen across the whole site. It has also been used to create the hover effects for the buttons and icons. On each of the pages, you will find the jinja template engine used. A 'base.html' page has been created to contain the HTML code that is to be used on each of the pages i.e. the head, header and the footer.

jQuery (https://jquery.com/) has been used in the navbar to control the dropdown menus. It is also used in the home page to allow the user to scroll between meal type, preferences or allergen, and switch the post it notes section between the most popular recipes on the site and the most recently uploaded recipes on the site. Javascrpt (https://www.javascript.com/) was used for the form in the contact page.

The contact form on the 'contact.html' page was created using HTML forms. An account and template for the data submitted was created on Emailjs, and this was connected with Javascrpt in the 'contact.js' file.

### Python

The site has been built using the Python based Flask framework (http://flask.pocoo.org/) and is run from the 'run.py' file which is stored in the outer folder. 

Within therecipestore folder, there are four more python files. The '__init__.py' file is where the project are configurations variables are stored, including the database. The database tables are created within the 'models.py file. The data for these are often collected from forms, which are created in 'forms.py'. Finally the 'routes.py' file contains all the routing for the templates, and also deals with the collection and display of the information.

Python has been used to create the logic within the 'run.py', '__init__.py', 'forms.py', 'models.py' and 'routes.py' files (https://www.python.org/). The 'jinja template engine' (http://jinja.pocoo.org/) has been used within the html template pages already described.

### Data Storage

To reduce the amount of code in the index.html page, the 'meal-type-homepage.json' file was created. I then ran a for loop in the 'index.html' template that called each of the objects.

The database was created using SQLAlchemy. The database was created in the 'models.py' file, and the data is gathered when the user fills in the forms, whether that be their personal information when signing up or creating a recipe.

### Version Control

Git was used throughout the project for version control.

## Issues While Building the Project

## Testing

The CSS was run through a CSS validator and errors were corrected. It now shows no errors. The javascript/jquery code was validated using jshint and showed no errors.

The site has been tested manually by clicking the links to the pages and checking all of the jQuery options. It has also been tested in different browsers.

Accounts have been created and I have created recipes to ensure that all functionality works well for new members. 

## Further Considerations

### Navbar

The navbar on all pages works well generally. However, on screen sizes such as mobile phone devices turned horizontally the screen is not high enough for all the links to fit on the screen. It is currently difficult to scroll, and therefore this would be a priority as a further consideration.

### Database and displaying recipes

There are many ways in which the database can be used to give the user more options. Currently the database is used on the home page to allow the user to select meal types, preference or allergen. More functionality can be provided to allow the user to search for desserts for people who are lactose intolerent, or nut free snacks etc. This could be achieved by having drop down box on the pages, or checkboxes to enable the user to specify their search while on the page.

### Update Page

If the user is logged in and clicks on a recipe they have created they will have the option to update a recipe. This takes them to a page that allows them to update the basics of the recipe. To complete this page I would allow the users to be able to update or add ingredients and recipes. The functionality for this would be handled within the update_recipe route in the 'routes.py' file.

### Character limits on recipes

Currently there are character limits on the title, ingredients and instructions within the recipe creation pages. Currently an error is thrown if the user exceeds this. I would adjust this to give the user an error message on the page to allow them to adjust their recipe accordingly. I would also increase the number of characters available for the recipe title from 20 to 40.

## Deployment

This project has been deployed to both Github and Heroku by using the push command in the terminal. Once in Heroku the database needed to be created separately using Postgres.

If you would like to contribute to the project can be cloned or downloaded from the Github link provided below. 

The individual files on Github can be found via https://github.com/JShad30/the_recipe_store, and the website can be viewed at https://recipes-data-centric-milestone.herokuapp.com/

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

I used the following to learn the basics of uploading the recipes with the SQLAlchemy database method (Corey Schafer youtube) https://www.youtube.com/watch?v=MwZwr5Tvyxo&list=PL-osiE80TeTs4UjLw5MM6OjgkjFeUxCYH

Sticky Social links on all pages when viewed on desktop - https://www.w3schools.com/howto/howto_css_sticky_social_bar.asp

To send the email from the contact form - https://code.tutsplus.com/tutorials/intro-to-flask-adding-a-contact-page--net-28982
