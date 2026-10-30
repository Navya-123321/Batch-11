import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path
from product_analysis import get_top_products, get_category_sales, get_region_sales, get_monthly_sales

st.set_page_config(page_title="Sales Data Analysis", page_icon="📊", layout="wide")

# Load optional custom CSS
css_path = Path("static/style.css")
if css_path.exists():
    st.markdown(f"<style>{css_path.read_text(encoding='utf-8')}</style>", unsafe_allow_html=True)

st.title("📊 Sales Data Analysis Dashboard")
st.caption("Explore sales, profit, product categories, regions, and monthly performance.")

@st.cache_data
def load_data(file):
    data = pd.read_excel(file, sheet_name="Sales Data")
    data["Order Date"] = pd.to_datetime(data["Order Date"], errors="coerce")
    for col in ["Sales", "Profit", "Quantity", "Discount"]:
        data[col] = pd.to_numeric(data[col], errors="coerce")
    return data.dropna(subset=["Order Date", "Sales", "Profit"])

uploaded_file = st.sidebar.file_uploader("Upload sales Excel file", type=["xlsx", "xls"])
default_file = Path("data/sales_data_analysis.xlsx")

try:
    if uploaded_file is not None:
        df = load_data(uploaded_file)
    elif default_file.exists():
        df = load_data(default_file)
    else:
        st.info("Upload your sales Excel file from the sidebar to begin.")
        st.stop()
except Exception as exc:
    st.error(f"Could not read the Excel file: {exc}")
    st.stop()

# Filters
st.sidebar.header("Filters")
regions = sorted(df["Region"].dropna().unique().tolist())
categories = sorted(df["Category"].dropna().unique().tolist())
selected_regions = st.sidebar.multiselect("Select region", regions, default=regions)
selected_categories = st.sidebar.multiselect("Select category", categories, default=categories)

filtered = df[
    df["Region"].isin(selected_regions) &
    df["Category"].isin(selected_categories)
].copy()

if filtered.empty:
    st.warning("No records match the selected filters.")
    st.stop()

# KPI cards
total_sales = filtered["Sales"].sum()
total_profit = filtered["Profit"].sum()
total_quantity = filtered["Quantity"].sum()
average_sales = filtered["Sales"].mean()

c1, c2, c3, c4 = st.columns(4)
c1.metric("Total Sales", f"${total_sales:,.2f}")
c2.metric("Total Profit", f"${total_profit:,.2f}")
c3.metric("Units Sold", f"{total_quantity:,.0f}")
c4.metric("Average Sale", f"${average_sales:,.2f}")

st.divider()

left, right = st.columns(2)
with left:
    st.subheader("Sales by Category")
    category_sales = get_category_sales(filtered)
    fig, ax = plt.subplots(figsize=(7, 4))
    category_sales.plot(kind="bar", ax=ax)
    ax.set_xlabel("Category")
    ax.set_ylabel("Sales")
    ax.tick_params(axis="x", rotation=25)
    fig.tight_layout()
    st.pyplot(fig)
    plt.close(fig)

with right:
    st.subheader("Profit by Region")
    region_sales = get_region_sales(filtered, value="Profit")
    fig, ax = plt.subplots(figsize=(7, 4))
    region_sales.plot(kind="bar", ax=ax)
    ax.set_xlabel("Region")
    ax.set_ylabel("Profit")
    ax.tick_params(axis="x", rotation=25)
    fig.tight_layout()
    st.pyplot(fig)
    plt.close(fig)

st.subheader("Monthly Sales Trend")
monthly_sales = get_monthly_sales(filtered)
fig, ax = plt.subplots(figsize=(12, 4))
monthly_sales.plot(kind="line", marker="o", ax=ax)
ax.set_xlabel("Month")
ax.set_ylabel("Sales")
fig.tight_layout()
st.pyplot(fig)
plt.close(fig)

st.subheader("Top 5 Products")
top_products = get_top_products(filtered, limit=5)
st.dataframe(top_products, use_container_width=True, hide_index=True)

with st.expander("View filtered sales data"):
    st.dataframe(filtered, use_container_width=True, hide_index=True)

csv_data = filtered.to_csv(index=False).encode("utf-8")
st.download_button("Download filtered data as CSV", csv_data, "filtered_sales_data.csv", "text/csv")
