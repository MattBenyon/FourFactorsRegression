# -*- coding: utf-8 -*-
"""
Created on Wed Jun  2 10:39:50 2021

@author: mattb
"""

import pandas as pd

from nba_api.stats.static import teams
from nba_api.stats.endpoints import leaguedashteamstats

# Create our testing data

teamsperformance = leaguedashteamstats.LeagueDashTeamStats(season='2020-21',per_mode_detailed="PerGame").get_data_frames()[0]
teamsperformance = teamsperformance.sort_values('TEAM_ID')
teamsperformance.drop(teamsperformance.columns.difference(["W_PCT",
            "FGM",
            "FGA",
            "FG_PCT",
            "FG3M",
            "FG3A",
            "FG3_PCT",
            "FTM",
            "FTA",
            "FT_PCT",
            "OREB",
            "DREB",
            "REB",
            "AST",
            "TOV",
            "STL",
            "BLK",
            "BLKA",
            "PF",
            "PFD",
            "PTS"]), 1, inplace=True)
teamsperformanceD = leaguedashteamstats.LeagueDashTeamStats(season='2020-21',per_mode_detailed="PerGame",measure_type_detailed_defense="Opponent").get_data_frames()[0]
teamsperformanceD = teamsperformanceD.sort_values('TEAM_ID')
teamsperformanceD.drop(teamsperformanceD.columns.difference([
            "OPP_FGM",
            "OPP_FGA",
            "OPP_FG_PCT",
            "OPP_FG3M",
            "OPP_FG3A",
            "OPP_FG3_PCT",
            "OPP_FTM",
            "OPP_FTA",
            "OPP_FT_PCT",
            "OPP_OREB",
            "OPP_DREB",
            "OPP_REB",
            "OPP_AST",
            "OPP_TOV",
            "OPP_STL",
            "OPP_BLK",
            "OPP_BLKA",
            "OPP_PF",
            "OPP_PFD",
            "OPP_PTS"]), 1, inplace=True)

teamsperformance_test = pd.concat([teamsperformance,teamsperformanceD],axis = 1)

# Create our training data from past few seasons

teamsperformance2020 = leaguedashteamstats.LeagueDashTeamStats(season='2019-20',per_mode_detailed="PerGame").get_data_frames()[0]
teamsperformance2020 = teamsperformance2020.sort_values('TEAM_ID')
teamsperformance2020.drop(teamsperformance2020.columns.difference(["W_PCT",
            "FGM",
            "FGA",
            "FG_PCT",
            "FG3M",
            "FG3A",
            "FG3_PCT",
            "FTM",
            "FTA",
            "FT_PCT",
            "OREB",
            "DREB",
            "REB",
            "AST",
            "TOV",
            "STL",
            "BLK",
            "BLKA",
            "PF",
            "PFD",
            "PTS"]), 1, inplace=True)
teamsperformance2020D = leaguedashteamstats.LeagueDashTeamStats(season='2019-20',per_mode_detailed="PerGame",measure_type_detailed_defense="Opponent").get_data_frames()[0]
teamsperformance2020D = teamsperformance2020D.sort_values('TEAM_ID')
teamsperformance2020D.drop(teamsperformance2020D.columns.difference([
            "OPP_FGM",
            "OPP_FGA",
            "OPP_FG_PCT",
            "OPP_FG3M",
            "OPP_FG3A",
            "OPP_FG3_PCT",
            "OPP_FTM",
            "OPP_FTA",
            "OPP_FT_PCT",
            "OPP_OREB",
            "OPP_DREB",
            "OPP_REB",
            "OPP_AST",
            "OPP_TOV",
            "OPP_STL",
            "OPP_BLK",
            "OPP_BLKA",
            "OPP_PF",
            "OPP_PFD",
            "OPP_PTS"]), 1, inplace=True)

teamsperformance2020 = pd.concat([teamsperformance2020,teamsperformance2020D],axis = 1)

teamsperformance2019 = leaguedashteamstats.LeagueDashTeamStats(season='2018-19',per_mode_detailed="PerGame").get_data_frames()[0]
teamsperformance2019 = teamsperformance2019.sort_values('TEAM_ID')
teamsperformance2019.drop(teamsperformance2019.columns.difference(["W_PCT",
            "FGM",
            "FGA",
            "FG_PCT",
            "FG3M",
            "FG3A",
            "FG3_PCT",
            "FTM",
            "FTA",
            "FT_PCT",
            "OREB",
            "DREB",
            "REB",
            "AST",
            "TOV",
            "STL",
            "BLK",
            "BLKA",
            "PF",
            "PFD",
            "PTS"]), 1, inplace=True)
