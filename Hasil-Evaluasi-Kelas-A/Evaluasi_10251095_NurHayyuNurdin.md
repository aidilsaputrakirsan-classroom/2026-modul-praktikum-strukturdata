# Laporan Evaluasi Terperinci - Praktikum Struktur Data

---

## Data Mahasiswa
- **Nama:** Nur Hayyu Nurdin
- **NIM:** 10251095
- **Kelas:** Struktur Data A
- **GitHub Username:** `strukturdata-a-NurHayyu-10251095`

---

## Hasil Evaluasi Modul 1: Pengantar Struktur Data

### 1. Tugas 1: Pengembangan ADT Counter
- **Pengecekan Kode:**
  - Fungsi penambahan `add` dan pengali `multiply` dieksekusi bersih. Restriksi *counter* pada batasan nol telah disuntikkan secara solid dalam fungsi pengurangan `subtract()`.
- **Hasil Testing Codelab:** **PASSED** ✅ (100%)

### 2. Tugas 2: Pengembangan ADT Stack - Aplikasi Reverse String
- **Pengecekan Kode:**
  - Teknik penyusunan `stack` cukup fundamental namun efektif dalam menargetkan memori LIFO (Last-In-First-Out) saat string dijejalkan (*push*) lantas dipanggil (*pop*) tanpa bocor ke indeks di bawahnya.
- **Hasil Testing Codelab:** **PASSED** ✅ (100%)

### 3. Tugas 3: Analisis Kompleksitas Lanjutan
- **Tabel Analisis Kompleksitas & Jawaban:**
  - Argumentasi logis dan bernarasi apik. Pembahasan tentang filter spam di email dengan jumlah lebih dari 1 juta entitas melawan 1 juta filter *blacklist* sebagai analogi $O(n^2)$ yang gagal (*crash real-time*) sangat inovatif dan akurat.
- **Hasil Testing Codelab:** **PASSED** ✅ (100%)

**NILAI MODUL 1: 100**

---

## Hasil Evaluasi Modul 2: Array

### 1. Tugas 1: Pengembangan MyArray
- **Pengecekan Kode:**
  - Penyematan kendali pergerakan node ke dalam awal array `insert_front` telah dijaga restriksinya dari kemungkinan error melalui indeks minus `if 0 <= len`. Namun pembalikan array `reverse` dikesekusi apik dengan menukar batas `left` dan `right`.
- **Hasil Testing Codelab:** **PASSED** ✅ (100%)

### 2. Tugas 2: Aplikasi Array - Statistik Data
- **Pengecekan Kode:**
  - Rata-rata elemen telah dihitung memakai `while loop` yang manual dan konsisten `while i < length`. Pada penemuan nilai kedua tertinggi `find_second_largest` kode mengimplementasikan komparasi single pass yang gesit.
- **Hasil Testing Codelab:** **PASSED** ✅ (100%)

### 3. Tugas 3: Aplikasi Matrix - Operasi Dasar
- **Pengecekan Kode:**
  - Kalkulasi linear dengan pertukaran matriks `transpose` berkerja mulus menggunakan baris/kolom. Loop perulangan matriks `for i in range` dirakit terstruktur dengan aman dari error bentrok tipe list dan integer.
- **Hasil Testing Codelab:** **PASSED** ✅ (100%)

**NILAI MODUL 2: 100**

---
### **NILAI RATA-RATA SEMENTARA: 100.00 🌟**

*Penilaian ini adalah nilai sementara untuk Modul 1 dan Modul 2, dievaluasi secara statis berdasarkan instruksi/flowchart dan divalidasi melalui unit test execution.*
