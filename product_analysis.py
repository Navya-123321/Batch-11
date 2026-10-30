"""Reusable analysis functions for the Sales Data Analysis dashboard."""
import pandas as pd

def get_category_sales(data):
    return data.groupby("Category")["Sales"].sum().sort_values(ascending=False)

def get_region_sales(data, value="Sales"):
    if value not in data.columns:
        raise ValueError(f"Column '{value}' is not available in the dataset.")
    return data.groupby("Region")[value].sum().sort_values(ascending=False)

def get_monthly_sales(data):
    monthly = data.set_index("Order Date").resample("MS")["Sales"].sum()
    return monthly

def get_top_products(data, limit=5):
    result = (
        data.groupby(["Product Name", "Category"], as_index=False)["Sales"]
        .sum()
        .sort_values("Sales", ascending=False)
        .head(limit)
        .rename(columns={"Sales": "Total Sales"})
    )
    return result
