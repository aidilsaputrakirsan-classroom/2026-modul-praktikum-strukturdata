# Laporan Evaluasi Terperinci - Praktikum Struktur Data

---

## Data Mahasiswa
- **Nama:** Arya Cahya Nugraha
- **NIM:** 10251023
- **Kelas:** Struktur Data A
- **GitHub Username:** `strukturdata-a-AryaCahyaNugraha22`

---

## Hasil Evaluasi Modul 1: Pengantar Struktur Data

### 1. Tugas 1: Pengembangan ADT Counter
- **Pengecekan Kode:**
  - Metode operasional `add()`, `subtract()`, dan `multiply()` berfungsi secara matematis dengan baik. Kondisi penjagaan _underflow_ `<0` berhasil di-construct memakai kontrol boolean rasional.
- **Hasil Testing Codelab:** **PASSED** ✅ (100%)

### 2. Tugas 2: Pengembangan ADT Stack - Aplikasi Reverse String
- **Pengecekan Kode:**
  - `Stack` terimplementasi natural menggunakan List. String reversal logic dengan `while not stack.is_empty(): result += stack.pop()` sesuai *flowchart*.
- **Hasil Testing Codelab:** **PASSED** ✅ (100%)

### 3. Tugas 3: Analisis Kompleksitas Lanjutan
- **Tabel Analisis Kompleksitas & Jawaban:**
  - Klasifikasi struktur _Big-O Notation_ (konstan, linier, kuadratik, logaritmik, kubik) sangat lugas. Definisi `O(n^3)` (delapan juta operasi) dan `O(log n)` (pembagian menjadi setengah) akurat. Argumentasi jawaban logis untuk kasus sistem nyata media sosial.
- **Hasil Testing Codelab:** **PASSED** ✅ (100%)

**NILAI MODUL 1: 100**

---

## Hasil Evaluasi Modul 2: Array

### 1. Tugas 1: Pengembangan MyArray
- **Pengecekan Kode:**
  - `insert_front` / `delete_front` di-approach menggunakan operasi list `insert(0)` dan `pop(0)`. In-place swap *reverse* array dibuat manual `while left < right` pertukaran variable tanpa function `reverse()` bawaan. Sangat bagus!
- **Hasil Testing Codelab:** **PASSED** ✅ (100%)

### 2. Tugas 2: Aplikasi Array - Statistik Data
- **Pengecekan Kode:**
  - Logika pengecekan _second largest_ elegan `-inf`. Algoritma untuk menghapus duplikasi loop di *remove_duplicates* dilakukan O(n^2) komparasi manual secara *pure* (bukan *built-in module module/set*). 
- **Hasil Testing Codelab:** **PASSED** ✅ (100%)

### 3. Tugas 3: Aplikasi Matrix - Operasi Dasar
- **Pengecekan Kode:**
  - Analisa dimensi saat `add_matrices` diaplikasikan dengan kokoh, menghindari kegagalan Index bila matrix *non-identik*. Fungsi simetri direpresentasi membandingkan *matrix* primer secara _boolean equal_ ke transponenya.
- **Hasil Testing Codelab:** **PASSED** ✅ (100%)

**NILAI MODUL 2: 100**

---
### **NILAI RATA-RATA SEMENTARA: 100.00 🌟**

*Penilaian ini adalah nilai sementara untuk Modul 1 dan Modul 2, dievaluasi secara statis berdasarkan instruksi/flowchart dan divalidasi melalui unit test execution.*
