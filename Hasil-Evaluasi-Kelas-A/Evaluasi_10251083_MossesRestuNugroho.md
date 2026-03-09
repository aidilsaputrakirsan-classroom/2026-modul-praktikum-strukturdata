# Laporan Evaluasi Terperinci - Praktikum Struktur Data

---

## Data Mahasiswa
- **Nama:** Mosses Restu Nugroho
- **NIM:** 10251083
- **Kelas:** Struktur Data A
- **GitHub Username:** `strukturdata-a-MossesRestuN`

---

## Hasil Evaluasi Modul 1: Pengantar Struktur Data

### 1. Tugas 1: Pengembangan ADT Counter
- **Pengecekan Kode:**
  - Metode `subtract()` dikerjakan dengan solid di mana batas nilai bawah 0 diamankan menggunakan validasi tambahan `if self._value < 0: self._value = 0` sehingga kondisi anomali tertangani dengan rapi. Konsep pemrograman berorientasi objek yang kuat.
- **Hasil Testing Codelab:** **PASSED** ✅ (100%)

### 2. Tugas 2: Pengembangan ADT Stack - Aplikasi Reverse String
- **Pengecekan Kode:**
  - Fungsi pembalikan *reverse_string* memanfaatkan mekanisme penambahan iteratif pada string baru, mengambil keluaran *stack.pop()* sehingga pola *Last In First Out* (LIFO) tereksekusi murni.
- **Hasil Testing Codelab:** **PASSED** ✅ (100%)

### 3. Tugas 3: Analisis Kompleksitas Lanjutan
- **Tabel Analisis Kompleksitas & Jawaban:**
  - Penjelasan cukup lugas, mahasiswa bisa mendeskripsikan Big O notation ke dalam bahasa awam yang ringkas seperti "tiap rekursi membagi n jadi n/2". Contoh kegagalan algoritma `O(n²)` (sistem perbandingan data jutaan pengguna) tepat sasaran dan rasional.
- **Hasil Testing Codelab:** **PASSED** ✅ (100%)

**NILAI MODUL 1: 100**

---

## Hasil Evaluasi Modul 2: Array

### 1. Tugas 1: Pengembangan MyArray
- **Pengecekan Kode:**
  - Pendefinisian fitur pada class `MyArray` stabil. `find_min()` dan `find_max()` dilengkapi pemblokiran `self.is_empty()` sebagai gerbang batas error *ValueError*. Fungsi `reverse` cukup padat dijalankan melalui fungsi bawaan python (*self._elements.reverse()*).
- **Hasil Testing Codelab:** **PASSED** ✅ (100%)

### 2. Tugas 2: Aplikasi Array - Statistik Data
- **Pengecekan Kode:**
  - Penerapan `find_second_largest` dijalin apik melalui penyelesaian dalam sekali melintas (*one pass O(n)*), menggunakan inisialisasi infinity negatif `float('-inf')` yang mendemonstrasikan keluwesan penguasaan Python tingkat menengah.
- **Hasil Testing Codelab:** **PASSED** ✅ (100%)

### 3. Tugas 3: Aplikasi Matrix - Operasi Dasar
- **Pengecekan Kode:**
  - Mahasiswa mampu menulis komputasi matriks dua dimensi (`add_matrices` dan `transpose_matrix`) secara stabil menggunakan iterasi baris-kolom mendasar tanpa ketergantungan *libraries* eksternal tambahan.
- **Hasil Testing Codelab:** **PASSED** ✅ (100%)

**NILAI MODUL 2: 100**

---
### **NILAI RATA-RATA SEMENTARA: 100.00 🌟**

*Penilaian ini adalah nilai sementara untuk Modul 1 dan Modul 2, dievaluasi secara statis berdasarkan instruksi/flowchart dan divalidasi melalui unit test execution.*
