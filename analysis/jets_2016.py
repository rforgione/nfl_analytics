from analysis_config import *
import pandas as pd

cols = [
    "week",
    "day",
    "date",
    "boxscore",
    "result",
    "ot",
    "resulting_record",
    "home_away",
    "opponent",
    "team_score",
    "opposing_score",
    "first_downs",
    "total_yards",
    "passing_yards",
    "rushing_yards",
    "turnovers",
    "fist_downs_allowed",
    "total_yards_allowed",
    "passing_yards_allowed",
    "rushing_yards_allowed",
    "turnovers_forced",
    "offensive_pts_to_expected",
    "defensive_pts_to_expected",
    "sp_tm_pts_to_expected"
]
data = pd.read_html("http://www.pro-football-reference.com/teams/nyj/2016.htm", attrs={"id": "games"}, skiprows=0)[0]
# 'OT' column comes through full of nulls, so we fill with Falses
data.iloc[:,5] = data.iloc[:,5].fillna(value=False).apply(int)
data = data.dropna(axis=1, how="all")
data.columns = cols

data.dropna(axis=0, how="all", subset=['date'])
data.to_csv("data/jets_2016.csv", index=False)
