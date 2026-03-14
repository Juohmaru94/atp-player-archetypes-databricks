# atp-player-archetypes-databricks

## Short project summary
This repository is an end-to-end analytics engineering and machine learning portfolio project built on historical ATP singles match data from Jeff Sackmann’s `tennis_atp` repository. The project demonstrates how to design a Databricks-first workflow that ingests raw data, models it using bronze/silver/gold layers, engineers player and match features, and generates cluster-based player archetypes plus dashboard-ready insights through 2024.

It is intentionally framed as a historical analytics and ML engineering project for portfolio and learning purposes, not a live betting system or real-time prediction engine.

## Business / analytics objective
Develop a reproducible tennis analytics platform that turns raw public match records into structured, analysis-ready datasets for:
- Player archetype discovery via unsupervised learning
- Match-stat performance analysis linked to winning outcomes
- Player-level insight generation suitable for reporting and dashboards

The objective is to show practical, job-ready skills in modern analytics engineering rather than claim production deployment.

## Key questions this project answers
- What recurring ATP player archetypes emerge from historical performance profiles?
- How do serving, returning, and error-related match statistics differ between wins and losses?
- Which statistical patterns are consistently associated with winning at a descriptive level?
- How can player-level profiles be translated into evidence-based performance insights?
- How can Databricks + PySpark + SQL pipelines support scalable sports analytics workflows?

## Tech stack
- **Platform:** Databricks (notebooks, jobs, Delta-style layered modeling)
- **Processing:** PySpark, SQL, Python (pandas/scikit-learn where appropriate)
- **Data modeling:** Bronze/Silver/Gold medallion architecture
- **Machine learning:** Clustering for player archetype segmentation
- **Analytics outputs:** Dashboard-ready gold tables and notebook-based case studies
- **Version control:** Git + GitHub
- **Data concepts:** ETL, feature engineering, dimensional modeling principles, data quality checks

## Architecture overview
The project follows a medallion-style architecture designed for transparency, reproducibility, and downstream analytics.

### Bronze layer (raw ingestion)
- Ingest ATP singles match files from source snapshots
- Preserve raw schema as closely as possible
- Add metadata fields (ingestion date, source file, load batch)

### Silver layer (cleaned and standardized)
- Standardize column names and data types
- Handle missing values and invalid records
- Normalize key identifiers (player names/IDs, tournament metadata, dates)
- Build consistent match-level and player-level intermediate tables

### Gold layer (analytics-ready marts)
- Curated feature sets for modeling and reporting
- Player aggregate performance profiles by season/window
- Archetype assignment tables from clustering outputs
- KPI-style tables for dashboard consumption

Core implementation is designed around **Databricks + PySpark + SQL**, with outputs intended for BI/dashboard tooling.

**Architecture diagram (placeholder):**
`[Insert architecture diagram image here — e.g., docs/images/architecture_overview.png]`

## Data source
Primary dataset: Jeff Sackmann’s public tennis data repository.

- Repository: `https://github.com/JeffSackmann/tennis_atp`
- Domain focus: ATP singles matches
- Practical analysis window: primarily **1991–2024** (chosen for richer stat availability)

This project does not claim ownership of the underlying source data. Users should review the source repository directly for full dataset details, update cadence, and license/usage terms.

## Project scope
In scope:
- Historical ATP singles analytics
- Databricks-based ETL and layered data modeling
- Feature engineering for player and match analysis
- Clustering-based player archetype segmentation
- Descriptive analysis of match stats associated with winning
- Dashboard-ready datasets and player case studies

Out of scope:
- Real-time match prediction services
- Live betting recommendations
- Claims of causal performance effects from observational data

## Repository structure
```text
atp-player-archetypes-databricks/
├── README.md
├── docs/
│   ├── project_scope.md
│   └── task_tracker.md
├── data/
│   ├── raw/                         # Source extracts (not committed or selectively versioned)
│   ├── bronze/                      # Raw-ingested tables/files
│   ├── silver/                      # Cleaned and standardized datasets
│   └── gold/                        # Analytics-ready marts/features
├── notebooks/
│   ├── 01_ingestion_etl
│   ├── 02_cleaning_transforms
│   ├── 03_feature_engineering
│   ├── 04_clustering_archetypes
│   ├── 05_winning_drivers
│   └── 06_player_case_studies
├── src/
│   ├── etl/
│   ├── features/
│   ├── modeling/
│   └── analytics/
├── dashboards/
│   ├── player_overview
│   ├── archetype_explorer
│   ├── winning_drivers
│   └── player_deep_dive
└── requirements.txt
```

## Methodology
### 1) Ingestion and ETL
- Pull and stage historical ATP files from source snapshots
- Apply schema checks and ingestion validation
- Load to bronze with traceable metadata

### 2) Cleaning and transformation
- Standardize formats across years and files
- Resolve common data quality issues (missing fields, inconsistent encoding, type coercion)
- Construct reliable silver-layer analytical keys

