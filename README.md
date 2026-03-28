# 📦 Sistem Inventory Barang

Aplikasi web sederhana untuk manajemen inventori barang menggunakan **Python Flask** dan **MySQL**. Proyek ini dibuat sebagai bagian dari pembelajaran pengembangan backend dan manajemen database.

## 🚀 Fitur Utama
* **Manajemen Barang (CRUD):** Tambah, lihat, edit, dan hapus data barang.
* **Sistem Kategori:** Pengelompokan barang berdasarkan kategori dinamis.
* **Pencarian & Filter:** Mencari barang berdasarkan nama dan filter berdasarkan kategori secara bersamaan.
* **Upload Gambar:** Mendukung unggah foto produk untuk setiap barang.
* **Format Rupiah Otomatis:** Input harga dengan format ribuan otomatis di sisi client.

## 🛠️ Tech Stack
* **Backend:** Python 3.x, Flask
* **Database:** MySQL (SQLAlchemy ORM)
* **Frontend:** HTML5, Bootstrap 5, Jinja2 (Templating)

## 📋 Langkah Instalasi

### 1. Persiapan Database (MySQL)
Sebelum menjalankan aplikasi, kamu perlu menyiapkan database di XAMPP/MySQL lokal:
* Buka **phpMyAdmin** (`localhost/phpmyadmin`).
* Buat database baru dengan nama `db_inventory`.
* Kamu tidak perlu membuat tabel secara manual, Flask-SQLAlchemy akan membuatnya otomatis saat pertama kali dijalankan lewat `db.create_all()`.

### 2. Pengaturan Virtual Environment (Venv)
Virtual environment digunakan agar library proyek ini tidak bentrok dengan library lain di komputermu:
```bash
# Membuat venv
python -m venv venv

# Mengaktifkan venv (Windows)
venv\Scripts\activate

# Mengaktifkan venv (Linux/macOS)
source venv/bin/activate
