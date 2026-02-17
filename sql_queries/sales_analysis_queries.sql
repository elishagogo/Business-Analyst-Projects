-- SQL Queries for Sales Data Analysis

-- 1. Total Revenue by Product Category
SELECT 
    Product_Category,
    COUNT(Order_ID) as Total_Orders,
    SUM(Total_Amount) as Total_Revenue,
    AVG(Total_Amount) as Average_Order_Value,
    SUM(Quantity) as Total_Units_Sold
FROM sales_data
GROUP BY Product_Category
ORDER BY Total_Revenue DESC;

-- 2. Monthly Sales Trend
SELECT 
    DATE_TRUNC('month', Date) as Month,
    COUNT(Order_ID) as Number_of_Orders,
    SUM(Total_Amount) as Monthly_Revenue,
    AVG(Total_Amount) as Average_Order_Value
FROM sales_data
GROUP BY DATE_TRUNC('month', Date)
ORDER BY Month;

-- 3. Top 10 Customers by Revenue
SELECT 
    Customer_ID,
    COUNT(Order_ID) as Total_Orders,
    SUM(Total_Amount) as Total_Spent,
    AVG(Total_Amount) as Average_Order_Value,
    MAX(Date) as Last_Purchase_Date
FROM sales_data
GROUP BY Customer_ID
ORDER BY Total_Spent DESC
LIMIT 10;

-- 4. Regional Sales Performance
SELECT 
    Region,
    COUNT(DISTINCT Customer_ID) as Unique_Customers,
    COUNT(Order_ID) as Total_Orders,
    SUM(Total_Amount) as Total_Revenue,
    AVG(Total_Amount) as Average_Order_Value
FROM sales_data
GROUP BY Region
ORDER BY Total_Revenue DESC;

-- 5. Payment Method Preferences
SELECT 
    Payment_Method,
    COUNT(Order_ID) as Number_of_Transactions,
    SUM(Total_Amount) as Total_Revenue,
    ROUND(COUNT(Order_ID) * 100.0 / SUM(COUNT(Order_ID)) OVER (), 2) as Percentage_of_Orders
FROM sales_data
GROUP BY Payment_Method
ORDER BY Number_of_Transactions DESC;

-- 6. Product Performance Analysis
SELECT 
    Product_Name,
    Product_Category,
    COUNT(Order_ID) as Times_Sold,
    SUM(Quantity) as Total_Quantity_Sold,
    SUM(Total_Amount) as Total_Revenue,
    AVG(Unit_Price) as Average_Unit_Price
FROM sales_data
GROUP BY Product_Name, Product_Category
ORDER BY Total_Revenue DESC;

-- 7. Customer Purchase Frequency
-- Note: DATEDIFF syntax varies by SQL dialect
-- SQL Server: DATEDIFF(day, start_date, end_date)
-- PostgreSQL: (end_date - start_date) or DATE_PART('day', end_date - start_date)
-- MySQL: DATEDIFF(end_date, start_date)
SELECT 
    Customer_ID,
    COUNT(Order_ID) as Purchase_Count,
    MIN(Date) as First_Purchase,
    MAX(Date) as Last_Purchase,
    DATEDIFF(day, MIN(Date), MAX(Date)) as Customer_Lifetime_Days,  -- SQL Server syntax
    SUM(Total_Amount) as Total_Revenue
FROM sales_data
GROUP BY Customer_ID
HAVING COUNT(Order_ID) > 1
ORDER BY Purchase_Count DESC;

-- 8. Daily Sales Performance
SELECT 
    Date,
    COUNT(Order_ID) as Daily_Orders,
    SUM(Total_Amount) as Daily_Revenue,
    AVG(Total_Amount) as Average_Order_Value
FROM sales_data
GROUP BY Date
ORDER BY Date DESC;

-- 9. Revenue by Category and Region
SELECT 
    Product_Category,
    Region,
    COUNT(Order_ID) as Orders,
    SUM(Total_Amount) as Revenue
FROM sales_data
GROUP BY Product_Category, Region
ORDER BY Product_Category, Revenue DESC;

-- 10. Customer Segmentation by Spending
SELECT 
    CASE 
        WHEN Total_Spent >= 1000 THEN 'High Value'
        WHEN Total_Spent >= 500 THEN 'Medium Value'
        ELSE 'Low Value'
    END as Customer_Segment,
    COUNT(*) as Customer_Count,
    AVG(Total_Spent) as Average_Spending,
    SUM(Total_Spent) as Total_Revenue
FROM (
    SELECT 
        Customer_ID,
        SUM(Total_Amount) as Total_Spent
    FROM sales_data
    GROUP BY Customer_ID
) customer_totals
GROUP BY 
    CASE 
        WHEN Total_Spent >= 1000 THEN 'High Value'
        WHEN Total_Spent >= 500 THEN 'Medium Value'
        ELSE 'Low Value'
    END
ORDER BY Average_Spending DESC;
