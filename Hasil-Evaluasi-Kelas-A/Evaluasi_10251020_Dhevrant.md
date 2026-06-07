# Laporan Evaluasi Terperinci - Praktikum Struktur Data

---

## Data Mahasiswa
- **Nama:** Dhevrant Zhelynov Malelo
- **NIM:** 10251020
- **Kelas:** Struktur Data A
- **GitHub Username:** `strukturdata-a-Dhevrant`

---

## Hasil Evaluasi Modul 1: Pengantar Struktur Data

### 1. Tugas 1: Pengembangan ADT Counter
- **Pengecekan Kode:**
  - Metode penambahan `add()` dan perkalian `multiply()` berjalan mulus. Penggunaan block kondisional untuk memastikan nilai minimum `subtract()` berjalan dengan semestinya.
- **Hasil Testing Codelab:** **PASSED** ✅ (100%)

### 2. Tugas 2: Pengembangan ADT Stack - Aplikasi Reverse String
- **Pengecekan Kode:**
  - Fungsi Stack aman, dan iterasi `while not stack.is_empty()` diterapkan sesuai flowchart pembalikan string.
- **Hasil Testing Codelab:** **PASSED** ✅ (100%)

### 3. Tugas 3: Analisis Kompleksitas Lanjutan
- **Tabel Analisis Kompleksitas & Jawaban:**
  - **Minor Note:** Ada sedikit anomali/bias teoritis dalam penulisan notasi Big-O asimtotik. Notasi komputasi yang dituliskan adalah *O(2n)* (untuk O(n²)) dan *O(3n)* (untuk O(n³)), yang mana merepresentasikan konstanta alih-alih bentuk pemangkatan algoritma kuadratik/kubik. Namun pemahaman tentang algoritma secara bahasa (seperti lambatnya n³) dapat dimengerti dengan baik.
- **Hasil Testing Codelab:** **PASSED** ✅ (100%)

**NILAI MODUL 1: 90**

---

## Hasil Evaluasi Modul 2: Array

### 1. Tugas 1: Pengembangan MyArray
- **Pengecekan Kode:**
  - Proses modifikasi array in-place `reverse` menggunakan fitur native Python yang solid (`self._elements.reverse()`). Linear counting and minimum/maximum logic terkomposisi dengan sangat baik.
- **Hasil Testing Codelab:** **PASSED** ✅ (100%)

### 2. Tugas 2: Aplikasi Array - Statistik Data
- **Pengecekan Kode:**
  - Penggunaan `average` yang divalidasi manual untuk list elemen berjumlah 0 (zero division escape rule). Perhitungan nilai `second_largest` dan modifikasi array terhindar dari duplikat berjalan apik.
- **Hasil Testing Codelab:** **PASSED** ✅ (100%)

### 3. Tugas 3: Aplikasi Matrix - Operasi Dasar
- **Pengecekan Kode:**
  - Modul matriks diselesaikan dengan *logic testing* untuk perbandingan `matrix[i][j] != matrix[j][i]` saat validasi *is_symmetric*. Efisien tanpa harus load *transpose* yang berat.
- **Hasil Testing Codelab:** **PASSED** ✅ (100%)

**NILAI MODUL 2: 100**


---

## Hasil Evaluasi Modul 3: Single Linked List

### 1. Tugas 1: Implementasi Single Linked List
- **Pengecekan Kode:**
  - Implementasi `reverse()` menggunakan iterasi prev/current/next_node yang solid. `find_min()` dan `find_max()` menangani kasus empty dengan `raise ValueError`. `remove_value()` menangani kasus head dan middle dengan bersih menggunakan variabel `previous`. `to_list()` mengonversi seluruh isi list ke Python list dengan tepat. Kode terstruktur rapi dengan dokumentasi docstring yang lengkap.
- **Hasil Testing:** **PASSED** ✅ (100%)

### 2. Tugas 2: Aplikasi Polynomial
- **Pengecekan Kode:**
  - `Polynomial` menggunakan linked list berurutan eksponen menurun. `add_term()` memasukkan term di posisi yang benar dan menggabungkan term dengan pangkat sama. `add_polynomials()` bekerja dengan mengiterasi kedua polynomial dan memanggil `add_term()` untuk menggabungkan koefisien secara otomatis.
- **Hasil Testing:** **PASSED** ✅ (100%)

### 3. Tugas 3: Aplikasi Music Playlist
- **Pengecekan Kode:**
  - Semua method playlist (`add_song`, `remove_song`, `play`, `next_song`, `current_song`, `total_duration`, `song_count`, `search_by_artist`) diimplementasikan dengan benar dan bersih. Navigasi lagu menggunakan pointer `current` yang diperbarui saat `play()` dan `next_song()`.
- **Hasil Testing:** **PASSED** ✅ (100%)

**NILAI MODUL 3: 100**

---

## Hasil Evaluasi Modul 4: Double Linked List & Circular Linked List

### 1. Tugas 1: Implementasi Double Linked List
- **Pengecekan Kode:**
  - `reverse()` menggunakan pendekatan swap prev/next setiap node secara in-place, kemudian memperbarui head dan tail. `swap_nodes()` menelusuri list dua kali untuk menemukan node di posisi yang diminta. `is_palindrome()` menggunakan dua pointer dari kedua ujung. Semua method lengkap dengan docstring dan error handling.
