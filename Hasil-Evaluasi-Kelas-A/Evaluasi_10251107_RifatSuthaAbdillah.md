# Laporan Evaluasi Terperinci - Praktikum Struktur Data

---

## Data Mahasiswa
- **Nama:** Rifat Sutha Abdillah
- **NIM:** 10251107
- **Kelas:** Struktur Data A
- **GitHub Username:** `strukturdata-a-RifatSuthaAbdillah`

---

## Hasil Evaluasi Modul 1: Pengantar Struktur Data

### 1. Tugas 1: Pengembangan ADT Counter
- **Pengecekan Kode:**
  - Operasi instansiasi `add` dan pengali `multiply` berfungsi wajar. Fungsi limit minimal 0 pada operasi kurang disikapi sangat berhati-hati melalui pengecekan `if self._value > 0`.
- **Hasil Testing Codelab:** **PASSED** ✅ (100%)

### 2. Tugas 2: Pengembangan ADT Stack - Aplikasi Reverse String
- **Pengecekan Kode:**
  - Metode pencetakan stack memanfaatkan mekanisme instan Python List dan balikan string diraih konsisten melalui struktur `while` loop yang merakit huruf baru berdasarkan metode pop satu persatu.
- **Hasil Testing Codelab:** **PASSED** ✅ (100%)

### 3. Tugas 3: Analisis Kompleksitas Lanjutan
- **Tabel Analisis Kompleksitas & Jawaban:**
  - Kalimat dan analoginya terjelaskan gamblang, bahkan menambahkan notasi logaritmik seperti "\$O(\log n)$". Eksperimen logika pergerakan untuk basis data pengguna KTP sebagai *bottleneck* skenario `O(n²)` dirumuskan realistis.
- **Hasil Testing Codelab:** **PASSED** ✅ (100%)

**NILAI MODUL 1: 100**

---

## Hasil Evaluasi Modul 2: Array

### 1. Tugas 1: Pengembangan MyArray
- **Pengecekan Kode:**
  - Fitur mutasi data *reverse* memamerkan implementasi perulangan bagi setengah array (`for i in range(n // 2):`) yang ditukar-silang untuk mengamankan redundansi pembacaan ulang, ini efisiensi algoritma kelas wahid. Pengecekan max dan min tersaring errornya dengan apik melalui iterasi natural `for val in self._elements`. 
- **Hasil Testing Codelab:** **PASSED** ✅ (100%)

### 2. Tugas 2: Aplikasi Array - Statistik Data
- **Pengecekan Kode:**
  - Performa *search* terbesar ke dua diamankan menggunakan penempatan nilai minus terekstrim (`float('-inf')`), dan penyortiran ganda diracik tepat guna mencegah error index yang bergeser. Pengecekan nilai *duplikat* terdistribusi rapi untuk verifikasi double loop.
- **Hasil Testing Codelab:** **PASSED** ✅ (100%)

### 3. Tugas 3: Aplikasi Matrix - Operasi Dasar
- **Pengecekan Kode:**
  - Semua operasi (termasuk perkalian skalar, rotasi matrix `transpose_matrix`, diagonal, dan uji simetris `is_symmetric`) dibina apik dengan alokasi iterasi baris yang berstruktur solid.
- **Hasil Testing Codelab:** **PASSED** ✅ (100%)

**NILAI MODUL 2: 100**

---
### **NILAI RATA-RATA SEMENTARA: 100.00 🌟**

*Penilaian ini adalah nilai sementara untuk Modul 1 dan Modul 2, dievaluasi secara statis berdasarkan instruksi/flowchart dan divalidasi melalui unit test execution.*
