# End-to-End Food Delivery Data Analysis & Business Insights Dashboard
### (Swiggy Case Study)

## 📊 Project Overview
This project provides a comprehensive analysis of food delivery data, simulating real-world scenarios from platforms like Swiggy. It encompasses data generation, cleaning, exploratory data analysis (EDA), predictive modeling, and business intelligence reporting to drive data-driven decision-making.

## 🧠 Business Objectives
- **Customer Behavior:** Identifying high-value segments and churn risks.
- **Delivery Performance:** Optimizing delivery times based on distance and traffic patterns.
- **Revenue Growth:** Analyzing the impact of discounts on overall profitability.
- **Operational Efficiency:** Identifying peak order times to manage rider supply.

## 🛠️ Tech Stack
- **Python:** Data manipulation (Pandas, Numpy), Visualization (Matplotlib, Seaborn, Plotly), and Machine Learning (Scikit-Learn).
- **SQL:** Complex queries for data extraction and business metrics.
- **Power BI / Excel:** Interactive dashboards for executive reporting.
- **Synthetic Data:** Custom Python scripts to generate realistic 5000+ order records.

## 📂 Repository Structure
- `data/`: Contains the raw dataset in CSV format.
- `scripts/`: Python scripts for data generation and advanced analytics.
- `sql/`: SQL scripts for database-level analysis.
- `notebooks/`: Visualization exports and analysis reports.

## 🚀 Key Features & Insights
### 1. Customer Segmentation (RFM Lite)
Categorized customers into **High, Medium, and Low Value** segments based on total revenue and order frequency.
> *Insight: Top 20% of customers contribute to ~60% of the total revenue.*

### 2. Predictive Analytics: Delivery Time
Developed a **Linear Regression model** to predict delivery times based on distance. 
> *Insight: Average delivery time increases by 3 minutes for every additional kilometer, with a baseline of 15 minutes.*

### 3. Peak Time Analysis
Analyzed order volume by hour to identify "Rush Hours".
> *Insight: Peak orders occur between 7:00 PM and 9:00 PM, suggesting a need for increased delivery fleet during these hours.*

### 4. Discount Impact Analysis
Compared profit margins between discounted and non-discounted orders.
> *Insight: While discounts increase order volume by 40%, they reduce the average profit per order by 15%.*

## 📈 Dashboard Highlights (Power BI)
- **Revenue Overview:** Monthly trends and city-wise performance.
- **Restaurant Leaderboard:** Top performing partners by revenue and ratings.
- **Delivery Efficiency:** Correlation between delivery time and customer satisfaction ratings.

---
*Developed for Data Analytics Portfolio | Focused on Business Intelligence & Machine Learning.*
