# Pocket Change
[Deployed on Heroku](https://pocket-change.herokuapp.com)

* Pocket change is a mobile game that leverages data to further social good      

* Players will choose from available teams based on the social need that is most important to that player.  Companies along the Elizabeth River Trail can pledge a percentage of their profits to the United Way, in order to become a point of interest in the game, called a 'United WayPoint'.  

* Players visit the United WayPoints and compete in the game for control.  The donations from the company that owns that WayPoint will go to the United Way social cause that is associated with the controlling team.  

* Players traveling along the Elizabeth River Trail can find virtual supplies within their game to help them control WayPoints.  Players can also earn supplies in game by participating in chartiable projects and community events.  

This alone is a good use of data to make a good change.  But Norfolk is a great city that deserves a great change.

___

The game will convert player activity to actionable data.  The city can use this data to meet the needs of the citizens, and modify the game, which in turn becomes better at meeting needs and generating charitable revnue.    Examples of this include

* Finding wifi and cellular deadspots

* Analyzing amenity use and needs

* More efficient marketing of charitable and social events.

* Heat Maps of Foot Traffic and Elizabeth River Trail Use

* Measurement of relative importance of various social issues to the citizens
___

Machine learning models have already been applied to leverage census data from the United Way Greater Hampton Roads Dashboard

This census data is input to Azure's Machine Learning Studio and the data is automatically joined based on city location, and years.  A SQL script reduces years into quarters for comparison, and a python script pulls the CSV data from the dashboard into the game's algorithm to perform multi variant statistical analysis, and deploys real time data via a https url.  Data is saved and used in future machine learning models to make predictions on how to best use the data we have for the greatest society impact.

* Create an even distribution of resources to social motivators

* Targeting awareness campaigns for cancer screenings  

* Promote social causes that need assistance to groups that are they are underpreferred to  

* Creating special events in real life that reward in game ( eg, Habitat for Humanity, blood drives)

All this data is self supporting, and as more data is gained, the game effectively designs itself.  Every aspect of the community can contribute, and can gain.

Many games analyze data to improve their game.  This one analyzes data to improve the community.  

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


