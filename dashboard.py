import streamlit as st
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

st.title("Dashboard Analisis E-Commerce")

# load data dari csv
@st.cache_data
def load_data():
    top_categories    = pd.read_csv('top_3_categories.csv')
    bottom_categories = pd.read_csv('bottom_3_categories.csv')
    avg_items         = pd.read_csv('avg_items_per_month.csv')
    avg_value         = pd.read_csv('avg_transaction_value_per_month.csv')
    avg_items['month'] = avg_items['month'].astype(str)
    avg_value['month'] = avg_value['month'].astype(str)
    return top_categories, bottom_categories, avg_items, avg_value
 
top_categories, bottom_categories, avg_items_monthly, avg_monthly_value = load_data()

#metric
st.subheader("Ringkasan Per Bulan")
 
max_val   = avg_monthly_value['avg_transaction_value'].max()
min_val   = avg_monthly_value['avg_transaction_value'].min()
avg_val   = avg_monthly_value['avg_transaction_value'].mean()
best_month = avg_monthly_value.loc[avg_monthly_value['avg_transaction_value'].idxmax(), 'month']
 
m1, m2, m3, m4 = st.columns(4)
m1.metric("Nilai Transaksi Tertinggi", f"USD {max_val:,.0f}")
m2.metric("Nilai Transaksi Terendah",  f"USD {min_val:,.0f}")
m3.metric("Rata-rata Transaksi",       f"USD {avg_val:,.0f}")
m4.metric("Bulan Terbaik",             best_month)
 
st.divider()

#kategori produk
st.subheader("Kategori Produk")
 
# Slider Top Kategori
n = st.slider("Menampilkan Jumlah Top Kategori:", min_value=1, max_value=3, value=3)
 
# Re-load semua kategori agar slider bisa expand lebih dari 3
# (fallback ke data asli kalau hanya tersedia 3 baris)
top_n    = top_categories.head(n)
bottom_n = bottom_categories.head(n)
 
col1, col2 = st.columns(2)
 
with col1:
    st.write(f"Top {n} Kategori Paling Sering Dibeli")
    st.dataframe(top_n, use_container_width=True)
    st.download_button(
        label="⬇️ Download CSV",
        data=top_n.to_csv(index=False),
        file_name=f"top_{n}_kategori.csv",
        mime="text/csv",
        key="dl_top"
    )
 
with col2:
    st.write(f"Top {n} Kategori Paling Jarang Dibeli")
    st.dataframe(bottom_n, use_container_width=True)
    st.download_button(
        label="⬇️ Download CSV",
        data=bottom_n.to_csv(index=False),
        file_name=f"bottom_{n}_kategori.csv",
        mime="text/csv",
        key="dl_bottom"
    )
 
st.divider()

#rata rata produk per persanan
st.subheader("Rata-rata Produk per Pesanan per Bulan")
 
# Filter bulan
semua_bulan  = avg_items_monthly['month'].tolist()
bulan_pilih  = st.multiselect(
    "Filter Bulan:",
    options=semua_bulan,
    default=semua_bulan,
    key="filter_items"
)
 
# Toggle tipe chart
chart_type_items = st.radio(
    "Tipe Chart:",
    ["Bar", "Line"],
    horizontal=True,
    key="chart_items"
)
 
filtered_items = avg_items_monthly[avg_items_monthly['month'].isin(bulan_pilih)]
 
if filtered_items.empty:
    st.warning("Pilih minimal satu bulan untuk menampilkan chart.")
else:
    fig, ax = plt.subplots(figsize=(7, 4))
 
    if chart_type_items == "Bar":
        ax.bar(filtered_items['month'], filtered_items['avg_items'], color='steelblue')
        for month, val in zip(filtered_items['month'], filtered_items['avg_items']):
            ax.annotate(f'{val:.2f}', (month, val), ha='center', va='bottom', fontsize=9)
    else:
        ax.plot(filtered_items['month'], filtered_items['avg_items'],
                marker='o', color='steelblue', linewidth=2)
        for month, val in zip(filtered_items['month'], filtered_items['avg_items']):
            ax.annotate(f'{val:.2f}', (month, val), textcoords="offset points",
                        xytext=(0, 8), ha='center', fontsize=9)
 
    ax.set_xlabel('Bulan')
    ax.set_ylabel('Rata-rata Jumlah Produk')
    ax.set_title('Rata-rata Produk per Pesanan per Bulan')
    plt.tight_layout()
    st.pyplot(fig, clear_figure=True)
 
    st.download_button(
        label="⬇️ Download Data CSV",
        data=filtered_items.to_csv(index=False),
        file_name="avg_items_filtered.csv",
        mime="text/csv",
        key="dl_items"
    )
 
st.divider()

#tren tranksaksi bulanan
st.subheader("Tren Transaksi Bulanan")
 
# Filter bulan
semua_bulan_val = avg_monthly_value['month'].tolist()
bulan_pilih_val = st.multiselect(
    "Filter Bulan:",
    options=semua_bulan_val,
    default=semua_bulan_val,
    key="filter_value"
)
 
# Toggle tipe chart
chart_type_val = st.radio(
    "Tipe Chart:",
    ["Line", "Bar"],
    horizontal=True,
    key="chart_value"
)
 
filtered_value = avg_monthly_value[avg_monthly_value['month'].isin(bulan_pilih_val)]
 
if filtered_value.empty:
    st.warning("Pilih minimal satu bulan untuk menampilkan chart.")
else:
    fig, ax = plt.subplots(figsize=(9, 4))
 
    if chart_type_val == "Line":
        ax.plot(filtered_value['month'], filtered_value['avg_transaction_value'],
                marker='o', color='coral', linewidth=2)
    else:
        ax.bar(filtered_value['month'], filtered_value['avg_transaction_value'],
               color='coral')
        for month, val in zip(filtered_value['month'], filtered_value['avg_transaction_value']):
            ax.annotate(f'USD {val:,.0f}', (month, val), ha='center', va='bottom', fontsize=8)
 
    ax.set_xlabel('Bulan')
    ax.set_ylabel('Rata-rata Nilai Transaksi')
    ax.set_title('Tren Rata-rata Nilai Transaksi per Bulan (Juni–Agustus 2018)')
    ax.tick_params(axis='x', rotation=45)
    plt.tight_layout()
    st.pyplot(fig, clear_figure=True)
 
    st.download_button(
        label="⬇️ Download Data CSV",
        data=filtered_value.to_csv(index=False),
        file_name="avg_value_filtered.csv",
        mime="text/csv",
        key="dl_value"
    )
