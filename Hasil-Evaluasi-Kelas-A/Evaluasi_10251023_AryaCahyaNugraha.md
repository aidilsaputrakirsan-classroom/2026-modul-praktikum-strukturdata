# Laporan Evaluasi Terperinci - Praktikum Struktur Data

---

## Data Mahasiswa
- **Nama:** Arya Cahya Nugraha
- **NIM:** 10251023
- **Kelas:** Struktur Data A
- **GitHub Username:** `strukturdata-a-AryaCahyaNugraha22`

---

## Hasil Evaluasi Modul 1: Pengantar Struktur Data

### 1. Tugas 1: Pengembangan ADT Counter
- **Pengecekan Kode:**
  - Metode operasional `add()`, `subtract()`, dan `multiply()` berfungsi secara matematis dengan baik. Kondisi penjagaan _underflow_ `<0` berhasil di-construct memakai kontrol boolean rasional.
- **Hasil Testing Codelab:** **PASSED** ✅ (100%)

### 2. Tugas 2: Pengembangan ADT Stack - Aplikasi Reverse String
- **Pengecekan Kode:**
  - `Stack` terimplementasi natural menggunakan List. String reversal logic dengan `while not stack.is_empty(): result += stack.pop()` sesuai *flowchart*.
- **Hasil Testing Codelab:** **PASSED** ✅ (100%)

### 3. Tugas 3: Analisis Kompleksitas Lanjutan
- **Tabel Analisis Kompleksitas & Jawaban:**
  - Klasifikasi struktur _Big-O Notation_ (konstan, linier, kuadratik, logaritmik, kubik) sangat lugas. Definisi `O(n^3)` (delapan juta operasi) dan `O(log n)` (pembagian menjadi setengah) akurat. Argumentasi jawaban logis untuk kasus sistem nyata media sosial.
- **Hasil Testing Codelab:** **PASSED** ✅ (100%)

**NILAI MODUL 1: 100**

---

## Hasil Evaluasi Modul 2: Array

### 1. Tugas 1: Pengembangan MyArray
- **Pengecekan Kode:**
  - `insert_front` / `delete_front` di-approach menggunakan operasi list `insert(0)` dan `pop(0)`. In-place swap *reverse* array dibuat manual `while left < right` pertukaran variable tanpa function `reverse()` bawaan. Sangat bagus!
- **Hasil Testing Codelab:** **PASSED** ✅ (100%)

### 2. Tugas 2: Aplikasi Array - Statistik Data
- **Pengecekan Kode:**
  - Logika pengecekan _second largest_ elegan `-inf`. Algoritma untuk menghapus duplikasi loop di *remove_duplicates* dilakukan O(n^2) komparasi manual secara *pure* (bukan *built-in module module/set*). 
- **Hasil Testing Codelab:** **PASSED** ✅ (100%)

### 3. Tugas 3: Aplikasi Matrix - Operasi Dasar
- **Pengecekan Kode:**
  - Analisa dimensi saat `add_matrices` diaplikasikan dengan kokoh, menghindari kegagalan Index bila matrix *non-identik*. Fungsi simetri direpresentasi membandingkan *matrix* primer secara _boolean equal_ ke transponenya.
- **Hasil Testing Codelab:** **PASSED** ✅ (100%)

**NILAI MODUL 2: 100**


---

## Hasil Evaluasi Modul 3: Single Linked List

### 1. Tugas 1: Implementasi Single Linked List
- **Pengecekan Kode:**
  - `reverse()`, `find_min()`, `find_max()`, `remove_value()`, dan `to_list()` terimplementasi dengan benar dan berjalan sesuai test cases. File berisi duplikasi kode (Node dan LinkedList didefinisikan berulang kali karena penggabungan beberapa file Praktikum), namun Python menggunakan definisi kelas terakhir yang valid.
- **Hasil Testing:** **PASSED** ✅ (100%)

### 2. Tugas 2: Aplikasi Polynomial
- **Pengecekan Kode:**
  - **Tidak sesuai requirement:** File "Tugas Terstruktur 2" yang dikumpulkan berisi kode Praktikum 3.2 (Insert/Delete di Posisi), bukan Aplikasi Polynomial. Mahasiswa mengumpulkan file Praktikum sebagai Tugas Terstruktur.
- **Hasil Testing:** **FAILED** ❌ (Bukan implementasi Polynomial — file salah)

### 3. Tugas 3: Aplikasi Music Playlist
- **Pengecekan Kode:**
  - **Tidak sesuai requirement:** File "Tugas Terstruktur 3" yang dikumpulkan berisi kode Praktikum 3.3 (Operasi Tambahan), bukan Aplikasi Music Playlist. Mahasiswa mengumpulkan file Praktikum sebagai Tugas Terstruktur.
- **Hasil Testing:** **FAILED** ❌ (Bukan implementasi Music Playlist — file salah)

**NILAI MODUL 3: 60**

---

## Hasil Evaluasi Modul 4: Double Linked List & Circular Linked List

### 1. Tugas 1: Implementasi Double Linked List
- **Pengecekan Kode:**
  - **Tidak ada Tugas Terstruktur:** Folder minggu 4 hanya berisi file Praktikum 4.1 (DLL), 4.2 (Circular LL), dan 4.3 (Insert/Delete DLL). Tidak ditemukan file Tugas Terstruktur yang mengimplementasikan `reverse()`, `find_min()`, `find_max()`, `swap_nodes()`, dan `is_palindrome()`.
- **Hasil Testing:** **FAILED** ❌ (Tidak ada submission Tugas Terstruktur)

### 2. Tugas 2: Aplikasi Text Editor Undo/Redo
- **Pengecekan Kode:**
  - Tidak ada submission.
- **Hasil Testing:** **FAILED** ❌ (Tidak ada submission)

### 3. Tugas 3: Aplikasi Round Robin Scheduler
- **Pengecekan Kode:**
  - Tidak ada submission.
- **Hasil Testing:** **FAILED** ❌ (Tidak ada submission)

**NILAI MODUL 4: 0**

---
### **NILAI RATA-RATA SEMENTARA: 65.00 🌟**

*Penilaian ini adalah nilai sementara untuk Modul 1 hingga Modul 4, dievaluasi secara statis berdasarkan instruksi/flowchart dan divalidasi melalui unit test execution.*
