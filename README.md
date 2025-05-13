# 🗽 NY Crime Analytics Application — Built with Preswald

Preswald - "Visual. Accessible. Actionable."

Hey there!
Welcome to a deep dive into crime trends across New York State — wrapped in a clean, interactive dashboard built entirely in **Python** with the magic of **Preswald**.

This isn’t just another data project — this is a **curious blend of public safety, data storytelling, and open-source passion**. 

---

## What This Dashboard Application Does

Ever wondered which NY county had the highest violent crime rate in 2010?  
Or how firearm-related crimes have trended over the last 30 years?  
This dashboard lets you explore all that and more:

🧭 **Interactive filtering**  
🎯 **County-wise breakdowns**  
📊 **Bar charts, line graphs, histograms** — all powered by **Plotly**  
📅 Data from **1990 to Present**  
💻 Runs entirely in the browser (thanks to [Preswald](https://github.com/StructuredLabs/preswald))

It’s like Google Maps for crime — just with fewer detours and cleaner data 😉

---

## Where the Data Comes From

Data is straight from the **Division of Criminal Justice Services (DCJS)** and pulled from:

👉 [data.gov Crime Dataset](https://catalog.data.gov/dataset/index-violent-property-and-firearm-rates-by-county-beginning-1990)

It includes:
- Population-adjusted crime **rates per 100k**
- Categories: **Violent**, **Property**, and **Firearm-related** crimes
- Granular to the **county-level**

This isn’t scraped data — it’s the real deal.

---

## How to Run It

> Super easy. You just need Python + Preswald.

1. Install Preswald  
   ```bash
   pip install preswald
   ```

This interactive application visualizes crime trends across counties in New York State from 1990 to 2023, using official data from the **Division of Criminal Justice Services (DCJS)**.

Built with [Preswald](https://github.com/StructuredLabs/preswald).

---

## Features

- Select any **county** and **year** to explore crime stats
- View **rates per 100,000 residents** for:
  - Violent crimes (murder, rape, robbery, aggravated assault)
  - Property crimes (burglary, larceny, motor vehicle theft)
  - Firearm-related incidents
- Interactive charts:
  - Bar chart of crime breakdown
  - Line chart showing trends over time
  - Histogram comparing counties
- Clean, responsive UI powered by Preswald

---

## 📁 Dataset

- 📦 **Name**: Index, Violent, Property and Firearm Rates by County (Beginning 1990)  
- 📌 **Source**: [data.gov](https://catalog.data.gov/dataset/index-violent-property-and-firearm-rates-by-county-beginning-1990)  
- 📅 **Time Range**: 1990–2023

---

## 🚀 Run Locally

```bash
# Step 1: Install Preswald
pip install preswald

# Step 2: Run your app locally
preswald run

# Step 3: Export to static HTML
#Coming soon
preswald export
```
---

### 🙌 Special Thanks
Big shoutout and heartfelt thanks to the amazing team behind Preswald, founders - [@amrutha97](https://github.com/amrutha97), [@shivam-singhal](https://github.com/shivam-singhal) — your work is making local-first, reactive, code-driven data apps a reality. This dashboard wouldn’t exist without your vision.

THanks for stopping by!
Feel free to ⭐ the repo this repo & the master mind repo [Preswald](https://github.com/StructuredLabs/preswald).
