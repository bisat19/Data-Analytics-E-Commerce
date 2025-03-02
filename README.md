#  Project Data Analytics: E-Commerce Public Dataset 

## 📚 Table of Contents

- [ Project Data Analytics: E-Commerce Public Dataset ](#-project-data-analytics-e-commerce-public-dataset-)
  - [📚 Table of Contents](#-table-of-contents)
  - [🎯 Pengenalan](#-pengenalan)
  - [💻 Instalasi](#-instalasi)
  - [🔄 Project Workflow](#-project-workflow)
  - [📈 Dashboard Explanation](#-dashboard-explanation)


## 🎯 Pengenalan

Proyek ini berfokus pada analisis kumpulan data publik e-commerce di Brasil. Himpunan data mencakup informasi tentang pesanan pelanggan, produk, pembayaran, ulasan, dan banyak lagi. Tujuan dari proyek ini adalah untuk mengekstrak wawasan yang bermakna dari data yang dapat membantu meningkatkan strategi bisnis dan pengalaman pelanggan.

## 💻 Instalasi

Ikuti langkah-langkah ini untuk mengaktifkan dan menjalankan proyek di komputer lokal Anda:

1. **Clone repository**

   Clone repository dengan git:

   ```bash
    link nanti
   ```

2. **Set up virtual environment** (Optional)

   Disarankan untuk membuat lingkungan virtual untuk menjaga dependensi yang diperlukan oleh proyek ini terpisah dari lingkungan Python sistem Anda. Berikut cara membuat lingkungan virtual:

   ```bash
   python3 -m venv env
   ```

   Activate the virtual environment:

   On Windows:

   ```bash
   .\env\Scripts\activate
   ```

   On Unix or MacOS:

   ```ls
   source env/bin/activate
   ```

3. **Install dependencies**

   Arahkan ke direktori proyek dan instal paket yang diperlukan menggunakan pip:

   ```bash
   pip install -r requirements.txt
   ```

4. **Run project**

   Sekarang Anda dapat menjalankan proyek dengan mudah dengan mengklik tombol jalankan semua di notebook jupyter

## 🔄 Project Workflow

1. **Data Wrangling**
    
   Langkah pertama dari proyek ini adalah membersihkan dan menyiapkan data untuk dianalisis. Proses Data Wrangling meliputi:

   - Handling missing values
   - Handling duplicate values
   - Handling data redundancy
   - Handling incorrect data types
   - Handling outliers
   - Handling inconsistent data


2. **Exploratory Data Anlaysis**

    Langkah kedua dari proyek ini adalah mengeksplorasi data dan mengekstrak wawasan yang bermakna. Proses analisis data eksplorasi meliputi:
    
    - Analisa Order
    - Analisa Produk
    - Analisa Pembayaran
    - Analisa Kustomer
    - Analisa Reviews
    - Analisa Sellers

3. **Data Visualization**
   
    Langkah ketiga dari proyek ini adalah memvisualisasikan data dan mengekstrak wawasan yang bermakna. Proses visualisasi data meliputi:
    
    - Visualisasi Trend Penjualan
    - Visualisasi Total Pendapatan
    - Visualisasi 10 Kategori Paling Laris
    - Visualisasi 10 Kategori dengan Rating Terbaik
    - Visualisasi On Time Percentage
    - Visualisasi Konsumen Terbaik dengan RFM
    - Visualisasi Distribusi Pelanggan
  
4. **Dashboard**

    Langkah terakhir dari proyek ini adalah membuat dasbor yang dapat digunakan untuk memvisualisasikan data dan mengekstrak wawasan yang bermakna. Dasbor meliputi:
    
    - Kinerja penjualan Kategori Produk
    - Kinerja penjualan Tahunan dan Bulanan

## 📈 Dashboard Explanation

Ikuti langkah-langkah ini untuk menjalankan dasbor di komputer lokal Anda:

1. **Run the Streamlit app**

   Arahkan ke direktori proyek dan jalankan aplikasi Streamlit menggunakan perintah berikut:

   ```sh
   streamlit run dashboard/dashboard.py
   ```

   Ini akan memulai server Streamlit dan membuka halaman baru di browser web default Anda dengan URL aplikasi Streamlit.

   Atau Anda dapat menjalankan dasbor langsung dari browser web dengan mengklik tautan berikut:[STREAMLIT APP LINK](link)

2. **Menggunakan Dashboard**

Dasbor menyediakan representasi visual dari data kinerja penjualan. Berikut cara menggunakannya:

- **Filter Tahun**

   Gunakan filter tahun untuk melihat total penjualan, rata-rata rating produk serta total pendapatan. 
   Anda juga dapat melihat pertumbuhan penjualan pada tahun yang anda pilih.
   Selain itu terdapat On Time Percentage pada tahun yang anda pilih, juga 10 Produk terlaris, dan 
   Distribusi kota paling banyak.

```python
print("Thank you for reading! 🙏")
```

**Thank you for reading! 🙏**

<div align='center'><img src="https://user-images.githubusercontent.com/74038190/212284115-f47cd8ff-2ffb-4b04-b5bf-4d1c14c0247f.gif" width="1000"></div>