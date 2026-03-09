# Laporan Evaluasi Terperinci - Praktikum Struktur Data

---

## Data Mahasiswa
- **Nama:** Ananda Eurico Rhiva Rifqia Salim
- **NIM:** 10251062
- **Kelas:** Struktur Data A
- **GitHub Username:** `strukturdata-a-AnandaEurico`

---

## Hasil Evaluasi Modul 1: Pengantar Struktur Data

### 1. Tugas 1: Pengembangan ADT Counter
- **Pengecekan Kode:**
  - Metode `subtract()` bekerja sangat baik menggunakan struktur kendali kondisional ganda `if n > 0 and self._value >= n:` dan varian penempatan ke 0 agar *value* tidak kurang dari 0.
- **Hasil Testing Codelab:** **PASSED** ✅ (100%)

### 2. Tugas 2: Pengembangan ADT Stack - Aplikasi Reverse String
- **Pengecekan Kode:**
  - Logika pembalikan String *while not stack.is_empty(): reversed_str += stack.pop()* dieksekusi elegan sesuai implementasi kerangka teori LIFO.
- **Hasil Testing Codelab:** **PASSED** ✅ (100%)

### 3. Tugas 3: Analisis Kompleksitas Lanjutan
- **Tabel Analisis Kompleksitas & Jawaban:**
  - Analisis dijawab dengan tepat, rapi, dan padat. Menyertakan contoh kasus sorting dengan bubble sort (O(n²)) sebagai implementasi *real world* kompleksitas yang tak diinginkan pada skala data besar.
- **Hasil Testing Codelab:** **PASSED** ✅ (100%)

**NILAI MODUL 1: 100**

---

## Hasil Evaluasi Modul 2: Array

### 1. Tugas 1: Pengembangan MyArray
- **Pengecekan Kode:**
  - Fitur `reverse` mengadopsi standar komputasi dengan `left, right = 0, len(self._elements) - 1` hingga ke titik temu antar iterator, metode eksekusi algoritma *in-place* optimal.
- **Hasil Testing Codelab:** **PASSED** ✅ (100%)

### 2. Tugas 2: Aplikasi Array - Statistik Data
- **Pengecekan Kode:**
  - Implementasi *second_largest* tidak menggunakan metode filter manual *range default*, pencarian iteratif ganda di set dengan variabel nilai awal ke `float('-inf')` yang efektif untuk merujuk perbandingan angka minimum dasar.
- **Hasil Testing Codelab:** **PASSED** ✅ (100%)

### 3. Tugas 3: Aplikasi Matrix - Operasi Dasar
- **Pengecekan Kode:**
  - Operasi manipulasi matriks bebas kendala secara dimensional. Struktur validasi yang disiapkan telah diimplementasikan dengan `ValueError` guna menghindari kerusakan kalkulasi.
- **Hasil Testing Codelab:** **PASSED** ✅ (100%)

**NILAI MODUL 2: 100**

---
### **NILAI RATA-RATA SEMENTARA: 100.00 🌟**

*Penilaian ini adalah nilai sementara untuk Modul 1 dan Modul 2, dievaluasi secara statis berdasarkan instruksi/flowchart dan divalidasi melalui unit test execution.*
