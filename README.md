# Search Engine Rekomendasi Kuliner

Aplikasi web berbasis Streamlit untuk merekomendasikan tempat kuliner berdasarkan preferensi pengguna menggunakan metode **TF-IDF** dan **Cosine Similarity**.

## Deskripsi Proyek

Proyek ini merupakan sistem rekomendasi kuliner yang menganalisis review bintang 5 dari Google Maps untuk memberikan rekomendasi restoran yang relevan dengan query pencarian pengguna. Sistem menggunakan teknik **Natural Language Processing (NLP)** dan **Information Retrieval** untuk mencocokkan preferensi pengguna dengan karakteristik restoran.

## Fitur Utama

- **Pencarian Berbasis Teks**: Cari berdasarkan nama makanan, rasa, atau suasana
- **Ranking dengan Cosine Similarity**: Hasil diurutkan berdasarkan tingkat kemiripan dengan query
- **Filter Berdasarkan Area**: Pilih area geografis tertentu untuk mempersempit hasil
- **Review Bintang 5**: Tampilkan review autentik dari Google Maps
- **Kontrol Jumlah Review**: Pilih jumlah review yang ingin ditampilkan (5 atau 10)
- **Responsive Interface**: Antarmuka yang bersih dan mudah digunakan

## Teknologi yang Digunakan

- **Python 3.14**
- **Streamlit** - Framework untuk membuat aplikasi web interaktif
- **Pandas** - Manipulasi dan analisis data
- **Scikit-learn** - Machine learning (TF-IDF dan Cosine Similarity)
- **JSON** - Parsing data review

## Instalasi

### Prasyarat

Pastikan Anda telah menginstal:
- Python 3.8 atau versi lebih baru
- pip (Python package manager)

### Langkah-langkah Instalasi

1. **Clone atau download repository ini**
   ```bash
   cd e:\Kuliah\STKI\Tugas Akhir\rekomendasi-makanan
   ```

2. **Buat virtual environment (opsional tapi disarankan)**
   ```bash
   python -m venv .venv
   ```

3. **Aktifkan virtual environment**
   
   Windows (PowerShell):
   ```bash
   .\.venv\Scripts\Activate.ps1
   ```
   
   Windows (Command Prompt):
   ```bash
   .venv\Scripts\activate.bat
   ```
   
   Linux/Mac:
   ```bash
   source .venv/bin/activate
   ```

4. **Install dependencies**
   ```bash
   pip install streamlit pandas scikit-learn
   ```

## Cara Menjalankan Aplikasi

1. Pastikan Anda berada di direktori proyek dan virtual environment sudah aktif

2. Jalankan aplikasi dengan perintah:
   ```bash
   streamlit run app.py
   ```

3. Aplikasi akan terbuka otomatis di browser Anda pada alamat:
   - **Local URL**: http://localhost:8501
   - **Network URL**: http://192.168.x.x:8501

4. Untuk menghentikan aplikasi, tekan `Ctrl+C` di terminal

## Cara Menggunakan

1. **Masukkan Query Pencarian**
   - Ketik kata kunci di kolom pencarian seperti "nasi goreng pedas gurih"
   - Sistem akan mencari restoran yang reviewnya mengandung karakteristik tersebut

2. **Filter Hasil (Opsional)**
   - Gunakan sidebar di sebelah kiri untuk memilih area tertentu
   - Pilih jumlah review yang ingin ditampilkan (5 atau 10)

3. **Lihat Hasil**
   - Hasil ditampilkan dengan skor cosine similarity
   - Klik "⭐ Lihat review bintang 5" untuk membaca review lengkap dari pengguna Google Maps

## Struktur Proyek

```
rekomendasi-makanan/
├── app.py                          # File utama aplikasi Streamlit
├── scraper_gmaps.py               # Script untuk scraping data Google Maps
├── output/                        # Folder berisi data hasil preprocessing
│   ├── kuliner_merged.csv        # Data gabungan untuk UI
│   └── kuliner_preprocessed.csv  # Data yang sudah dipreprocess untuk model
├── data_raw/                      # Data mentah hasil scraping
├── notebooks/                     # Jupyter notebooks untuk analisis
├── .venv/                         # Virtual environment (jika ada)
└── README.md                      # Dokumentasi proyek (file ini)
```

## Cara Kerja Sistem

1. **Preprocessing**: Review dari Google Maps dibersihkan dan dinormalisasi (lowercase)
2. **TF-IDF Vectorization**: Mengubah teks review menjadi vektor numerik dengan bobot TF-IDF
   - Menggunakan bigram (1-2 kata)
   - Min document frequency: 2
   - Max document frequency: 90%
3. **Query Processing**: Query pengguna dipreprocess dengan cara yang sama
4. **Cosine Similarity**: Menghitung kemiripan antara query dan setiap review
5. **Ranking**: Hasil diurutkan berdasarkan skor similarity tertinggi
6. **Filtering**: Menerapkan filter area jika dipilih pengguna

## Data

Aplikasi ini menggunakan dua file CSV:
- `kuliner_merged.csv`: Berisi informasi restoran dan review untuk ditampilkan
- `kuliner_preprocessed.csv`: Berisi review yang sudah dibersihkan untuk pemrosesan model

Kolom kunci untuk join:
- `restaurant`: Nama restoran
- `area`: Area/lokasi restoran

## Konfigurasi

Anda dapat memodifikasi parameter TF-IDF di file `app.py`:

```python
vectorizer = TfidfVectorizer(
    ngram_range=(1, 2),  # Gunakan unigram dan bigram
    min_df=2,            # Minimum muncul di 2 dokumen
    max_df=0.9           # Maksimum muncul di 90% dokumen
)
```

## Troubleshooting

### Error: "ModuleNotFoundError"
Pastikan semua dependencies sudah terinstall:
```bash
pip install streamlit pandas scikit-learn
```

### Error: "Kolom join tidak ditemukan"
Pastikan file CSV di folder `output/` memiliki kolom `restaurant` dan `area`

### Error: "FileNotFoundError"
Pastikan file berikut ada di folder `output/`:
- `kuliner_merged.csv`
- `kuliner_preprocessed.csv`

## Catatan

- Aplikasi ini hanya menampilkan review dengan **rating bintang 5** dari Google Maps
- Skor cosine similarity berkisar dari 0 (tidak relevan) hingga 1 (sangat relevan)
- Hasil pencarian hanya menampilkan review dengan skor > 0

## Pembuat

- Nama    : Bintang Rifky Ananta
- NIM     : A11.2023.15116

## Lisensi

Proyek ini dibuat untuk keperluan akademik.
