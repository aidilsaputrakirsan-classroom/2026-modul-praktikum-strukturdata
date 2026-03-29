# Laporan Evaluasi Terperinci - Praktikum Struktur Data

---

## Data Mahasiswa
- **Nama:** Zacky Ahmad Ardian
- **NIM:** 10251014
- **Kelas:** Struktur Data A
- **GitHub Username:** `strukturdata-a-Zacky10251014`

---

## Hasil Evaluasi Modul 1: Pengantar Struktur Data

### 1. Tugas 1: Pengembangan ADT Counter
- **Pengecekan Kode:**
  - Metode `subtract()`, `add()` dan `multiply()` dibuat dan divalidasi dengan baik. Fungsionalitas sesuai flowchart ADT.
- **Hasil Testing Codelab:** **PASSED** ✅ (100%)

### 2. Tugas 2: Pengembangan ADT Stack - Aplikasi Reverse String
- **Pengecekan Kode:**
  - `print_stack` menampilkan list stack yang valid. 
  - `reverse_string` mengimplentasikan pemanfaatan Stack `pop()` linear yang bersih.
- **Hasil Testing Codelab:** **PASSED** ✅ (100%)

### 3. Tugas 3: Analisis Kompleksitas Lanjutan
- **Tabel Analisis Kompleksitas & Jawaban:**
  - Evaluasi runtime logis, perhitungan jumlah loop dan alur eksekusinya tepat sasaran (C-E-A-F-B-D). Analisa Big O benar semua.
- **Hasil Testing Codelab:** **PASSED** ✅ (100%)

**NILAI MODUL 1: 100**

---

## Hasil Evaluasi Modul 2: Array

### 1. Tugas 1: Pengembangan MyArray
- **Pengecekan Kode:**
  - Logika modifikasi array `insert_front` dan reversi menggunakan struktur pivot pointer ganda O(n) yang sangat matang. Pencarian min/max stabil.
- **Hasil Testing Codelab:** **PASSED** ✅ (100%)

### 2. Tugas 2: Aplikasi Array - Statistik Data
- **Pengecekan Kode:**
  - `average`, `second_largest`, hingga `remove_duplicates` O(n²) divalidasi dengan cermat dan tepat. Penggunaan `float('-inf')` diamati dengan sangat baik. 
- **Hasil Testing Codelab:** **PASSED** ✅ (100%)

### 3. Tugas 3: Aplikasi Matrix - Operasi Dasar
- **Pengecekan Kode:**
  - Iterasi matriks 2D (baris dan kolom) untuk rekalkulasi dan validasi (simetri, diagonal) berjalan sesuai standar operasi matematis array.
- **Hasil Testing Codelab:** **PASSED** ✅ (100%)

**NILAI MODUL 2: 100**

---

## Hasil Evaluasi Modul 3: Single Linked List

### 1. Tugas 1: Implementasi Single Linked List
- **Pengecekan Kode:**
  - Implementasi `reverse()`, `find_min()`, `find_max()`, `remove_value()`, dan `to_list()` semuanya benar. Menggunakan mixed indentation (tab dan spasi) namun konsisten. Semua test assertions berhasil dilalui.
- **Hasil Testing:** **PASSED** ✅ (100%)

### 2. Tugas 2: Aplikasi Polynomial
- **Pengecekan Kode:**
  - `Polynomial` diimplementasikan dengan baik. `add_polynomials()` menggunakan pendekatan merge dua sorted linked list yang lebih efisien (simultaneous traversal), berbeda dari mahasiswa lain. Semua test assertions lulus.
- **Hasil Testing:** **PASSED** ✅ (100%)

### 3. Tugas 3: Aplikasi Music Playlist
- **Pengecekan Kode:**
  - Terdapat **duplikasi definisi** `next_song()` (baris 79-85 dan 88-97) dan `total_duration()` (baris 101-110 dan 122-134) — Python menggunakan definisi terakhir sehingga tidak error. Method `display()` **tidak mencetak footer** (baris `total = format_duration(...)` dihitung tapi tidak di-print, tidak ada `print("=====...")` di akhir). Namun semua test assertions berhasil karena test tidak memeriksa output `display()` secara langsung.
- **Hasil Testing:** **PASSED** ✅ (90%) — Semua assertion lulus, namun display() tidak menampilkan footer total

**NILAI MODUL 3: 97**

---

## Hasil Evaluasi Modul 4: Double Linked List & Circular Linked List

### 1. Tugas 1: Implementasi Double Linked List
- **Pengecekan Kode:**
  - File memiliki duplikasi blok `reverse()` (satu dengan mixed tab indentation dan satu dengan spasi standar), Python menggunakan definisi kedua yang valid. Semua method (`reverse()`, `find_min()`, `find_max()`, `swap_nodes()`, `is_palindrome()`, `to_list()`) diimplementasikan dengan benar dan lulus semua assertions.
- **Hasil Testing:** **PASSED** ✅ (100%)

### 2. Tugas 2: Aplikasi Text Editor Undo/Redo
- **Pengecekan Kode:**
  - Implementasi clean dan lengkap. `type_text()` memotong redo history dengan benar. `undo()`/`redo()` berfungsi dengan tepat. `show_history()` menandai state aktif dengan ` ^current`.
- **Hasil Testing:** **PASSED** ✅ (100%)

### 3. Tugas 3: Aplikasi Round Robin Scheduler
- **Pengecekan Kode:**
  - Implementasi CLL Round Robin Scheduler lengkap dan benar. `add_process()`, `remove_process()`, `execute_one_cycle()`, dan `run()` semuanya berjalan menghasilkan timeline yang tepat. `get_statistics()` mengembalikan total waktu dan jumlah proses.
- **Hasil Testing:** **PASSED** ✅ (100%)

**NILAI MODUL 4: 100**

---
### **NILAI RATA-RATA SEMENTARA: 99 🌟**

*Penilaian ini adalah nilai sementara untuk Modul 1 hingga Modul 4, dievaluasi secara statis berdasarkan instruksi/flowchart dan divalidasi melalui unit test execution.*
