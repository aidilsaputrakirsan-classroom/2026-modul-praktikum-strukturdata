# 📝 Laporan Evaluasi Terperinci - Praktikum Struktur Data

---

## 👤 Data Mahasiswa
- **Nama:** Firni Fauziah Ramadhini
- **NIM:** 10231038
- **Kelas:** Struktur Data B
- **GitHub Username:** `strukturdata-b-firnifziah`

---

## 🥇 Hasil Evaluasi Modul 1: Pengantar Struktur Data

### 1. Tugas 1: Pengembangan ADT Counter
- **Pengecekan Kode:**
  - Metode penambahan fungsi baru (`add`, `subtract`, `multiply`) telah dioperasikan dengan baik tanpa mengganggu bawaannya. Substraksi bekerja memvalidasi kondisi minimum result `0`.
- **Hasil Testing Terminal:** **PASSED** ✅ (100%)

### 2. Tugas 2: Pengembangan ADT Stack - Aplikasi Reverse String
- **Pengecekan Kode:**
  - `Stack` memori ditambahkan iterasi method *push/pop* LIFO untuk membalik *reverse strings*. Program berjalan baik tanpa cacat pada compiler.
- **Hasil Testing Terminal:** **PASSED** ✅ (100%)

### 3. Tugas 3: Analisis Kompleksitas Lanjutan
- **Pengecekan Kode:**
  - Print logic profiler eksekusi untuk Time komputasi (triple array, rekursi `n/2`, iterasi max array value) berjalan sangat cepat dalam sekian _microsecond_.
- **Hasil Testing Terminal:** **PASSED** ✅ (100%)

**✨ NILAI MODUL 1: 100 ✨**

---

## 🥈 Hasil Evaluasi Modul 2: Array

### 1. Tugas 1: Pengembangan MyArray
- **Pengecekan Kode:**
  - Fungsi iterabel _indexing_ List `insert_front()`, *delete*, komputasi loop max dan min `count()` direkayasa memanipulasi _in-place array_ logic.
- **Hasil Testing Terminal:** **PASSED** ✅ (100%)

### 2. Tugas 2: Aplikasi Array - Statistik Data
- **Pengecekan Kode:**
  - Filter logic _second maximum array list_, menghapus baris duplikasi elemen iterasi ganda dan kalkulator `range` - mean dirangkai komputasinya.
- **Hasil Testing Terminal:** **PASSED** ✅ (100%)

### 3. Tugas 3: Aplikasi Matrix - Operasi Dasar
- **Pengecekan Kode:**
  - Logic matrix penjumlahan matriks array sum (`add_matrices()`), transpose matrix logic baris menjadi index sumbu kolom, beserta validasi matrix _Symmetric_ berjalan stabil.
- **Hasil Testing Terminal:** **PASSED** ✅ (100%)

**✨ NILAI MODUL 2: 100 ✨**

---

## 🥉 Hasil Evaluasi Modul 3: Single Linked List

### 1. Tugas 1: Pengembangan LinkedList
- **Pengecekan Kode:** Implementasi `reverse()`, `find_min()`, `find_max()`, `remove_value()`, dan `to_list()` lengkap dan benar. Terdapat artefak minor berupa deklarasi `class LinkedList:` bersarang di baris komentar dalam kelas yang sama (baris 18), namun tidak memengaruhi fungsionalitas karena seluruh method ada di kelas outer. Semua test case dari soal terpenuhi.
- **Hasil Testing Terminal:** **PASSED** ✅

### 2. Tugas 2: Aplikasi Linked List - Polynomial
- **Pengecekan Kode:** Implementasi `add_term()` (terurut descending, merge koefisien jika pangkat sama), `evaluate()`, `degree()`, dan `add_polynomials()` benar. Pengujian `P1+P2` menghasilkan `5x^2 + 6x^1 + 8x^0` dan `evaluate(1)=19` sesuai ekspektasi.
- **Hasil Testing Terminal:** **PASSED** ✅

### 3. Tugas 3: Aplikasi Linked List - Music Playlist
- **Pengecekan Kode:** Kelas `Playlist` mengimplementasikan `add_song()`, `remove_song()`, `play()`, `next_song()`, `current_song()`, `total_duration()`, `song_count()`, `display()`, dan `search_by_artist()` dengan benar. Penanganan current pointer saat remove_song sudah tepat.
- **Hasil Testing Terminal:** **PASSED** ✅

