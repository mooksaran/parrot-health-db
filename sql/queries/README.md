📂 sql/queries/ – Advanced SQL Query Documentation

This folder contains analytical SQL queries used to extract insights from the outbreak database.

1. top_species.sql
   - Purpose: Find top 5 most infected bird species
   - Logic: COUNT outbreaks grouped by species_id

2. top_provinces.sql
   - Purpose: Identify top outbreak regions
   - Logic: Aggregate cases per region from outbreaks table

3. trends_by_month.sql
   - Purpose: Monthly trend of outbreaks across years
   - Logic: DATE_TRUNC & COUNT by confirmation_date

🧪 Each query assumes schema built from schema.sql and validated with test_queries.sql