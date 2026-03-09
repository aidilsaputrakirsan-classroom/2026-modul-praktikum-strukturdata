# Laporan Evaluasi Terperinci - Praktikum Struktur Data

---

## Data Mahasiswa
- **Nama:** Dhevrant Zhelynov Malelo
- **NIM:** 10251020
- **Kelas:** Struktur Data A
- **GitHub Username:** `strukturdata-a-Dhevrant`

---

## Hasil Evaluasi Modul 1: Pengantar Struktur Data

### 1. Tugas 1: Pengembangan ADT Counter
- **Pengecekan Kode:**
  - Metode penambahan `add()` dan perkalian `multiply()` berjalan mulus. Penggunaan block kondisional untuk memastikan nilai minimum `subtract()` berjalan dengan semestinya.
- **Hasil Testing Codelab:** **PASSED** ✅ (100%)

### 2. Tugas 2: Pengembangan ADT Stack - Aplikasi Reverse String
- **Pengecekan Kode:**
  - Fungsi Stack aman, dan iterasi `while not stack.is_empty()` diterapkan sesuai flowchart pembalikan string.
- **Hasil Testing Codelab:** **PASSED** ✅ (100%)

### 3. Tugas 3: Analisis Kompleksitas Lanjutan
- **Tabel Analisis Kompleksitas & Jawaban:**
  - **Minor Note:** Ada sedikit anomali/bias teoritis dalam penulisan notasi Big-O asimtotik. Notasi komputasi yang dituliskan adalah *O(2n)* (untuk O(n²)) dan *O(3n)* (untuk O(n³)), yang mana merepresentasikan konstanta alih-alih bentuk pemangkatan algoritma kuadratik/kubik. Namun pemahaman tentang algoritma secara bahasa (seperti lambatnya n³) dapat dimengerti dengan baik.
- **Hasil Testing Codelab:** **PASSED** ✅ (100%)

**NILAI MODUL 1: 90**

---

## Hasil Evaluasi Modul 2: Array

### 1. Tugas 1: Pengembangan MyArray
- **Pengecekan Kode:**
  - Proses modifikasi array in-place `reverse` menggunakan fitur native Python yang solid (`self._elements.reverse()`). Linear counting and minimum/maximum logic terkomposisi dengan sangat baik.
- **Hasil Testing Codelab:** **PASSED** ✅ (100%)

### 2. Tugas 2: Aplikasi Array - Statistik Data
- **Pengecekan Kode:**
  - Penggunaan `average` yang divalidasi manual untuk list elemen berjumlah 0 (zero division escape rule). Perhitungan nilai `second_largest` dan modifikasi array terhindar dari duplikat berjalan apik.
- **Hasil Testing Codelab:** **PASSED** ✅ (100%)

### 3. Tugas 3: Aplikasi Matrix - Operasi Dasar
- **Pengecekan Kode:**
  - Modul matriks diselesaikan dengan *logic testing* untuk perbandingan `matrix[i][j] != matrix[j][i]` saat validasi *is_symmetric*. Efisien tanpa harus load *transpose* yang berat.
- **Hasil Testing Codelab:** **PASSED** ✅ (100%)

**NILAI MODUL 2: 100**

---
### **NILAI RATA-RATA SEMENTARA: 95.00 🌟**

*Penilaian ini adalah nilai sementara untuk Modul 1 dan Modul 2, dievaluasi secara statis berdasarkan instruksi/flowchart dan divalidasi melalui unit test execution.*
