# Laporan Evaluasi Terperinci - Praktikum Struktur Data

---

## Data Mahasiswa
- **Nama:** Putri Nabila Safitri
- **NIM:** 10251035
- **Kelas:** Struktur Data A
- **GitHub Username:** `strukturdata-a-10251035-Putri`

---

## Hasil Evaluasi Modul 1: Pengantar Struktur Data

### 1. Tugas 1: Pengembangan ADT Counter
- **Pengecekan Kode:**
  - Metode `subtract()` dikontrol tepat untuk mencegah nilai negatif bersisa (`if self._value < 0: self._value = 0`). Seluruh implementasi kalkulatif beroperasi dengan sempurna.
- **Hasil Testing Codelab:** **PASSED** ✅ (100%)

### 2. Tugas 2: Pengembangan ADT Stack - Aplikasi Reverse String
- **Pengecekan Kode:**
  - Stack methods komplit. Pembalikan string (`reverse_string`) dilakukan via stack push per karakter yang ringkas, dengan *pop* di dalam *while loop* untuk penyesuaian string balasan.
- **Hasil Testing Codelab:** **PASSED** ✅ (100%)

### 3. Tugas 3: Analisis Kompleksitas Lanjutan
- **Tabel Analisis Kompleksitas & Jawaban:**
  - Pemahaman Notasi Big-O (termasuk kompleksitas kubik & logaritmik) dijawab dengan akurasi tinggi. Studi kasus yang digunakan logis, seperti sosial media skala jutaan *user* untuk O(n^2).
- **Hasil Testing Codelab:** **PASSED** ✅ (100%)

**NILAI MODUL 1: 100**

---

## Hasil Evaluasi Modul 2: Array

### 1. Tugas 1: Pengembangan MyArray
- **Pengecekan Kode:**
  - Modul pengecekan nilai min & max beroperasi efektif. Pergerakan loop array balikan `reverse(self)` diatur ringkas via variabel in-place swap tuple `self._elements[left], self._elements[right] = self._elements[right], self._elements[left]`.
- **Hasil Testing Codelab:** **PASSED** ✅ (100%)

### 2. Tugas 2: Aplikasi Array - Statistik Data
- **Pengecekan Kode:**
  - `remove_duplicates` ditangani via *search* untuk pengecekan elemen non-redundant. Metode *second largest* (mencari terbesar kedua) diformulasikan efisien menggunakan `float('-inf')` untuk pembanding awal.
- **Hasil Testing Codelab:** **PASSED** ✅ (100%)

### 3. Tugas 3: Aplikasi Matrix - Operasi Dasar
- **Pengecekan Kode:**
  - Pertahanan error handling diaplikasikan penuh (seperti memfilter *rows != len(matrix2)*). Implementasi diagonal dengan `range(min(rows, cols))` dinilai sebagai *best practice* keamanan memory.
- **Hasil Testing Codelab:** **PASSED** ✅ (100%)

**NILAI MODUL 2: 100**

---
### **NILAI RATA-RATA SEMENTARA: 100.00 🌟**

*Penilaian ini adalah nilai sementara untuk Modul 1 dan Modul 2, dievaluasi secara statis berdasarkan instruksi/flowchart dan divalidasi melalui unit test execution.*
