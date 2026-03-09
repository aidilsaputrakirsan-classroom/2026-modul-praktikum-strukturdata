# Laporan Evaluasi Terperinci - Praktikum Struktur Data

---

## Data Mahasiswa
- **Nama:** Nurul Syahira A
- **NIM:** 10251047
- **Kelas:** Struktur Data A
- **GitHub Username:** `strukturdata-a-syahira10251047`

---

## Hasil Evaluasi Modul 1: Pengantar Struktur Data

### 1. Tugas 1: Pengembangan ADT Counter
- **Pengecekan Kode:**
  - Metode `subtract()` bekerja lancar menggunakan kondisi terstruktur `if self._value >= n`. Method kalkulatif lainnya tertulis efisien. 
- **Hasil Testing Codelab:** **PASSED** ✅ (100%)

### 2. Tugas 2: Pengembangan ADT Stack - Aplikasi Reverse String
- **Pengecekan Kode:**
  - Struktur Stack menggunakan prinsip LIFO tanpa kompromi. Loop `for` dikombinasikan secara proporsional dengan `while` loop pada `reverse_string()`.
- **Hasil Testing Codelab:** **PASSED** ✅ (100%)

### 3. Tugas 3: Analisis Kompleksitas Lanjutan
- **Tabel Analisis Kompleksitas & Jawaban:**
  - Alasan di balik penentuan kompleksitas ditulis singkat dan tepat sasaran. Penjelasan O(log n) berpusat pada rekursi *halving*, membuktikan penguasaan algoritma pencarian lanjutan.
- **Hasil Testing Codelab:** **PASSED** ✅ (100%)

**NILAI MODUL 1: 100**

---

## Hasil Evaluasi Modul 2: Array

### 1. Tugas 1: Pengembangan MyArray
- **Pengecekan Kode:**
  - Method `find_min()` dan `find_max()` dilengkapi error exception standar jika array kosong. Operasi array dasar ditangani baik.
- **Hasil Testing Codelab:** **PASSED** ✅ (100%)

### 2. Tugas 2: Aplikasi Array - Statistik Data
- **Pengecekan Kode:**
  - *Logic* pada `calculate_sum` sangat padat dan ringkas: memanggil `self._elements[i]` menghindari *overhead* akses get(). `remove_duplicates` dioptimalkan dengan iterasi bertingkat.
- **Hasil Testing Codelab:** **PASSED** ✅ (100%)

### 3. Tugas 3: Aplikasi Matrix - Operasi Dasar
- **Pengecekan Kode:**
  - Validasi *is_symmetric* dipermudah menggunakan komparasi langsung: `t = transpose_matrix(matrix); return matrix == t`. Strategi pengkodean yang sangat "Pythonic" dan *clean*.
- **Hasil Testing Codelab:** **PASSED** ✅ (100%)

**NILAI MODUL 2: 100**

---
### **NILAI RATA-RATA SEMENTARA: 100.00 🌟**

*Penilaian ini adalah nilai sementara untuk Modul 1 dan Modul 2, dievaluasi secara statis berdasarkan instruksi/flowchart dan divalidasi melalui unit test execution.*
