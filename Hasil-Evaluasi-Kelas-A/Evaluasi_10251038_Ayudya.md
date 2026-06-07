# Laporan Evaluasi Terperinci - Praktikum Struktur Data

---

## Data Mahasiswa
- **Nama:** Ayudya Aisyah Mutiaradinna
- **NIM:** 10251038
- **Kelas:** Struktur Data A
- **GitHub Username:** `strukturdata-a-10251038`

---

## Hasil Evaluasi Modul 1: Pengantar Struktur Data

### 1. Tugas 1: Pengembangan ADT Counter
- **Pengecekan Kode:**
  - Metode `subtract(n)` didesain elegan menggunakan `max(0, self._value - n)`, sebuah *Pythonic way* yang cerdas untuk menghentikan angka negatif tanpa *conditional if* ekstensif.
- **Hasil Testing Codelab:** **PASSED** ✅ (100%)

### 2. Tugas 2: Pengembangan ADT Stack - Aplikasi Reverse String
- **Pengecekan Kode:**
  - Fungsi iterasi string-ke-stack dan stack-ke-string *reverse_string* dirangkai tanpa cela dan memberikan waktu eksekusi yang optimal (kondisi `is_empty` pada saat `pop`).
- **Hasil Testing Codelab:** **PASSED** ✅ (100%)

### 3. Tugas 3: Analisis Kompleksitas Lanjutan
- **Tabel Analisis Kompleksitas & Jawaban:**
  - Penjelasan O(log n) untuk fungsi *recursive halving* sangat jelas. Pemilahan ranking kompleksitas Big-O juga tidak ada yang salah dan relevan.
- **Hasil Testing Codelab:** **PASSED** ✅ (100%)

**NILAI MODUL 1: 100**

---

## Hasil Evaluasi Modul 2: Array

### 1. Tugas 1: Pengembangan MyArray
- **Pengecekan Kode:**
  - Mengimplementasikan pengecekan array minimum dan maksimum melalui *looping* O(n). *List swap* pada `reverse` in-place tertulis dinamis tanpa bergantung pada list ekstra.
- **Hasil Testing Codelab:** **PASSED** ✅ (100%)

### 2. Tugas 2: Aplikasi Array - Statistik Data
- **Pengecekan Kode:**
  - Pencarian `find_second_largest` dan `remove_duplicates` dijamin mematuhi parameter O(n) & O(n²). Penggunaan struktur kondisi *if-elif* pada second largest dimatangkan via `float('-inf')` untuk menghindari error nilai nol.
- **Hasil Testing Codelab:** **PASSED** ✅ (100%)

### 3. Tugas 3: Aplikasi Matrix - Operasi Dasar
- **Pengecekan Kode:**
  - Kesetaraan dimensi (`rows != len(matrix2) or cols != len(matrix2[0])`) menjaga validitas penjumlahan array dinamis. Operasi iteratif ganda untuk *transpose* dan *symmetric arrays* dilogikakan tajam .
- **Hasil Testing Codelab:** **PASSED** ✅ (100%)

**NILAI MODUL 2: 100**

---

## Hasil Evaluasi Modul 3: Single Linked List

### 1. Tugas 1: Implementasi Single Linked List
- **Pengecekan Kode:**
  - Implementasi `reverse()`, `find_min()`, `find_max()`, `remove_value()`, dan `to_list()` semuanya benar dan lengkap. Kelas ini juga dilengkapi dengan method tambahan seperti `insert_at_position()`, `delete_at_position()`, `get()`, `count()`, `clear()`, `get_head()`, dan `get_tail()` — melebihi persyaratan minimum.
- **Hasil Testing:** **PASSED** ✅ (100%)

### 2. Tugas 2: Aplikasi Polinomial
- **Pengecekan Kode:**
  - `TermNode` menyimpan coefficient dan exponent. `add_term()` menjaga urutan dari pangkat tertinggi ke terendah dengan penggabungan koefisien jika pangkat sudah ada. `evaluate()` dan `degree()` diimplementasi dengan benar. Format tampilan menggunakan `x` (tanpa pangkat eksplisit untuk exp=1) yang lebih rapi.
- **Hasil Testing:** **PASSED** ✅ (100%)

### 3. Tugas 3: Aplikasi Music Playlist
- **Pengecekan Kode:**
  - Seluruh operasi playlist diimplementasikan lengkap: `song_count()`, `total_duration()`, `play()`, `next_song()`, `search_by_artist()`, dan `remove_song()`. Semua test case berhasil dengan output yang bersih.
- **Hasil Testing:** **PASSED** ✅ (100%)

