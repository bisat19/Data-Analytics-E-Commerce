#Nama   : Abisatya Hastarangga Pradana
#Email  : riabitya@gmail.com
#ID     : abisatya_19
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

# Load dataset
@st.cache_data
def load_data():
    df = pd.read_csv("all_data.csv", parse_dates=["order_purchase_timestamp"])
    df["year"] = df["order_purchase_timestamp"].dt.year  
    return df

df = load_data()

# Sidebar filter tahun
years = sorted(df["year"].unique())
selected_year = st.sidebar.selectbox("Pilih Tahun", years, index=len(years)-1)
df_filtered = df[df["year"] == selected_year]

# Add year_month column
df_filtered["year_month"] = df_filtered["order_purchase_timestamp"].dt.to_period("M").astype(str)

# Dashboard Title
st.title("📊 Dashboard Penjualan E-Commerce")

# Metrics Display
col1, col2, col3 = st.columns(3)

# Total Penjualan
col1.metric("Total Penjualan", f"{df_filtered['order_id'].nunique():,}")

# Rata-rata Review Score
avg_rating = df_filtered["review_score"].mean()
col2.metric("Rata-rata Rating", f"{avg_rating:.1f} ⭐")

# Total Pendapatan
col3.metric("Total Pendapatan", f"${df_filtered['total_price'].sum():,.2f}")

# Growth Rate Calculation
growth_df = df_filtered.groupby("year_month")["total_price"].sum().pct_change() * 100
growth_df = growth_df.reset_index().rename(columns={"total_price": "growth_rate"})

# Trend Growth Rate Plot
st.subheader("📈 Trend Pertumbuhan Penjualan")

# Prepare the data for st.line_chart
growth_df.set_index("year_month", inplace=True)  # Set the index to the x-axis values

# Create the line chart
st.line_chart(growth_df["growth_rate"])  # Pass the y-values directly

# Pie Chart On-Time vs Late
st.subheader("⏳ Persentase Pengiriman On-Time vs Late")
on_time_counts = df_filtered["on_time"].value_counts(normalize=True) * 100
fig_pie = px.pie(
    names=["On Time", "Late"],
    values=on_time_counts,
    color_discrete_sequence=px.colors.sequential.Viridis
)
st.plotly_chart(fig_pie)

# Bar Chart Top 5 Best-Selling Categories
st.subheader("🏆 5 Kategori Produk Terlaris")
top_categories = df_filtered["product_category_name_english"].value_counts().head(5)
fig_bar = px.bar(
    x=top_categories.index,
    y=top_categories.values,
    labels={'x': 'Kategori', 'y': 'Jumlah Penjualan'},
    text=top_categories.values,
    color=top_categories.values,
    color_continuous_scale=px.colors.sequential.Viridis 
)
st.plotly_chart(fig_bar)

# Bar Chart 10 Kota dengan Pelanggan Terbanyak
st.subheader("📍 10 Kota dengan Pelanggan Terbanyak")
top_customers_city = df_filtered["customer_city"].value_counts().head(10)
fig_city = px.bar(
    x=top_customers_city.index,
    y=top_customers_city.values,
    labels={'x': 'Kota', 'y': 'Jumlah Pelanggan'},
    text=top_customers_city.values,
    color=top_customers_city.values,
    color_continuous_scale=px.colors.sequential.Viridis
)
st.plotly_chart(fig_city)


