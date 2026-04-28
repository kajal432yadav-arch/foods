-- SQL Queries for Swiggy Food Delivery Analysis

-- 1. Top 10 restaurants by revenue
SELECT 
    Restaurant_Name, 
    SUM(Order_Value) AS Total_Revenue,
    COUNT(Order_ID) AS Total_Orders
FROM orders
GROUP BY Restaurant_Name
ORDER BY Total_Revenue DESC
LIMIT 10;

-- 2. Highest order cities
SELECT 
    City, 
    COUNT(Order_ID) AS Total_Orders
FROM orders
GROUP BY City
ORDER BY Total_Orders DESC;

-- 3. Average delivery time by city
SELECT 
    City, 
    AVG(Delivery_Time) AS Avg_Delivery_Time
FROM orders
GROUP BY City
ORDER BY Avg_Delivery_Time ASC;

-- 4. Repeat customers (Loyalty Analysis)
SELECT 
    Customer_ID, 
    COUNT(Order_ID) AS Order_Count
FROM orders
GROUP BY Customer_ID
HAVING Order_Count > 5
ORDER BY Order_Count DESC;

-- 5. Peak order time analysis (Hourly)
-- Assuming Order_Date is a timestamp
SELECT 
    strftime('%H', Order_Date) AS Order_Hour, 
    COUNT(Order_ID) AS Total_Orders
FROM orders
GROUP BY Order_Hour
ORDER BY Total_Orders DESC;

-- 6. Revenue lost due to discounts
SELECT 
    SUM(Discount) AS Total_Discount_Given,
    AVG(Discount) AS Avg_Discount_Per_Order
FROM orders
WHERE Discount > 0;

-- 7. Delivery Status Distribution
SELECT 
    Delivery_Status, 
    COUNT(Order_ID) AS Status_Count
FROM orders
GROUP BY Delivery_Status;
