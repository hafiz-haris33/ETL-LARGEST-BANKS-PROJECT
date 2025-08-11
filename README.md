# 🏦 Acquiring and Processing Information on the World's Largest Banks

## 📌 Project Overview
This project is a **Python-based ETL (Extract, Transform, Load) pipeline** developed as part of the *IBM Python Project for Data Engineering* course on Coursera. It automates the retrieval of the **Top 10 Largest Banks in the World** ranked by **Market Capitalization (in Billion USD)**, transforms the data into multiple currencies (GBP, EUR, INR), and stores the results in both CSV and database formats for analysis. The pipeline is designed to be **reusable every financial quarter**, ensuring the data remains up to date.

---

## 🎯 Project Scenario
You are hired as a **Data Engineer** at a research organization. Your task is to:
1. Extract the latest market capitalization data of the top 10 banks from Wikipedia.
2. Convert the values into **GBP**, **EUR**, and **INR** using provided exchange rate data.
3. Store the processed data locally in a CSV file and in an SQL database table.
4. Log all steps of the process for transparency and debugging.

---

## 🔹 Data Sources
1. **Bank Data URL:**  
[Wikipedia (Archived)](https://web.archive.org/web/20230908091635/https://en.wikipedia.org/wiki/List_of_largest_banks)  
2. **Exchange Rates CSV:**  
[Exchange Rates CSV](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMSkillsNetwork-PY0221EN-Coursera/labs/v2/exchange_rate.csv)

---

## 📂 Files Generated
- **Largest_banks_data.csv** → Processed data with market capitalization in USD, GBP, EUR, INR.
- **Banks.db** → SQLite database storing processed data in table `Largest_banks`.
- **code_log.txt** → Log file with step-by-step execution records and timestamps.

---

## 🛠️ Technologies & Libraries Used
- **Python** (Core language)
- **Pandas** (Data manipulation, CSV reading/writing)
- **Requests** (HTTP requests for data fetching)
- **BeautifulSoup** (Web scraping)
- **SQLite3** (Database storage)
- **Logging** (Execution tracking)

---

## 🔄 ETL Pipeline Steps

### 1. **Logging Setup**
Implemented a `log_progress()` function to log execution steps in `code_log.txt`.

### 2. **Extract**
- Scraped the Wikipedia table under **"By market capitalization"**.
- Extracted columns:  
  - `Name` → Bank name  
  - `MC_USD_Billion` → Market capitalization in USD (billions)

### 3. **Transform**
- Loaded the exchange rate data from CSV.
- Added three new columns:  
  - `MC_GBP_Billion`  
  - `MC_EUR_Billion`  
  - `MC_INR_Billion`  
- Converted values from USD using exchange rates and rounded to **2 decimal places**.

### 4. **Load**
- Saved the transformed DataFrame to:
  - **CSV** → `Largest_banks_data.csv`  
  - **SQLite DB** → `Banks.db`, table `Largest_banks`

### 5. **Query Execution**
Implemented a `run_queries()` function to run SQL queries on the database for validation.

### 6. **Final Logging**
Logged all stages: extraction, transformation, loading, and query execution.

---

## 📊 Example Output (Transformed Data)

| Name                | MC_USD_Billion | MC_GBP_Billion | MC_EUR_Billion | MC_INR_Billion |
|---------------------|----------------|----------------|----------------|----------------|
| JPMorgan Chase      | 406.88         | 331.50         | 374.35         | 33540.12       |
| ICBC                | 281.25         | 229.19         | 258.67         | 23181.75       |
| Bank of America     | 279.73         | 228.01         | 257.32         | 23061.19       |
| ...                 | ...            | ...            | ...            | ...            |

---

## 🚀 How to Run

### 1️⃣ Install Dependencies
```bash
pip install requests beautifulsoup4 pandas numpy
```

### 2️⃣ Run the Script
```bash
python banks_project.py
```

### 3️⃣ Check Outputs
- `Largest_banks_data.csv` → CSV file with processed data.
- `Banks.db` → SQLite database with table `Largest_banks`.
- `code_log.txt` → Log file with execution steps.

---

## 📌 Key Features
- Automated **ETL pipeline** for banking market cap data.
- Currency conversion to GBP, EUR, INR using real exchange rate data.
- Storage in both CSV and SQLite database formats.
- Built-in logging for process transparency.
- Reusable script for quarterly data updates.

---

## 📜 License
This project is for **educational purposes** as part of IBM’s *Python Project for Data Engineering* course.
