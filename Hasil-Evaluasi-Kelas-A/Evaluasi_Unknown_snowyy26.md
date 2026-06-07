# Laporan Evaluasi Terperinci - Praktikum Struktur Data

---

## Data Mahasiswa
- **Nama:** snowyy26
- **NIM:** Tidak Diketahui
- **Kelas:** Struktur Data A
- **GitHub Username:** `strukturdata-a-snowyy26`

---

## Hasil Evaluasi Modul 1: Pengantar Struktur Data

- **Pengecekan Kode:**
  - Repositori GitHub ditemukan, namun terlambat.
- **Hasil Testing Codelab:** **PASSED** ✅ (50%)

**NILAI MODUL 1: 50**

---

## Hasil Evaluasi Modul 2: Array

- **Pengecekan Kode:**
  - Repositori GitHub ditemukan, namun terlambat.
- **Hasil Testing Codelab:** **PASSED** ✅ (50%)

**NILAI MODUL 2: 50**

---

## Hasil Evaluasi Modul 3: Single Linked List

### 1. Tugas 1: Implementasi Single Linked List
- **Pengecekan Kode:** `reverse()`, `find_min()`, `find_max()`, `remove_value()`, `to_list()` diimplementasikan dengan benar. Semua assert test lulus.
- **Hasil Testing:** **PASSED** ✅ (100%)

### 2. Tugas 2: Aplikasi Polinomial
- **Pengecekan Kode:** `add_polynomials()` menggunakan merge yang benar — koefisien pangkat sama digabungkan (`3x^2 + 2x^2 = 5x^2`). Output: `5x^2 + 6x^1 + 8x^0`. Semua test lulus.
- **Hasil Testing:** **PASSED** ✅ (100%)

### 3. Tugas 3: Aplikasi Music Playlist
- **Pengecekan Kode:** Semua operasi playlist (`add_song`, `remove_song`, `play`, `next_song`, `search_by_artist`, `total_duration`, `song_count`) diimplementasikan dan lulus semua test.
- **Hasil Testing:** **PASSED** ✅ (100%)

**NILAI MODUL 3: 100**

---

## Hasil Evaluasi Modul 4: Double Linked List & Circular Linked List

### 1. Tugas 1: Implementasi Double Linked List
- **Pengecekan Kode:** File berisi program "Sistem Profil dan Analisis Nilai Mahasiswa" yang menggunakan `input()` — **bukan implementasi Double Linked List**. Konten sama sekali tidak relevan dengan tugas yang diminta.
- **Hasil Testing:** **SALAH FILE** ❌ (0%)

### 2. Tugas 2: Aplikasi Text Editor Undo/Redo
- **Pengecekan Kode:** File identik dengan T1 — program profil mahasiswa yang sama, bukan Text Editor dengan DLL.
- **Hasil Testing:** **SALAH FILE** ❌ (0%)

### 3. Tugas 3: Aplikasi Round Robin Scheduler
- **Pengecekan Kode:** Round Robin benar: eksekusi bergantian `A→B→C→A→B(selesai)→C(selesai)→A(selesai)`. Rotasi head setelah tiap quantum berjalan baik.
- **Hasil Testing:** **PASSED** ✅ (100%)

**NILAI MODUL 4: 33** *(T1:0 + T2:0 + T3:100) / 3 ≈ 33*

---

## Hasil Evaluasi Modul 5: Stack

### 1. Tugas 1: Pengembangan Stack dengan Method Baru
- **Pengecekan Kode:** Semua method baru diimplementasikan dengan benar. Semua test lulus.
- **Hasil Testing:** **PASSED** ✅ (100%)

### 2. Tugas 2: Konversi dan Evaluasi Ekspresi
- **Pengecekan Kode:** `infix_to_postfix()` benar termasuk right-associativity `^`. Semua test lulus.
- **Hasil Testing:** **PASSED** ✅ (100%)

### 3. Tugas 3: Aplikasi Browser History
- **Pengecekan Kode:** `BrowserHistory` benar. Semua test lulus.
- **Hasil Testing:** **PASSED** ✅ (100%)

