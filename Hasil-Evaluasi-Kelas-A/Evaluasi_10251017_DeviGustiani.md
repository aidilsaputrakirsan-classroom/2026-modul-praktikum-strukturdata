# Laporan Evaluasi Terperinci - Praktikum Struktur Data

---

## Data Mahasiswa
- **Nama:** Devi Gustiani
- **NIM:** 10251017
- **Kelas:** Struktur Data A
- **GitHub Username:** `strukturdata-a-devigustiani`

---

## Hasil Evaluasi Modul 1: Pengantar Struktur Data

### 1. Tugas 1: Pengembangan ADT Counter
- **Pengecekan Kode:**
  - Metode penambahan dan pengurangan bekerja sesuai requirement. `subtract()` memverifikasi batas minimum `< 0` dengan solid.
- **Hasil Testing Codelab:** **PASSED** ✅ (100%)

### 2. Tugas 2: Pengembangan ADT Stack - Aplikasi Reverse String
- **Pengecekan Kode:**
  - Penggunaan `stack.push()` dan iterasi pembalikan `while not stack.is_empty(): result += stack.pop()` sesuai algoritma.
- **Hasil Testing Codelab:** **PASSED** ✅ (100%)

### 3. Tugas 3: Analisis Kompleksitas Lanjutan
- **Tabel Analisis Kompleksitas & Jawaban:**
  - Tabel analisa time complexity tepat. Argumentasi yang dilampirkan logis, terkhusus soal n log n dan logaritmik tree halving. 
- **Hasil Testing Codelab:** **PASSED** ✅ (100%)

**NILAI MODUL 1: 100**

---

## Hasil Evaluasi Modul 2: Array

### 1. Tugas 1: Pengembangan MyArray
- **Pengecekan Kode:**
  - **Minor Bugs:** Terdapat kesalahan *indentation* `return` variabel di dalam scope perulangan `for` pada method `find_min`, `find_max`, dan `count`. Hal ini menyebabkan *test execution* berhenti dan membalikkan nilai saat perulangan loop pertama selesai.
  - **Typo Pointer:** Di dalam fungsi `reverse()`, pemanggilan indeks array memiliki kesalahan ketik pointer `self._elements[1]` (angka satu) alih-alih `self._elements[i]` yang menyebabkan *logic overwrite* indeks 1 terus-menerus.
- **Hasil Testing Codelab:** **FAILED** ❌ (Beberapa syntax error & indeks bug).

### 2. Tugas 2: Aplikasi Array - Statistik Data
- **Pengecekan Kode:**
  - Perbaikan pada method *find_min* / *find_max* dilakukan pada baris kode di tugas ini (identasi benar). Fungsionalitas data analitik linear dan pencarian `second_largest` berjalan baik.
- **Hasil Testing Codelab:** **PASSED** ✅ (100%)

### 3. Tugas 3: Aplikasi Matrix - Operasi Dasar
- **Pengecekan Kode:**
  - Implementasi komparasi matriks 2D, enumerasi ordo (baris x kolom), boolean simetri serta kalkulasi matriks berhasil dienkapsulasi dengan rapi di skrip ini.
- **Hasil Testing Codelab:** **PASSED** ✅ (100%)

**NILAI MODUL 2: 80**

---
### **NILAI RATA-RATA SEMENTARA: 90.00 🌟**

*Penilaian ini adalah nilai sementara untuk Modul 1 dan Modul 2, dievaluasi secara statis berdasarkan instruksi/flowchart dan divalidasi melalui unit test execution.*
