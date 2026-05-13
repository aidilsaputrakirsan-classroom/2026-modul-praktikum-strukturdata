# Laporan Evaluasi Terperinci - Praktikum Struktur Data

---

## Data Mahasiswa
- **Nama:** A. Suci Maharani P
- **NIM:** 10251011
- **Kelas:** Struktur Data A
- **GitHub Username:** `strukturdata-a-Asuci-Maharani`

---

## Hasil Evaluasi Modul 1: Pengantar Struktur Data

### 1. Tugas 1: Pengembangan ADT Counter
- **Pengecekan Kode:**
  - Metode penambahan positif (`add`) dan pengurangannya merangkum nilai absolut untuk minimum nilai Counter.
- **Hasil Testing Codelab:** **PASSED** ✅ (100%)

### 2. Tugas 2: Pengembangan ADT Stack - Aplikasi Reverse String
- **Pengecekan Kode:**
  - Method `reverse_string` dengan peramuan `stack.pop()` bekerja dengan baik, fungsional *print_stack* juga diekspose secara memadai.
- **Hasil Testing Codelab:** **PASSED** ✅ (100%)

### 3. Tugas 3: Analisis Kompleksitas Lanjutan
- **Tabel Analisis Kompleksitas & Jawaban:**
  - Menyimulasikan jawaban pemrosesan jumlah runtime (n³, log n). Penjelasannya mendasar, misal perumpamaan logis bahwa O(n²) untuk 6000 mahasiswa tak efisien bila dibandingkan langsung satu sama lain (6000x6000), ini membuktikan mahasiswi memahami implementasi O-Notation di kehidupan nyata.
- **Hasil Testing Codelab:** **PASSED** ✅ (100%)

**NILAI MODUL 1: 100**

---

## Hasil Evaluasi Modul 2: Array

### 1. Tugas 1: Pengembangan MyArray
- **Pengecekan Kode:**
  - Pengecekan limit (IndexError) di `find_min` dan `find_max` cukup aman untuk array kosong.
- **Hasil Testing Codelab:** **PASSED** ✅ (100%)

### 2. Tugas 2: Aplikasi Array - Statistik Data
- **Pengecekan Kode:**
  - Array tracking pada `second_largest` dan modifikasi `remove_duplicates` O(n²) berjalan.
- **Hasil Testing Codelab:** **PASSED** ✅ (100%)

### 3. Tugas 3: Aplikasi Matrix - Operasi Dasar
- **Pengecekan Kode:**
  - `add_matrices`, skalar, dan transpos terkonsep dengan apik secara sintaksis.
- **Hasil Testing Codelab:** **PASSED** ✅ (100%)

**NILAI MODUL 2: 100**

---

## Hasil Evaluasi Modul 3: Single Linked List

### 1. Tugas 1: Implementasi Single Linked List
- **Pengecekan Kode:**
  - Terdapat duplikasi `__init__` (baris 248 mendefinisikan ulang `__init__` di dalam class), namun Python menggunakan definisi terakhir dan semua method yang relevan tetap berfungsi karena method baru (reverse, find_min, dll) berada di bawah blok duplikasi tersebut.
  - `reverse()`, `find_min()`, `find_max()`, `remove_value()`, dan `to_list()` semuanya diimplementasikan dengan benar dan lulus semua test assertions.
- **Hasil Testing:** **PASSED** ✅ (100%)

### 2. Tugas 2: Aplikasi Polynomial
- **Pengecekan Kode:**
  - Implementasi `Polynomial` lengkap dengan `add_term()` yang menjaga urutan pangkat dan menangani merge koefisien. `evaluate()`, `degree()`, dan `add_polynomials()` semuanya benar. Display menggunakan format `3x^2 + 2x^1 + 5x^0`.
- **Hasil Testing:** **PASSED** ✅ (100%)

### 3. Tugas 3: Aplikasi Music Playlist
- **Pengecekan Kode:**
  - Semua fitur playlist diimplementasikan dengan lengkap dan benar. `add_song()`, `remove_song()`, `play()`, `next_song()`, `current_song()`, `total_duration()`, `song_count()`, `display()`, `search_by_artist()` semuanya berfungsi dengan baik.
- **Hasil Testing:** **PASSED** ✅ (100%)

**NILAI MODUL 3: 100**

---

## Hasil Evaluasi Modul 4: Double Linked List & Circular Linked List

