# Laporan Evaluasi Terperinci - Praktikum Struktur Data

---

## Data Mahasiswa
- **Nama:** Muhammad Fajri Ikhsan
- **NIM:** 10251068
- **Kelas:** Struktur Data A
- **GitHub Username:** `strukturdata-a-Fajri-ITK`

---

## Hasil Evaluasi Modul 1: Pengantar Struktur Data

### 1. Tugas 1: Pengembangan ADT Counter
- **Pengecekan Kode:**
  - Metode `subtract()` disusun dengan struktur *if/elif* yang memagari operasi decrement agar hasil akhir absolut tidak pernah berada di bawah nilai nol. 
- **Hasil Testing Codelab:** **PASSED** ✅ (100%)

### 2. Tugas 2: Pengembangan ADT Stack - Aplikasi Reverse String
- **Pengecekan Kode:**
  - Metode pembalikan (*reverse_string*) beraksi valid dengan metode pengumpulan per karakter kembali (*string concatenation*) setelah dilempar satu per satu (*pop*) memastikan skema komputas LIFO berjalan konsisten.
- **Hasil Testing Codelab:** **PASSED** ✅ (100%)

### 3. Tugas 3: Analisis Kompleksitas Lanjutan
- **Tabel Analisis Kompleksitas & Jawaban:**
  - Ketajaman analisa nampak kuat di bagian algoritma skala besar `O(n²)`. Contoh *real case* pencocokan satu juta pengguna di platform digital memperterang konsekuensi dari *nested loop* secara faktual.
- **Hasil Testing Codelab:** **PASSED** ✅ (100%)

**NILAI MODUL 1: 100**

---

## Hasil Evaluasi Modul 2: Array

### 1. Tugas 1: Pengembangan MyArray
- **Pengecekan Kode:**
  - Operasi manipulasi standar terenkapsulasi secara wajar. Fungsi `reverse` cukup minimalis dan langsung mengandalkan *built-in function* `reverse()` dasar Python, efisien secara fungsi internal namun perlu ditekankan pada konsep algoritmanya (`two pointer`) kedepannya.
- **Hasil Testing Codelab:** **PASSED** ✅ (100%)

### 2. Tugas 2: Aplikasi Array - Statistik Data
- **Pengecekan Kode:**
  - `remove_duplicates` diformulasikan kreatif mengandalkan properti struktur data *dictionary keys* (`dict.fromkeys()`) untuk pemastian keunikan elemen, suatu bentuk solusi yang langka di level perkenalan pemrograman, memperlihatkan usaha eksploratif eksternal.
- **Hasil Testing Codelab:** **PASSED** ✅ (100%)

### 3. Tugas 3: Aplikasi Matrix - Operasi Dasar
- **Pengecekan Kode:**
  - Penggunaan *list comprehension* dominan digunakan di setiap blok metode tugas matriks terstruktur (`add_matrices`, `transpose_matrix`, dll), merefleksikan alur yang padat alias *one-liner Pythonic way*. Sangat mahir memanfaatkan fungsionalitas lanjutan seperti eksekusi *zip()*.
- **Hasil Testing Codelab:** **PASSED** ✅ (100%)

**NILAI MODUL 2: 100**

---
### **NILAI RATA-RATA SEMENTARA: 100.00 🌟**

*Penilaian ini adalah nilai sementara untuk Modul 1 dan Modul 2, dievaluasi secara statis berdasarkan instruksi/flowchart dan divalidasi melalui unit test execution.*
