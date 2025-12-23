# 📚 Aplikasi Kuis Pembelajaran

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Tests](https://img.shields.io/badge/Tests-124%20Passed-brightgreen.svg)](test_all.py)

Aplikasi kuis pembelajaran interaktif berbasis command-line yang dibangun dengan Python. Aplikasi ini memungkinkan pengguna untuk mengerjakan kuis dari berbagai mata pelajaran dengan tingkat kesulitan yang berbeda.

---

## 📋 Daftar Isi

- [Fitur](#-fitur)
- [Struktur Proyek](#-struktur-proyek)
- [Persyaratan Sistem](#-persyaratan-sistem)
- [Instalasi](#-instalasi)
- [Cara Penggunaan](#-cara-penggunaan)
- [Arsitektur Aplikasi](#-arsitektur-aplikasi)
- [API Reference](#-api-reference)
- [Menambah Soal Baru](#-menambah-soal-baru)

---

## ✨ Fitur

### 🔐 Autentikasi Pengguna

- **Sign Up** - Pendaftaran akun baru dengan validasi email dan password
- **Login** - Masuk ke akun yang sudah terdaftar
- **Logout** - Keluar dari akun
- **Lupa Password** - Reset password melalui email (simulasi)
- **Ubah Password** - Mengubah password akun

### 📝 Sistem Kuis

- **Multiple Mata Pelajaran** - Matematika, IPA, PKN, Sejarah
- **3 Tingkat Kesulitan** - Mudah, Sedang, Sulit
- **Penilaian Otomatis** - Perhitungan skor real-time
- **Feedback Performa** - Umpan balik berdasarkan nilai

### 📊 Riwayat & Statistik

- **Simpan Riwayat** - Setiap hasil kuis disimpan otomatis
- **Lihat Riwayat** - Akses riwayat kuis sebelumnya
- **Filter by User** - Riwayat per pengguna

### 🛡️ Keamanan & Validasi

- **Input Validation** - Validasi semua input pengguna
- **Error Handling** - Penanganan error yang komprehensif
- **Data Persistence** - Penyimpanan data dengan JSON

---

---

## 💻 Persyaratan Sistem

| Komponen | Versi Minimum           |
| -------- | ----------------------- |
| Python   | 3.8+                    |
| OS       | Windows / Linux / macOS |
| RAM      | 512 MB                  |
| Storage  | 50 MB                   |

### Dependencies

Aplikasi ini menggunakan **standard library Python** saja, tidak memerlukan package eksternal:

- `json` - Parsing dan serialisasi JSON
- `os` - Operasi file system
- `sys` - System-specific parameters
- `datetime` - Manipulasi tanggal dan waktu
- `typing` - Type hints
- `re` - Regular expressions

---

## 🚀 Instalasi

### 1. Clone Repository

```bash
git clone https://github.com/Afdiand/quiz-edu.git
cd quiz-edu
```

### 2. Verifikasi Python

```bash
python --version
# Output: Python 3.8.x atau lebih tinggi
```

### 3. Jalankan Aplikasi

```bash
python main.py
```

Aplikasi akan otomatis membuat folder `assets/` dan file-file yang diperlukan pada saat pertama kali dijalankan.

---

## 📖 Cara Penggunaan

### Menjalankan Aplikasi

```bash
python main.py
```

### Menu Utama (Guest)

```
==================================================
      📚 APLIKASI KUIS PEMBELAJARAN 📚
==================================================

  MENU:
  1.   Login
  2.   Daftar Akun
  3.   Lupa Password
  4.   Lihat Daftar Mapel
  0.   Keluar

  Pilihan Anda: _
```

### Menu Utama (Logged In)

```
==================================================
        APLIKASI KUIS PEMBELAJARAN
==================================================

  👤 Login sebagai: john_doe

  MENU:
  1.   Mulai Kuis
  2.   Lihat Riwayat
  3.   Lihat Daftar Mapel
  4.   Ubah Password
  5.   Logout
  0.   Keluar

  Pilihan Anda: _
```

### Contoh Alur Kuis

#### 1. Pilih Mata Pelajaran

```
  DAFTAR MATA PELAJARAN:
------------------------------
  0. Matematika (MTK)
  1. IPA (IPA)
  2. IPS (IPS)
  3. Bahasa Indonesia (BIN)
  4. Bahasa Inggris (BIG)
------------------------------

  Pilih mapel (0-4): 0
  Mata pelajaran 'Matematika' terpilih.
```

#### 2. Pilih Tingkat Kesulitan

```
    TINGKAT KESULITAN:
  1.   Mudah (3 soal)
  2.   Sedang (2 soal)
  3.   Sulit (2 soal)

  Pilih tingkat (1-3): 1
  Tingkat kesulitan 'mudah' dipilih. (3 soal)
```

#### 3. Mengerjakan Soal

```
╔════════════════════════════════════════════════╗
║     SOAL 1 dari 3                              ║
╠════════════════════════════════════════════════╣
║  Berapakah hasil dari 5 + 3?                   ║
╠════════════════════════════════════════════════╣
║    0. (A) 6                                    ║
║    1. (B) 7                                    ║
║    2. (C) 8                                    ║
║    3. (D) 9                                    ║
╚════════════════════════════════════════════════╝

  Jawaban Anda (atau 'q' untuk keluar): 2
```

#### 4. Hasil Kuis

```
🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉

         KUIS SELESAI!

===================================
             HASIL KUIS
===================================
  ✓ Benar       : 3
  ✗ Salah       : 0
     Total Soal : 3
-----------------------------------
    Nilai Akhir: 100.00%
===================================
    LUAR BIASA! Sempurna!

  Riwayat berhasil disimpan.
```

---
