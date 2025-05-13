# 💡 SQL Query Explanations

This document explains the key SQL queries used to analyze the HPAI (Highly Pathogenic Avian Influenza) outbreak dataset. Each query focuses on different aspects of outbreak tracking: species affected, geographic hotspots, and time-based trends.

---

## 1. Top 5 Bird Species with Most Outbreaks

```sql
SELECT s.common_name, COUNT(*) AS total_cases
FROM outbreaks o
JOIN species s ON o.species_id = s.species_id
GROUP BY s.common_name
ORDER BY total_cases DESC
LIMIT 5;

SELECT r.province, COUNT(*) AS outbreak_count
FROM outbreaks o
JOIN regions r ON o.region_id = r.region_idß
GROUP BY r.province
ORDER BY outbreak_count DESC
LIMIT 5;

SELECT
    DATE_TRUNC('month', o.confirmation_date) AS month,
    COUNT(*) AS monthly_cases
FROM outbreaks o
GROUP BY month
ORDER BY month;

