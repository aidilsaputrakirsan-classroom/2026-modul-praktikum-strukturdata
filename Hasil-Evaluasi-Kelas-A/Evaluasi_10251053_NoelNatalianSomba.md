# Laporan Evaluasi Terperinci - Praktikum Struktur Data

---

## Data Mahasiswa
- **Nama:** Noel Natalian Somba
- **NIM:** 10251053
- **Kelas:** Struktur Data A
- **GitHub Username:** `strukturdata-a-N3CH0`

---

## Hasil Evaluasi Modul 1: Pengantar Struktur Data

### 1. Tugas 1: Pengembangan ADT Counter
- **Pengecekan Kode:**
  - Metode penambahan dan perkalian tersusun secara fungsional. Pada metode *subtract()*, pembatasan ke tingkat operasional nihil telah divalidasi dengan lancar `if self._value < 0: self._value = 0` guna proteksi kalkulasi.
- **Hasil Testing Codelab:** **PASSED** ✅ (100%)

### 2. Tugas 2: Pengembangan ADT Stack - Aplikasi Reverse String
- **Pengecekan Kode:**
  - Fungsi balik string dirancang memakai pengulangan standard Python melalui iterasi dan mekanisme `pop`, mematuhi pakem tata cara Stack secara efisien.
- **Hasil Testing Codelab:** **PASSED** ✅ (100%)

### 3. Tugas 3: Analisis Kompleksitas Lanjutan
- **Tabel Analisis Kompleksitas & Jawaban:**
  - Mahasiswa memahami betul teori analisis komparatif performa algoritma (Big-O). Pembuktian matematis serta penjelasan di contoh iterasi sangat lugas. Penjabaran untuk *bubble sort* dengan algoritma $O(n^2)$ pada 1 juta data logis karena membutuhkan operasi sangat masif senilai $10^{12}$.
- **Hasil Testing Codelab:** **PASSED** ✅ (100%)

**NILAI MODUL 1: 100**

---

## Hasil Evaluasi Modul 2: Array

### 1. Tugas 1: Pengembangan MyArray
- **Pengecekan Kode:**
  - Semua metode esensial (`insert_front`, `delete_front`, `find_min`, `find_max`, `reverse`, dan `count`) berfungsi sempurna tanpa cacat kompilasi atau kesalahan runtime. Teknik `reverse` *in-place swap* diimplementasikan dengan presisi yang mantul.
- **Hasil Testing Codelab:** **PASSED** ✅ (100%)

### 2. Tugas 2: Aplikasi Array - Statistik Data
- **Pengecekan Kode:**
  - Pencarian elemen unik dan penyisihan terduplikat dimodelkan menggunakan class *MyArray* dari tugas sebelumnya. Fungsi `find_second_largest` dan rentang dieksekusi efisien karena mahasiswa meletakkan conditional pointer logic tanpa fungsi library sort Python sama sekali.
- **Hasil Testing Codelab:** **PASSED** ✅ (100%)

### 3. Tugas 3: Aplikasi Matrix - Operasi Dasar
- **Pengecekan Kode:**
  - *Nested loops* matriks untuk kalkulasi aljabar linier ditangani solid dengan pemantauan panjang index baris/kolom `len(matrix[0])`. Perulangan pada rotasi transpose matrix dibuat efisien. 
- **Hasil Testing Codelab:** **PASSED** ✅ (100%)

**NILAI MODUL 2: 100**

---
### **NILAI RATA-RATA SEMENTARA: 100.00 🌟**

*Penilaian ini adalah nilai sementara untuk Modul 1 dan Modul 2, dievaluasi secara statis berdasarkan instruksi/flowchart dan divalidasi melalui unit test execution.*
