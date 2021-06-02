# -*- coding: utf-8 -*-
"""
Created on Wed Jun  2 10:54:36 2021

@author: mattb
"""
import pandas as pd
import numpy as np

import tensorflow as tf

import sklearn
from sklearn import linear_model
from sklearn.utils import shuffle

# Read in the CSV


#teamsperformance_train = pd.read_csv("FourFactorsTrainingData.csv")
teamsperformance_train = pd.read_csv("TraditionalLargeTrainingData.csv")

#teamsperformance_test = pd.read_csv("FourFactorsTestingData.csv")
teamsperformance_test = pd.read_csv("TraditionalLargeTestingData.csv")


# Split the data into numpy arrays for training and testing the model

predict = "W_PCT"

X_train = np.array(teamsperformance_train.drop([predict],1))

Y_train = np.array(teamsperformance_train[predict])

X_test = np.array(teamsperformance_test.drop([predict],1))

Y_test = np.array(teamsperformance_test[predict])

corr = teamsperformance_test.corr()
corr.style.background_gradient(cmap='coolwarm').set_precision(2)

# The model

linear = linear_model.LinearRegression()

linear.fit(X_train, Y_train)


acc = linear.score(X_test,Y_test)
print("Accuracy: ",round(acc,3))
print("Co: \n", linear.coef_)
print("Intercept: \n", linear.intercept_)
print('\n')

predictions = linear.predict(X_test)

for i in range(len(predictions)):
    print(round(predictions[i],3), X_test[i], round(Y_test[i],3))



# Predictions - comparing to actual outcomes

from nba_api.stats.endpoints import leaguedashteamstats

teams = leaguedashteamstats.LeagueDashTeamStats(season='2020-21',
                                        measure_type_detailed_defense='Four Factors').get_data_frames()[0]
teams = teams.sort_values('TEAM_ID')
teams.drop(teams.columns.difference([
            "TEAM_NAME",'W_PCT']), 1, inplace=True)
teams = teams.reset_index(drop=True)

predictions_df = pd.DataFrame(predictions, columns = ['Predicted WIN PCT'])
predicted_wins = teams.join(predictions_df)

difference =  (predicted_wins['Predicted WIN PCT'] - predicted_wins['W_PCT'])*100

difference_df = pd.DataFrame(difference, columns = ['difference %'])

predicted_wins = predicted_wins.join(difference_df)

games_in_season = 72

predicted_wins["Predicted Ws"] = round((predicted_wins['Predicted WIN PCT'] * games_in_season),0)
predicted_wins["Predicted Ls"] = (games_in_season - round((predicted_wins['Predicted WIN PCT'] * games_in_season),0))

print(predicted_wins.sort_values('Predicted Ws',ascending=False))


predicted_wins.to_csv("WinPredictionsTradLarge.csv")