# Pocket Change
[Deployed on Heroku](https://pocket-change.herokuapp.com)

* One sentence overview of the game

* Players will choose from available teams based on the social need that is most important to that player.  Companies along the Elizabeth River Trail can pledge a percentage of their profits to the United Way, in order to become a point of interest in the game, a 'United WayPoint'.  

* Players visit the United WayPoints and compete in the game for control.  The donations from the company that owns that WayPoint will go to the United Way social cause that is associated with the controlling team.  

* Players traveling along the Elizabeth River Trail can find virtual supplies within their game to help them control WayPoints, including drops sponsored by involved companies.  Players can also earn supplies by participating in chartiable projects and community events.  
This alone is a good use of data to make a good change.  But we want a great change.
___

The game will make massive ammounts of non personalized data available.  The city can use this data to meet the needs of the citizens, and modify the game, which in turn becomes better at meeting needs and generating charitable revnue.  Examples of this include

* Finding wifi and cellular deadspots

* Analyzing amenity use, such as the number of users waiting for availability

* More efficient marketing of charitable and social events.

* Foot Traffic heat maps of the trail

* Measurement of relative importance of various social issues to the citizens
___

How you play the game,  

Machine learning models have already been applied to leverage census data from the United Way Greater Hampton Roads Dashboard

*granulate data based on city, interest, times, weather, 

A python script pulls the CSV data from the dashboard into the game's algorithm- developed in azure - to perform multi variant statistical analysis, and deploys real time data via a https url.  Data is saved and used in future machine learning models to make predictions on how to best use the data we have for the greatest society impact.

* Examples

Many games analyze data to improve their game.  This one analyzes data to improve the community.  

data slicing
___

# Credits

Created for [Dominion Enterprise's](https://dominionenterprises.com/) Hack Data Hackathon

## Technology
* Deployed on Heroku via HTML5, CSS, Javascript, and NodeJS with Express.
* Data acquisition done with Microsoft Azure through Python and Javascript web scraping.
* Data pipelining through Microsoft Azure and T-SQL
* Excel VBA for data analysis 
* Microsoft Power BI for Visualization
* File sharing in Slack.

## APIs 
* Google Maps
* Greater Hampton Roads Connect
* Blizzard Battle.Net


[Brandon Burr](https://www.linkedin.com/in/baburr) - Machine Learning, Modeling and Simulation  
[Marc Fogleman](https://www.linkedin.com/in/marcfogleman) - Web Design, Data Acquisition  
[Andrew Hollis](https://www.linkedin.com/in/andrew-hollis-a8680b25) - Design, Visualization   
[Corey Wofford](https://www.linkedin.com/in/coreywofford) - Python Scripting, Data Analysis  


