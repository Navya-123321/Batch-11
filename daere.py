# ============================================================
# SALES DATA ANALYSIS SYSTEM
# ============================================================
# Product Performance
# Category Analysis
# Regional Sales Analysis
# Profit Analysis
# Sales Trend Analysis
# Data Cleaning
# Data Visualization
# Correlation Analysis
# Business Insights
# ============================================================


# ------------------------------------------------------------
# 1. IMPORT REQUIRED LIBRARIES
# ------------------------------------------------------------

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# ------------------------------------------------------------
# 2. LOAD THE EXCEL DATASET
# ------------------------------------------------------------

# Read the Excel file
df = pd.read_excel(
    "sales_data_analysis (1).xlsx",
    sheet_name="Sales Data"
)

print("============================================================")
print("ORIGINAL DATASET")
print("============================================================")

print("\nFirst 5 Records:")
print(df.head())

print("\nDataset Shape:")
print(df.shape)

print("\nColumn Names:")
print(df.columns)


# ------------------------------------------------------------
# 3. DATASET INFORMATION
# ------------------------------------------------------------

print("\n============================================================")
print("DATASET INFORMATION")
print("============================================================")

print("\nDataset Information:")
print(df.info())

print("\nData Types:")
print(df.dtypes)


# ------------------------------------------------------------
# 4. CHECK MISSING VALUES AND DUPLICATES
# ------------------------------------------------------------

print("\n============================================================")
print("BEFORE CLEANING")
print("============================================================")

print("\nMissing Values:")
print(df.isnull().sum())

print("\nDuplicate Rows:")
print(df.duplicated().sum())


# ------------------------------------------------------------
# 5. DATA CLEANING
# ------------------------------------------------------------

print("\n============================================================")
print("DATA CLEANING")
print("============================================================")


# Create a copy of the original dataset
df_clean = df.copy()


# Remove duplicate rows
df_clean = df_clean.drop_duplicates()


# Remove rows containing missing values
df_clean = df_clean.dropna()


# Convert Order Date to datetime
df_clean["Order Date"] = pd.to_datetime(
    df_clean["Order Date"],
    errors="coerce"
)


# Convert numerical columns into numeric format
numeric_columns = [
    "Quantity",
    "Discount",
    "Sales",
    "Profit"
]

for column in numeric_columns:

    df_clean[column] = pd.to_numeric(
        df_clean[column],
        errors="coerce"
    )


# Remove rows where important values are invalid
df_clean = df_clean.dropna(
    subset=[
        "Order Date",
        "Category",
        "Product Name",
        "Region",
        "Quantity",
        "Sales",
        "Profit"
    ]
)


# Remove negative quantity
df_clean = df_clean[
    df_clean["Quantity"] >= 0
]


# Remove negative sales
df_clean = df_clean[
    df_clean["Sales"] >= 0
]


# ------------------------------------------------------------
# 6. AFTER CLEANING
# ------------------------------------------------------------

print("\n============================================================")
print("AFTER CLEANING")
print("============================================================")

print("\nMissing Values After Cleaning:")
print(df_clean.isnull().sum())

print("\nDuplicate Rows After Cleaning:")
print(df_clean.duplicated().sum())

print("\nFinal Dataset Shape:")
print(df_clean.shape)


# Use cleaned dataset from this point
df = df_clean


# ------------------------------------------------------------
# 7. EXPLORATORY DATA ANALYSIS
# ------------------------------------------------------------

print("\n============================================================")
print("EXPLORATORY DATA ANALYSIS")
print("============================================================")


# Statistical summary
print("\nStatistical Summary:")
print(df.describe())


# Number of records
print("\nTotal Records:")
print(len(df))


# Number of products
print("\nNumber of Products:")
print(df["Product Name"].nunique())


# Product names
print("\nProducts:")
print(df["Product Name"].unique())


# Number of categories
print("\nNumber of Categories:")
print(df["Category"].nunique())


# Categories
print("\nCategories:")
print(df["Category"].unique())


# Number of regions
print("\nNumber of Regions:")
print(df["Region"].nunique())


