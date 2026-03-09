# Laporan Evaluasi Terperinci - Praktikum Struktur Data

---

## Data Mahasiswa
- **Nama:** Julian Zaky Saputra
- **NIM:** 10251080
- **Kelas:** Struktur Data A
- **GitHub Username:** `strukturdata-a-Julian-Zaky-Saputra`

---

## Hasil Evaluasi Modul 1: Pengantar Struktur Data

### 1. Tugas 1: Pengembangan ADT Counter
- **Pengecekan Kode:**
  - Metode `subtract()` diimplementasikan menahan value counter untuk tak jatuh di bawah nol `if self._value < 0: self._value = 0` setelah dilakukan pengurangan. Langkah yang ringkas dan fungsional.
- **Hasil Testing Codelab:** **PASSED** ✅ (100%)

### 2. Tugas 2: Pengembangan ADT Stack - Aplikasi Reverse String
- **Pengecekan Kode:**
  - Fungsi penumpukan dan pengeluaran berlapis dari *stack* untuk *reverse_string* dieksekusi benar.
- **Hasil Testing Codelab:** **PASSED** ✅ (100%)

### 3. Tugas 3: Analisis Kompleksitas Lanjutan
- **Tabel Analisis Kompleksitas & Jawaban:**
  - Mahasiswa mendeskripsikan secara awam namun cukup deskriptif, misal *Triple nested loop* dilambangkan "Angka diulang tiga kali bertingkat" membuktikan pemahaman inti materi, walau disarankan menggunakan terminologi ilmiah di lingkungan akademis. Contoh pencarian duplikasi data dari 5 juta nasabah bank (skala triliun operasi) untuk kasus batas toleransi `O(n²)` diuraikan sangat brilian.
- **Hasil Testing Codelab:** **PASSED** ✅ (100%)

**NILAI MODUL 1: 100**

---

## Hasil Evaluasi Modul 2: Array

### 1. Tugas 1: Pengembangan MyArray
- **Pengecekan Kode:**
  - Terdapat deteksi tambahan pada blok *find_min* dan *find_max* yang memeriksa via `len() == 0` dan kemudian melakukan eksekusi inisasial. Fungsi `reverse` telah berjalan aman menggunakan *two pointer strategy*.
- **Hasil Testing Codelab:** **PASSED** ✅ (100%)

### 2. Tugas 2: Aplikasi Array - Statistik Data
- **Pengecekan Kode:**
  - Mahkamah kode menemukan sebuah praktik impresif di mana perhitungan elemen terbesar kedua *find_second_largest* tidak memakai sorting sama sekali (memenuhi kompleksitas `O(n)` sejati) tetapi menginisiasi dua angka variabel bantuan paling kecil dari Python `float("-inf")` (*infinity* negatif), algoritma yang brilian dan tingkat tinggi.
- **Hasil Testing Codelab:** **PASSED** ✅ (100%)

### 3. Tugas 3: Aplikasi Matrix - Operasi Dasar
- **Pengecekan Kode:**
  - Pemeriksaan ukuran matriks dipertahankan aman, struktur for bersarang (*nested-for loop*) standar beroperasi untuk melakukan modifikasi nilai *matrix*, sesuai algoritma dasar perkalian dan penjumlahan matriks.
- **Hasil Testing Codelab:** **PASSED** ✅ (100%)

**NILAI MODUL 2: 100**

---
### **NILAI RATA-RATA SEMENTARA: 100.00 🌟**

*Penilaian ini adalah nilai sementara untuk Modul 1 dan Modul 2, dievaluasi secara statis berdasarkan instruksi/flowchart dan divalidasi melalui unit test execution.*
