# Dashboard Analisis E-Commerce

Proyek analisis data menggunakan dataset publik e-commerce Brasil untuk menjawab pertanyaan bisnis seputar tren pembelian produk periode **Juni – Agustus 2018**.

---

## Struktur Proyek

```
submission/
├── notebook.ipynb                        # Notebook analisis data lengkap
├── dashboard.py                          # Aplikasi dashboard Streamlit
├── orders_dataset.csv                    # Dataset pesanan
├── order_items_dataset.csv              # Dataset item pesanan
├── products_dataset.csv                 # Dataset produk
├── product_category_name_translation.csv # Terjemahan kategori produk
├── main_data.csv                         # Data gabungan hasil wrangling
├── top_3_categories.csv                  # Output: top 3 kategori paling sering diberli
├── bottom_3_categories.csv              # Output: top 3 kategori paling jarang dibeli
├── avg_items_per_month.csv              # Output: rata-rata item per pesanan per bulan
├── avg_transaction_value_per_month.csv  # Output: rata-rata nilai transaksi per bulan
└── README.md
```

---

## Pertanyaan Bisnis

1. Kategori produk mana yang **paling sering** dan **paling jarang** dibeli customer dalam 3 bulan terakhir (Juni – Agustus 2018)?
2. Berapa **rata-rata jumlah produk** dalam satu pesanan setiap bulan selama periode tersebut?
3. Berapa **rata-rata total nilai transaksi** dalam satu pesanan setiap bulan selama periode tersebut?

---

## Kesimpulan

- **Kategori terlaris:** `health_beauty`, `bed_bath_table`, dan `housewares`
- **Kategori terjarang dibeli:** `furniture_mattress_and_upholstery`, `tablets_printing_image`, dan `fashion_sport`
- **Rata-rata produk per pesanan:** 1,12 – 1,15 produk (customer cenderung memesan 1 produk per transaksi)
- **Tren nilai transaksi:** berfluktuasi selama periode tersebut; tertinggi di Juli 2018, terendah di Agustus 2018

---

## Rekomendasi

- Tampilkan kategori populer secara prominan di halaman utama
- Tambahkan fitur rekomendasi produk di halaman keranjang
- Terapkan diskon atau bundling untuk kategori yang jarang dibeli
- Gencarkan promosi pada bulan-bulan dengan nilai transaksi rendah

---

## Setup Environment

### Prasyarat

- Python 3.7+
- pip

### Instalasi dependensi

```bash
pip install pandas numpy matplotlib seaborn scipy streamlit
```

---

## Menjalankan Notebook

Buka dan jalankan `notebook.ipynb` menggunakan Jupyter Notebook atau JupyterLab:

```bash
jupyter notebook notebook.ipynb
```

Pastikan semua file CSV dataset berada dalam folder yang sama dengan notebook.

---

## Menjalankan Dashboard Streamlit

Pastikan semua file CSV output (`top_3_categories.csv`, `bottom_3_categories.csv`, `avg_items_per_month.csv`, `avg_transaction_value_per_month.csv`) sudah tersedia — file ini dihasilkan setelah menjalankan notebook.

```bash
streamlit run dashboard.py
```

Dashboard akan terbuka otomatis di browser pada `http://localhost:8501`.

---

## Author

- **Nama:** Azkia Wahtilafinnahri
- **Email:** Azkiawahtilafinnahri@gmail.com
- **ID Dicoding:** azkiajeon