# Regions
print("\nRegions:")
print(df["Region"].unique())


# Number of states
print("\nNumber of States:")
print(df["State"].nunique())


# Number of customers
print("\nNumber of Customers:")
print(df["Customer ID"].nunique())


# ------------------------------------------------------------
# 8. BASIC SALES CALCULATIONS
# ------------------------------------------------------------

print("\n============================================================")
print("BASIC SALES CALCULATIONS")
print("============================================================")


# Total quantity
total_quantity = df["Quantity"].sum()

print("\nTotal Quantity Sold:")
print(total_quantity)


# Total sales
total_sales = df["Sales"].sum()

print("\nTotal Sales:")
print(total_sales)


# Total profit
total_profit = df["Profit"].sum()

print("\nTotal Profit:")
print(total_profit)


# Average sales
average_sales = df["Sales"].mean()

print("\nAverage Sales:")
print(average_sales)


# Average profit
average_profit = df["Profit"].mean()

print("\nAverage Profit:")
print(average_profit)


# Average discount
average_discount = df["Discount"].mean()

print("\nAverage Discount:")
print(average_discount)


# ------------------------------------------------------------
# 9. REGION + CATEGORY PROFIT ANALYSIS
# ------------------------------------------------------------

print("\n============================================================")
print("REGION + CATEGORY PROFIT ANALYSIS")
print("============================================================")


groupby_output = df.groupby(
    ["Region", "Category"]
)[["Profit"]].sum()


print("\nProfit by Region and Category:")
print(groupby_output)


# ------------------------------------------------------------
# 10. REGION-WISE AGGREGATE ANALYSIS
# ------------------------------------------------------------

print("\n============================================================")
print("REGION-WISE AGGREGATE ANALYSIS")
print("============================================================")


agg_output = df.groupby("Region").agg(
    Units=("Quantity", "sum"),
    Total_Sales=("Sales", "sum"),
    Total_Profit=("Profit", "sum"),
    Avg_Sales=("Sales", "mean"),
    Avg_Profit=("Profit", "mean")
)


print("\nRegion-wise Analysis:")
print(agg_output)


# ------------------------------------------------------------
# 11. REGION-WISE QUANTITY
# ------------------------------------------------------------

print("\n============================================================")
print("REGION-WISE QUANTITY")
print("============================================================")


region_quantity = df.groupby(
    "Region"
)["Quantity"].sum()


print("\nQuantity Sold by Region:")
print(region_quantity)


# ------------------------------------------------------------
# 12. REGION-WISE PROFIT
# ------------------------------------------------------------

print("\n============================================================")
print("REGION-WISE PROFIT")
print("============================================================")


region_profit = df.groupby(
    "Region"
)["Profit"].sum()


print("\nProfit by Region:")
print(region_profit)


# ------------------------------------------------------------
# 13. REGION-WISE SALES
# ------------------------------------------------------------

print("\n============================================================")
print("REGION-WISE SALES")
print("============================================================")


region_sales = df.groupby(
    "Region"
)["Sales"].sum()


print("\nSales by Region:")
print(region_sales)


# ------------------------------------------------------------
# 14. SALES PERCENTAGE BY REGION
# ------------------------------------------------------------

region_sales_percentage = (
    region_sales / region_sales.sum()
) * 100


print("\nSales Percentage by Region:")
print(region_sales_percentage)


# ------------------------------------------------------------
# 15. PRODUCT-WISE SALES
# ------------------------------------------------------------

print("\n============================================================")
print("PRODUCT-WISE SALES")
print("============================================================")


product_sales = df.groupby(
    "Product Name"
)["Sales"].sum()


product_sales = product_sales.sort_values(
    ascending=False
)


print("\nSales by Product:")
print(product_sales)


# ------------------------------------------------------------
# 16. PRODUCT PERFORMANCE ANALYSIS
# ------------------------------------------------------------

print("\n============================================================")
print("PRODUCT PERFORMANCE ANALYSIS")
print("============================================================")


