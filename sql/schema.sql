-- Table: regions
CREATE TABLE regions (
    region_id SERIAL PRIMARY KEY,
    region_name VARCHAR(100),
    province VARCHAR(100),
    abbreviation VARCHAR(10)
);

-- Table: species
CREATE TABLE species (
    species_id SERIAL PRIMARY KEY,
    common_name VARCHAR(150),
    scientific_name VARCHAR(150)
);

-- Table: outbreaks
CREATE TABLE outbreaks (
    outbreak_id SERIAL PRIMARY KEY,
    region_id INT REFERENCES regions(region_id),
    species_id INT REFERENCES species(species_id),
    latitude DECIMAL(9,6),
    longitude DECIMAL(9,6),
    num_animals INT,
    hpai_strain VARCHAR(50),
    confirmation_date DATE
);