**✨ NILAI MODUL 3: 100 ✨**

---

## 🏅 Hasil Evaluasi Modul 4: Double & Circular Linked List

### 1. Tugas 1: Pengembangan Double Linked List
- **Pengecekan Kode:** `reverse()` menggunakan swap prev/next in-place dengan benar, `find_min()`/`find_max()` benar, `swap_nodes()` menukar data (bukan node), `is_palindrome()` menggunakan dua pointer dari head dan tail yang bertemu di tengah. Semua method berjalan sempurna.
- **Hasil Testing Terminal:** **PASSED** ✅

### 2. Tugas 2: Aplikasi DLL - Text Editor Undo/Redo
- **Pengecekan Kode:** `type_text()` memutus redo history dengan benar (branching), `append_text()` menggabungkan teks lama+baru, `undo()`/`redo()` menggeser pointer current, `can_undo()`/`can_redo()` benar. Branching test juga lulus.
- **Hasil Testing Terminal:** **PASSED** ✅

### 3. Tugas 3: Aplikasi CLL - Round Robin Scheduler
- **Pengecekan Kode:** `add_process()` membangun CLL dengan benar, `remove_process()` menangani kasus head dan non-head, `execute_one_cycle()` mengurangi `remaining_time` dan memindahkan head ke proses berikutnya. Output timeline sesuai ekspektasi (total 12 satuan waktu).
- **Hasil Testing Terminal:** **PASSED** ✅

**✨ NILAI MODUL 4: 100 ✨**

---

## 🔢 Hasil Evaluasi Modul 5: Stack

### 1. Tugas 1: Pengembangan Stack
- **Hasil Testing Terminal:** **PASSED** ✅ (100%)

### 2. Tugas 2: Infix → Postfix + Evaluasi Ekspresi
- **Pengecekan Kode:** Right-associativity `^`: `A^B^C` → `A B C ^ ^` ✅. Semua test case lulus.
- **Hasil Testing Terminal:** **PASSED** ✅ (100%)

### 3. Tugas 3: Browser History
- **Hasil Testing Terminal:** **PASSED** ✅ (100%)

**✨ NILAI MODUL 5: 100 ✨**

---

## 🔢 Hasil Evaluasi Modul 6: Queue

### 1. Tugas 1: Priority Queue
- **Hasil Testing Terminal:** **PASSED** ✅ (100%)

### 2. Tugas 2: Deque + is_palindrome()
- **Pengecekan Kode:** File yang dikumpulkan adalah file **praktikum** (`PRAKTIKUM 6.2: Implementasi Circular Queue`) — bukan implementasi Deque + `is_palindrome()` yang diminta. Konten tidak sesuai tugas.
- **Hasil Testing Terminal:** **FAILED** ❌ (0%) — salah konten

### 3. Tugas 3: Simulasi Antrian Bank
- **Pengecekan Kode:** File yang dikumpulkan adalah file **praktikum** (`PRAKTIKUM 6.3: Implementasi Queue dengan Linked List`) — bukan simulasi antrian bank 20 customer 3 teller. Konten tidak sesuai tugas.
- **Hasil Testing Terminal:** **FAILED** ❌ (0%) — salah konten

**✨ NILAI MODUL 6: 33 ✨**

---
## 🔢 Hasil Evaluasi Modul 7: Review & Studi Kasus (Persiapan UTS)

### 1. Tugas 1: Soal Teori (PDF)
- **Pengecekan Kode:** Tidak ada file PDF jawaban teori di folder `modul07/`.
- **Hasil:** **TIDAK DIKUMPULKAN** ❌ (0%)

### 2. Tugas 2: Sistem Manajemen Perpustakaan
- **Pengecekan Kode:** `Library` lengkap — Linked List, Stack history, Queue, semua 8 test lulus.
- **Hasil Testing Terminal:** **PASSED** ✅ (100%)

**✨ NILAI MODUL 7: 50 ✨**

---

## 🔢 Hasil Evaluasi Modul 9: Tree & Binary Tree