product_analysis = df.groupby(
    "Product Name"
).agg(
    Total_Quantity=("Quantity", "sum"),
    Total_Sales=("Sales", "sum"),
    Total_Profit=("Profit", "sum"),
    Average_Sales=("Sales", "mean"),
    Average_Profit=("Profit", "mean")
).sort_values(
    by="Total_Sales",
    ascending=False
)


print("\nProduct Performance:")
print(product_analysis)


# Best-selling product based on quantity
best_selling_product = product_analysis[
    "Total_Quantity"
].idxmax()


print("\nBest-Selling Product:")
print(best_selling_product)


# Highest sales product
highest_sales_product = product_analysis[
    "Total_Sales"
].idxmax()


print("\nHighest-Sales Product:")
print(highest_sales_product)


# Highest profit product
highest_profit_product = product_analysis[
    "Total_Profit"
].idxmax()


print("\nHighest-Profit Product:")
print(highest_profit_product)


# ------------------------------------------------------------
# 17. CATEGORY-WISE SALES
# ------------------------------------------------------------

print("\n============================================================")
print("CATEGORY-WISE SALES")
print("============================================================")


category_sales = df.groupby(
    "Category"
)["Sales"].sum()


category_sales = category_sales.sort_values(
    ascending=False
)


print("\nSales by Category:")
print(category_sales)


# ------------------------------------------------------------
# 18. CATEGORY PERFORMANCE ANALYSIS
# ------------------------------------------------------------

print("\n============================================================")
print("CATEGORY PERFORMANCE ANALYSIS")
print("============================================================")


category_analysis = df.groupby(
    "Category"
).agg(
    Total_Quantity=("Quantity", "sum"),
    Total_Sales=("Sales", "sum"),
    Total_Profit=("Profit", "sum"),
    Average_Sales=("Sales", "mean"),
    Average_Profit=("Profit", "mean")
).sort_values(
    by="Total_Sales",
    ascending=False
)


print("\nCategory Performance:")
print(category_analysis)


# Category sales percentage
category_analysis["Sales_Percentage"] = (
    category_analysis["Total_Sales"]
    / category_analysis["Total_Sales"].sum()
) * 100


print("\nCategory Sales Percentage:")
print(category_analysis)


# Highest sales category
highest_sales_category = category_analysis[
    "Total_Sales"
].idxmax()


print("\nHighest-Sales Category:")
print(highest_sales_category)


# Highest profit category
highest_profit_category = category_analysis[
    "Total_Profit"
].idxmax()


print("\nHighest-Profit Category:")
print(highest_profit_category)


# ------------------------------------------------------------
# 19. SUB-CATEGORY ANALYSIS
# ------------------------------------------------------------

print("\n============================================================")
print("SUB-CATEGORY ANALYSIS")
print("============================================================")


subcategory_analysis = df.groupby(
    "Sub-Category"
).agg(
    Total_Quantity=("Quantity", "sum"),
    Total_Sales=("Sales", "sum"),
    Total_Profit=("Profit", "sum")
).sort_values(
    by="Total_Sales",
    ascending=False
)


print("\nSub-Category Performance:")
print(subcategory_analysis)


# ------------------------------------------------------------
# 20. STATE-WISE SALES
# ------------------------------------------------------------

print("\n============================================================")
print("STATE-WISE SALES")
print("============================================================")


state_sales = df.groupby(
    "State"
)["Sales"].sum().sort_values(
    ascending=False
)


print("\nSales by State:")
print(state_sales)


# ------------------------------------------------------------
# 21. CUSTOMER ANALYSIS
# ------------------------------------------------------------

print("\n============================================================")
print("CUSTOMER ANALYSIS")
print("============================================================")


customer_sales = df.groupby(
    ["Customer ID", "Customer Name"]
)["Sales"].sum().sort_values(
    ascending=False
)


print("\nSales by Customer:")
print(customer_sales.head(10))


# ------------------------------------------------------------
# 22. SHIP MODE ANALYSIS
# ------------------------------------------------------------

print("\n============================================================")
print("SHIP MODE ANALYSIS")
print("============================================================")