**NILAI MODUL 5: 100**

---

## Hasil Evaluasi Modul 6: Queue

### 1. Tugas 1: Implementasi Priority Queue
- **Pengecekan Kode:** `PriorityQueue` benar, urutan prioritas terjaga. Semua test lulus.
- **Hasil Testing:** **PASSED** ✅ (100%)

### 2. Tugas 2: Implementasi Deque + Palindrome
- **Pengecekan Kode:** `Deque` benar. Namun `is_palindrome()` tidak mengembalikan nilai apapun (return `None`) — tidak ada `return True/False`. Akibatnya semua pemanggilan `is_palindrome()` mengembalikan `None`.
- **Hasil Testing:** **FAILED** ❌ — `is_palindrome()` selalu return `None` (50%)

### 3. Tugas 3: Simulasi Antrian Bank
- **Pengecekan Kode:** 20 customers, 3 tellers, avg wait 0.30 menit — statistik benar.
- **Hasil Testing:** **PASSED** ✅ (100%)

**NILAI MODUL 6: 83** *(T1:100 + T2:50 + T3:100) / 3 ≈ 83*

---

## Hasil Evaluasi Modul 7: Review & Studi Kasus (Persiapan UTS)

### 1. Tugas 1: Soal Teori (PDF)
- **Pengecekan:** PDF `Tugas7.1_10251092_Razi.pdf` ada di folder minggu7.
- **Hasil:** **DIKUMPULKAN** ✅ (100%)

### 2. Tugas 2: Sistem Manajemen Perpustakaan
- **Pengecekan Kode:** Semua 8 test case lulus.
- **Hasil Testing Terminal:** **PASSED** ✅ (100%)

**NILAI MODUL 7: 100**

---

## Hasil Evaluasi Modul 9: Tree & Binary Tree

### 1. Tugas 1: BinaryTree Class
- **Hasil Testing Terminal:** **PASSED** ✅ (100%)

### 2. Tugas 2: Expression Tree
- **Hasil Testing Terminal:** **PASSED** ✅ (100%)

### 3. Tugas 3: Analisis Kompleksitas Tree
- **Pengecekan Kode:** `height()` rekursif tanpa `sys.setrecursionlimit` → `RecursionError` pada skewed tree.
- **Hasil Testing Terminal:** **FAILED** ❌ (0%)

**NILAI MODUL 9: 67**

---

## Hasil Evaluasi Modul 10: Binary Search Tree (BST)

### 1. Tugas 1: Pengembangan BST Class
- **Hasil Testing Terminal:** **PASSED** ✅ (100%)

### 2. Tugas 2: Sistem Phonebook dengan BST
- **Hasil Testing Terminal:** **PASSED** ✅ (100%)

### 3. Tugas 3: Analisis Performa BST
- **Hasil Testing Terminal:** **PASSED** ✅ (100%)

**NILAI MODUL 10: 100**

---

## Hasil Evaluasi Modul 11: Graph

> **Catatan teknis:** Folder `Minggu 1 /` di repo mengandung trailing space (invalid pada Windows) sehingga `git checkout` gagal. File Modul 11 dibaca via `git show HEAD:"Minggu 11/Tugas {N}_*.py"`.

### 1. Tugas 1: Pengembangan Graph Class
- **Pengecekan Kode:** Method baru lengkap, 7 test case lulus.
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

### **NILAI RATA-RATA (Modul 1-7, 9-14): 83.31**

| Modul | Nilai | Keterangan |
|-------|-------|------------|
| Modul 1 | 50 | Telat (Maks 50) |
| Modul 2 | 50 | Telat (Maks 50) |
| Modul 3 | 100 | |
| Modul 4 | 33 | T1/T2 salah file (profil mahasiswa, bukan DLL) |
| Modul 5 | 100 | |
| Modul 6 | 83 | |
| Modul 7 | 100 | |
| Modul 9 | 67 | |
| Modul 10 | 100 | |
| Modul 11 | 100 | |
| Modul 12 | 100 | |
| Modul 13 | 100 |
| Modul 14 | 100 |
| **Rata-rata** | **83.31** | |
