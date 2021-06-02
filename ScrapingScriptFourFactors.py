# -*- coding: utf-8 -*-
"""
Created on Wed Jun  2 10:39:50 2021

@author: mattb
"""

import pandas as pd

from nba_api.stats.static import teams
from nba_api.stats.endpoints import leaguedashteamstats

# Create our testing data

teamsperformance_test = leaguedashteamstats.LeagueDashTeamStats(season='2020-21',
                                        measure_type_detailed_defense='Four Factors').get_data_frames()[0]
teamsperformance_test = teamsperformance_test.sort_values('TEAM_ID')
teamsperformance_test.drop(teamsperformance_test.columns.difference(['W_PCT','EFG_PCT',
                                                           'FTA_RATE','TM_TOV_PCT','OREB_PCT',
                                                           'OPP_EFG_PCT',
                                                          'OPP_FTA_RATE','OPP_TOV_PCT','OPP_OREB_PCT'])
                                                                 , 1, inplace=True)

# Create our training data from past few seasons

teamsperformance2020 = leaguedashteamstats.LeagueDashTeamStats(season='2019-20',
                                        measure_type_detailed_defense='Four Factors').get_data_frames()[0]
teamsperformance2020 = teamsperformance2020.sort_values('TEAM_ID')
teamsperformance2020.drop(teamsperformance2020.columns.difference(['W_PCT','EFG_PCT',
                                                           'FTA_RATE','TM_TOV_PCT','OREB_PCT',
                                                           'OPP_EFG_PCT',
                                                          'OPP_FTA_RATE','OPP_TOV_PCT','OPP_OREB_PCT'])
                                                                 , 1, inplace=True)

teamsperformance2019 = leaguedashteamstats.LeagueDashTeamStats(season='2018-19',
                                        measure_type_detailed_defense='Four Factors').get_data_frames()[0]
teamsperformance2019 = teamsperformance2019.sort_values('TEAM_ID')
teamsperformance2019.drop(teamsperformance2019.columns.difference(['W_PCT','EFG_PCT',
                                                           'FTA_RATE','TM_TOV_PCT','OREB_PCT',
                                                           'OPP_EFG_PCT',
                                                          'OPP_FTA_RATE','OPP_TOV_PCT','OPP_OREB_PCT'])
                                                                 , 1, inplace=True)

teamsperformance2018 = leaguedashteamstats.LeagueDashTeamStats(season='2017-18',
                                        measure_type_detailed_defense='Four Factors').get_data_frames()[0]
teamsperformance2018 = teamsperformance2018.sort_values('TEAM_ID')
teamsperformance2018.drop(teamsperformance2018.columns.difference(['W_PCT','EFG_PCT',
                                                           'FTA_RATE','TM_TOV_PCT','OREB_PCT',
                                                           'OPP_EFG_PCT',
                                                          'OPP_FTA_RATE','OPP_TOV_PCT','OPP_OREB_PCT'])
                                                                 , 1, inplace=True)

teamsperformance2017 = leaguedashteamstats.LeagueDashTeamStats(season='2016-17',
                                        measure_type_detailed_defense='Four Factors').get_data_frames()[0]
teamsperformance2017 = teamsperformance2017.sort_values('TEAM_ID')
teamsperformance2017.drop(teamsperformance2017.columns.difference(['W_PCT','EFG_PCT',
                                                           'FTA_RATE','TM_TOV_PCT','OREB_PCT',
                                                           'OPP_EFG_PCT',
                                                          'OPP_FTA_RATE','OPP_TOV_PCT','OPP_OREB_PCT'])
                                                                 , 1, inplace=True)

# Merge the test dataframes

teamsperformance_train = pd.concat([teamsperformance2019,
                                   teamsperformance2020,teamsperformance2018,teamsperformance2017], ignore_index=True)


# Export CSV files

teamsperformance_train.to_csv('Data/FourFactorsTrainingData.csv', index = False)

teamsperformance_test.to_csv('Data/FourFactorsTestingData.csv', index = False)