### 1. Tugas 1: Pengembangan BinaryTree Class
- **Pengecekan Kode:** Semua method (count_leaves, count_internal, is_full, mirror, __str__) benar. Edge case tree kosong lulus.
- **Hasil Testing Terminal:** **PASSED** ✅ (100%)

### 2. Tugas 2: Expression Tree
- **Pengecekan Kode:** Evaluate & traversal infix/prefix/postfix benar untuk semua test.
- **Hasil Testing Terminal:** **PASSED** ✅ (100%)

### 3. Tugas 3: Analisis Kompleksitas Tree
- **Pengecekan Kode:** Tabel height + waktu search lengkap; eksekusi tanpa error.
- **Hasil Testing Terminal:** **PASSED** ✅ (100%)

**✨ NILAI MODUL 9: 100 ✨**

---
## Hasil Evaluasi Modul 10: Binary Search Tree (BST)

### 1. Tugas 1: Pengembangan BST Class
- **Pengecekan Kode:** Semua test lulus.
- **Hasil Testing Terminal:** **PASSED** ✅ (100%)

### 2. Tugas 2: Sistem Phonebook dengan BST
- **Pengecekan Kode:** Semua test lulus.
- **Hasil Testing Terminal:** **PASSED** ✅ (100%)

### 3. Tugas 3: Analisis Performa BST
- **Pengecekan Kode:** Sorted BST heights tidak menunjukkan pola degenerate (height 11,23,18,25,29 untuk n=100-10000 seharusnya n-1). Bug metodologi pada implementasi sorted BST.
- **Hasil Testing Terminal:** **PASSED** ✅ (80%)

**NILAI MODUL 10: 93** *(T1:100 + T2:100 + T3:80) / 3 ≈ 93*

---

## Hasil Evaluasi Modul 11: Graph

### 1. Tugas 1: Pengembangan Graph Class
- **Pengecekan Kode:** Semua method baru lengkap, 7 test case lulus.
- **Hasil Testing Terminal:** **PASSED** ✅ (100%)

### 2. Tugas 2: Sistem Navigasi Kampus
- **Pengecekan Kode:** BFS route, shortest route (270m A→E), all_reachable berjalan benar.
- **Hasil Testing Terminal:** **PASSED** ✅ (100%)

### 3. Tugas 3: Analisis Kompleksitas Graph
- **Pengecekan Kode:** Perbandingan adjacency list vs matrix lengkap.
- **Hasil Testing Terminal:** **PASSED** ✅ (100%)

**NILAI MODUL 11: 100**

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

### 1. Tugas 1: Sorting dengan Custom Comparator
- **Pengecekan Kode:** `bubble_sort_custom`, `selection_sort_custom`, `insertion_sort_custom` dengan parameter `key` & `reverse` benar.
- **Hasil Testing Terminal:** **PASSED** ✅ (100%)

### 2. Tugas 2: Sistem Ranking Mahasiswa
- **Pengecekan Kode:** `RankingSystem` (`sort_by_nama`, `sort_by_nilai_akhir`, `sort_by_grade_then_nama`, `get_top_n`, `grade_distribution`) benar.
- **Hasil Testing Terminal:** **PASSED** ✅ (100%)

### 3. Tugas 3: Analisis dan Visualisasi Sorting
- **Pengecekan Kode:** Trace verbose, uji stabilitas, tabel observasi & 5 jawaban analisis lengkap.
- **Hasil Testing Terminal:** **PASSED** ✅ (100%)

**NILAI MODUL 13: 100**

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

### **NILAI RATA-RATA (Modul 1-7, 9-14): 90.46**

| Modul | Nilai |
|-------|-------|
| Modul 1 | 100 |
| Modul 2 | 100 |
| Modul 3 | 100 |
| Modul 4 | 100 |
| Modul 5 | 100 |
| Modul 6 | 33 |
| Modul 7 | 50 |
| Modul 9 | 100 |
| Modul 10 | 93 |
| Modul 11 | 100 |
| Modul 12 | 100 |
| Modul 13 | 100 |
| Modul 14 | 100 |
| **Rata-rata** | **90.46** |

*Penilaian dievaluasi secara statis-manual berdasarkan kode program dan divalidasi melalui eksekusi unit test satu per satu.*
