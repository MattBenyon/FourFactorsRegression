# -*- coding: utf-8 -*-
"""
Created on Wed Jun  2 11:08:29 2021

@author: mattb
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Read the Four factor data

predicted_wins = pd.read_csv("WinPredictionsFourFactors.csv")

# Visualisation of the data

#select fivethirtyeight style for visuals
import matplotlib.style as style
plt.style.use('fivethirtyeight')

#create scatter plot- colour is the RMS of the difference
plt.scatter(predicted_wins['W_PCT'],predicted_wins['Predicted WIN PCT'],c= np.sqrt(predicted_wins["difference %"] ** 2),
            cmap="coolwarm",s=200)
#plot a straight line to show a 1:1 (or R^2 = 1) relationship for comp.
plt.plot([0.2, 0.8], [0.2, 0.8])

#format
plt.xlabel("Actual Win Percentage")
plt.ylabel("Predicted Win Percentage")
plt.title("Four Factors Predictions")
plt.text(0.25,0.75, "R-squared value = 0.882")
fig = plt.gcf()
fig.set_size_inches(10, 10)
plt.savefig('FourFactors.png')

plt.show()

# Read the Traditional data

predicted_wins = pd.read_csv("WinPredictionsTradLarge.csv")

# Visualisation of the data

import matplotlib.style as style
plt.style.use('fivethirtyeight')
plt.scatter(predicted_wins['W_PCT'],predicted_wins['Predicted WIN PCT'],c= np.sqrt(predicted_wins["difference %"] ** 2),
            cmap="coolwarm",s=200)
plt.plot([0.2, 0.8], [0.2, 0.8])

plt.xlabel("Actual Win Percentage")
plt.ylabel("Predicted Win Percentage")
plt.title("Traditional stats Predictions")
plt.text(0.25,0.75, "R-squared value = 0.873")
fig = plt.gcf()
fig.set_size_inches(10, 10)
plt.savefig('TradLarge.png')

plt.show()

# Correlation plot

import seaborn as sns

data = pd.read_csv('FourFactorsTrainingData.csv')
plt.style.use('default')
sns.set_theme(style="white")
corr = data.corr()

#https://seaborn.pydata.org/examples/many_pairwise_correlations.html
# Generate a mask for the upper triangle
mask = np.triu(np.ones_like(corr, dtype=bool))

# Set up the matplotlib figure
f, ax = plt.subplots(figsize=(11, 9))

# Generate a custom diverging colormap
cmap = sns.diverging_palette(230, 20, as_cmap=True)

# Draw the heatmap with the mask and correct aspect ratio
sns.heatmap(corr, mask=mask, cmap=cmap, vmax=.3, center=0,
            square=True, linewidths=.5, cbar_kws={"shrink": .5})
fig = plt.gcf()
fig.set_size_inches(18.5, 10.5)
plt.title("Correlation of basketball four factors",fontsize=26)
plt.savefig('FourFactorsCorr.png', bbox_inches="tight")
plt.show()

# Correlation plot for traditional statsitics

import seaborn as sns

data = pd.read_csv('TraditionalLargeTrainingData.csv')
plt.style.use('default')
sns.set_theme(style="white")
corr = data.corr()

# Generate a mask for the upper triangle
mask = np.triu(np.ones_like(corr, dtype=bool))

# Set up the matplotlib figure
f, ax = plt.subplots(figsize=(11, 9))

# Generate a custom diverging colormap
cmap = sns.diverging_palette(230, 20, as_cmap=True)

# Draw the heatmap with the mask and correct aspect ratio
sns.heatmap(corr, mask=mask, cmap=cmap, vmax=.3, center=0,
            square=True, linewidths=.5, cbar_kws={"shrink": .5})
fig = plt.gcf()
fig.set_size_inches(18.5, 10.5)
plt.title("Correlation of basketball statistics",fontsize=26)
plt.savefig('TraditionalCorr.png', bbox_inches="tight")
plt.show()