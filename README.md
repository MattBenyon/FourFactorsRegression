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
* The training data was from the 2017, 2018, 2019 and 2020 seasons and the test data was from the current 2021 season.
* I could have used a larger training set howver I opted to use a smaller one as in the past half decade the game has evolved to a different play style centred around 3-point shooting and pace. I analysed both of these factors and decided the furthest I could go back to ensure that the prediction applied appropriately to the current state of the NBA.
* The model will be a linear regression
  

## Model performance
* The model had a root mean square error of 4.7(%) and a mean absolute error of 3.8(%)
* The R squared value for the four factor model was 0.882
* The R squared value for the traditional statistics was 0.873

The four factor model was slighlty more effective despite using much fewer data points. This means that the four factors are very helpful when assessing how good a team is.

## Predictions
  
  Traditional | Advanced (Four Factors)
--- | ---
![alt text](https://raw.githubusercontent.com/MattBenyon/FourFactorsRegression/master/Images/TradLarge.png "Traditional Stats") | ![alt text](https://raw.githubusercontent.com/MattBenyon/FourFactorsRegression/master/Images/FourFactors.png "Four Factors")  
  
These visualisations demonstrate the effectiveness of the model at predicting a teams win percentage. One issue with the four factor model is it appears to have over predicted for a couple of teams with lower win percentages. This is most likely down to the teams underachieving compared to their four factors. 
  
The model was particularly effective at predicting the win percentages of the teams with better win percentages while less effective with lower win percentage teams. This most likely is due to a number of complex interactions of different variables that can be summed up by the fact that poor teams are less consistent have less to play for.
  

Please feel free to make any recomendations on how to improve this project.





