import pandas as pd
import numpy as np

# Load synthetic data
soil = pd.read_csv("data/raw/soil_samples.csv")
traits = pd.read_csv("data/raw/tree_species_traits.csv")

# Create a fake "community" table: each plot has a dominant species
np.random.seed(123)
community = pd.DataFrame({
    "plot_id": soil["plot_id"],
    "dominant_species": np.random.choice(traits["species_id"], len(soil))
})

# Merge community with traits and soil
merged = community.merge(traits, left_on="dominant_species", right_on="species_id")
merged = merged.merge(soil, on="plot_id", suffixes=("_trait", "_soil"))

# Define a simple "health score" using soil carbon and pH
def health_score(row):
    carbon_score = (row["soil_carbon_pct"] - 2.0) / (6.0 - 2.0)  # scale 2–6% to 0–1
    ph_score = 1.0 - abs(row["ph"] - 6.0) / 2.0  # best around pH 6
    return max(0.0, min(1.0, 0.5 * carbon_score + 0.5 * ph_score))

merged["health_score"] = merged.apply(health_score, axis=1)

# Simple "restoration" rule:
# If health_score > 0.6 and current species is a pioneer,
# we "restore" by switching to a random non_pioneer high wood density species.
non_pioneers = traits[traits["pioneer_status"] == "non_pioneer"].copy()
high_density = non_pioneers.sort_values("wood_density_g_cm3", ascending=False)

restored_species = []

for _, row in merged.iterrows():
    if row["health_score"] > 0.6 and row["pioneer_status"] == "pioneer":
        # pick one of the top 5 densest species
        candidate = np.random.choice(high_density["species_id"].head(5))
        restored_species.append(candidate)
    else:
        restored_species.append(row["dominant_species"])

merged["restored_species"] = restored_species

# Compare original vs restored wood density
merged = merged.merge(
    traits[["species_id", "wood_density_g_cm3"]],
    left_on="restored_species",
    right_on="species_id",
    how="left",
    suffixes=("_original", "_restored"),
)

avg_original = merged["wood_density_g_cm3_original"].mean()
avg_restored = merged["wood_density_g_cm3_restored"].mean()

print(f"Average wood density (original community): {avg_original:.3f} g/cm^3")
print(f"Average wood density (after simple 'restoration'): {avg_restored:.3f} g/cm^3")

if avg_restored > avg_original:
    print("Restoration scenario increased average wood density (a rough proxy for old-growth traits).")
else:
    print("Restoration scenario did not improve average wood density in this toy model.")
