# 📝 Laporan Evaluasi Terperinci - Praktikum Struktur Data

---

## 👤 Data Mahasiswa
- **Nama:** Cindy Callista BS
- **NIM:** 10251112
- **Kelas:** Struktur Data B
- **GitHub Username:** `strukturdata-b-galeryc-afk`

---

## 🥇 Hasil Evaluasi Modul 1: Pengantar Struktur Data

- **Pengecekan Kode:**
  - Terjadi isu sintaksis struktural dan pemanggilan fungsi pada file modul 1 (`Tugas2_10251112_cindyCallistaBS.py`). Uji testing terminal mendapati AttributeError karena skrip salah merujuk penambahan array pada `self.items.append` alih-alih `self._items.append()` seperti deklarasi stack encapsulation utamanya. Hal ini menyebabkan Stack gagal jalan.
- **Hasil Testing Terminal:** **FAILED** ❌ (0%)

**✨ NILAI MODUL 1: 0 ✨**

---

## 🥈 Hasil Evaluasi Modul 2: Array

### 1. Tugas 1: Pengembangan MyArray
- **Pengecekan Kode:**
  - Script program sanggup mengadopsi fungsionalitas memanipulasi _in-place list_ (insert awal index array, delete, count dan function reverse).
- **Hasil Testing Terminal:** **PASSED** ✅ (100%)

### 2. Tugas 2: Aplikasi Array - Statistik Data
- **Pengecekan Kode:**
  - Metode filter rekursif menghapus index duplicate angkay array `remove_duplicates()`, komputasi maximum array - perbandingan dan penggabungan loop _average_ tidak crash.
- **Hasil Testing Terminal:** **PASSED** ✅ (100%)

### 3. Tugas 3: Aplikasi Matrix - Operasi Dasar
- **Pengecekan Kode:**
  - Menerapkan iterasi komputasi tambah row dan cols Array ganda (matrix tambah), dan rotasi iterasi loop 2D (`transpose`) dengan efisien.
- **Hasil Testing Terminal:** **PASSED** ✅ (100%)

**✨ NILAI MODUL 2: 100 ✨**

---

## 🥉 Hasil Evaluasi Modul 3: Single Linked List

### 1. Tugas 1: Pengembangan LinkedList
- **Pengecekan Kode:** Implementasi `reverse()`, `find_min()`, `find_max()`, `remove_value()`, dan `to_list()` semua benar dan lengkap. Logika identik dengan template soal, berjalan tanpa error. Semua test case lulus.
- **Hasil Testing Terminal:** **PASSED** ✅

### 2. Tugas 2: Aplikasi Linked List - Polynomial
- **Pengecekan Kode:** `add_term()` menggunakan pendekatan merge saat exponent sama. `evaluate()` dan `degree()` benar. `add_polynomials()` menggunakan merge dua pointer yang lebih efisien (O(n)). Display menggunakan format lebih ringkas (misal `2x` bukan `2x^1`).
- **Hasil Testing Terminal:** **PASSED** ✅

### 3. Tugas 3: Aplikasi Linked List - Music Playlist
- **Pengecekan Kode:** Semua method `Playlist` terimplementasi dengan benar. `search_by_artist()` berjalan normal. `remove_song()` tidak mengupdate pointer current jika current bukan lagu yang dihapus (aman). Test semua lulus.
- **Hasil Testing Terminal:** **PASSED** ✅

**✨ NILAI MODUL 3: 100 ✨**

---

## 🏅 Hasil Evaluasi Modul 4: Double & Circular Linked List

### 1. Tugas 1: Pengembangan Double Linked List
- **Pengecekan Kode:** `reverse()`, `find_min()`, `find_max()`, `swap_nodes()`, `is_palindrome()` semua diimplementasikan dengan benar menggunakan algoritma pointer dua arah. Terdapat beberapa baris `pass` setelah `return` (dead code) yang tidak berpengaruh pada eksekusi.
- **Hasil Testing Terminal:** **PASSED** ✅

