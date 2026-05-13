# 📝 Laporan Evaluasi Terperinci - Praktikum Struktur Data

---

## 👤 Data Mahasiswa
- **Nama:** Muhammad Hanif Murtadho
- **NIM:** 10251063
- **Kelas:** Struktur Data B
- **GitHub Username:** `strukturdata-b-liandizgo-design`

---

## 🥇 Hasil Evaluasi Modul 1: Pengantar Struktur Data

### 1. Tugas 1: Pengembangan ADT Counter
- **Pengecekan Kode:**
  - Logic fungsi penambahan nilai *add*, *subtract* yang dicegah limit `0`, positif *increment* dan fungsi kali/ *multiply* diimplementasikan dengan sangat baik pada file ADT Counter.
- **Hasil Testing Terminal:** **PASSED** ✅ (100%)

### 2. Tugas 2: Pengembangan ADT Stack - Aplikasi Reverse String
- **Pengecekan Kode:**
  - Penambahan parameter fungsi `pop()` ke iterasi list reverse terkompilasi merespon test unit array class stack _LIFO_ dengan nilai string yang benar.
- **Hasil Testing Terminal:** **PASSED** ✅ (100%)

### 3. Tugas 3: Analisis Kompleksitas Lanjutan
- **Tabel Analisis Kompleksitas & Jawaban:**
  - Fungsi cetakan `Time Execution` dieksekusi normal dan mencetak detik mikro profiler Big O untuk `triple nested loops`, recursive arrays, dll hingga maximum runtime threshold.
- **Hasil Testing Terminal:** **PASSED** ✅ (100%)

**✨ NILAI MODUL 1: 100 ✨**

---

## 🥈 Hasil Evaluasi Modul 2: Array

### 1. Tugas 1: Pengembangan MyArray
- **Pengecekan Kode:**
  - Modifikasi komputasi algoritma *first element delete* `delete_front()`, *reverse method* node, rentang index *max/min*, hingga validasi *insert array* lancar diperasikan.
- **Hasil Testing Terminal:** **PASSED** ✅ (100%)

### 2. Tugas 2: Aplikasi Array - Statistik Data
- **Pengecekan Kode:**
  - Filter logic _second maximum array list_, menghapus baris duplikasi elemen data ganda, algoritma perhitungan `average`, hingga operator kalkulator `range` dieksekusi valid tanpa IndexError.
- **Hasil Testing Terminal:** **PASSED** ✅ (100%)

### 3. Tugas 3: Aplikasi Matrix - Operasi Dasar
- **Pengecekan Kode:**
  - Metode pengerjaan validasi matrix _Symmetric_ dengan array boolean, tambah matrix array list iterables (`add_matrices()`), fungsi dot cols baris jadi _transpose_ dapat dioperasikan efisien.
- **Hasil Testing Terminal:** **PASSED** ✅ (100%)

**✨ NILAI MODUL 2: 100 ✨**

---

## 🥉 Hasil Evaluasi Modul 3: Single Linked List

### 1. Tugas 1: Pengembangan LinkedList
- **Pengecekan Kode:** Implementasi `reverse()`, `find_min()`, `find_max()`, `remove_value()`, dan `to_list()` dilakukan dengan benar menggunakan algoritma traversal standar. Metode `reverse()` menggunakan pola three-pointer (prev, current, next) yang tepat. Semua method ditempatkan sebelum docstring (pola deklarasi unik) namun secara fungsional berjalan sempurna.
- **Hasil Testing Terminal:** **PASSED** ✅

### 2. Tugas 2: Aplikasi Linked List - Polynomial
- **Pengecekan Kode:** Implementasi `add_term()` mengelola penyisipan terurut dari pangkat tertinggi ke terendah dan penggabungan suku sejenis. Fungsi `evaluate()`, `degree()`, dan `add_polynomials()` bekerja dengan tepat.
- **Hasil Testing Terminal:** **PASSED** ✅

### 3. Tugas 3: Aplikasi Linked List - Music Playlist
- **Pengecekan Kode:** Seluruh method Playlist (`add_song`, `remove_song`, `play`, `next_song`, `current_song`, `total_duration`, `song_count`, `search_by_artist`) diimplementasikan lengkap dan benar. Minor: output `display()` mencetak `/n` literal (seharusnya `\n` newline) namun tidak mempengaruhi assert test.
- **Hasil Testing Terminal:** **PASSED** ✅

**✨ NILAI MODUL 3: 100 ✨**

---

## 🏅 Hasil Evaluasi Modul 4: Double & Circular Linked List

### 1. Tugas 1: Pengembangan Double Linked List
- **Pengecekan Kode:** Implementasi `reverse()` dengan teknik swap prev/next per node, `find_min()`, `find_max()`, `swap_nodes()` (tukar data), dan `is_palindrome()` (two-pointer front/back) semuanya benar dan efisien.
- **Hasil Testing Terminal:** **PASSED** ✅

