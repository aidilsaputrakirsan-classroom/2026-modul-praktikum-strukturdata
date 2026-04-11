# 📝 Laporan Evaluasi Terperinci - Praktikum Struktur Data

---

## 👤 Data Mahasiswa
- **Nama:** Marine Fajar Sprinkler Taranda
- **NIM:** 10251036
- **Kelas:** Struktur Data B
- **GitHub Username:** `strukturdata-b-MarineTaranda`

---

## 🥇 Hasil Evaluasi Modul 1: Pengantar Struktur Data

### 1. Tugas 1: Pengembangan ADT Counter
- **Pengecekan Kode:**
  - Metode penambahan (`add`), pengurangan nilai (`subtract`) terlimit di 0 berkoordinasi baik, begitu juga iterasi logikal operasi `multiply`.
- **Hasil Testing Terminal:** **PASSED** ✅ (100%)

### 2. Tugas 2: Pengembangan ADT Stack - Aplikasi Reverse String
- **Pengecekan Kode:**
  - Kode pemrograman ADT Stack merespon parameter *reverse_string* dengan fungsi `push` dan `pop` tepat sasaran tanpa bug LIFO yang fatal.
- **Hasil Testing Terminal:** **PASSED** ✅ (100%)

### 3. Tugas 3: Analisis Kompleksitas Lanjutan
- **Tabel Analisis Kompleksitas & Jawaban:**
  - Perbandingan _performance_ pada triple loop diselingrekursi dan runtime milidetik pengukuran _profiling_ logis telah ditampilkan.
- **Hasil Testing Terminal:** **PASSED** ✅ (100%)

**✨ NILAI MODUL 1: 100 ✨**

---

## 🥈 Hasil Evaluasi Modul 2: Array

### 1. Tugas 1: Pengembangan MyArray
- **Pengecekan Kode:**
  - Modul MyArray seperti memanggil insert item awal dan belakang (`delete_front`), pengurut *max/min*, iterasi *count*, *reverse* direspon in-place.
- **Hasil Testing Terminal:** **PASSED** ✅ (100%)

### 2. Tugas 2: Aplikasi Array - Statistik Data
- **Pengecekan Kode:**
  - Sistem komputasi pada method OOP mencari rerata (`average`), rentang `range` nilai dan mengeleminir record iterasi item duplikat dieksekusi benar.
- **Hasil Testing Terminal:** **PASSED** ✅ (100%)

### 3. Tugas 3: Aplikasi Matrix - Operasi Dasar
- **Pengecekan Kode:**
  - Fungsional operasi dua dimensi yang mencakup penambahan (*addition*), rotasi transpose, validasi asymetric loop (i/j) dijalankan *bug-free*.
- **Hasil Testing Terminal:** **PASSED** ✅ (100%)

**✨ NILAI MODUL 2: 100 ✨**

---

## 🥉 Hasil Evaluasi Modul 3: Single Linked List

### 1. Tugas 1: Pengembangan LinkedList
- **Pengecekan Kode:** Implementasi `reverse()` (iteratif 3-pointer), `find_min()`, `find_max()`, `remove_value()`, dan `to_list()` semuanya benar dan efisien. Logika penghapusan node pertama dengan nilai tertentu sudah tepat sasaran.
- **Hasil Testing Terminal:** **PASSED** ✅

### 2. Tugas 2: Aplikasi Linked List - Polynomial
- **Pengecekan Kode:** Class `Polynomial` menggunakan `TermNode` dengan penyimpanan terurut dari pangkat tertinggi ke terendah. Method `add_term()` menangani merge koefisien dengan pangkat sama secara benar. Fungsi `add_polynomials()` memanfaatkan `defaultdict` untuk akumulasi koefisien. Method `evaluate()` dan `degree()` sudah tepat.
- **Hasil Testing Terminal:** **PASSED** ✅

### 3. Tugas 3: Aplikasi Linked List - Music Playlist
- **Pengecekan Kode:** Logika inti `add_song`, `remove_song`, `play`, `next_song`, `current_song`, `total_duration`, `song_count`, dan `search_by_artist` semuanya benar. Namun fungsi `format_duration()` tidak diimplementasikan (hanya `minutes = seconds`, tidak ada return), sehingga tampilan durasi menjadi `None`. Semua assert tetap lulus karena tidak menguji format string durasi.
- **Hasil Testing Terminal:** **PASSED** ✅ (semua assert lulus, namun display durasi menampilkan `None`)

**✨ NILAI MODUL 3: 90 ✨**

---

## 🏅 Hasil Evaluasi Modul 4: Double & Circular Linked List

### 1. Tugas 1: Pengembangan Double Linked List
- **Pengecekan Kode:** Implementasi `reverse()` (swap prev/next setiap node), `find_min()`, `find_max()`, `swap_nodes()` (tukar data), dan `is_palindrome()` (two-pointer head dan tail) sudah benar dan lulus semua test case termasuk palindrome dan non-palindrome.
- **Hasil Testing Terminal:** **PASSED** ✅

### 2. Tugas 2: Aplikasi DLL - Text Editor Undo/Redo
- **Pengecekan Kode:** File `Tugas 4.2.py` yang dikumpulkan berisi implementasi **Circular Linked List** (praktikum 4.2), bukan aplikasi Text Editor Undo/Redo yang diminta. Tugas 2 tidak dikerjakan sesuai soal.
- **Hasil Testing Terminal:** **FAILED** ❌ (bukan submission yang sesuai soal)

### 3. Tugas 3: Aplikasi CLL - Round Robin Scheduler
- **Pengecekan Kode:** File `Tugas 4.3.py` yang dikumpulkan berisi implementasi **DLL insert/delete di posisi tertentu** (praktikum 4.3), bukan Round Robin Scheduler yang diminta. Tugas 3 tidak dikerjakan sesuai soal.
- **Hasil Testing Terminal:** **FAILED** ❌ (bukan submission yang sesuai soal)

**✨ NILAI MODUL 4: 70 ✨**

## 🔢 Hasil Evaluasi Modul 5: Stack

- **Pengecekan Kode:** Tidak ada submission Modul 5 saat evaluasi dilakukan.

**✨ NILAI MODUL 5: 0 ✨**

---
## 🔢 Hasil Evaluasi Modul 6: Queue

- **Pengecekan Kode:** Tidak ada submission Modul 6 saat evaluasi dilakukan.

**✨ NILAI MODUL 6: 0 ✨**


---
### **🏆 NILAI RATA-RATA (Modul 1-6): 60.00 🏆**

*Penilaian dievaluasi secara statis-manual berdasarkan kode program dan divalidasi melalui eksekusi unit test satu per satu.*
