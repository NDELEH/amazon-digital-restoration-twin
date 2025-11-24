# Amazon Digital Restoration Twin (Concept Project)

> ⚠️ **Important:**  
> This is a **student / independent sample project** using **synthetic data only**.  
> It is **not an official Lancaster University project**, but is **inspired by** their research on how human disturbances are transforming Amazon forest ecology and evolutionary history.

![Status](https://img.shields.io/badge/status-concept--prototype-blue)
![Python](https://img.shields.io/badge/python-3.10+-green)
![Synthetic Data](https://img.shields.io/badge/data-synthetic-orange)

## Background & Inspiration

This project is a small, home-built attempt to explore an idea inspired by recent work from researchers at Lancaster University and collaborators on how logging, fire and other disturbances affect the **species**, **functional**, and **evolutionary** diversity of Amazonian forests.

Their work shows that disturbed and secondary forests are not just “less diverse” versions of intact forest – they are **ecologically and evolutionarily different systems**.

This repository is a **toy, synthetic-data “digital twin” concept** that:

- Imagines how soil, water, air and biodiversity data could be combined
- Uses fake data to simulate simple “restoration scenarios”
- Documents a possible framework for a future, real project

I built this from home without access to real field data, purely as a learning exercise & idea to share.

## What this repo contains

- `README.md` – overview (this file)
- `proposal/digital_amazon_restoration_proposal.md` – written concept proposal inspired by Lancaster’s research
- `data/raw/` – **synthetic** CSV files representing soil, water, air and tree trait data
- `src/data_generation.py` – script to generate the synthetic datasets
- `src/simulate_restoration.py` – very simple “restoration” simulation using the fake data
- `docs/methodology.md` – notes on the assumptions and structure

## Important notes

- All data in this repo are **synthetic / randomly generated**.
- This project **does not use any confidential, field, or proprietary data**.
- This project is **not endorsed by** Lancaster University or the authors of the original study.
- It is simply a **student/independent attempt** to think about digital tools that could support Amazon restoration.

## How to run (locally)

1. Clone the repo:

   ```bash
   git clone https://github.com/<NDELEH/amazon-digital-restoration-twin.git
   cd amazon-digital-restoration-twin
