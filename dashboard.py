import streamlit as st
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

st.title("Dashboard Analisis E-Commerce")

# load data dari csv
top_3 = pd.read_csv('top_3_categories.csv')
bottom_3 = pd.read_csv('bottom_3_categories.csv')
avg_items_monthly = pd.read_csv('avg_items_per_month.csv')
avg_monthly_value = pd.read_csv('avg_transaction_value_per_month.csv')

# clean data
avg_items_monthly['month'] = avg_items_monthly['month'].astype(str)
avg_monthly_value['month'] = avg_monthly_value['month'].astype(str)

# Kategori produk yang sering dan paling jarang dibeli customer
st.subheader("Kategori Produk")

col1, col2 = st.columns(2)

with col1:
    st.write("Top 3 Kategori Paling Sering Dibeli")
    st.dataframe(top_3)

with col2:
    st.write("Top 3 Kategori Paling Jarang Dibeli")
    st.dataframe(bottom_3)

# Rata-rata jumlah produk dalam satu pesanan
st.subheader("Rata-rata Produk per Pesanan per Bulan")

fig, ax = plt.subplots(figsize=(5, 4))
ax.bar(avg_items_monthly['month'], avg_items_monthly['avg_items'])
for i, (month, val) in enumerate(zip(avg_items_monthly['month'], avg_items_monthly['avg_items'])):
    ax.annotate(f'{val:.2f}', (month, val), ha='center', va='bottom')
ax.set_xlabel('Bulan')
ax.set_ylabel('Rata-rata Jumlah Produk')
ax.set_title('Rata-rata Produk per Pesanan per Bulan')
st.pyplot(fig, clear_figure=True)

# Tren transaksi bulanan
st.subheader("Tren Transaksi Bulanan")

fig, ax = plt.subplots(figsize=(8, 3))
ax.plot(avg_monthly_value['month'], avg_monthly_value['avg_transaction_value'], marker='o')
ax.set_xlabel('Bulan')
ax.set_ylabel('Rata-rata Nilai Transaksi')
ax.set_title('Tren Rata-rata Nilai Transaksi per Bulan (Juni–Agustus 2018)')
ax.tick_params(axis='x', rotation=45)
plt.tight_layout()
st.pyplot(fig, clear_figure=True)
