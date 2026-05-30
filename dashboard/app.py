import streamlit as st
import pandas as pd
import psycopg2
import plotly.express as px
from streamlit_autorefresh import st_autorefresh

# =====================================================
# PAGE CONFIG
# =====================================================

st.set_page_config(
    page_title="Real-Time E-Commerce Analytics",
    page_icon="🛒",
    layout="wide"
)

# Auto refresh every 5 seconds
st_autorefresh(interval=5000, key="refresh")

# =====================================================
# DATABASE CONNECTION
# =====================================================

@st.cache_resource
def get_connection():
    return psycopg2.connect(
        host="localhost",
        port="5433",
        database="ecommerce",
        user="postgres",
        password="postgres"
    )

conn = get_connection()

# =====================================================
# LOAD DATA
# =====================================================

query = """
SELECT *
FROM orders
"""

df = pd.read_sql(query, conn)

if df.empty:
    st.warning("No data available.")
    st.stop()

# =====================================================
# DATA PREPARATION
# =====================================================

df["order_timestamp"] = pd.to_datetime(df["order_timestamp"])

# Revenue fallback
if "revenue" not in df.columns:
    df["revenue"] = df["price"] * df["quantity"]

# Fill missing customer names
df["customer_name"] = df["customer_name"].fillna("Unknown")

# =====================================================
# HEADER
# =====================================================

st.markdown("""
# 🛒 Real-Time E-Commerce Analytics Platform

### Kafka • PostgreSQL • Streamlit • Event-Driven Architecture
""")

# =====================================================
# KPI METRICS
# =====================================================

total_orders = len(df)
total_revenue = df["revenue"].sum()
avg_order_value = round(total_revenue / total_orders, 2)

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        label="Total Orders",
        value=f"{total_orders:,}"
    )

with col2:
    st.metric(
        label="Total Revenue",
        value=f"₹{total_revenue:,.0f}"
    )

with col3:
    st.metric(
        label="Average Order Value",
        value=f"₹{avg_order_value:,.0f}"
    )

st.markdown("---")

# =====================================================
# LIVE ORDER FEED
# =====================================================

st.subheader("⚡ Live Order Feed")

latest_orders = (
    df.sort_values("order_timestamp", ascending=False)
      .head(10)
)

for _, row in latest_orders.iterrows():

    st.success(
        f"🛍️ {row['customer_name']} ordered "
        f"{row['quantity']} x {row['product']} "
        f"for ₹{row['revenue']:,} from {row['city']}"
    )

st.markdown("---")

# =====================================================
# CHARTS ROW 1
# =====================================================

col1, col2 = st.columns(2)

with col1:

    city_sales = (
        df.groupby("city")["revenue"]
        .sum()
        .reset_index()
        .sort_values("revenue", ascending=False)
    )

    fig_city = px.bar(
        city_sales,
        x="city",
        y="revenue",
        title="Revenue by City"
    )

    st.plotly_chart(
        fig_city,
        use_container_width=True
    )

with col2:

    category_sales = (
        df.groupby("category")["revenue"]
        .sum()
        .reset_index()
    )

    fig_category = px.pie(
        category_sales,
        names="category",
        values="revenue",
        title="Revenue by Category"
    )

    st.plotly_chart(
        fig_category,
        use_container_width=True
    )

# =====================================================
# CHARTS ROW 2
# =====================================================

col1, col2 = st.columns(2)

with col1:

    top_products = (
        df.groupby("product")["revenue"]
        .sum()
        .reset_index()
        .sort_values("revenue", ascending=False)
    )

    fig_products = px.bar(
        top_products,
        x="product",
        y="revenue",
        title="Top Products"
    )

    st.plotly_chart(
        fig_products,
        use_container_width=True
    )

with col2:

    revenue_trend = (
        df.groupby(
            df["order_timestamp"].dt.strftime("%Y-%m-%d %H:%M")
        )["revenue"]
        .sum()
        .reset_index()
    )

    fig_trend = px.line(
        revenue_trend,
        x="order_timestamp",
        y="revenue",
        title="Revenue Trend"
    )

    st.plotly_chart(
        fig_trend,
        use_container_width=True
    )

# =====================================================
# TOP CUSTOMERS + CITY ORDERS
# =====================================================

st.markdown("---")

col1, col2 = st.columns(2)

with col1:

    st.subheader("🏆 Top Customers")

    top_customers = (
        df.groupby("customer_name")["revenue"]
        .sum()
        .reset_index()
        .sort_values("revenue", ascending=False)
        .head(10)
    )

    st.dataframe(
        top_customers,
        use_container_width=True
    )

with col2:

    st.subheader("🔥 Orders by City")

    city_orders = (
        df.groupby("city")
        .size()
        .reset_index(name="orders")
    )

    fig_orders = px.bar(
        city_orders,
        x="city",
        y="orders",
        title="Order Volume by City"
    )

    st.plotly_chart(
        fig_orders,
        use_container_width=True
    )

# =====================================================
# HEATMAP TABLE
# =====================================================

st.markdown("---")

st.subheader("📊 Product Revenue Heatmap")

heatmap_data = pd.pivot_table(
    df,
    values="revenue",
    index="city",
    columns="product",
    aggfunc="sum",
    fill_value=0
)

st.dataframe(
    heatmap_data,
    use_container_width=True
)

# =====================================================
# RECENT ORDERS
# =====================================================

st.markdown("---")

st.subheader("📦 Recent Orders")

recent_orders = (
    df.sort_values(
        "order_timestamp",
        ascending=False
    )
    .head(20)
)

st.dataframe(
    recent_orders,
    use_container_width=True
)