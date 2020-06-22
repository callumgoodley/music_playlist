# music_playlist_app

### Resources

* Trello - https://trello.com/b/zCibjKkO/number-1s-music-app
* Website - http://35.242.143.43:5000


## Contents 

* Brief
  * Minimum Requirements
* Functionality
* Data
* Tech Stack
* CI Pipeline 
* Testing 
* Front-End Design
* Risk Assessment
* Known Issues
* Future Improvements
* Authors


## Brief

The brief that was given to me for this particular project was 'To create a CRUD application with utilisation of supporting tools, methodologies and technologies that encapsulate all core modules covered during training.'. 

In the simplest terms this meant that I was tasked with creating an application that can take input from a user in order to create, read, update and delete data stored in a database and visible to the user via the app itself.

### Minimum requirements

* Project tracking via Trello or similar
* A relational database with at least two tables and one relationship
* Clear documentation 
* A functional CRUD application created in Python follwoing best practices and meeting requirements set on Trello
* Fully designed test suites for application with high coverage and reports on testing
* Functional front-end website and integrated API's using Flask.
* Code integrated into a version control system using feature branch model which will subsequently be built through a CI server and deployed to a cloud-based VM


## Functionality

To satisfy the brief I designed an music playlist app that would users to create and edit playists and store songs within them which I hoped could be used as a means digital storage for physical record collections. 

The users stories that satisified the brief were as follows:

* A user must be able to CREATE an account with first name, last name, unique email address and a password (hashed for storage)

* A user must be able CREATE playlists each playlist created is stored in the database with the id of the user that created it requiring two tables and a relationship within the database.

* A user must be able to CREATE songs and add them to a playlist - the database realtionship between songs and playlists must be many to many to avoid storing duplicates of song data for songs that feature on multiple playlists.

* A user must be able to READ a list of their playlists displayed to them as well as the songs for that playlist

* A user must be able to DELETE songs and playlists that they have added themselves as well as their own account

* A user must be able to UPDATE their playlist names as well as their own account details 

The images below display the full extent of the user stories created for making this application as well as the layout and flow of the agile cycle implemented throughout the course of the project:

![Trello1](https://user-images.githubusercontent.com/56595709/85229389-4e3f3480-b3e1-11ea-9a10-c69106a355c3.png)
![Trello2](https://user-images.githubusercontent.com/56595709/85229384-497a8080-b3e1-11ea-81c4-91f90f5fadd6.png)


## Data

Firstly it is important to outline the data for the database and the relationships between them. Below is an entity relationship diagram outlining just that:

![ERD](https://user-images.githubusercontent.com/56595709/85230226-b2b0c280-b3e6-11ea-8834-0fade483c8a8.jpg)

As you can see in the image the afforementioned many to many relationship between between songs and playlists uses an intermidiary table to afford the ability for songs to belong to multiple playlists without creating duplicates and also for playlists to be associated with mutliple songs as one would expect.

Also visible within this diagram is the realtiohsip between users and playlists in which a playlist must always belong to a user and the schema dictates that each playlist must have a user id attached to it.  


## Tech Stack

Following the brief I have implemented the following tech stack as learned during training: 

* Trello for a Kanban Board
* GCP SQL Server using mySQL for Database purposes
* Python for back end pogramming
* Pytest for unit testing
* Selenium for intergation testing
* Flask as a framework with HTML for front-end webpages
* Git for version control
* Jenkins as a CI server 
* GCP compute engine cloud server
* Gunicorn to run the app
* Systemsd to run the app as service 


## CI Pipeline

Below is an image depicting the flow of the app and how each part of the tech stack fits into the CI pipeline.

![CI Pipeline](https://user-images.githubusercontent.com/56595709/85229371-3ff11880-b3e1-11ea-95ae-694909481f6b.jpg)

As can be seen in the image of the continuous integration pipeline the flow goes as follows:

* Source code is created - this is where the programming of the app itself takes place on the GCP VM
* When effective changes are made to the source code the code is then pushed up to the git repository on GitHub
* After a block of code is pushed up to Github it is time to look at the project tracking on Trello to ascertain what the next task will be
* This process continues until I am happy enough with the basic functionality of the code to start testing
* By automating this through Jenkins it is possible to test and run the app just by triggering a Jenkins job
* The Jenkins job will run Pytest and produce a report of the test results and will run the app itself as a systemsd service running on Gunicorn

## Testing

![pytest](https://user-images.githubusercontent.com/56595709/85231941-5acc8880-b3f3-11ea-808d-4c0989797cb5.png)

Testing the app involved implementing two types of testing Unit and Integration. For the unit testing I used Unittest with Pytest and then for the integration testing I used Selenium and Pytest. Above is an image of the coverage report supplied by pytest this indicates how much of the application is and is not tested.

The Unit testing mainly tests the functionality of the back end of the project and the integration testing assesses the functionality of the front end in conjunction with the back end. Both of these testing suites have been automated using Jenkins the result of which you can see in the image below.

![jenkins](https://user-images.githubusercontent.com/56595709/85231870-9c106880-b3f2-11ea-8629-3364a5a4329c.png)

## Front end design

The front end design is very simple and operates on a purely operational basis.

The app url loads the first page up for the user.

![home](https://user-images.githubusercontent.com/56595709/85233986-65dae500-b402-11ea-8616-9659d9c32c7b.png)

From the home page the first port of call will be to register for an account on the registration page.

![registration](https://user-images.githubusercontent.com/56595709/85233988-670c1200-b402-11ea-9566-45161abb9b4e.png)

Once an account has been created the user can then log in to their account.

![login](https://user-images.githubusercontent.com/56595709/85233989-683d3f00-b402-11ea-9cba-5045f7b8b4e8.png)

Once a user has logged in they will be redirected to the playlist page where they can view a list of the playlists they've created or create a new playlist.

![playlists](https://user-images.githubusercontent.com/56595709/85233991-696e6c00-b402-11ea-9964-65d610cb1a82.png)

Once a user has created a playlist they will be able to then view that playlist and add songs to it on the playlists individual page.

![individual playlist](https://user-images.githubusercontent.com/56595709/85233992-696e6c00-b402-11ea-8fbc-6fc84215c5e8.png)

Once the user has created playlists they always have the option to change that playlists name.

![change playlist](https://user-images.githubusercontent.com/56595709/85233993-6a070280-b402-11ea-9604-a897c67e4cbe.png)

Lastly the user always has the ability to change their account details via the account page.

![account](https://user-images.githubusercontent.com/56595709/85233994-6a9f9900-b402-11ea-82b8-deb37939012c.png)

## Risk Assessment 

![risk](https://user-images.githubusercontent.com/56595709/85253838-eaefe980-b456-11ea-8531-8d3a8c153663.png)

## Current issues

* The main issue currently is that the redirects from certain URL's arent working when a user is not logged in
* Also users are currently able to create duplicated databases for which an alert and prevention could be in place


## Possible improvements

* As previously mentioned this app would work very well as a digitisation of a physical record collection on playlist could be a want list with links to purchase the records
* It would be great to connect user accounts to their social media accounts
* The front end design could do with some colour and a better design as well

## Author

Callum Goodley