### 1. Tugas 1: Implementasi Double Linked List
- **Pengecekan Kode:**
  - `reverse()` diimplementasikan dengan baik (swap prev/next + swap head/tail secara eksplisit). `find_min()`, `find_max()` menggunakan traversal O(n). `swap_nodes()` menukar data berdasarkan posisi. `is_palindrome()` menggunakan kondisi `while left != right and left.prev != right` yang lebih aman.
- **Hasil Testing:** **PASSED** ✅ (100%)

### 2. Tugas 2: Aplikasi Text Editor Undo/Redo
- **Pengecekan Kode:**
  - Implementasi clean dan sederhana. `type_text()` menghapus redo history dengan `self.current.next = None`. `undo()`/`redo()` berfungsi dengan benar. `show_history()` menandai state aktif dengan ` <== current`.
- **Hasil Testing:** **PASSED** ✅ (100%)

### 3. Tugas 3: Aplikasi Round Robin Scheduler
- **Pengecekan Kode:**
  - Implementasi CLL Round Robin Scheduler lengkap dan benar. `add_process()`, `remove_process()` (menangani semua kasus termasuk head), `execute_one_cycle()`, dan `run()` semuanya berjalan dengan tepat menghasilkan timeline yang benar.
- **Hasil Testing:** **PASSED** ✅ (100%)

**NILAI MODUL 4: 100**

---

## Hasil Evaluasi Modul 5: Stack

### 1. Tugas 1: Pengembangan Stack dengan Method Baru
- **Pengecekan Kode:** Semua method baru benar dan lulus test.
- **Hasil Testing:** **PASSED** ✅ (100%)

### 2. Tugas 2: Konversi dan Evaluasi Ekspresi
- **Pengecekan Kode:** `infix_to_postfix()` benar termasuk right-associativity `^`. `evaluate_postfix()` dan `calculate()` semua benar.
- **Hasil Testing:** **PASSED** ✅ (100%)

### 3. Tugas 3: Aplikasi Browser History
- **Pengecekan Kode:** Dua stack browser history berjalan benar.
- **Hasil Testing:** **PASSED** ✅ (100%)

**NILAI MODUL 5: 100**

---

## Hasil Evaluasi Modul 6: Queue

### 1. Tugas 1: Implementasi Priority Queue
- **Pengecekan Kode:** Priority Queue dengan insertion sort, semua test lulus.
- **Hasil Testing:** **PASSED** ✅ (100%)

### 2. Tugas 2: Implementasi Deque + Palindrome
- **Pengecekan Kode:** Deque benar. Palindrome checker menggunakan Deque lokal — semua 7 test lulus.
- **Hasil Testing:** **PASSED** ✅ (100%)

### 3. Tugas 3: Simulasi Antrian Bank
- **Pengecekan Kode:** 20 customers, 3 tellers — semua terlayani. Statistik benar.
- **Hasil Testing:** **PASSED** ✅ (100%)

**NILAI MODUL 6: 100**

---

## Hasil Evaluasi Modul 7: Review & Studi Kasus (Persiapan UTS)

### 1. Tugas 1: Soal Teori (PDF)
- **Pengecekan:** PDF `Tugas7_10251011_A.Suci Maharani.P.pdf` ada di folder Modul-7.
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
- **Pengecekan Kode:** Traversal (preorder, postorder, level-order), height, dan leaves berjalan benar (5 test pass). Namun method `successor()` memanggil `self._find_min_node(node.right)` yang tidak didefinisikan di class BST → `AttributeError` saat Test 4/5.
- **Hasil Testing Terminal:** **FAILED** ❌ — `AttributeError: 'BST' object has no attribute '_find_min_node'` (60%)

### 2. Tugas 2: Sistem Phonebook dengan BST
- **Pengecekan Kode:** `list_all()` memanggil `self._inorder(self.root, result)` namun `result` tidak didefinisikan sebelumnya (kemungkinan typo `esult = []`). Test 1 (size) lulus, kemudian crash.
- **Hasil Testing Terminal:** **FAILED** ❌ — `NameError: name 'result' is not defined` (0%)

### 3. Tugas 3: Analisis Performa BST
- **Hasil Testing Terminal:** **PASSED** ✅ (100%)

**NILAI MODUL 10: 53** *((60+0+100)/3 ≈ 53)*

---

### **NILAI RATA-RATA (Modul 1-7, 9, 10): 91.11**

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
| Modul 10 | 53 |
| **Rata-rata** | **91.11** |
