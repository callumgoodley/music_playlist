# music_playlist_app

### Resources

* Presentation
* Trello - https://trello.com/b/zCibjKkO/number-1s-music-app
* Website - http://35.242.143.43:5000


## Contents 

* Brief
  * Additional Requirements
  * My Approach
* Architecture
  * Databse Structure
  * CI Pipeline
* Project Tracking
* Risk Assessment
* Testing 
* Front-End Design
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

## Tech Stack

Following the brief I ahve implemented the following tech stack as learned during training: 

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

![CI Pipeline](/Users/user1/Downloads/copy%20of%20Untitled%20Diagram.jpg?raw=True)
