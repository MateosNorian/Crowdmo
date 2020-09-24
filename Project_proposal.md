# EasyRequest project proposal

## Big idea:
An app that makes splitting bills with roommates easier and more efficient, and gives users insight on their spending habits.

## The MVP
Our MVP will be a mobile-friendly website that allows users to input a dollar amount, and then select a list of venmo friends to request money. Our app will then automatically divide the charge amongst the people in the list and request them the exact amount they owe. 

## The stretch
If we are able to comlete our MVP in a timely manner then we will add on the budgeting/spending habits functionality to our application. Users will have the ability to categorize their spending/requests so they can see where they are spending the most money on a monthly basis. Basically, it will be a budgeting app tied to a program that allows users to divvy up payments more quickly.

## Learning goals
* Learn how to use an API
* Learn how to implement multiple frameworks into one working application (Flask, Bootstrap, Venmo API)
* Finish a project using Agile methodology

## Implementation plan
* Use Venmo API (someone has built a python wrapper for accessing the venmo API using Python) to access venmo user info/make requests on user's behalf
* Use Flask to set up web application, and use Flask/Jinga for website templates
* Use Bootstrap to design sleek mobile-first screens

## Project schedule

#### Sprint 1 (Weeks 1-2):
##### Week 1: 
* Create login/logout requirements 
* Design login/logout screens
* Begin implementing Venmo login/logout functionality

##### Week 2: 
* Finish login/logout implementation
* Extensively test functionality


#### Sprint 2 (Weeks 3-4):
##### Week 3:
* Create requesting screen requirements
* Design request screens
* Begin implementation of Venmo requesting functionality

##### Week 4:
* Finish implemenation of request screens
* Test functionality


#### Sprint 3 (Weeks 5-6):
##### Week 5:
* Create budgeting screen requirements
* Design budgeting screens
* Begin implementing visualizations for budgeting screens

##### Week 6:
* Finish implementation of budgeting visualizations
* Test budgeting screens
* Deploy application to AWS


#### Sprint 4 (Weeks 7-8):
##### Week 7:
* Correct bugs
* Begin project website

##### Week 8:
* Final bug fixes
* Finish project website
* Deploy project website

## Collaboration plan
* Majority paired programming, this will help make sure all project members understand the code behind the project
* Certain tasks may be individualized, such as screen designs/mockups
* We will use Agile development, and will set up a Trello board to hold members accountable
* Will have 2x weekly standup meeting to review progress
* Using Agile because it is now the standard in tech and is important for us to understand, also will allow us to build and test core features quickly

## Risks
* Difficulty implementing Venmo API
* Not being able to leverage the API in the way we expect, for example if some user information is not accessible through the API
* Difficulty learning/implementing Flask

## Aditional course contents
The Flask sessions seems like they will be very useful and relevant to our project because we are creating a web application.