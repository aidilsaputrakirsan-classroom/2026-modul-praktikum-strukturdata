# Laporan Evaluasi Terperinci - Praktikum Struktur Data

---

## Data Mahasiswa
- **Nama:** Muhammad Zennin Feriatta Dzakwan
- **NIM:** 10251050
- **Kelas:** Struktur Data A
- **GitHub Username:** `strukturdata-a-Zennin2511`

---

## Hasil Evaluasi Modul 1: Pengantar Struktur Data

### 1. Tugas 1: Pengembangan ADT Counter
- **Pengecekan Kode:**
  - Fungsi kalkulatif tambahan seperti `add` dan `multiply` diterapkan dengan validasi tipe. `subtract()` memiliki *if-elif conditional* unik yang akurat: `elif n > 0 and self.value < n: self.value = 0` memastikan angka nol absolut.
- **Hasil Testing Codelab:** **PASSED** ✅ (100%)

### 2. Tugas 2: Pengembangan ADT Stack - Aplikasi Reverse String
- **Pengecekan Kode:**
  - Metode LIFO dikerjakan utuh. `reverse_string` mengonsumsi *push* dalam `for loop` serta *pop* dalam `while loop` yang optimal membentuk ulang string dari stack.
- **Hasil Testing Codelab:** **PASSED** ✅ (100%)

### 3. Tugas 3: Analisis Kompleksitas Lanjutan
- **Tabel Analisis Kompleksitas & Jawaban:**
  - Jawaban memuat deskripsi spesifik tentang loop konstan Big-O. Saran untuk memperbaiki limitasi O(n^2) dan perbandingan logaritmik disajikan terstruktur, menunjukkan pemahaman algoritma tingkat mendalam.
- **Hasil Testing Codelab:** **PASSED** ✅ (100%)

**NILAI MODUL 1: 100**

---

## Hasil Evaluasi Modul 2: Array

### 1. Tugas 1: Pengembangan MyArray
- **Pengecekan Kode:**
  - *Slicing* standar digantikan dengan komparasi limit. Operasi *reverse* in-place digunakan secara terpusat `self._elements.reverse()`.
- **Hasil Testing Codelab:** **PASSED** ✅ (100%)

### 2. Tugas 2: Aplikasi Array - Statistik Data
- **Pengecekan Kode:**
  - Proses identifikasi *second largest value* ditangani rapi. *Duplication check* dikalkulasikan melalui instansi baru Array `unique.search(val)` yang menekan ambiguitas data.
- **Hasil Testing Codelab:** **PASSED** ✅ (100%)

### 3. Tugas 3: Aplikasi Matrix - Operasi Dasar
- **Pengecekan Kode:**
  - Logika komparasi *transpose* secara implisit dipanggil di parameter *is_symmetric*. *Multiply Scalar* divisualisasikan rapi dengan `new_row.append(val * scalar)`.
- **Hasil Testing Codelab:** **PASSED** ✅ (100%)

**NILAI MODUL 2: 100**

---

## Hasil Evaluasi Modul 3: Single Linked List

### 1. Tugas 1: Implementasi Single Linked List
- **Pengecekan Kode:**
  - Implementasi `reverse()`, `find_min()`, `find_max()`, `remove_value()`, dan `to_list()` semuanya benar dan lengkap. Validasi posisi pada `insert_at_position()` dan `delete_at_position()` menggunakan pola `if current is None` yang lebih robust dibanding pengecekan `size()` berulang.
- **Hasil Testing:** **PASSED** ✅ (100%)

