# ⚡ Strategic Power Grid Capacity Planning Dashboard

![Power BI](https://img.shields.io/badge/Tool-Power%20BI-F2C811?style=flat&logo=powerbi&logoColor=black)
![Status](https://img.shields.io/badge/Status-Completed-success)
![Domain](https://img.shields.io/badge/Domain-Energy%20%26%20Utilities-blue)

## 📖 Executive Summary
This project analyzes a 10-year trend (2004–2015) of power demand versus maximum grid capacity. The primary objective was to stress-test current infrastructure against a hypothetical "GenAI Demand Scenario"—a surge in power consumption driven by new data center requirements.

**Key Finding:** The analysis reveals that while historical demand remained stable under 7M MW, the projected "GenAI Scenario" creates a critical spike in 2015, potentially exceeding safe operating margins relative to the Max Capacity limit (~10.6M MW).

## 📊 Dashboard Preview
<img width="903" height="670" alt="image" src="https://github.com/user-attachments/assets/dde2e374-72c6-4395-80b4-c8d6a515dbde" />

## ❓ Business Problem
Utility providers must balance the high cost of infrastructure expansion with the risk of blackouts. This analysis answers three key questions:
1. **Historical Baseline:** How has actual demand tracked against our baseline forecasts?
2. **Capacity Risk:** At what point does projected demand threaten the 10.6M MW capacity ceiling?
3. **Scenario Modeling:** What is the impact of a sudden technological shift (GenAI adoption) on grid stability?

## 🛠️ Tools & Technologies Used
* **Power BI:** For interactive visualization, DAX measures, and scenario modeling.
* **Power Query:** For ETL (Extract, Transform, Load) processes and data cleaning.
* **DAX:** Custom measures created for `Total Load`, `Capacity Variances`, and `YoY Growth`.
* **Excel/CSV:** Raw data storage.

## 📈 Methodology
1.  **Data Modeling:** Established relationships between Calendar tables and Fact tables (Actuals, Forecasts, Capacity).
2.  **Visualization:**
    * Used a **Line Chart** with multiple series to compare Actuals vs. Scenarios.
    * Implemented a **Stepped Line** for Max Capacity to reflect fixed infrastructure limits.
    * Applied **Zoom Sliders** to allow stakeholders to investigate specific historical periods (e.g., 2004–2010).
3.  **UX Enhancements:**
    * Renamed technical field names to business-friendly labels (e.g., "Sum of GenAI_Scenario" → "GenAI Scenario").
    * Used **Conditional Formatting** (Red Dashed Line) to highlight safety thresholds.

## 💡 Key Insights
* **Stability (2004-2014):** Historical actuals tracked closely with the baseline forecast, hovering between 6M and 7M MW.
* **The 2015 Surge:** The "GenAI Scenario" (Blue Line) deviates sharply in 2015, indicating a massive load increase.
* **Capacity Buffer:** While the 2015 surge does not breach the 10.6M MW limit, it significantly reduces the safety buffer, suggesting an immediate need for infrastructure planning before 2016.

## 📂 Repository Structure

/energy-capacity-analysis
│
├── README.md               
├── energy_analysis.pbix    
├── requirements.txt        <-- Dependencies (pandas, numpy, etc.)
│
├── data/                   
│   └── power_demand_data.csv
│
├── scripts/                <-- NEW FOLDER
│   └── data_preprocessing.py
│
└── images/                 
    └── dashboard_screenshot.png
