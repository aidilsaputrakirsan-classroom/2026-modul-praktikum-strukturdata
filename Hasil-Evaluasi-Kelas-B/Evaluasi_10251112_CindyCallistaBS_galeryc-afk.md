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
## Hasil Evaluasi Modul 10: Binary Search Tree (BST)

### 1. Tugas 1: Pengembangan BST Class
- **Pengecekan Kode:** Tidak ada folder/file Modul 10 di repo.
- **Hasil Testing Terminal:** **TIDAK DIKUMPULKAN** ❌ (0%)

### 2. Tugas 2: Sistem Phonebook dengan BST
- **Pengecekan Kode:** Tidak ada folder/file Modul 10 di repo.
- **Hasil Testing Terminal:** **TIDAK DIKUMPULKAN** ❌ (0%)

### 3. Tugas 3: Analisis Performa BST
- **Pengecekan Kode:** Tidak ada folder/file Modul 10 di repo.
- **Hasil Testing Terminal:** **TIDAK DIKUMPULKAN** ❌ (0%)

**NILAI MODUL 10: 0**

---

## Hasil Evaluasi Modul 11: Graph

### 1. Tugas 1: Pengembangan Graph Class
- **Pengecekan Kode:** Method baru lengkap, 7 test case lulus.
- **Hasil Testing Terminal:** **PASSED** ✅ (100%)

### 2. Tugas 2: Sistem Navigasi Kampus
- **Pengecekan Kode:** BFS route, shortest route (270m A→E), all_reachable berjalan benar.
- **Hasil Testing Terminal:** **PASSED** ✅ (100%)

### 3. Tugas 3: Analisis Kompleksitas Graph
- **Pengecekan:** File `tugas11.3_10251112_CindyCallista.py` berisi kode **PRAKTIKUM 11.3: BFS/DFS pada Adjacency Matrix** (header file `PRAKTIKUM 11.3: BFS/DFS pada Adjacency Matrix`), bukan Tugas Terstruktur 11.3 (Analisis Kompleksitas Graph).
- **Hasil:** **KONTEN SALAH** ❌ (0%) — praktikum dikumpulkan sebagai tugas

**NILAI MODUL 11: 67** *((100+100+0)/3 ≈ 67)*

---

## Hasil Evaluasi Modul 12: Algoritma Searching

### 1. Tugas 1: Binary Search Lanjutan
- **Pengecekan Kode:** Semua fungsi lulus 5 test case.
- **Hasil Testing Terminal:** **PASSED** ✅ (100%)

### 2. Tugas 2: Hash Table - Open Addressing
- **Pengecekan Kode:** Linear probing + tombstone, resize & rehash bekerja.
- **Hasil Testing Terminal:** **PASSED** ✅ (100%)

### 3. Tugas 3: Sistem Kamus Digital
- **Pengecekan Kode:** Bidirectional dictionary dengan multiple translations dan prefix search benar.
- **Hasil Testing Terminal:** **PASSED** ✅ (100%)

**NILAI MODUL 12: 100**

---
## Hasil Evaluasi Modul 13: Sorting Dasar

- **Catatan:** Tidak ada folder/file Modul 13 di repositori.

**NILAI MODUL 13: 0**

---

## Hasil Evaluasi Modul 14: Sorting Lanjutan

### 1. Tugas 1: Perbandingan Sorting Dasar vs Lanjutan
- **Pengecekan Kode:** Implementasi `merge_sort`, `quick_sort_inplace`, dan `heap_sort` benar; benchmark berjalan serta tabel observasi & 5 jawaban analisis terisi lengkap.
- **Hasil Testing Terminal:** **PASSED** (100%)

### 2. Tugas 2: Sorting pada Data Kompleks
- **Pengecekan Kode:** `merge_sort_by_key`, `quick_sort_by_key`, dan `multi_key_sort` benar (stabil & mendukung reverse/multi-key).
- **Hasil Testing Terminal:** **PASSED** (100%)

### 3. Tugas 3: Counting Sort dan Hybrid Sort
- **Pengecekan Kode:** `counting_sort` (stable) & `hybrid_sort` (Quick+Insertion) benar.
- **Hasil Testing Terminal:** **PASSED** (100%)

**NILAI MODUL 14: 100**

---

### **NILAI RATA-RATA (Modul 1-7, 9-14): 60.31**

| Modul | Nilai |
|-------|-------|
| Modul 1 | 0 |
| Modul 2 | 100 |
| Modul 3 | 100 |
| Modul 4 | 100 |
| Modul 5 | 100 |
| Modul 6 | 0 |
| Modul 7 | 50 |
| Modul 9 | 67 |
| Modul 10 | 0 |
| Modul 11 | 67 |
| Modul 12 | 100 |
| Modul 13 | 0 |
| Modul 14 | 100 |
| **Rata-rata** | **60.31** |

*Catatan: M11 T3 berisi file Praktikum 11.3, bukan Tugas Terstruktur 11.3 — T3=0.*

*Penilaian dievaluasi secara statis-manual berdasarkan kode program dan divalidasi melalui eksekusi unit test satu per satu.*
