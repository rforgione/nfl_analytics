drop table if exists nfl.pbp_data_2015;
create table nfl.pbp_data_2015 (
  game_id int,
  game_date date,
  quarter int,
  minute int,
  second int,
  offense_team varchar(3),
  defense_team varchar(3),
  down int,
  to_go int,
  yard_line int,
  series_first_down int,
  next_score int,
  description varchar(1024),
  team_win int,
  season_year int,
  yards int,
  formation varchar(32),
  play_type varchar(32),
  is_rush int,
  is_pass int,
  is_incomplete int,
  is_touchdown int,
  pass_type varchar(32),
  is_sack int,
  is_challenge int,
  is_challenge_reversed int,
  challenger varchar(32),
  is_measurement int,
  is_interception int,
  is_fumble int,
  is_penalty int,
  is_two_point_conversion int,
  is_two_point_conversion_successful int,
  rush_direction varchar(32),
  yard_line_fixed int,
  yard_line_direction varchar(3),
  is_penalty_accepted int,
  penalty_team varchar(32),
  is_no_play int,
  penalty_type varchar(64),
  penalty_yards int
);

copy nfl.pbp_data_2015
from '/home/ubuntu/development/nfl_analytics/data/pbp-2015-clean.csv'
with delimiter ','
csv quote '"'
;
