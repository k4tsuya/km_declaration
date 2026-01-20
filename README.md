# Km Declaration

This is a Python-based data analysis tool that processes transaction exports from **Rabobank** to calculate estimated driven kilometers based on transaction frequency at a fixed location.

This project was developed for private workplace use and is published as part of my  **junior backend developer portfolio**.

---

## Project Summary

* Language: Python
* Domain: Financial transaction analysis
* Data source: CSV exports from Rabobank
* Purpose: Kilometer calculation based on transaction frequency

---

## Core Functionality

* Read CSV transaction data using **pandas**
* Filter transactions by ATM or terminal identifier
* Count location-specific purchases
* Calculate estimated kilometers
* Produce clear, reproducible results

---

## Technical Skills Demonstrated

* Python programming
* Data processing with pandas
* CSV file handling
* Filtering and aggregation logic
* Writing maintainable backend scripts
* Translating business requirements into code

---

## Workflow Overview

1. Export transaction data from Rabobank
2. Load CSV into pandas DataFrame
3. Apply filters based on terminal or location
4. Count matching transactions
5. Calculate distance using predefined rules
