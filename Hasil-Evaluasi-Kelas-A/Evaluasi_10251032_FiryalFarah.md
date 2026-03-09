# Laporan Evaluasi Terperinci - Praktikum Struktur Data

---

## Data Mahasiswa
- **Nama:** Firyal Farah Khulaidah
- **NIM:** 10251032
- **Kelas:** Struktur Data A
- **GitHub Username:** `strukturdata-a-FiryalFarah`

---

## Hasil Evaluasi Modul 1: Pengantar Struktur Data

### 1. Tugas 1: Pengembangan ADT Counter
- **Pengecekan Kode:**
  - Metode operasional kalkulasi statis Counter (`add()`, `subtract()`, `multiply()`) terimplementasi mulus dengan validasi `< 0` yang aman dan sesuai flowchart.
- **Hasil Testing Codelab:** **PASSED** ✅ (100%)

### 2. Tugas 2: Pengembangan ADT Stack - Aplikasi Reverse String
- **Pengecekan Kode:**
  - Stack pop terlindungi validasi _is_empty()_. Pemisahan method _print_stack_ di-coding tepat sasaran dan operasi *reverse string* via inersi stack (`pop()` dan _concatenation_) sangat bersih.
- **Hasil Testing Codelab:** **PASSED** ✅ (100%)

### 3. Tugas 3: Analisis Kompleksitas Lanjutan
- **Tabel Analisis Kompleksitas & Jawaban:**
  - Pemaparan notasi Big-O (konstan, linear, logaritmik, kuadratik, kubik) pada tabel cukup singkat namun jelas intisarinya. Simulasi waktu eksekusi dipahami dengan baik (ex: kasus sorting ecommerce untuk Big-O $O(n^2)$).
- **Hasil Testing Codelab:** **PASSED** ✅ (100%)

**NILAI MODUL 1: 100**

---

## Hasil Evaluasi Modul 2: Array

### 1. Tugas 1: Pengembangan MyArray
- **Pengecekan Kode:**
  - Error Handling tertangani ideal dengan menaikkan argumen `ValueError` atau `IndexError` pada posisi list kosong. Pemutaran array *reverse()* in-place `self._elements[left], self._elements[right] = self._elements[right], self._elements[left]` ditangani secara ringkas.
- **Hasil Testing Codelab:** **PASSED** ✅ (100%)

### 2. Tugas 2: Aplikasi Array - Statistik Data
- **Pengecekan Kode:**
  - Penghapusan duplikat *remove_duplicates* mendelegasikan iterasi perbandingan O(n^2) melalui panggilan linear dari instance method pencarian (`result.search() == -1`), ini *best practice* yang dianjurkan.
- **Hasil Testing Codelab:** **PASSED** ✅ (100%)

### 3. Tugas 3: Aplikasi Matrix - Operasi Dasar
- **Pengecekan Kode:**
  - Fungsi iteratif matriks mengelola komputasi *matrix operations* secara natural. Algoritma perbandingan transposisi (*is_symmetric*) dikembangkan elegan membedakan dimensi `matrix[i][j] != matrix[j][i]` untuk menghindari nested memori yang boros.
- **Hasil Testing Codelab:** **PASSED** ✅ (100%)

**NILAI MODUL 2: 100**

---
### **NILAI RATA-RATA SEMENTARA: 100.00 🌟**

*Penilaian ini adalah nilai sementara untuk Modul 1 dan Modul 2, dievaluasi secara statis berdasarkan instruksi/flowchart dan divalidasi melalui unit test execution.*
