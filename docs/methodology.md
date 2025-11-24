# Methodology (Toy Concept)

This document explains the rough structure of this sample project.

## Data

All data in `data/raw/` are **synthetic**, generated with `src/data_generation.py`:

- `soil_samples.csv` – randomised soil chemistry and erosion risk
- `water_quality.csv` – randomised pH, temperature, oxygen, turbidity, mercury
- `air_metrics.csv` – randomised CO2, CH4, smoke index, humidity
- `tree_species_traits.csv` – randomised species trait values (wood density, height, etc.)

These are **not** real Amazon measurements.

## Simulation

`src/simulate_restoration.py` builds a tiny toy model:

1. Assigns each plot a dominant species.
2. Computes a crude “health score” using soil carbon and pH.
3. If a plot is healthy and dominated by a pioneer species, it “restores” the plot by assigning a high wood-density, non-pioneer species.
4. Compares average wood density before and after restoration.

This is not ecologically realistic, but it demonstrates:

- How environmental variables and species traits might be linked,
- How a digital twin could test rules like “restore old-growth traits when conditions are ready”.

## Relationship to Lancaster Research

This is an **independent concept project** inspired by published work from Lancaster University on how human disturbances affect species, functional and phylogenetic diversity in Amazon forests.

It uses:

- No real field data  
- No confidential information  
- Only synthetic data and simple models  

The goal is to explore ideas, learn, and potentially start conversations with real researchers.