ship_mode_analysis = df.groupby(
    "Ship Mode"
).agg(
    Orders=("Order ID", "count"),
    Quantity=("Quantity", "sum"),
    Sales=("Sales", "sum"),
    Profit=("Profit", "sum")
).sort_values(
    by="Sales",
    ascending=False
)


print("\nShip Mode Analysis:")
print(ship_mode_analysis)


# ------------------------------------------------------------
# 23. SALES TREND OVER TIME
# ------------------------------------------------------------

print("\n============================================================")
print("SALES TREND OVER TIME")
print("============================================================")


# Create Month column
df["Month"] = df["Order Date"].dt.to_period("M")


# Monthly sales
monthly_sales = df.groupby(
    "Month"
)["Sales"].sum()


print("\nMonthly Sales:")
print(monthly_sales)


# Monthly quantity
monthly_quantity = df.groupby(
    "Month"
)["Quantity"].sum()


print("\nMonthly Quantity:")
print(monthly_quantity)


# Monthly profit
monthly_profit = df.groupby(
    "Month"
)["Profit"].sum()


print("\nMonthly Profit:")
print(monthly_profit)


# Yearly sales
yearly_sales = df.groupby(
    df["Order Date"].dt.year
)["Sales"].sum()


print("\nYearly Sales:")
print(yearly_sales)


# Yearly profit
yearly_profit = df.groupby(
    df["Order Date"].dt.year
)["Profit"].sum()


print("\nYearly Profit:")
print(yearly_profit)


# Highest sales month
highest_sales_month = monthly_sales.idxmax()


print("\nHighest-Sales Month:")
print(highest_sales_month)


# Highest monthly sales value
highest_sales_value = monthly_sales.max()


print("\nHighest Monthly Sales:")
print(highest_sales_value)


# ------------------------------------------------------------
# 24. PROFIT ANALYSIS
# ------------------------------------------------------------

print("\n============================================================")
print("PROFIT ANALYSIS")
print("============================================================")


# Profit by category
profit_by_category = df.groupby(
    "Category"
)["Profit"].sum().sort_values(
    ascending=False
)


print("\nProfit by Category:")
print(profit_by_category)


# Profit by region
profit_by_region = df.groupby(
    "Region"
)["Profit"].sum().sort_values(
    ascending=False
)


print("\nProfit by Region:")
print(profit_by_region)


# Profit by product
profit_by_product = df.groupby(
    "Product Name"
)["Profit"].sum().sort_values(
    ascending=False
)


print("\nProfit by Product:")
print(profit_by_product)


# Highest profit region
highest_profit_region = profit_by_region.idxmax()


print("\nHighest-Profit Region:")
print(highest_profit_region)


# ------------------------------------------------------------
# 25. DISCOUNT ANALYSIS
# ------------------------------------------------------------

print("\n============================================================")
print("DISCOUNT ANALYSIS")
print("============================================================")


discount_analysis = df.groupby(
    "Discount"
).agg(
    Quantity=("Quantity", "sum"),
    Sales=("Sales", "sum"),
    Profit=("Profit", "sum")
).sort_index()


print("\nSales and Profit by Discount:")
print(discount_analysis)


# ------------------------------------------------------------
# 26. CORRELATION ANALYSIS
# ------------------------------------------------------------

print("\n============================================================")
print("CORRELATION ANALYSIS")
print("============================================================")


correlation = df[
    [
        "Quantity",
        "Discount",
        "Sales",
        "Profit"
    ]
].corr()


print("\nCorrelation Matrix:")
print(correlation)


# ------------------------------------------------------------
# 27. VISUALIZATION
# ------------------------------------------------------------

print("\n============================================================")
print("VISUALIZATION")
print("============================================================")


# ------------------------------------------------------------
# 27.1 SALES BY REGION
# ------------------------------------------------------------

plt.figure(figsize=(8, 6))

plt.bar(
    region_sales.index,
    region_sales.values
)

plt.xlabel("Region")
plt.ylabel("Total Sales")
plt.title("Sales by Region")

plt.tight_layout()
plt.show()


# ------------------------------------------------------------
# 27.2 QUANTITY BY REGION
# ------------------------------------------------------------

plt.figure(figsize=(8, 6))

