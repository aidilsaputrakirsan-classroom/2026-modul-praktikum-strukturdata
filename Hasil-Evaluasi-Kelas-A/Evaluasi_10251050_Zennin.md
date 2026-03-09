# Laporan Evaluasi Terperinci - Praktikum Struktur Data

---

## Data Mahasiswa
- **Nama:** Muhammad Zennin Feriatta Dzakwan
- **NIM:** 10251050
- **Kelas:** Struktur Data A
- **GitHub Username:** `strukturdata-a-Zennin2511`

---

## Hasil Evaluasi Modul 1: Pengantar Struktur Data

### 1. Tugas 1: Pengembangan ADT Counter
- **Pengecekan Kode:**
  - Fungsi kalkulatif tambahan seperti `add` dan `multiply` diterapkan dengan validasi tipe. `subtract()` memiliki *if-elif conditional* unik yang akurat: `elif n > 0 and self.value < n: self.value = 0` memastikan angka nol absolut.
- **Hasil Testing Codelab:** **PASSED** ✅ (100%)

### 2. Tugas 2: Pengembangan ADT Stack - Aplikasi Reverse String
- **Pengecekan Kode:**
  - Metode LIFO dikerjakan utuh. `reverse_string` mengonsumsi *push* dalam `for loop` serta *pop* dalam `while loop` yang optimal membentuk ulang string dari stack.
- **Hasil Testing Codelab:** **PASSED** ✅ (100%)

### 3. Tugas 3: Analisis Kompleksitas Lanjutan
- **Tabel Analisis Kompleksitas & Jawaban:**
  - Jawaban memuat deskripsi spesifik tentang loop konstan Big-O. Saran untuk memperbaiki limitasi O(n^2) dan perbandingan logaritmik disajikan terstruktur, menunjukkan pemahaman algoritma tingkat mendalam.
- **Hasil Testing Codelab:** **PASSED** ✅ (100%)

**NILAI MODUL 1: 100**

---

## Hasil Evaluasi Modul 2: Array

### 1. Tugas 1: Pengembangan MyArray
- **Pengecekan Kode:**
  - *Slicing* standar digantikan dengan komparasi limit. Operasi *reverse* in-place digunakan secara terpusat `self._elements.reverse()`.
- **Hasil Testing Codelab:** **PASSED** ✅ (100%)

### 2. Tugas 2: Aplikasi Array - Statistik Data
- **Pengecekan Kode:**
  - Proses identifikasi *second largest value* ditangani rapi. *Duplication check* dikalkulasikan melalui instansi baru Array `unique.search(val)` yang menekan ambiguitas data.
- **Hasil Testing Codelab:** **PASSED** ✅ (100%)

### 3. Tugas 3: Aplikasi Matrix - Operasi Dasar
- **Pengecekan Kode:**
  - Logika komparasi *transpose* secara implisit dipanggil di parameter *is_symmetric*. *Multiply Scalar* divisualisasikan rapi dengan `new_row.append(val * scalar)`.
- **Hasil Testing Codelab:** **PASSED** ✅ (100%)

**NILAI MODUL 2: 100**

---
### **NILAI RATA-RATA SEMENTARA: 100.00 🌟**

*Penilaian ini adalah nilai sementara untuk Modul 1 dan Modul 2, dievaluasi secara statis berdasarkan instruksi/flowchart dan divalidasi melalui unit test execution.*
