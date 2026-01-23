---

# Transaction Analyzer

**Transaction Analyzer** is a Python-based backend project that processes transaction exports from **Rabobank** to analyze, filter, and report on financial transaction data.

The application allows users to search transactions by  **IBAN**,  **counterparty name**, and  **date**, generate summaries for specific shops or locations, estimate driven kilometers based on transaction frequency, and export reports as  **PDF files** .

This project was originally developed for **private workplace use** (a snackbar) and is now maintained as part of my  **junior backend developer portfolio** , demonstrating practical data processing, reporting, and automation skills in Python.

> **Status:** Actively developed — new features and reports are added over time as the project evolves.
>

## 📌 Project Summary

* **Language:** Python
* **Domain:** Transaction data processing / reporting
* **Input:** CSV exports from Rabobank
* **Output:** Summaries, statistics, and PDF reports
* **Status:** Active development (features growing over time)

---

## 🧠 What It Does

This tool helps you:

* 💾 Load Rabobank CSV transaction exports
* 📍 Filter transactions for specific shops or terminals
* 📊 Count purchases per location
* 🚗 Estimate driven kilometers based on purchase frequency
* 📄 Generate PDF summaries of results
* 🛠 Future capability: more reporting and formats

---

## 🛠️ Technologies Used

* 🐍 **Python 3**
* 📊 **pandas** for data processing
* 📄 PDF generation library (fpdf)
* CSV file handling and text encoding
