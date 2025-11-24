import os
import numpy as np
import pandas as pd

# Make sure the output folders exist
os.makedirs("data/raw", exist_ok=True)

np.random.seed(42)  # for reproducibility

# ---- Soil samples ----
n_plots = 50
plot_ids = [f"P{str(i).zfill(3)}" for i in range(1, n_plots + 1)]

soil = pd.DataFrame({
    "plot_id": plot_ids,
    "nitrogen_pct": np.round(np.random.uniform(0.1, 0.4, n_plots), 3),
    "phosphorus_ppm": np.random.randint(5, 30, n_plots),
    "potassium_ppm": np.random.randint(100, 300, n_plots),
    "soil_carbon_pct": np.round(np.random.uniform(2.0, 6.0, n_plots), 2),
    "ph": np.round(np.random.uniform(4.5, 6.8, n_plots), 2),
    "erosion_risk": np.random.choice(["low", "medium", "high"], n_plots, p=[0.4, 0.4, 0.2])
})
soil.to_csv("data/raw/soil_samples.csv", index=False)

# ---- Water quality ----
water = pd.DataFrame({
    "plot_id": plot_ids,
    "ph": np.round(np.random.uniform(5.5, 7.5, n_plots), 2),
    "temperature_c": np.round(np.random.uniform(22, 30, n_plots), 1),
    "dissolved_oxygen_mg_per_l": np.round(np.random.uniform(4, 9, n_plots), 2),
    "turbidity_ntu": np.round(np.random.uniform(1, 30, n_plots), 1),
    "mercury_ug_per_l": np.round(np.random.exponential(0.5, n_plots), 3),
})
water.to_csv("data/raw/water_quality.csv", index=False)

# ---- Air metrics ----
air = pd.DataFrame({
    "plot_id": plot_ids,
    "co2_ppm": np.round(np.random.uniform(380, 450, n_plots), 1),
    "ch4_ppb": np.round(np.random.uniform(1700, 2000, n_plots), 1),
    "smoke_index": np.random.randint(0, 100, n_plots),
    "relative_humidity_pct": np.round(np.random.uniform(60, 100, n_plots), 1),
})
air.to_csv("data/raw/air_metrics.csv", index=False)

# ---- Tree species traits ----
n_species = 40
species_ids = [f"Species_{i:02d}" for i in range(1, n_species + 1)]

traits = pd.DataFrame({
    "species_id": species_ids,
    "wood_density_g_cm3": np.round(np.random.uniform(0.3, 0.9, n_species), 3),
    "max_height_m": np.round(np.random.uniform(10, 50, n_species), 1),
    "leaf_area_cm2": np.round(np.random.uniform(20, 200, n_species), 1),
    "seed_mass_g": np.round(np.random.uniform(0.1, 20, n_species), 2),
    "pioneer_status": np.random.choice(["pioneer", "non_pioneer"], n_species, p=[0.4, 0.6]),
})
traits.to_csv("data/raw/tree_species_traits.csv", index=False)

print("Synthetic raw data generated in data/raw/")
