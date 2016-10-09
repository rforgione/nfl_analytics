import csv
from os.path import dirname, abspath
import pandas as pd

PROJECT_ROOT = dirname(dirname(abspath(__file__)))
SOURCE_FILE_EXT = "/data/pbp-2015.csv"
OUTPUT_FILE_EXT = "/data/pbp-2015-clean.csv"

data = pd.read_csv(PROJECT_ROOT + SOURCE_FILE_EXT)

relevant_columns = [
    "GameId",
    "GameDate",
    "Quarter",
    "Minute",
    "Second",
    "OffenseTeam",
    "DefenseTeam",
    "Down",
    "ToGo",
    "YardLine",
    "SeriesFirstDown",
    "NextScore",
    "Description",
    "TeamWin",
    "SeasonYear",
    "Yards",
    "Formation",
    "PlayType",
    "IsRush",
    "IsPass",
    "IsIncomplete",
    "IsTouchdown",
    "PassType",
    "IsSack",
    "IsChallenge",
    "IsChallengeReversed",
    "Challenger",
    "IsMeasurement",
    "IsInterception",
    "IsFumble",
    "IsPenalty",
    "IsTwoPointConversion",
    "IsTwoPointConversionSuccessful",
    "RushDirection",
    "YardLineFixed",
    "YardLineDirection",
    "IsPenaltyAccepted",
    "PenaltyTeam",
    "IsNoPlay",
    "PenaltyType",
    "PenaltyYards"
]

data = data.loc[:,relevant_columns]
data.to_csv(PROJECT_ROOT + OUTPUT_FILE_EXT, index=False, header=False)