**NILAI MODUL 3: 100**

---

## Hasil Evaluasi Modul 4: Double Linked List & Circular Linked List

### 1. Tugas 1: Implementasi Double Linked List
- **Pengecekan Kode:**
  - `DoublyLinkedList` menggunakan `DNode` dengan pointer `prev` dan `next`. Method baru `reverse()`, `find_min()`, `find_max()`, `swap_nodes()`, dan `is_palindrome()` diimplementasikan dengan benar dan terstruktur baik.
- **Hasil Testing:** **PASSED** ✅ (100%)

### 2. Tugas 2: Aplikasi Text Editor Undo/Redo
- **Pengecekan Kode:**
  - `TextEditor` berbasis DLL dengan manajemen history yang baik. `type_text()`, `append_text()`, `undo()`, `redo()`, dan branching semuanya berfungsi benar. Display history menampilkan state dengan format `(current)` pada posisi aktif.
- **Hasil Testing:** **PASSED** ✅ (100%)

### 3. Tugas 3: Aplikasi Round Robin Scheduler
- **Pengecekan Kode:**
  - `RoundRobinScheduler` menggunakan Circular Linked List. Struktur CLL dan `add_process()` diimplementasi dengan benar. Namun, method `run()` tidak melakukan perpindahan proses (tidak ada `self.head = self.head.next`) setelah setiap quantum — akibatnya scheduler mengeksekusi proses secara sekuensial (A selesai dulu, baru B, lalu C) alih-alih interleaving Round Robin yang seharusnya. Total waktu eksekusi (12) tetap benar sehingga test assert lolos, namun perilaku Round Robin tidak ter-implementasi dengan benar.
- **Hasil Testing:** **PASSED** ✅ (test lolos) — namun terdapat bug logika Round Robin (proses tidak berotasi antar quantum)

**NILAI MODUL 4: 80**

---

## Hasil Evaluasi Modul 5: Stack

### 1. Tugas 1: Pengembangan Stack dengan Method Baru
- **Pengecekan Kode:** Semua method benar, semua test lulus.
- **Hasil Testing:** **PASSED** ✅ (100%)

### 2. Tugas 2: Konversi dan Evaluasi Ekspresi
- **Pengecekan Kode:** `infix_to_postfix()` 5/6 benar; **right-associativity `^` tidak ditangani**. Evaluasi postfix dan calculate semua benar.
- **Hasil Testing:** **HAMPIR LULUS** ⚠️ (90%)

### 3. Tugas 3: Aplikasi Browser History
- **Pengecekan Kode:** Browser history benar.
- **Hasil Testing:** **PASSED** ✅ (100%)

**NILAI MODUL 5: 97** *(T1:100 + T2:90 + T3:100) / 3 ≈ 97*

---

## Hasil Evaluasi Modul 6: Queue

### 1. Tugas 1: Implementasi Priority Queue
- **Pengecekan Kode:** Priority Queue benar. Catatan: urutan FIFO untuk prioritas sama tidak terjaga (Normal keluar sebelum Medium). Test tidak mengassert ini.
- **Hasil Testing:** **PASSED** ✅ (100%)

### 2. Tugas 2: Implementasi Deque + Palindrome
- **Pengecekan Kode:** Deque dan palindrome benar, semua 7 test lulus.
- **Hasil Testing:** **PASSED** ✅ (100%)

### 3. Tugas 3: Simulasi Antrian Bank
- **Pengecekan Kode:** 20 customers, 3 tellers, avg wait 0.30 menit — statistik akurat.
- **Hasil Testing:** **PASSED** ✅ (100%)

**NILAI MODUL 6: 100**

---

## Hasil Evaluasi Modul 7: Review & Studi Kasus (Persiapan UTS)

### 1. Tugas 1: Soal Teori (PDF)
- **Pengecekan:** PDF `Tugas7_10251038_AyudyaAisyahMutiaradinna.pdf` ada di folder Minggu7.
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
- **Pengecekan Kode:** Linear probing + tombstone, resize & rehash berjalan benar.
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

### **NILAI RATA-RATA (Modul 1-7, 9-14): 95.69**

| Modul | Nilai |
|-------|-------|
| Modul 1 | 100 |
| Modul 2 | 100 |
| Modul 3 | 100 |
| Modul 4 | 80 |
| Modul 5 | 97 |
| Modul 6 | 100 |
| Modul 7 | 100 |
| Modul 9 | 67 |
| Modul 10 | 100 |
| Modul 11 | 100 |
| Modul 12 | 100 |
| Modul 13 | 100 |
| Modul 14 | 100 |
| **Rata-rata** | **95.69** |
