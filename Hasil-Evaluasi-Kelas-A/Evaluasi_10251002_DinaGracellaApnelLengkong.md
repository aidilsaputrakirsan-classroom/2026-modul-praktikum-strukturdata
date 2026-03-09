# Laporan Evaluasi Manual - Praktikum Struktur Data

---

## Data Mahasiswa
- **Nama:** Dina Gracella Apnel Lengkong
- **NIM:** 10251002
- **Kelas:** Struktur Data A
- **GitHub Username:** `strukturdata-a-10251002`

---

## Hasil Evaluasi Modul 1: Pengantar Struktur Data

### 1. Tugas 1: Pengembangan ADT Counter
- **Pengecekan Kode:**
  - `add(n)`: Diimplementasikan dengan benar. Terdapat pengecekan kondisi agar nilai `n` harus positif.
  - `subtract(n)`: Diimplementasikan dengan benar. Terdapat penanganan *error* jika `n` bernilai kurang dari nol, dan logika memastikan selisih tidak di bawah `0`.
  - `multiply(n)`: Diimplementasikan dengan benar. Terdapat *error handling* jika `n` negatif.
  - `__str__()`: Diimplementasikan dengan penulisan format string yang tepat.
- **Hasil Testing Codelab:** **PASSED** ✅ (100%)
- **Catatan:** Kode ditulis sangat bersih dan memperhatikan penanganan batasan *error* (*edge cases*).

### 2. Tugas 2: Pengembangan ADT Stack - Aplikasi Reverse String
- **Pengecekan Kode:**
  - `print_stack()`: Berhasil menampilkan daftar list/item stack dengan benar.
  - `clear()`: Method `clear()` di list berhasil meniadakan elemen stack.
  - Aplikasi `reverse_string(s)`: Logika memanfaatkan Stack LIFO berhasil membalikkan string sesuai diagram flowchart.
- **Hasil Testing Codelab:** **PASSED** ✅ (100%)

### 3. Tugas 3: Analisis Kompleksitas Lanjutan
- **Tabel Analisis Kompleksitas & Jawaban:**
  - Pengisian kompleksitas fungsi A sampai F seluruhnya **BENAR**. Alasan yang diberikan akurat. Jawaban atas pertanyaan 1-5 menunjukkan pemahaman yang sangat mendalam terkait konsep *Big-O Notation*, pengenalan eksponensial/logaritmik, dan implementasi kasus nyata.
- **Catatan:** Pemahaman konseptual sangat *solid*.

**NILAI MODUL 1: 100**

---

## Hasil Evaluasi Modul 2: Array

### 1. Tugas 1: Pengembangan MyArray
- **Pengecekan Kode:**
  - Fungsi `insert_front()`, `delete_front()`, `find_min()`, `find_max()`, `count()`, dan `reverse()` diimplementasikan dengan logika iterasi list Array yang kuat dan rapi sesuai flowchart.
- **Hasil Testing Codelab:** **PASSED** ✅ (100%)

### 2. Tugas 2: Aplikasi Array - Statistik Data
- **Pengecekan Kode:**
  - Mampu menggunakan Array buatan (`MyArray`) untuk melakukan penghitungan agregat (`sum`, `average`, `range`, pola duplikat `remove_duplicates`, dll.) dengan presisi tipe data `float`/`int` yang tepat.
- **Hasil Testing Codelab:** **PASSED** ✅ (100%)

### 3. Tugas 3: Aplikasi Matrix - Operasi Dasar
- **Pengecekan Kode:**
  - Pemahaman Array Multidimensi (Matrix) sudah sangat baik. Logika penjumlahan matriks (`add_matrices`), matriks perputaran transpose (`transpose_matrix`), matriks perkalian skalar, pembuktian simetris (`is_symmetric`), dan pengambilan diagonal matriks ter-implementasi sempurna.
- **Hasil Testing Codelab:** **PASSED** ✅ (100%)

**NILAI MODUL 2: 100**

---
### **NILAI RATA-RATA SEMENTARA: 100 (SANGAT BAIK) 🌟**

*Penilaian ini adalah nilai sementara untuk Modul 1 dan Modul 2, dievaluasi secara statis berdasarkan instruksi/flowchart dan divalidasi melalui unit test execution.*
