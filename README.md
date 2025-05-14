# 🦜 Parrot Health & Human Outbreak Analytics Portfolio

An advanced, end-to-end data analytics project that integrates SQL, Python, and Tableau to investigate global avian influenza (HPAI) outbreaks in both wild birds and humans (2003–2023).  
This multi-tool portfolio highlights skills in database design, data wrangling, exploratory analysis, geospatial visualization, and interactive BI dashboarding.

---

## 📌 Project Summary

| Component         | Description                                                                 |
|------------------|-----------------------------------------------------------------------------|
| 🗃️ **Data Sources**     | WHO and FAO datasets on HPAI outbreaks in birds and humans               |
| 🛠 **Tools Used**        | SQL (PostgreSQL-style), Python (Pandas, Seaborn, Plotly), Tableau Public |
| 🧱 **Database Schema**   | 3-table relational model: `regions`, `species`, `outbreaks`              |
| 📊 **Dashboard Output**  | Tableau with KPI cards, map, line chart, bar chart                        |
| 📈 **Notebook Analysis** | Colab EDA with time-series, grouping, custom charts                      |

---

## 📁 Project Structure

```bash
parrot-health-db/
├── data/                         # Raw datasets (CSV)
│   └── README.md                 # Dataset descriptions and sources
│
├── sql/                          # Relational schema + analytics queries
│   ├── schema.sql
│   ├── queries/                  # Advanced insights queries
│   └── README.md                 # Query logic explanations
│
├── analysis/notebooks/
│   └── parrot_health_analysis.ipynb   # Google Colab EDA notebook
│
├── tableau/                      # Tableau dashboard assets
│   ├── dashboard-preview.png
│   └── README.md                 # Dashboard link + visual structure
│
├── docs/
│   └── er-diagram.png            # Entity Relationship Diagram (ERD)
│
├── streamlit_app.py (optional)  # Local dashboard (for extension)
└── README.md (this file)

## 🧠 Key Features

### ✅ SQL + Data Modeling

- Designed normalized schema for bird outbreaks (wildlife surveillance)
- Created reusable views and queries for:
  - Most infected species
  - Regional outbreaks by province
  - Monthly trend detection
- Used ERD to define relationships with foreign key constraints

---

### ✅ Python (Colab)

- Data cleansing, group-by aggregation, and datetime handling
- Trend analysis using seaborn, plotly, and pandas visualizations
- Country/year analysis + species-level exploration

---

### ✅ Tableau Dashboard

- KPI Cards: Total Cases, Total Deaths, CFR%
- Interactive map view and filters by country
- Time-series trends and Top 10 Country breakdown
- 📎 View Live Dashboard:  
  [https://public.tableau.com/views/your-dashboard-link](https://public.tableau.com/views/your-dashboard-link)

---

## 🔗 Demo Links

- 📊 **Tableau Dashboard**  
  [View on Tableau Public](https://public.tableau.com/views/your-dashboard-link)

- 📓 **Colab Notebook**  
  [`analysis/notebooks/parrot_health_analysis.ipynb`](analysis/notebooks/parrot_health_analysis.ipynb)

- 🧮 **SQL Queries Overview**  
  [`sql/queries/README.md`](sql/queries/README.md)

---

## 💼 About the Author

**Mook S.**  
Aspiring Data Analyst with hands-on experience in SQL, Python, BI tools, and real-world health datasets.  
Portfolio developed as part of a full-stack analytics track for healthcare + public data analytics.

📧 [GitHub Profile](https://github.com/mooksaran)  
🔗 [Tableau](#)(https://public.tableau.com/app/profile/saranya.sangsuk.iem/vizzes)

---

## 🏷 Tags

`#data-analytics` `#portfolio-project` `#tableau` `#sql` `#public-health` `#avian-flu` `#EDA`
