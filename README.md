```markdown
# Technical-Assessment-Arithmetic

## Bagian I: Deret Bilangan Aritmatika

### Deskripsi
Program ini menghasilkan deret bilangan aritmatika dengan panjang sesuai input pengguna. Setiap bilangan dalam deret memiliki angka awal **2** dan beda **3** antar bilangan berturut-turut.

### Cara Menjalankan
1. **Clone repository ini:**
   ```bash
   git clone <repository-link>
   ```
2. **Navigasi ke folder:**
   ```bash
   cd Technical-Assessment-Arithmetic
   ```
3. **Jalankan program:**
   ```bash
   python arithmetic_series.py
   ```
4. **Contoh Input dan Output:**
   - **Input:** 4
   - **Output:** 2, 5, 8, 11

### Persyaratan
- Python 3.x

### Struktur Direktori
```
Technical-Assessment-Arithmetic/
│
├── arithmetic_series.py
└── README.md
```

### Cara Penggunaan
1. Pastikan Python 3.x sudah terinstal.
2. Buka terminal dan arahkan ke folder proyek.
3. Jalankan program dengan perintah:
   ```bash
   python arithmetic_series.py
   ```
4. Masukkan jumlah deret saat diminta.

### Contoh Error Handling
Jika input bukan bilangan positif, program akan menampilkan pesan kesalahan:
```
Error: Jumlah N harus bilangan positif.
```

Berikut adalah **README.md** untuk **Bagian II: Modul Odoo** menggunakan format serupa dengan yang di bagian 1:

---

# **Technical-Assessment-Odoo**

## **Bagian II: Modul Pemesanan Ruangan**

### **Deskripsi**
Modul ini menyediakan sistem pemesanan ruangan di Odoo dengan dua tabel utama:
1. **Master Ruangan**: Menyimpan informasi ruangan seperti nama, tipe, lokasi, kapasitas, dan foto.
2. **Pemesanan Ruangan**: Mencatat pemesanan dan statusnya (Draft, On Going, Done) dengan validasi agar tidak ada pemesanan duplikat.

### **Cara Menjalankan**
1. **Clone repository ini:**
   ```bash
   git clone <repository-link>
   ```
2. **Navigasi ke folder:**
   ```bash
   cd Technical-Assessment-Odoo
   ```
3. **Copy modul ke direktori addons Odoo:**
   ```bash
   cp -r odoo_module_folder /path/to/odoo/addons/
   ```
4. **Restart server Odoo:**
   ```bash
   sudo service odoo restart
   ```
5. **Aktifkan modul di Odoo:**
   - Login sebagai admin ke Odoo.
   - Pergi ke menu **Apps** dan aktifkan **Developer Mode**.
   - Cari dan install modul **Room Reservation**.

### **Contoh Penggunaan**
1. **Buat Master Ruangan** dengan mengisi nama, tipe, lokasi, kapasitas, dan foto ruangan.
2. **Lakukan Pemesanan** dengan memilih ruangan dan tanggal yang tersedia.
3. **Update Status Pemesanan** menggunakan tombol yang tersedia:
   - Draft → On Going → Done

### **Validasi dan Pesan Kesalahan**
- **Nama pemesan harus unik**.
- **Tidak boleh ada pemesanan ruangan** yang sama pada tanggal yang sama.
- **Nama ruangan tidak boleh duplikat**.

### **Struktur Direktori**
```
Technical-Assessment-Odoo/
│
├── models/
│   └── models.py
├── views/
│   └── views.xml
├── __init__.py
├── __manifest__.py
└── README.md
```

### **Persyaratan**
- Odoo 15+
- Python 3.x
- PostgreSQL

### **Contoh Error Handling**
- Jika ruangan yang sama dipesan pada tanggal yang sama:
  ```
  ValidationError: Ruangan sudah dipesan pada tanggal tersebut.
  ```
- Jika nama pemesan sudah ada:
  ```
  ValidationError: Nama pemesan sudah ada.
  ```