### 2. Tugas 2: Aplikasi DLL - Text Editor Undo/Redo
- **Pengecekan Kode:** Mekanisme `type_text()` menghapus history setelah current (branching), `undo()`/`redo()` traversal DLL, `can_undo()`/`can_redo()` berjalan tepat. `show_history()` menampilkan posisi current dengan pointer visual yang akurat.
- **Hasil Testing Terminal:** **PASSED** ✅

### 3. Tugas 3: Aplikasi CLL - Round Robin Scheduler
- **Pengecekan Kode:** CLL diimplementasikan dengan benar pada `add_process()` dan `remove_process()`. `execute_one_cycle()` menjalankan quantum/remaining time dengan rotasi head, dan `run()` mencetak timeline eksekusi sesuai ekspektasi.
- **Hasil Testing Terminal:** **PASSED** ✅

**✨ NILAI MODUL 4: 100 ✨**

---

## 🥇 Hasil Evaluasi Modul 5: Stack

### 1. Tugas 1: Pengembangan Stack
- **Pengecekan Kode:** Stack dengan `get_min()`, `get_max()`, `to_list()`, `copy()`, `reverse()`, `clear()` diimplementasikan dengan benar.
- **Hasil Testing Terminal:** **PASSED** ✅ (100%)

### 2. Tugas 2: Konversi dan Evaluasi Ekspresi
- **Pengecekan Kode:** Infix to postfix dengan right-associativity `^` benar (`A^B^C` → `A B C ^ ^`). Evaluate postfix dan full calculation lulus.
- **Hasil Testing Terminal:** **PASSED** ✅ (100%)

### 3. Tugas 3: Aplikasi Stack - Browser History
- **Pengecekan Kode:** BrowserHistory dengan `visit()`, `back()`, `forward()` menggunakan 2 stack benar. Semua test lulus.
- **Hasil Testing Terminal:** **PASSED** ✅ (100%)

**✨ NILAI MODUL 5: 100 ✨**

---

## 🥈 Hasil Evaluasi Modul 6: Queue

### 1. Tugas 1: Priority Queue
- **Pengecekan Kode:** PriorityQueue dengan enqueue, dequeue berdasar prioritas, peek, dan FIFO untuk prioritas sama benar.
- **Hasil Testing Terminal:** **PASSED** ✅ (100%)

### 2. Tugas 2: Deque dan Palindrome
- **Pengecekan Kode:** Deque dengan add/remove front/rear, Deque as Stack/Queue, `is_palindrome()` mengembalikan `True`/`False` benar.
- **Hasil Testing Terminal:** **PASSED** ✅ (100%)

### 3. Tugas 3: Simulasi Antrian Bank
- **Pengecekan Kode:** Simulasi 20 customers, 3 tellers. Avg waiting time 0.30 menit (positif), semua customers terlayani.
- **Hasil Testing Terminal:** **PASSED** ✅ (100%)

**✨ NILAI MODUL 6: 100 ✨**

---
## 🔢 Hasil Evaluasi Modul 7: Review & Studi Kasus (Persiapan UTS)

### 1. Tugas 1: Soal Teori (PDF)
- **Pengecekan:** PDF `Tugas7_10251063_...pdf` ada di `STRUKTUR DATA_10251063_Muhammad Hanif Murtadho/TUGAS/minggu7/`.
- **Hasil:** **DIKUMPULKAN** ✅ (100%)

### 2. Tugas 2: Sistem Manajemen Perpustakaan
- **Hasil Testing Terminal:** **PASSED** ✅ (100%)

**✨ NILAI MODUL 7: 100 ✨**

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
- **Pengecekan Kode:** Semua test lulus.
- **Hasil Testing Terminal:** **PASSED** ✅ (100%)

### 2. Tugas 2: Sistem Phonebook dengan BST
- **Pengecekan Kode:** Semua test lulus.
- **Hasil Testing Terminal:** **PASSED** ✅ (100%)

### 3. Tugas 3: Analisis Performa BST
- **Pengecekan Kode:** Sorted BST height n-1 benar. Analisis lengkap n=50000.
- **Hasil Testing Terminal:** **PASSED** ✅ (100%)

**NILAI MODUL 10: 100**

---
### **NILAI RATA-RATA (Modul 1-7, 9, 10): 96.33**

| Modul | Nilai |
|-------|-------|
| Modul 1 | 100 |
| Modul 2 | 100 |
| Modul 3 | 100 |
| Modul 4 | 100 |
| Modul 5 | 100 |
| Modul 6 | 100 |
| Modul 7 | 100 |
| Modul 9 | 67 |
| Modul 10 | 100 |
| **Rata-rata** | **96.33** |

*Penilaian dievaluasi secara statis-manual berdasarkan kode program dan divalidasi melalui eksekusi unit test satu per satu.*