### 2. Tugas 2: Aplikasi Polinomial
- **Pengecekan Kode:**
  - `Polynomial` menggunakan `TermNode`. Terdapat bug pada `add_term()`: saat menambahkan term dengan pangkat sama ke head (e.g., 2x^2 ke existing 3x^2), kondisi `self.head.exponent < exponent` bernilai False, lalu masuk else — namun `current` dimulai dari head dan pengecekan `current.next.exponent == exponent` melewati perbandingan dengan head itu sendiri, sehingga term baru ditambahkan sebagai node terpisah. Akibatnya `P1 + P2` ditampilkan sebagai `3x^2 + 2x^2 + 6x + 8` (bukan `5x^2 + 6x + 8`). Test `evaluate(1) == 19` tetap lolos karena nilai numeriknya benar (3+2+6+8=19), namun representasi display polynomial tidak akurat.
- **Hasil Testing:** **PASSED** ✅ (test lolos) — namun terdapat bug display pada penjumlahan term dengan pangkat sama di head

**NILAI TUGAS 2 MODUL 3: 90** (minor display bug pada add_polynomials)

### 3. Tugas 3: Aplikasi Music Playlist
- **Pengecekan Kode:**
  - Semua operasi playlist diimplementasikan lengkap dan benar: `song_count()`, `total_duration()`, `play()`, `next_song()`, `search_by_artist()`, dan `remove_song()`. Format display menggunakan separator panjang 30 karakter yang konsisten.
- **Hasil Testing:** **PASSED** ✅ (100%)

**NILAI MODUL 3: 90**

---

## Hasil Evaluasi Modul 4: Double Linked List & Circular Linked List

### 1. Tugas 1: Implementasi Double Linked List
- **Pengecekan Kode:**
  - `DoublyLinkedList` menggunakan `DNode`. Method `reverse()`, `find_min()`, `find_max()`, `swap_nodes()`, dan `is_palindrome()` diimplementasikan dengan benar. Output display menggunakan spasi sebelum `DLL:` (minor cosmetic), tidak memengaruhi fungsionalitas.
- **Hasil Testing:** **PASSED** ✅ (100%)

### 2. Tugas 2: Aplikasi Text Editor Undo/Redo
- **Pengecekan Kode:**
  - `TextEditor` berbasis DLL berfungsi dengan baik. `type_text()`, `append_text()`, `undo()`, `redo()`, dan branching semuanya benar. Display history tidak ditampilkan (tidak ada kode di bagian display, hanya ada di test case terpisah), namun semua assert test lolos.
- **Hasil Testing:** **PASSED** ✅ (100%)

### 3. Tugas 3: Aplikasi Round Robin Scheduler
- **Pengecekan Kode:**
  - `RoundRobinScheduler` menggunakan Circular Linked List. `add_process()`, `remove_process()`, dan `execute_one_cycle()` diimplementasi dengan benar — termasuk perpindahan `self.head = self.head.next` setelah setiap quantum. Timeline interleaving Round Robin benar. Namun `display_queue()` tidak memiliki logika tampilan (hanya menangani kasus kosong tanpa menampilkan proses yang ada), sehingga output "Initial Queue:" tidak menampilkan isi antrian.
- **Hasil Testing:** **PASSED** ✅ (test lolos) — namun `display_queue()` tidak menampilkan isi antrian (minor bug)

**NILAI MODUL 4: 90**

---

## Hasil Evaluasi Modul 5: Stack

### 1. Tugas 1: Pengembangan Stack dengan Method Baru
- **Pengecekan Kode:** Semua method benar, semua test lulus.
- **Hasil Testing:** **PASSED** ✅ (100%)

### 2. Tugas 2: Konversi dan Evaluasi Ekspresi
- **Pengecekan Kode:** `infix_to_postfix()` benar termasuk right-associativity `^`. Semua test lulus.
- **Hasil Testing:** **PASSED** ✅ (100%)

### 3. Tugas 3: Aplikasi Browser History
- **Pengecekan Kode:** Browser history benar.
- **Hasil Testing:** **PASSED** ✅ (100%)

**NILAI MODUL 5: 100**

---

## Hasil Evaluasi Modul 6: Queue

### 1. Tugas 1: Implementasi Priority Queue
- **Pengecekan Kode:** Priority Queue benar. Catatan: FIFO untuk prioritas sama tidak terjaga (Normal sebelum Medium).
- **Hasil Testing:** **PASSED** ✅ (100%)