### 3) Feature engineering
- Create player-level and match-level features across serving, returning, and efficiency dimensions
- Aggregate rolling/seasonal indicators where appropriate
- Prepare normalized feature matrices for clustering and comparative analysis

### 4) Clustering / archetype analysis (flagship method)
Clustering is the flagship analytical method in this project. The goal is to segment players into interpretable style-based groups using historical performance characteristics.

Illustrative archetype labels include:
- **Big server**
- **Return specialist**
- **All-court aggressor**
- **Baseline grinder**

These labels are analytical abstractions used to summarize statistical style profiles, not definitive player identities.

### 5) Performance-driver analysis
In parallel with clustering, the project evaluates descriptive relationships between match statistics and winning outcomes.

- Focus is on robust descriptive analytics and effect-size interpretation
- Findings are framed as associations/correlations from historical observational data
- The analysis explicitly avoids causal overclaiming

### 6) Player case studies
- Build player-level deep dives that combine archetype assignment and trend metrics
- Generate evidence-based performance insights and practical discussion points
- Recommendations are framed as analytical guidance, not coaching certainties

## Planned dashboards / outputs
- **Player Overview:** profile, trends, and headline KPIs
- **Archetype Explorer:** cluster distribution, centroids, and comparable players
- **Winning Drivers:** key stat differentials associated with wins vs losses
- **Player Deep Dive:** longitudinal analysis and matchup-relevant context

**Dashboard screenshots (placeholders):**
- `[Insert Player Overview screenshot]`
- `[Insert Archetype Explorer screenshot]`
- `[Insert Winning Drivers screenshot]`
- `[Insert Player Deep Dive screenshot]`

**Example insights (placeholder):**
- `[Insert example insight #1]`
- `[Insert example insight #2]`

**Notebook links (placeholders):**
- `[Ingestion notebook]`
- `[Feature engineering notebook]`
- `[Clustering notebook]`
- `[Winning drivers notebook]`

## Skills demonstrated
- Databricks workflow design and notebook orchestration
- PySpark and SQL transformation logic across layered data models
- ETL engineering and data quality handling for multi-year historical data
- Feature engineering for unsupervised learning and analytics
- Clustering model development, interpretation, and segmentation storytelling
- Analytical communication with caveats around observational data
- Git/GitHub collaboration and portfolio-grade project documentation

## Limitations and caveats
- Public historical data can contain missingness, schema drift, and uneven stat coverage across periods
- The 1991–2024 scope improves consistency but still reflects source constraints
- Observational match statistics support descriptive/correlational analysis, not causal claims
- Archetype clusters are sensitive to feature design, scaling, and chosen clustering approach
- Player insights are evidence-based analytical interpretations, not deterministic prescriptions

## Roadmap / future improvements
- Finalize robust data validation checks and automated ETL quality reporting
- Add experiment tracking for clustering configurations and feature-set versions
- Expand matchup-context features (surface, opponent style, tournament tier)
- Harden dashboard semantic layer and documentation for reproducibility
- Add optional supervised benchmarking models for comparison (clearly separated from core scope)
- Improve CI checks for notebook/code quality and data contract validation

## How to run the project
1. **Clone repository**
   ```bash
   git clone https://github.com/<your-username>/atp-player-archetypes-databricks.git
   cd atp-player-archetypes-databricks
   ```
2. **Set up environment**
   - Create a Python virtual environment
   - Install dependencies from `requirements.txt` (placeholder until finalized)
3. **Acquire source data**
   - Download ATP files from Jeff Sackmann’s `tennis_atp` repository
   - Place files in configured raw data path or cloud storage mount used by Databricks
4. **Run pipeline sequence**
   - Execute ingestion notebooks/jobs (bronze)
   - Execute cleaning/standardization notebooks/jobs (silver)
   - Execute feature and analytics notebooks/jobs (gold)
5. **Run clustering and analysis notebooks**
   - Generate archetype assignments
   - Produce winning-driver tables and case-study artifacts
6. **Build dashboards**
   - Connect BI/dashboard layer to gold tables
   - Load project dashboard templates/placeholders

> Note: Some paths, jobs, and configs are intentionally placeholder while the repository build-out continues.

## Attribution
This project uses ATP match data made publicly available by Jeff Sackmann.

- Source repository: `https://github.com/JeffSackmann/tennis_atp`

All credit for source data collection and publication belongs to the original data author/maintainer. Please consult the source repository for current dataset scope and applicable license/usage terms.

## Resume-ready project summary
- Built an end-to-end Databricks analytics pipeline (bronze/silver/gold) for historical ATP singles match data, transforming raw public files into dashboard-ready analytical marts.
- Engineered player-level and match-level features and implemented clustering-based archetype segmentation (e.g., big server, return specialist, all-court aggressor, baseline grinder).
- Developed descriptive winning-driver analyses and player case-study outputs, emphasizing rigorous interpretation of correlation-based findings for portfolio-grade analytics communication.
