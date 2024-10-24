# Technical-Assessment-Arithmetic

Bagian I: Deret Bilangan Aritmatika

Deskripsi
Aplikasi ini membuat deret bilangan aritmatika berdasarkan input jumlah bilangan. Deret dimulai dari 2 dengan beda 3.

Cara Menjalankan
Clone repository ini:
bash
Copy code
git clone <repository-link>
Navigasi ke folder:
bash
Copy code
cd Technical-Assessment-Arithmetic
Jalankan program:
bash
Copy code
python arithmetic_series.py
Contoh Input:
Input: 4
Output: 2, 5, 8, 11
Persyaratan
Python 3.x
Bagian II: Modul Odoo

Deskripsi
Modul ini menyediakan sistem pemesanan ruangan dengan dua tabel:

Master Ruangan: Menyimpan informasi ruangan.
Pemesanan Ruangan: Mengatur pemesanan dan statusnya.
Fitur Utama
Validasi pemesanan:
Tidak boleh memesan ruangan dan tanggal yang sama.
Nama pemesan harus unik.
Status pemesanan dapat diubah (Draft → On Going → Done).
Cara Install Modul Odoo
Clone repository ini:
bash
Copy code
git clone <repository-link>
Masuk ke folder:
bash
Copy code
cd Technical-Assessment-Odoo
Copy folder modul ke direktori addons Odoo:
bash
Copy code
cp -r odoo_module_folder /path/to/odoo/addons/
Restart Odoo server:
bash
Copy code
sudo service odoo restart
Aktifkan modul di Odoo:
Login ke Odoo sebagai admin.
Pergi ke Apps, aktifkan Developer Mode.
Cari dan install modul Room Reservation.
Validasi
Tidak ada duplikat pemesanan pada ruangan dan tanggal yang sama.
Nama pemesan unik.
Nama ruangan tidak boleh sama.
Contoh Tampilan
Master Ruangan: Ditampilkan dalam format Grid/List.
Pemesanan Ruangan: Menampilkan status dan memungkinkan perubahan status pemesanan.
Persyaratan
Odoo 15+
Python 3.x
PostgreSQL
Struktur Direktori
markdown
Copy code
Technical-Assessment-Odoo/
│
├── models/
│   └── models.py
├── views/
│   └── views.xml
├── __init__.py
├── __manifest__.py
└── README.md
Cara Penggunaan
Buat Master Ruangan terlebih dahulu dari menu.
Lakukan Pemesanan dengan memilih ruangan dan tanggal.
Update status pemesanan menggunakan tombol yang tersedia.