plt.bar(
    region_quantity.index,
    region_quantity.values
)

plt.xlabel("Region")
plt.ylabel("Quantity Sold")
plt.title("Quantity Sold by Region")

plt.tight_layout()
plt.show()


# ------------------------------------------------------------
# 27.3 PROFIT BY REGION
# ------------------------------------------------------------

plt.figure(figsize=(8, 6))

plt.bar(
    region_profit.index,
    region_profit.values
)

plt.xlabel("Region")
plt.ylabel("Total Profit")
plt.title("Profit by Region")

plt.tight_layout()
plt.show()


# ------------------------------------------------------------
# 27.4 SALES BY CATEGORY
# ------------------------------------------------------------

plt.figure(figsize=(8, 6))

plt.bar(
    category_sales.index,
    category_sales.values
)

plt.xlabel("Category")
plt.ylabel("Total Sales")
plt.title("Sales by Category")

plt.tight_layout()
plt.show()


# ------------------------------------------------------------
# 27.5 PROFIT BY CATEGORY
# ------------------------------------------------------------

plt.figure(figsize=(8, 6))

plt.bar(
    category_analysis.index,
    category_analysis["Total_Profit"]
)

plt.xlabel("Category")
plt.ylabel("Total Profit")
plt.title("Profit by Category")

plt.tight_layout()
plt.show()


# ------------------------------------------------------------
# 27.6 SALES BY PRODUCT
# ------------------------------------------------------------

plt.figure(figsize=(12, 6))

plt.bar(
    product_sales.index,
    product_sales.values
)

plt.xlabel("Product")
plt.ylabel("Total Sales")
plt.title("Sales by Product")

plt.xticks(rotation=90)

plt.tight_layout()
plt.show()


# ------------------------------------------------------------
# 27.7 QUANTITY BY PRODUCT
# ------------------------------------------------------------

plt.figure(figsize=(12, 6))

plt.bar(
    product_analysis.index,
    product_analysis["Total_Quantity"]
)

plt.xlabel("Product")
plt.ylabel("Quantity Sold")
plt.title("Quantity Sold by Product")

plt.xticks(rotation=90)

plt.tight_layout()
plt.show()


# ------------------------------------------------------------
# 27.8 PROFIT BY PRODUCT
# ------------------------------------------------------------

plt.figure(figsize=(12, 6))

plt.bar(
    profit_by_product.index,
    profit_by_product.values
)

plt.xlabel("Product")
plt.ylabel("Total Profit")
plt.title("Profit by Product")

plt.xticks(rotation=90)

plt.tight_layout()
plt.show()


# ------------------------------------------------------------
# 27.9 REGIONAL SALES DISTRIBUTION
# ------------------------------------------------------------

plt.figure(figsize=(8, 8))

plt.pie(
    region_sales_percentage,
    labels=region_sales_percentage.index,
    autopct="%1.1f%%"
)

plt.title("Regional Sales Distribution")

plt.show()


# ------------------------------------------------------------
# 27.10 CATEGORY SALES DISTRIBUTION
# ------------------------------------------------------------

plt.figure(figsize=(8, 8))

plt.pie(
    category_analysis["Sales_Percentage"],
    labels=category_analysis.index,
    autopct="%1.1f%%"
)

plt.title("Category Sales Distribution")

plt.show()


# ------------------------------------------------------------
# 27.11 MONTHLY SALES TREND
# ------------------------------------------------------------

plt.figure(figsize=(12, 6))

plt.plot(
    monthly_sales.index.astype(str),
    monthly_sales.values,
    marker="o"
)

plt.xlabel("Month")
plt.ylabel("Sales")
plt.title("Monthly Sales Trend")

plt.xticks(rotation=45)

plt.tight_layout()
plt.show()


# ------------------------------------------------------------
# 27.12 MONTHLY PROFIT TREND
# ------------------------------------------------------------

plt.figure(figsize=(12, 6))

plt.plot(
    monthly_profit.index.astype(str),
    monthly_profit.values,
    marker="o"
)

plt.xlabel("Month")
plt.ylabel("Profit")
plt.title("Monthly Profit Trend")