- **Hasil Testing:** **PASSED** ✅ (100%)

### 2. Tugas 2: Aplikasi Text Editor Undo/Redo
- **Pengecekan Kode:**
  - `TextEditor` menggunakan DLL state-based. `type_text()` memutus redo chain sebelum menyisipkan state baru (branching). `undo()` dan `redo()` berfungsi dengan memeriksa `prev`/`next`. `show_history()` menampilkan seluruh chain dengan marker `^current` yang tepat.
- **Hasil Testing:** **PASSED** ✅ (100%)

### 3. Tugas 3: Aplikasi Round Robin Scheduler
- **Pengecekan Kode:**
  - `RoundRobinScheduler` menggunakan Circular Linked List dengan manajemen head yang tepat. `remove_process()` menangani kasus single-node, head-node, dan non-head. `execute_one_cycle()` memisahkan tracking waktu mulai/akhir dari metode `run()` dan mengembalikan info detail. Output timeline sesuai ekspektasi.
- **Hasil Testing:** **PASSED** ✅ (100%)

**NILAI MODUL 4: 100**

---

## Hasil Evaluasi Modul 5: Stack

### 1. Tugas 1: Pengembangan Stack dengan Method Baru
- **Pengecekan Kode:** Semua method benar, semua test lulus.
- **Hasil Testing:** **PASSED** ✅ (100%)

### 2. Tugas 2: Konversi dan Evaluasi Ekspresi
- **Pengecekan Kode:** `infix_to_postfix()` benar termasuk right-associativity `^`. Semua test lulus.
- **Hasil Testing:** **PASSED** ✅ (100%)

### 3. Tugas 3: Aplikasi Browser History
- **Pengecekan Kode:** Browser history dengan dua stack, semua operasi benar.
- **Hasil Testing:** **PASSED** ✅ (100%)

**NILAI MODUL 5: 100**

---

## Hasil Evaluasi Modul 6: Queue

### 1. Tugas 1: Implementasi Priority Queue
- **Pengecekan Kode:** Priority Queue benar, semua test lulus.
- **Hasil Testing:** **PASSED** ✅ (100%)

### 2. Tugas 2: Implementasi Deque + Palindrome
- **Pengecekan Kode:** Deque benar. Palindrome checker — semua 7 test lulus.
- **Hasil Testing:** **PASSED** ✅ (100%)

### 3. Tugas 3: Simulasi Antrian Bank
- **Pengecekan Kode:** Simulasi 20 customers, 3 tellers — semua terlayani. Statistik akurat.
- **Hasil Testing:** **PASSED** ✅ (100%)

**NILAI MODUL 6: 100**

---

## Hasil Evaluasi Modul 7: Review & Studi Kasus (Persiapan UTS)

### 1. Tugas 1: Soal Teori (PDF)
- **Pengecekan:** PDF `tugas1_10251020_DhevrantZhelynovMalelo.pdf` ada di folder Minggu7.
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
- **Pengecekan Kode:** Menggunakan `sys.setrecursionlimit(20000)` — berhasil menghitung height skewed tree n=10000 tanpa RecursionError.
- **Hasil Testing Terminal:** **PASSED** ✅ (100%)

**NILAI MODUL 9: 100**

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
- **Pengecekan Kode:** Semua method baru lengkap, 7 test case lulus termasuk count_paths A→E=4 dan disconnected detection.
- **Hasil Testing Terminal:** **PASSED** ✅ (100%)

### 2. Tugas 2: Sistem Navigasi Kampus
- **Pengecekan Kode:** BFS route, shortest route (270m A→E), dan all_reachable berjalan benar.
- **Hasil Testing Terminal:** **PASSED** ✅ (100%)

### 3. Tugas 3: Analisis Kompleksitas Graph
- **Pengecekan Kode:** Perbandingan adjacency list vs matrix untuk 5 konfigurasi (sparse & dense) lengkap.
- **Hasil Testing Terminal:** **PASSED** ✅ (100%)

**NILAI MODUL 11: 100**

---

## Hasil Evaluasi Modul 12: Algoritma Searching

### 1. Tugas 1: Binary Search Lanjutan
- **Pengecekan Kode:** `lower_bound`, `upper_bound`, `count_occurrences`, `find_closest`, `search_rotated` semua benar.
- **Hasil Testing Terminal:** **PASSED** ✅ (100%)

### 2. Tugas 2: Hash Table - Open Addressing
- **Pengecekan Kode:** Linear probing dengan tombstone, resize & rehash bekerja sempurna.
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

### **NILAI RATA-RATA (Modul 1-7, 9-14): 99.23**

| Modul | Nilai |
|-------|-------|
| Modul 1 | 90 |
| Modul 2 | 100 |
| Modul 3 | 100 |
| Modul 4 | 100 |
| Modul 5 | 100 |
| Modul 6 | 100 |
| Modul 7 | 100 |
| Modul 9 | 100 |
| Modul 10 | 100 |
| Modul 11 | 100 |
| Modul 12 | 100 |
| Modul 13 | 100 |
| Modul 14 | 100 |
| **Rata-rata** | **99.23** |
