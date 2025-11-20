# 📘 Bundahara Digital – Aplikasi Catatan Keuangan Sederhana (Python)

Aplikasi **Bundahara Digital** adalah program sederhana berbasis Python yang digunakan untuk menyimpan dan menampilkan daftar catatan keuangan. Aplikasi ini berjalan pada terminal/command prompt dan cocok untuk pemula yang ingin belajar dasar-dasar Python seperti:

* Variabel global
* Fungsi
* List
* Perulangan
* Input user
* Percabangan

---

## 🚀 Fitur Aplikasi

### 1. **Melihat Daftar Catatan**

Menampilkan seluruh catatan keuangan yang tersimpan dalam list `dataCatatan`.

### 2. **Menambah Catatan Baru**

Pengguna dapat memasukkan catatan baru, dan catatan tersebut akan disimpan ke dalam list.

### 3. **Membatasi Penggunaan (Loop)**

Aplikasi berjalan maksimum **10 kali interaksi** menggunakan perulangan `for`.

### 4. **Keluar dari Aplikasi**

Pengguna dapat mengetik **exit** untuk menghentikan aplikasi kapan saja.

---

## 🗂️ Struktur Kode

### 🔹 Variabel Global

```python
dataCatatan = ["Uang Jajan", "Biaya Sekolah", "Tabungan"]
```

Menyimpan daftar catatan awal.

### 🔹 Fungsi `daftarCatatan()`

Mengembalikan seluruh isi catatan.

### 🔹 Fungsi `tambahCatatan(catatanBaru)`

Menambahkan catatan baru ke dalam list global.

### 🔹 Loop Utama Program

Menampilkan menu dan menjalankan aksi sesuai pilihan pengguna.

---

## ▶️ Cara Menjalankan Program

1. Pastikan Python sudah terinstall.
2. Simpan kode ke file bernama `bundahara.py`.
3. Jalankan melalui terminal:

   ```bash
   python bundahara.py
   ```

---

## 📌 Contoh Penggunaan

```
Hello Selamat Datang Di Aplikasi Bundahara Digital
---------------------------------------------------
Silahkan Pilih Menu Dibawah Ini:
1. Lihat Daftar Catatan
2. Tambah Catatan Baru
Masukkan pilihan Anda (1/2):
```

---

## 🧠 Catatan Tambahan

* Program menggunakan list Python untuk menyimpan data selama aplikasi berjalan.
* Ketika program selesai ditutup, data tidak disimpan permanen.
* Cocok untuk latihan memahami konsep dasar Python.

---

Jika kamu ingin, aku bisa bantu buat versi aplikasinya yang **menyimpan data ke file**, atau yang **menggunakan database** biar lebih nyata!