plt.xticks(rotation=45)

plt.tight_layout()
plt.show()


# ------------------------------------------------------------
# 27.13 YEARLY SALES
# ------------------------------------------------------------

plt.figure(figsize=(8, 6))

plt.bar(
    yearly_sales.index.astype(str),
    yearly_sales.values
)

plt.xlabel("Year")
plt.ylabel("Sales")
plt.title("Yearly Sales")

plt.tight_layout()
plt.show()


# ------------------------------------------------------------
# 27.14 YEARLY PROFIT
# ------------------------------------------------------------

plt.figure(figsize=(8, 6))

plt.bar(
    yearly_profit.index.astype(str),
    yearly_profit.values
)

plt.xlabel("Year")
plt.ylabel("Profit")
plt.title("Yearly Profit")

plt.tight_layout()
plt.show()


# ------------------------------------------------------------
# 27.15 CORRELATION MATRIX
# ------------------------------------------------------------

plt.figure(figsize=(8, 6))

plt.imshow(
    correlation,
    interpolation="nearest"
)

plt.colorbar()

plt.xticks(
    range(len(correlation.columns)),
    correlation.columns,
    rotation=45
)

plt.yticks(
    range(len(correlation.columns)),
    correlation.columns
)

plt.title("Correlation Matrix")

plt.tight_layout()
plt.show()


# ------------------------------------------------------------
# 28. BUSINESS INSIGHTS
# ------------------------------------------------------------

print("\n============================================================")
print("BUSINESS INSIGHTS")
print("============================================================")


print("\n1. PRODUCT INSIGHT")

print(
    f"{best_selling_product} has the highest total quantity sold."
)

print(
    f"{highest_sales_product} generates the highest total sales."
)

print(
    f"{highest_profit_product} generates the highest total profit."
)


print("\n2. CATEGORY INSIGHT")

print(
    f"{highest_sales_category} generates the highest total sales."
)

print(
    f"{highest_profit_category} generates the highest total profit."
)


print("\n3. REGIONAL INSIGHT")

print(
    f"{highest_sales_region} generates the highest total sales."
    if (highest_sales_region := region_sales.idxmax())
    else ""
)

print(
    f"{highest_profit_region} generates the highest total profit."
)


print("\n4. SALES TREND INSIGHT")

print(
    f"The highest monthly sales occurred in "
    f"{highest_sales_month}."
)


print("\n5. BUSINESS RECOMMENDATIONS")

print(
    "- Maintain sufficient inventory for high-performing products."
)

print(
    "- Analyze high-sales regions for future business planning."
)

print(
    "- Monitor category-wise sales and profit."
)

print(
    "- Study monthly sales trends for inventory planning."
)

print(
    "- Monitor discount, sales and profit together."
)

print(
    "- Compare quantity sold with profit before making stock decisions."
)


# ------------------------------------------------------------
# 29. FINAL SUMMARY
# ------------------------------------------------------------

print("\n============================================================")
print("FINAL SUMMARY")
print("============================================================")


print(
    "Total Records Analyzed:",
    len(df)
)


print(
    "Total Sales:",
    total_sales
)


print(
    "Total Profit:",
    total_profit
)


print(
    "Total Quantity Sold:",
    total_quantity
)


print(
    "Average Sales:",
    average_sales
)


print(
    "Average Profit:",
    average_profit
)


print(
    "Best-Selling Product:",
    best_selling_product
)


print(
    "Highest-Sales Product:",
    highest_sales_product
)


print(
    "Highest-Profit Product:",
    highest_profit_product
)


print(
    "Highest-Sales Category:",
    highest_sales_category
)


print(
    "Highest-Profit Category:",
    highest_profit_category
)


print(
    "Highest-Sales Region:",
    region_sales.idxmax()
)


print(
    "Highest-Profit Region:",
    highest_profit_region
)


print(
    "Highest-Sales Month:",
    highest_sales_month
)


print(
    "Highest Monthly Sales:",
    highest_sales_value
)


print("\n============================================================")
print("SALES DATA ANALYSIS COMPLETED SUCCESSFULLY!")
print("============================================================")