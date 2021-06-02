Under development  

# Project Overview: Predicting the number of wins teams achieved using the 'four factors' of basketball
* Project was to use ML to predict the win percentage of teams in the NBA
* Completed two models - one with traditional statistics, and one using the 'four factors' of basketball
* Chose to use a linear regression as this gave the best R-squared results
* 'Four factor' model R-squared ~ 0.882
* Traditional stats model R-squared ~ 0.873
* As a result we see that using just 8 advanced statistics we can predict a teams win percentage with better accuracy than using a large collection of traditional box score statistics
* Provided visualisations to demonstrate the results- this shows how effective the model was at projecting each teams percentage

## Code and Resources Used 
**Python Version:** 3.8.5  
**Packages:** pandas, numpy, sklearn, matplotlib, seaborn, nba_api   
**NBA API github:** https://github.com/swar/nba_api   
**Mathletics by Wayne L. Winston** https://www.amazon.co.uk/Mathletics-Gamblers-Enthusiasts-Mathematics-Basketball/dp/0691154589


## Obtaining the data

Used the `nba_api` python package to obtain the data. Provides clean data direct from the official NBA API. To make the testing data I obtained the advanced metrics for each team in the current year and created a `.csv`. To create the training data I obtained the data for each of the last 4 seasons and merged them. This seemed easier and less time consuming than trying to create an elegant solution. For the traditional stats I joined two dataframes together for each season. This was because I wanted to include a teams opponents stats in the model for this case.


## The four factor model

Traditional | Advanced (Four Factors)
--- | ---
![alt text](https://raw.githubusercontent.com/MattBenyon/FourFactorsRegression/master/Images/TraditionalCorr.png "Traditional Stats Correlation") | ![alt text](https://raw.githubusercontent.com/MattBenyon/FourFactorsRegression/master/Images/FourFactorsCorr.png "Four Factors Correlation")  

As can be seen in these correlation plots, basketball statistics have little correlation to each other. We also see that no one statistic correlates particulary well with win percentages, however the ones that correlate the most are related to a teams field goal makes, their rebounding and their opponents equivalent.

The 'four factor' model attempts to capture this into four statistics. Instead of using field goal percentage, the model uses effective field goal percentage to determine a teams efficiency.

<div align="center"> eFG% = (FGM + 0.5 * 3FGM) / FGA    
<div align="left">  <br/><br/> 
Effective field goal percentage takes into consideration the efficiency of a 3-point shot compared with a 2-point shot.
  
The next statistics are:
  * Team turnovers per possession
  * Offensive rebounding percentage - the percentage of rebounds a team makes from their missed shots
  * Free throw rate - FTM / FGA  
  
The four factor model also includes the oppositions statistics.  

## Model Building 

Linear regression
  


## Model performance

R squared and predictions
RMSE = 4.7(%)  
MAE = 3.8(%)
Visuals





