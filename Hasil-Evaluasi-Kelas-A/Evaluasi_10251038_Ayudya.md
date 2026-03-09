# Laporan Evaluasi Terperinci - Praktikum Struktur Data

---

## Data Mahasiswa
- **Nama:** Ayudya Aisyah Mutiaradinna
- **NIM:** 10251038
- **Kelas:** Struktur Data A
- **GitHub Username:** `strukturdata-a-10251038`

---

## Hasil Evaluasi Modul 1: Pengantar Struktur Data

### 1. Tugas 1: Pengembangan ADT Counter
- **Pengecekan Kode:**
  - Metode `subtract(n)` didesain elegan menggunakan `max(0, self._value - n)`, sebuah *Pythonic way* yang cerdas untuk menghentikan angka negatif tanpa *conditional if* ekstensif.
- **Hasil Testing Codelab:** **PASSED** ✅ (100%)

### 2. Tugas 2: Pengembangan ADT Stack - Aplikasi Reverse String
- **Pengecekan Kode:**
  - Fungsi iterasi string-ke-stack dan stack-ke-string *reverse_string* dirangkai tanpa cela dan memberikan waktu eksekusi yang optimal (kondisi `is_empty` pada saat `pop`).
- **Hasil Testing Codelab:** **PASSED** ✅ (100%)

### 3. Tugas 3: Analisis Kompleksitas Lanjutan
- **Tabel Analisis Kompleksitas & Jawaban:**
  - Penjelasan O(log n) untuk fungsi *recursive halving* sangat jelas. Pemilahan ranking kompleksitas Big-O juga tidak ada yang salah dan relevan.
- **Hasil Testing Codelab:** **PASSED** ✅ (100%)

**NILAI MODUL 1: 100**

---

## Hasil Evaluasi Modul 2: Array

### 1. Tugas 1: Pengembangan MyArray
- **Pengecekan Kode:**
  - Mengimplementasikan pengecekan array minimum dan maksimum melalui *looping* O(n). *List swap* pada `reverse` in-place tertulis dinamis tanpa bergantung pada list ekstra.
- **Hasil Testing Codelab:** **PASSED** ✅ (100%)

### 2. Tugas 2: Aplikasi Array - Statistik Data
- **Pengecekan Kode:**
  - Pencarian `find_second_largest` dan `remove_duplicates` dijamin mematuhi parameter O(n) & O(n²). Penggunaan struktur kondisi *if-elif* pada second largest dimatangkan via `float('-inf')` untuk menghindari error nilai nol.
- **Hasil Testing Codelab:** **PASSED** ✅ (100%)

### 3. Tugas 3: Aplikasi Matrix - Operasi Dasar
- **Pengecekan Kode:**
  - Kesetaraan dimensi (`rows != len(matrix2) or cols != len(matrix2[0])`) menjaga validitas penjumlahan array dinamis. Operasi iteratif ganda untuk *transpose* dan *symmetric arrays* dilogikakan tajam .
- **Hasil Testing Codelab:** **PASSED** ✅ (100%)

**NILAI MODUL 2: 100**

---
### **NILAI RATA-RATA SEMENTARA: 100.00 🌟**

*Penilaian ini adalah nilai sementara untuk Modul 1 dan Modul 2, dievaluasi secara statis berdasarkan instruksi/flowchart dan divalidasi melalui unit test execution.*
