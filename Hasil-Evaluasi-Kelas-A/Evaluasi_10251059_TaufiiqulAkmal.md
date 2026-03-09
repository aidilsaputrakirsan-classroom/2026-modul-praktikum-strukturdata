# Laporan Evaluasi Terperinci - Praktikum Struktur Data

---

## Data Mahasiswa
- **Nama:** Taufiiqul Akmal
- **NIM:** 10251059
- **Kelas:** Struktur Data A
- **GitHub Username:** `strukturdata-a-10251059-coder`

---

## Hasil Evaluasi Modul 1: Pengantar Struktur Data

### 1. Tugas 1: Pengembangan ADT Counter
- **Pengecekan Kode:**
  - Metode penambahan kalkulatif berjalan baik. Fungsi `subtract()` menggunakan pendekatan perbaikan kondisional tambahan yang menjamin proteksi data jika counter turun di bawah nol (`if self._value < 0: self._value = 0`).
- **Hasil Testing Codelab:** **PASSED** ✅ (100%)

### 2. Tugas 2: Pengembangan ADT Stack - Aplikasi Reverse String
- **Pengecekan Kode:**
  - `Stack` didesain sangat *clean* dengan konsep LIFO murni. `reverse_string()` menyusun string dengan operasi dorong/tarik yang disajikan dengan jelas pada skrip algoritma terstruktur di dalam komentar atas fungsinya.
- **Hasil Testing Codelab:** **PASSED** ✅ (100%)

### 3. Tugas 3: Analisis Kompleksitas Lanjutan
- **Tabel Analisis Kompleksitas & Jawaban:**
  - Pertanyaan dijawab dengan argumentasi rasional yang tepat sasaran. Contoh soal nomor 5 divisualisasikan dengan probabilitas kasus (1000000 pengguna -> 1 triliun loop pengecekan), memberikan gambaran Big-O konkrit pada realita pemodelan algoritma lamban $O(n^2)$.
- **Hasil Testing Codelab:** **PASSED** ✅ (100%)

**NILAI MODUL 1: 100**

---

## Hasil Evaluasi Modul 2: Array

### 1. Tugas 1: Pengembangan MyArray
- **Pengecekan Kode:**
  - Penyelesaian metode modifikasi letak internal terpusat aman dengan exception handler. *Reverse* array memanfaatkan metode *two pointer* konvensional dengan *assignment* sejajar `[left], [right] = [right], [left]`.
- **Hasil Testing Codelab:** **PASSED** ✅ (100%)

### 2. Tugas 2: Aplikasi Array - Statistik Data
- **Pengecekan Kode:**
  - Modul array `from tugas1... import MyArray` dikemas sebagai *dependency* yang modular. Metode deduplikasi melacak identitas variabel per indeks menggunakan sub-loop verifikasi yang valid.
- **Hasil Testing Codelab:** **PASSED** ✅ (100%)

### 3. Tugas 3: Aplikasi Matrix - Operasi Dasar
- **Pengecekan Kode:**
  - Validasi matrix tersusun apik sebelum melakukan eksekusi komputasional, mencegah ValueError sedini mungkin. Matrix symmetric berhasil diperiksa komparasi boolean dengan pengembalian statis.
- **Hasil Testing Codelab:** **PASSED** ✅ (100%)

**NILAI MODUL 2: 100**

---
### **NILAI RATA-RATA SEMENTARA: 100.00 🌟**

*Penilaian ini adalah nilai sementara untuk Modul 1 dan Modul 2, dievaluasi secara statis berdasarkan instruksi/flowchart dan divalidasi melalui unit test execution.*
