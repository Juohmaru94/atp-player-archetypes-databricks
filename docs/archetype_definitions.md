# Archetype Definitions

This document explains the four first-pass player archetypes created in the clustering stage of the project.

These archetypes were generated from player-season features using KMeans clustering on the following metrics:

- win rate
- average player rank
- aces per match
- double faults per match
- first serve in rate
- first serve win rate
- second serve win rate
- break points saved rate

Important note: these archetypes are **analytical labels**, not absolute truths. They are meant to summarize broad player-season patterns in the data, not to fully define every aspect of a player’s game.

---

## 1. High-Risk Big Server

### Why this label was chosen
This cluster combines:
- high ace production
- very strong first-serve win rate
- relatively low first-serve-in rate
- elevated double-fault rate
- weaker average ranking and win rate than the top-serving cluster

### What it means
These players appear to rely heavily on aggressive serving. Their profile suggests that serve can be a major weapon, but also comes with more volatility and risk. Compared with the Elite Big Server group, they look less efficient overall and less successful in match outcomes.

### Typical characteristics
- high aces
- high double faults
- strong first-serve effectiveness
- lower consistency than top-tier big servers
- more uneven overall results

### How to explain it in conversation
> This archetype represents players with strong serve-driven profiles, but with more risk and less overall match efficiency than the elite version of that style.

---

## 2. Balanced All-Court Player

### Why this label was chosen
This cluster sits in the middle on many metrics:
- moderate ace production
- moderate double-fault rate
- decent first- and second-serve performance
- better ranking and win rate than the lower-power cluster
- less extreme serve profile than the big-server groups

### What it means
These players do not appear to depend on one dominant serve-based trait. Instead, they look more balanced across multiple areas. They are neither the most explosive servers nor the weakest power players in the sample.

### Typical characteristics
- moderate serve strength
- moderate serve risk
- solid but not extreme winning profile
- relatively balanced statistical profile

### How to explain it in conversation
> This archetype captures players with a more rounded performance profile rather than one built around extreme serve dominance or low-power grinding.

---

## 3. Lower-Power Grinder

### Why this label was chosen
This cluster showed:
- the lowest ace production
- the weakest first-serve win rate
- the weakest break-points-saved profile
- the weakest average ranking and lowest win rate among the four groups
- relatively high first-serve-in rate, but without strong payoff on serve effectiveness

### What it means
This group appears less serve-dominant and less explosive. The label “grinder” reflects a profile that looks more likely to rely on extended play and lower-power match patterns, though the current feature set is still serve-heavy and does not directly measure rally tolerance or defensive skill.

### Typical characteristics
- low ace output
- lower first-serve effectiveness
- weaker overall results
- less ability to generate cheap points on serve

### Important caution
This is the cluster label that should be explained most carefully. It does **not** mean these players are literally classic clay-court grinders in every tactical sense. It means that, within this project’s feature space, they look less serve-powered and less explosive than the other groups.

### How to explain it in conversation
> This archetype refers to player-seasons with lower serve power and weaker overall performance metrics, not necessarily to a full tactical scouting label.

---

## 4. Elite Big Server

### Why this label was chosen
This cluster showed:
- very high ace production
- very strong first-serve win rate
- the strongest second-serve win rate in the sample
- the best break-points-saved profile
- the best average ranking and highest win rate of all four clusters

### What it means
This is the strongest serve-driven cluster in the project. These players combine big serve performance with strong overall match results. Unlike the High-Risk Big Server group, they do not just hit a lot of aces — they also convert that serve strength into consistently better outcomes.

### Typical characteristics
- high aces
- strong first-serve effectiveness
- strong second-serve effectiveness
- strong overall winning profile
- top-tier ranking level

### How to explain it in conversation
> This archetype represents the most effective serve-led player-seasons in the dataset: players who combine serve power with consistently strong overall results.

---

# How to Talk About the Archetypes in Interviews

A good way to explain the archetypes is:

> These are unsupervised cluster labels based on player-season performance features. I used them as interpretable summaries of broad statistical profiles, not as absolute truths about a player’s identity. The labels help organize the data, but player-level case studies are still needed because players in the same archetype can differ meaningfully by surface, season, and performance pattern.

That last point is important. One of the strengths of the project is that it shows:
- clustering is useful
- clustering is not the whole story

---

# Final Caveat

These archetypes depend on the features included in the model. Because the feature set is currently centered on serve performance and match outcome indicators, the labels should be interpreted as **data-driven summaries of this feature space**, not as complete tactical scouting categories.