teamsperformance2019D = leaguedashteamstats.LeagueDashTeamStats(season='2018-19',per_mode_detailed="PerGame",measure_type_detailed_defense="Opponent").get_data_frames()[0]
teamsperformance2019D = teamsperformance2019D.sort_values('TEAM_ID')
teamsperformance2019D.drop(teamsperformance2019D.columns.difference([
            "OPP_FGM",
            "OPP_FGA",
            "OPP_FG_PCT",
            "OPP_FG3M",
            "OPP_FG3A",
            "OPP_FG3_PCT",
            "OPP_FTM",
            "OPP_FTA",
            "OPP_FT_PCT",
            "OPP_OREB",
            "OPP_DREB",
            "OPP_REB",
            "OPP_AST",
            "OPP_TOV",
            "OPP_STL",
            "OPP_BLK",
            "OPP_BLKA",
            "OPP_PF",
            "OPP_PFD",
            "OPP_PTS"]), 1, inplace=True)

teamsperformance2019 = pd.concat([teamsperformance2019,teamsperformance2019D],axis = 1)

teamsperformance2018 = leaguedashteamstats.LeagueDashTeamStats(season='2017-18',per_mode_detailed="PerGame").get_data_frames()[0]
teamsperformance2018 = teamsperformance2018.sort_values('TEAM_ID')
teamsperformance2018.drop(teamsperformance2018.columns.difference(["W_PCT",
            "FGM",
            "FGA",
            "FG_PCT",
            "FG3M",
            "FG3A",
            "FG3_PCT",
            "FTM",
            "FTA",
            "FT_PCT",
            "OREB",
            "DREB",
            "REB",
            "AST",
            "TOV",
            "STL",
            "BLK",
            "BLKA",
            "PF",
            "PFD",
            "PTS"]), 1, inplace=True)
teamsperformance2018D = leaguedashteamstats.LeagueDashTeamStats(season='2017-18',per_mode_detailed="PerGame",measure_type_detailed_defense="Opponent").get_data_frames()[0]
teamsperformance2018D = teamsperformance2018D.sort_values('TEAM_ID')
teamsperformance2018D.drop(teamsperformance2018D.columns.difference([
            "OPP_FGM",
            "OPP_FGA",
            "OPP_FG_PCT",
            "OPP_FG3M",
            "OPP_FG3A",
            "OPP_FG3_PCT",
            "OPP_FTM",
            "OPP_FTA",
            "OPP_FT_PCT",
            "OPP_OREB",
            "OPP_DREB",
            "OPP_REB",
            "OPP_AST",
            "OPP_TOV",
            "OPP_STL",
            "OPP_BLK",
            "OPP_BLKA",
            "OPP_PF",
            "OPP_PFD",
            "OPP_PTS"]), 1, inplace=True)

teamsperformance2018 = pd.concat([teamsperformance2018,teamsperformance2018D],axis = 1)

teamsperformance2017 = leaguedashteamstats.LeagueDashTeamStats(season='2016-17',per_mode_detailed="PerGame").get_data_frames()[0]
teamsperformance2017 = teamsperformance2017.sort_values('TEAM_ID')
teamsperformance2017.drop(teamsperformance2017.columns.difference(["W_PCT",
            "FGM",
            "FGA",
            "FG_PCT",
            "FG3M",
            "FG3A",
            "FG3_PCT",
            "FTM",
            "FTA",
            "FT_PCT",
            "OREB",
            "DREB",
            "REB",
            "AST",
            "TOV",
            "STL",
            "BLK",
            "BLKA",
            "PF",
            "PFD",
            "PTS"]), 1, inplace=True)
teamsperformance2017D = leaguedashteamstats.LeagueDashTeamStats(season='2016-17',per_mode_detailed="PerGame",measure_type_detailed_defense="Opponent").get_data_frames()[0]
teamsperformance2017D = teamsperformance2017D.sort_values('TEAM_ID')
teamsperformance2017D.drop(teamsperformance2017D.columns.difference([
            "OPP_FGM",
            "OPP_FGA",
            "OPP_FG_PCT",
            "OPP_FG3M",
            "OPP_FG3A",
            "OPP_FG3_PCT",
            "OPP_FTM",
            "OPP_FTA",
            "OPP_FT_PCT",
            "OPP_OREB",
            "OPP_DREB",
            "OPP_REB",
            "OPP_AST",
            "OPP_TOV",
            "OPP_STL",
            "OPP_BLK",
            "OPP_BLKA",
            "OPP_PF",
            "OPP_PFD",
            "OPP_PTS"]), 1, inplace=True)

teamsperformance2017 = pd.concat([teamsperformance2017,teamsperformance2017D],axis = 1)
# Merge the test dataframes

teamsperformance_train = pd.concat([teamsperformance2019,
                                   teamsperformance2020,teamsperformance2018,teamsperformance2017], ignore_index=True)


# Export CSV files

teamsperformance_train.to_csv('TraditionalLargeTrainingData.csv', index = False)

teamsperformance_test.to_csv('TraditionalLargeTestingData.csv', index = False)
