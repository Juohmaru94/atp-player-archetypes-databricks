# Table Plan

## Bronze
- `bronze_atp_matches` — raw union of `atp_matches_2020.csv` to `atp_matches_2024.csv` with added `source_file` and `season`
- `bronze_atp_players` — raw `atp_players.csv`

## Silver
- `silver_matches_clean` — cleaned match-level table with parsed dates, cleaned types, and created `match_id`
- `silver_players_clean` — cleaned player reference table
- `silver_player_match` — normalized player-match table with one row per player per match

## Gold
- `fact_player_match` — one row per player per match, created by normalizing winner and loser sides
- `fact_player_season` — one row per player per season with aggregated performance metrics
- `player_archetype_features` — clustering-ready player-season feature table with minimum match threshold