### 2. Tugas 2: Implementasi Deque + Palindrome
- **Pengecekan Kode:** Deque dan palindrome benar, semua 7 test lulus.
- **Hasil Testing:** **PASSED** ✅ (100%)

### 3. Tugas 3: Simulasi Antrian Bank
- **Pengecekan Kode:** Avg waiting time -6.15 menit (negatif) — bug logika pada perhitungan waktu. Semua 20 customers terlayani tapi statistik tidak valid.
- **Hasil Testing:** **BUG LOGIKA** ⚠️ (60%)

**NILAI MODUL 6: 87** *(T1:100 + T2:100 + T3:60) / 3 ≈ 87*

---

## Hasil Evaluasi Modul 7: Review & Studi Kasus (Persiapan UTS)

### 1. Tugas 1: Soal Teori (PDF)
- **Pengecekan:** PDF `Tugas7.1_10251050_M.ZenninFeriattaDzakwan.pdf` ada di folder Minggu7.
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
- **Pengecekan:** File `Tugas1_10251050.py` berisi kode **Praktikum 11.1: Representasi Graph**, bukan Tugas Terstruktur 11.1 (Pengembangan Graph Class). Header file: `PRAKTIKUM 11.1: Representasi Graph`.
- **Hasil:** **KONTEN SALAH** ❌ (0%) — praktikum dikumpulkan sebagai tugas

### 2. Tugas 2: Sistem Navigasi Kampus
- **Pengecekan:** File `Tugas2_10251050.py` berisi kode **Praktikum 11.2: Implementasi BFS dan DFS**. Header file: `PRAKTIKUM 11.2: Implementasi BFS dan DFS`.
- **Hasil:** **KONTEN SALAH** ❌ (0%) — praktikum dikumpulkan sebagai tugas

### 3. Tugas 3: Analisis Kompleksitas Graph
- **Pengecekan:** File `Tugas3_10251050.py` berisi kode **Praktikum 11.3: BFS/DFS pada Adjacency Matrix**. Header file: `PRAKTIKUM 11.3: BFS/DFS pada Adjacency Matrix`.
- **Hasil:** **KONTEN SALAH** ❌ (0%) — praktikum dikumpulkan sebagai tugas

**NILAI MODUL 11: 0** *(semua T1/T2/T3 berisi kode Praktikum bukan Tugas Terstruktur)*

---

## Hasil Evaluasi Modul 12: Algoritma Searching

### 1. Tugas 1: Binary Search Lanjutan
- **Pengecekan Kode:** Semua fungsi (`lower_bound`, `upper_bound`, `count_occurrences`, `find_closest`, `search_rotated`) benar.
- **Hasil Testing Terminal:** **PASSED** ✅ (100%)

### 2. Tugas 2: Hash Table - Open Addressing
- **Pengecekan Kode:** Linear probing + tombstone, resize & rehash berjalan benar.
- **Hasil Testing Terminal:** **PASSED** ✅ (100%)

### 3. Tugas 3: Sistem Kamus Digital
- **Pengecekan Kode:** Dictionary dua arah dengan multiple translations berjalan benar.
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

### **NILAI RATA-RATA (Modul 1-7, 9-13): 86.17**

| Modul | Nilai |
|-------|-------|
| Modul 1 | 100 |
| Modul 2 | 100 |
| Modul 3 | 90 |
| Modul 4 | 90 |
| Modul 5 | 100 |
| Modul 6 | 87 |
| Modul 7 | 100 |
| Modul 9 | 67 |
| Modul 10 | 100 |
| Modul 11 | 0 |
| Modul 12 | 100 |
| Modul 13 | 100 |
| **Rata-rata** | **86.17** |

*Catatan: Modul 11 T1/T2/T3 semua file berisi kode Praktikum 11.1/11.2/11.3 (file salah) — M11=0.*
