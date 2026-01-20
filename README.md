
# km_declaration *(working title, may be renamed in future)*

This is a Python-based data analysis tool designed to process transaction exports from **Rabobank** and estimate driven kilometers based on transaction frequency at specific locations.

This project was originally created for **private use** at a snackbar to simplify kilometer declarations, and is now shared as part of my  **junior backend developer portfolio** .

> ⚡ **Note:** This project is under active development. Features and the project name may be updated as new functionality is added.

---

## Project Summary

* **Language:** Python
* **Domain:** Financial transaction analysis / internal tooling
* **Data Source:** CSV exports from Rabobank
* **Purpose:** Calculate kilometers driven based on transaction frequency at defined locations
* **Status:** Ongoing development; new features and improvements will be added over time

---

## Core Functionality

Current features include:

* Load CSV transaction exports using **pandas**
* Filter transactions by ATM or terminal identifier
* Count location-specific purchases
* Calculate estimated kilometers
* Produce clear, reproducible results

Future features (planned):

* Configurable distance logic per terminal or location
* Advanced reporting (CSV / summary output)
* Integration with multiple transaction sources or automated data fetch
* Better CLI options and configuration files

---

## Technical Skills Demonstrated

* Python programming for data processing
* CSV handling and data filtering using pandas
* Aggregation and counting logic for backend data tasks
* Translating real-world business requirements into code
* Writing maintainable and extendable scripts

---

## Workflow Overview

1. Export transaction data from Rabobank
2. Load CSV into pandas DataFrame
3. Apply filters based on terminal or location
4. Count matching transactions
5. Calculate distance using predefined rules
6. *(Future) Generate summary reports or automated outputs*
