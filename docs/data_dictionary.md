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

### `fact_player_match`
- Source: `silver_matches_clean`
- Grain: one row per player per match
- Logic:
  - each source match becomes two rows
  - one row for the winner as player
  - one row for the loser as player
- Main use:
  - player-level aggregation
  - archetype feature engineering
  - match stats analysis

### `fact_player_season`
- Source: `fact_player_match`
- Grain: one row per player per season
- Main use:
  - seasonal player summaries
  - clustering feature input
  - player comparison analysis
- Example metrics:
  - matches played
  - wins
  - win rate
  - ace per match
  - double faults per match
  - first serve in rate
  - first serve win rate
  - second serve win rate
  - break points saved rate

### `player_archetype_features`
- Source: `fact_player_season`
- Grain: one row per player per season
- Filter:
  - only player-seasons with at least 10 matches played
- Main use:
  - input table for archetype clustering
- Initial feature set:
  - win rate
  - average rank
  - ace per match
  - double faults per match
  - first serve in rate
  - first serve win rate
  - second serve win rate
  - break points saved rate

### `player_archetype_clusters`
- Source: `player_archetype_features`
- Grain: one row per player per season
- Method:
  - standardized numeric features
  - KMeans clustering with 4 clusters for the first pass
- Main use:
  - identify broad player archetypes
  - compare player styles across seasons

### `cluster_profiles`
- Source: `player_archetype_clusters`
- Grain: one row per cluster
- Main use:
  - interpret cluster characteristics
  - compare average performance/style metrics across clusters
- Includes:
  - average feature values by cluster
  - player-season counts
  - unique player counts

### `player_archetype_clusters_labeled`
- Source: `player_archetype_clusters`
- Grain: one row per player per season
- Main use:
  - assign human-readable archetype names to each cluster
- Current first-pass labels:
  - High-Risk Big Server
  - Balanced All-Court Player
  - Lower-Power Grinder
  - Elite Big Server

### `first_serve_in_win_rate_buckets`
- Source: `fact_player_match`
- Grain: one row per first-serve-in percentage bucket
- Main use:
  - analyze how match win rate changes across first-serve-in percentage ranges
- Notes:
  - this is descriptive analysis
  - it shows association, not causation

### `first_serve_points_won_win_rate_buckets`
- Source: `fact_player_match`
- Grain: one row per first-serve-points-won percentage bucket
- Main use:
  - analyze how win rate changes across first-serve effectiveness ranges
- Notes:
  - this is descriptive analysis
  - it shows association, not causation

### `second_serve_win_rate_buckets`
- Source: `fact_player_match`
- Grain: one row per second-serve-win-rate bucket
- Main use:
  - analyze how win rate changes across second-serve effectiveness ranges
- Notes:
  - this is descriptive analysis
  - it shows association, not causation
 
### `insight_summary_table`
- Source:
  - `first_serve_in_win_rate_buckets`
  - `first_serve_points_won_win_rate_buckets`
  - `second_serve_win_rate_buckets`
- Grain: one row per metric and bucket
- Main use:
  - compare descriptive win-rate relationships across key serving metrics

### `break_points_saved_rate_buckets`
- Source: `fact_player_match`
- Grain: one row per break-points-saved-rate bucket
- Main use:
  - analyze how win rate changes across break-point defense ranges
- Notes:
  - this is descriptive analysis
  - it shows association, not causation

### `aces_per_match_buckets`
- Source: `fact_player_match`
- Grain: one row per ace-count bucket
- Main use:
  - analyze how win rate changes across ace volume ranges
- Notes:
  - this is descriptive analysis
  - it shows association, not causation

### `double_fault_buckets`
- Source: `fact_player_match`
- Grain: one row per double-fault-count bucket
- Main use:
  - analyze how win rate changes across double-fault ranges
- Notes:
  - this is descriptive analysis
  - it shows association, not causation

### `win_rate_by_surface`
- Source: `fact_player_match`
- Grain: one row per surface
- Main use:
  - compare player-match win distribution across surfaces

### `first_serve_points_won_by_surface`
- Source: `fact_player_match`
- Grain: one row per surface
- Main use:
  - compare first-serve effectiveness across surfaces

### `aces_by_surface`
- Source: `fact_player_match`
- Grain: one row per surface
- Main use:
  - compare ace volume, double faults, and match duration across surfaces

### `surface_stat_differences`
- Source: `fact_player_match`
- Grain: one row per surface
- Main use:
  - compare core serve and match metrics across surfaces
- Notes:
  - better suited than raw win-rate summaries for the player-match table

### Player case study outputs
- Source: `fact_player_match` and `player_archetype_clusters_labeled`
- Main use:
  - create player-specific summary tables for portfolio case studies
- Output files:
  - `{player_name}_case_study_summary.csv`
  - `{player_name}_case_study_surface.csv`
  - `{player_name}_case_study_season.csv`
  - `{player_name}_case_study_clusters.csv`

### Player comparison documents
- Main use:
  - compare two player case studies side by side
  - show how players in the same cluster can still differ in surface strengths and match profile  

### Documentation outputs
- `results_summary.md` — high-level summary of clustering, descriptive insights, and case studies
- `chart_index.md` — organized list of visual outputs for the portfolio  

## Bronze Output

### `bronze_atp_matches`
- Source: `atp_matches_2020.csv` to `atp_matches_2024.csv`
- Grain: one row per match
- Notes:
  - raw union of yearly match files
  - includes added `source_file` column
  - includes added `season` column

## Silver Output

### `silver_matches_clean`
- Source: `bronze_atp_matches`
- Grain: one row per match
- Key additions:
  - parsed `tourney_date`
  - standardized types
  - created `match_id`



