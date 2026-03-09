# Laporan Evaluasi Terperinci - Praktikum Struktur Data

---

## Data Mahasiswa
- **Nama:** Salsabila Yulianti Salim
- **NIM:** 10251026
- **Kelas:** Struktur Data A
- **GitHub Username:** `strukturdata-a-Salsabilaayees`

---

## Hasil Evaluasi Modul 1: Pengantar Struktur Data

### 1. Tugas 1: Pengembangan ADT Counter
- **Pengecekan Kode:**
  - Fungsi penambahan `add()`, `subtract()`, dan perkalian matematis `multiply()` ditulis dengan *if kondisional* pencegahan *underflow* yang jelas. Logic algoritma aman dan berjalan mulus.
- **Hasil Testing Codelab:** **PASSED** ✅ (100%)

### 2. Tugas 2: Pengembangan ADT Stack - Aplikasi Reverse String
- **Pengecekan Kode:**
  - Metode Stack diproteksi dengan `if not self.is_empty():` sebelum memodifikasi `self._items`. Implementasi string pembalikan terkomposisi dengan baik.
- **Hasil Testing Codelab:** **PASSED** ✅ (100%)

### 3. Tugas 3: Analisis Kompleksitas Lanjutan
- **Tabel Analisis Kompleksitas & Jawaban:**
  - Memberikan argumen konkrit terhadap setiap nilai *Time Complexity* di tabel. Untuk `O(log n)` (fungsi E), disertakan simulasi runut *tree* (10000 -> 5000 -> 2500 -> ...), merefleksikan pamahaman rekursif yang prima. Analisa kasus nyatanya sangat dalam dan detail.
- **Hasil Testing Codelab:** **PASSED** ✅ (100%)

**NILAI MODUL 1: 100**

---

## Hasil Evaluasi Modul 2: Array

### 1. Tugas 1: Pengembangan MyArray
- **Pengecekan Kode:**
  - Kode solid dilengkapi mitigasi error (Raising ValueError/IndexError) jika array kosong. Penggunaan dua variabel swap pada fungsi *reverse()* array *in-place* bekerja secara efisien.
- **Hasil Testing Codelab:** **PASSED** ✅ (100%)

### 2. Tugas 2: Aplikasi Array - Statistik Data
- **Pengecekan Kode:**
  - Fungsi iterasi saat penghitungan data kuantitatif tidak menggunakan fungsi instan/bawaan python (seperti min/max), mencerminkan adopsi kompetensi Algoritma. Algoritma `remove_duplicates` dibuat secara murni mengitari elemen array O(n^2).
- **Hasil Testing Codelab:** **PASSED** ✅ (100%)

### 3. Tugas 3: Aplikasi Matrix - Operasi Dasar
- **Pengecekan Kode:**
  - Komparasi ordo dan nilai matriks ditangani rapi. *is_symmetric* menggunakan komparator presisi dengan baris `matrix[i][j] != matrix[j][i]` untuk check kelayakan identitas tanpa merombak memori untuk replikasi transpose penuh. 
- **Hasil Testing Codelab:** **PASSED** ✅ (100%)

**NILAI MODUL 2: 100**

---
### **NILAI RATA-RATA SEMENTARA: 100.00 🌟**

*Penilaian ini adalah nilai sementara untuk Modul 1 dan Modul 2, dievaluasi secara statis berdasarkan instruksi/flowchart dan divalidasi melalui unit test execution.*
