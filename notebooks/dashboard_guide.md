# 📊 Power BI Dashboard Implementation Guide

Follow these steps to create a professional dashboard using the generated data.

## 1. Data Connection
- Open **Power BI Desktop**.
- Click on **Get Data** -> **Text/CSV**.
- Select `data/swiggy_delivery_data.csv`.
- Click **Transform Data** to open Power Query Editor.

## 2. Data Transformation (Power Query)
- Ensure `Order_Date` is set to **Date/Time** type.
- Ensure `Order_Value` and `Discount` are **Decimal Number** types.
- Create a custom column for **Net Revenue**: `[Order_Value] - [Discount]`.
- Click **Close & Apply**.

## 3. Key Measures (DAX)
Create these measures to make your dashboard interactive:
- **Total Revenue**: `Sum_Revenue = SUM(orders[Order_Value])`
- **Total Orders**: `Total_Orders = COUNT(orders[Order_ID])`
- **Avg Rating**: `Avg_Rating = AVERAGE(orders[Ratings])`
- **Repeat Customer Rate %**: 
  ```dax
  Repeat_Rate = 
  VAR TotalCust = DISTINCTCOUNT(orders[Customer_ID])
  VAR RepeatCust = COUNTROWS(FILTER(VALUES(orders[Customer_ID]), [Total_Orders] > 1))
  RETURN DIVIDE(RepeatCust, TotalCust)
  ```

## 4. Visualizations to Create
- **KPI Cards:** Display Total Revenue, Total Orders, and Avg Delivery Time at the top.
- **Line Chart:** `Order_Date` (Axis) vs `Total_Orders` (Values). Use hierarchy to show Daily/Monthly trends.
- **Bar Chart:** `Restaurant_Name` vs `Total Revenue`. Filter for Top 10.
- **Pie/Donut Chart:** `Customer Segment` (created in Python) or `Payment_Method`.
- **Map Visual:** `City` vs `Total Orders` to see geographical distribution.

## 5. Design Tips
- **Theme:** Use a Dark Theme (View -> Themes).
- **Colors:** Use Swiggy Orange (`#FC8019`) for primary metrics.
- **Interactivity:** Add Slicers for `City` and `Order_Date` to allow users to filter the data.

---
*This guide helps you build the visual component of your portfolio project.*