### 2. Tugas 2: Aplikasi DLL - Text Editor Undo/Redo
- **Pengecekan Kode:** Undo/Redo menggunakan DLL state node. Branching (mengetik setelah undo) menghapus redo history dengan benar. `show_history()` menampilkan riwayat edit lengkap. Semua test case lulus.
- **Hasil Testing Terminal:** **PASSED** ✅

### 3. Tugas 3: Aplikasi CLL - Round Robin Scheduler
- **Pengecekan Kode:** Implementasi CLL Round Robin lengkap. `add_process()`, `remove_process()`, `execute_one_cycle()`, dan `run()` benar. Output timeline sesuai ekspektasi. `get_statistics()` mengembalikan total_time dan total_completed.
- **Hasil Testing Terminal:** **PASSED** ✅

**✨ NILAI MODUL 4: 100 ✨**

---

## 🥇 Hasil Evaluasi Modul 5: Stack

### 1. Tugas 1: Pengembangan Stack
- **Pengecekan Kode:** Stack dengan `get_min/max`, `to_list`, `copy`, `reverse`, `clear` diimplementasikan benar.
- **Hasil Testing Terminal:** **PASSED** ✅ (100%)

### 2. Tugas 2: Konversi dan Evaluasi Ekspresi
- **Pengecekan Kode:** Infix to postfix dengan right-associativity `^` benar. Full calculation lulus semua.
- **Hasil Testing Terminal:** **PASSED** ✅ (100%)

### 3. Tugas 3: Aplikasi Stack - Browser History
- **Pengecekan Kode:** BrowserHistory dengan 2 stack, visit/back/forward benar.
- **Hasil Testing Terminal:** **PASSED** ✅ (100%)

**✨ NILAI MODUL 5: 100 ✨**

---

## 🥈 Hasil Evaluasi Modul 6: Queue

- **Pengecekan Kode:** Repositori diperiksa, **tidak ada file tugas untuk Modul 6** — hanya terdapat file praktikum (`praktikum6.1/2/3.py`) dan placeholder `callista`. ⚠️
- **Hasil Testing Terminal:** **FAILED** ❌ (0%)

**✨ NILAI MODUL 6: 0 ✨**

---
## 🔢 Hasil Evaluasi Modul 7: Review & Studi Kasus (Persiapan UTS)

### 1. Tugas 1: Soal Teori (PDF)
- **Pengecekan:** PDF `Tugas7_10251112_CindyCallistaBeatriceS.pdf` ada di `minggu7/`.
- **Hasil:** **DIKUMPULKAN** ✅ (100%)

### 2. Tugas 2: Sistem Manajemen Perpustakaan
- **Pengecekan Kode:** Header file menuliskan "TUGAS 7.2: Sistem Manajemen Perpustakaan", namun isi kode adalah `class Task` & `class TaskScheduler` (Task Scheduler) — konten salah, bukan Library/Perpustakaan.
- **Hasil:** **KONTEN SALAH** ❌ (0%)

**✨ NILAI MODUL 7: 50 ✨**

---

## 🔢 Hasil Evaluasi Modul 9: Tree & Binary Tree

### 1. Tugas 1: BinaryTree Class
- **Hasil Testing Terminal:** **PASSED** ✅ (100%)

### 2. Tugas 2: Expression Tree
- **Hasil Testing Terminal:** **PASSED** ✅ (100%)

### 3. Tugas 3: Analisis Kompleksitas Tree
- **Pengecekan Kode:** `height()` rekursif tanpa `sys.setrecursionlimit` → `RecursionError` pada skewed tree.
- **Hasil Testing Terminal:** **FAILED** ❌ (0%)

**✨ NILAI MODUL 9: 67 ✨**

---
### **🏆 NILAI RATA-RATA (Modul 1-7, 9): 64.63 🏆**

*Penilaian dievaluasi secara statis-manual berdasarkan kode program dan divalidasi melalui eksekusi unit test satu per satu.*
