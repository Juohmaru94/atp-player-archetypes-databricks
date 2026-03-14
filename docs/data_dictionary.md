# Data Dictionary

## Source Files

- `atp_matches_2020.csv` to `atp_matches_2024.csv` — ATP tour-level main-draw match data for analysis
- `atp_players.csv` — player reference data
- `atp_rankings_current.csv` — not used in v1

## V1 Scope

- Seasons used: 2020–2024
- Tour: ATP main tour
- Match type: singles
- Primary method: player archetype clustering
- Secondary analysis: match stats associated with winning

## Target Table 1

**Table name:** `fact_player_match`  
**Grain:** one row per player per match  
**Purpose:** normalized table for analysis, where each match becomes two rows: one for the winner and one for the loser

## Planned Core Columns for `fact_player_match`

### Match context
- `match_id` — unique match identifier to be created in the project
- `tourney_id` — tournament identifier
- `tourney_name` — tournament name
- `surface` — court surface
- `draw_size` — tournament draw size
- `tourney_level` — event level
- `tourney_date` — tournament date
- `match_num` — match number within tournament
- `round` — round of the match
- `best_of` — best-of format
- `minutes` — match duration in minutes

### Player fields
- `player_id` — player identifier
- `player_name` — player name
- `player_hand` — handedness
- `player_ht` — height
- `player_age` — age at match time
- `player_rank` — ranking at match time
- `player_rank_points` — ranking points at match time

### Opponent fields
- `opponent_id` — opponent identifier
- `opponent_name` — opponent name
- `opponent_hand` — opponent handedness
- `opponent_ht` — opponent height
- `opponent_age` — opponent age at match time
- `opponent_rank` — opponent ranking at match time
- `opponent_rank_points` — opponent ranking points at match time

### Outcome field
- `won_match` — 1 if player won, 0 if player lost

### Player performance stats
- `ace` — aces
- `df` — double faults
- `svpt` — service points played
- `1stIn` — first serves in
- `1stWon` — first serve points won
- `2ndWon` — second serve points won
- `SvGms` — service games played
- `bpSaved` — break points saved
- `bpFaced` — break points faced

### Opponent performance stats
- `opp_ace` — opponent aces
- `opp_df` — opponent double faults
- `opp_svpt` — opponent service points played
- `opp_1stIn` — opponent first serves in
- `opp_1stWon` — opponent first serve points won
- `opp_2ndWon` — opponent second serve points won
- `opp_SvGms` — opponent service games played
- `opp_bpSaved` — opponent break points saved
- `opp_bpFaced` — opponent break points faced

## Notes

- `fact_player_match` will be the main base table for analysis.
- This table will later feed player-level aggregation, clustering features, and winning-driver analysis.
- Rankings data will not be separately integrated in v1 unless needed later.

## Raw Source Schema Notes

### Match files
- Match files contain winner-side and loser-side fields in a denormalized structure.
- Rankings and ranking points are already included in the match files.
- Player performance stats are available separately for winner and loser.

### Player file
- `atp_players.csv` is a reference table with player-level biographical fields.
- It can be used to validate or enrich player identity fields later if needed.
