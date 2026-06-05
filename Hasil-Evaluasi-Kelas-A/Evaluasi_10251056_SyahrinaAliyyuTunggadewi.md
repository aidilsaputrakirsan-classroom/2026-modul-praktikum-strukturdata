# Laporan Evaluasi Terperinci - Praktikum Struktur Data

---

## Data Mahasiswa
- **Nama:** Syahrina Aliyyu Tunggadewi
- **NIM:** 10251056
- **Kelas:** Struktur Data A
- **GitHub Username:** `strukturdata-a-SyahrinaAliyyuTunggadewi`

---

## Hasil Evaluasi Modul 1: Pengantar Struktur Data

### 1. Tugas 1: Pengembangan ADT Counter
- **Pengecekan Kode:**
  - Metode penambahan `add` dikodekan dengan baik tanpa redundansi iterasi. Kontrol untuk error aritmatika minimal nol telah divalidasi tepat melalui baris `else: self._value = 0` sehingga kalkulasi `subtract()` sepenuhnya mulus.
- **Hasil Testing Codelab:** **PASSED** ✅ (100%)

### 2. Tugas 2: Pengembangan ADT Stack - Aplikasi Reverse String
- **Pengecekan Kode:**
  - `print_stack()` mengandalkan *built-in list behavior* sementara fungsi balik `reverse_string` mengaplikan format Stack sesuai kriteria, *push*-*pop* karakter dilalui mulus menggunakan tipe list array sederhana.
- **Hasil Testing Codelab:** **PASSED** ✅ (100%)

### 3. Tugas 3: Analisis Kompleksitas Lanjutan
- **Tabel Analisis Kompleksitas & Jawaban:**
  - Argumen Big-O dirumuskan jelas, mahasiswa juga membandingkan waktu kompleksitas dalam skala real, misal bahwa `1 juta operasi bagi O(n)` tersebut sudah cukup mudah bagi komputer modern namun untuk jumlah miliaran disarankan "optimasi paralel". Sangat kritis dan mantap!  
- **Hasil Testing Codelab:** **PASSED** ✅ (100%)

**NILAI MODUL 1: 100**

---

## Hasil Evaluasi Modul 2: Array

### 1. Tugas 1: Pengembangan MyArray
- **Pengecekan Kode:**
  - Operasi struktur `insert_front` dieksekusi dengan metode built-in namun masih terisolir dengan baik. Fungsi max & min dideklarasikan cermat menggunakan pengisian sementara indeks ke-0 dan diteruskan dengan pemotongan pembacaan `for el in self._elements[1:]`. Pertukaran pemutaran dinamis (reverse swap) tersusun efisien menggunakan rasio tengah `.size() // 2`.
- **Hasil Testing Codelab:** **PASSED** ✅ (100%)

### 2. Tugas 2: Aplikasi Array - Statistik Data
- **Pengecekan Kode:**
  - Pada pembentukan pencarian angka terbesar kedua, implementasi `None` digunakan dengan elegan sebagai flag sementara ganda. Fungsi range dideklarasikan matang. Metode eliminasi terduplikasi `remove_duplicates()` membandingkan nilai sebelum dimasukkan (O(n²)) dengan fungsionalitas mulus.
- **Hasil Testing Codelab:** **PASSED** ✅ (100%)

### 3. Tugas 3: Aplikasi Matrix - Operasi Dasar
- **Pengecekan Kode:**
  - Metode permutasi matrix dimodelkan secara komprehensif. Syarat pengecekan operasi diagonal pun disertakan tanpa kendala. Nested loop kalkulasi matematika `add_matrices` dikendalikan sangat tanggap pada setiap koordinat *row-column*.
- **Hasil Testing Codelab:** **PASSED** ✅ (100%)

**NILAI MODUL 2: 100**

---

## Hasil Evaluasi Modul 3: Single Linked List

### 1. Tugas 1: Implementasi Single Linked List
- **Pengecekan Kode:**
  - Semua method wajib (reverse, find_min, find_max, remove_value, to_list) diimplementasikan dengan benar. Algoritma reverse menggunakan tiga pointer (prev, current, next_node) yang efisien O(n). find_min/find_max menggunakan traversal linear dengan tracking nilai min/max. remove_value menangani kasus head maupun tengah/akhir dengan tepat.
- **Hasil Testing:** **PASSED** ✅ (100%)

### 2. Tugas 2: Aplikasi Polinomial
- **Pengecekan Kode:**
  - Kelas Polynomial menggunakan linked list terurut dari pangkat tertinggi ke terendah. Method add_term menangani penggabungan koefisien pada pangkat yang sama. evaluate dan degree diimplementasikan dengan benar. add_polynomials membangun polynomial baru dari dua polynomial input.
- **Hasil Testing:** **PASSED** ✅ (100%)

### 3. Tugas 3: Aplikasi Music Playlist
- **Pengecekan Kode:**
  - Kelas Playlist dengan SongNode lengkap. Method add_song, remove_song, play, next_song, current_song, total_duration, song_count, display, dan search_by_artist diimplementasikan dengan benar dan berfungsi baik. search_by_artist menggunakan case-insensitive comparison.
- **Hasil Testing:** **PASSED** ✅ (100%)

**NILAI MODUL 3: 100**

---

## Hasil Evaluasi Modul 4: Double Linked List & Circular Linked List

### 1. Tugas 1: Implementasi Double Linked List
- **Pengecekan Kode:**
  - Implementasi DLL lengkap dengan head dan tail. Method reverse, find_min, find_max, swap_nodes diimplementasikan dengan benar. Namun terdapat bug kritis pada method is_palindrome: baris `left = left.next` dan `right = right.prev` berada di luar while loop (indentasi salah), menyebabkan pointer tidak pernah diperbarui dan program masuk infinite loop saat method dipanggil.
- **Hasil Testing:** **FAILED** ❌ - is_palindrome menyebabkan infinite loop (timeout), program terhenti paksa setelah 10 detik.

### 2. Tugas 2: Aplikasi Text Editor Undo/Redo
- **Pengecekan Kode:**
  - Implementasi TextEditor menggunakan DLL dengan StateNode. Method type_text, append_text, undo, redo, get_text, can_undo, can_redo, dan show_history semuanya berfungsi dengan benar. Branching (menghapus history redo saat mengetik setelah undo) ditangani dengan tepat.
- **Hasil Testing:** **PASSED** ✅ (100%)

### 3. Tugas 3: Aplikasi Round Robin Scheduler
- **Pengecekan Kode:**
  - Implementasi RoundRobinScheduler menggunakan Circular Linked List. add_process, remove_process, execute_one_cycle, run, display_queue, dan get_statistics diimplementasikan dengan benar. Eksekusi rotasi proses berjalan sesuai algoritma Round Robin.
- **Hasil Testing:** **PASSED** ✅ (100%)

**NILAI MODUL 4: 90**

---

## Hasil Evaluasi Modul 5: Stack

### 1. Tugas 1: Pengembangan Stack dengan Method Baru
- **Pengecekan Kode:** Semua method baru (`get_min`, `get_max`, `clear`, `to_list`, `copy`, `reverse`) diimplementasikan dengan benar. Semua test lulus.
- **Hasil Testing:** **PASSED** ✅ (100%)

### 2. Tugas 2: Konversi dan Evaluasi Ekspresi
- **Pengecekan Kode:** `infix_to_postfix()` benar termasuk right-associativity `^`. `evaluate_postfix()` dan `calculate()` juga benar. Semua test lulus.
- **Hasil Testing:** **PASSED** ✅ (100%)

### 3. Tugas 3: Aplikasi Browser History
- **Pengecekan Kode:** `BrowserHistory` menggunakan dua stack (`back_stack`, `forward_stack`). `visit()`, `back()`, `forward()`, dan `current_page()` diimplementasikan dengan benar.
- **Hasil Testing:** **PASSED** ✅ (100%)

**NILAI MODUL 5: 100**

---

## Hasil Evaluasi Modul 6: Queue

### 1. Tugas 1: Implementasi Priority Queue
- **Pengecekan Kode:** `PriorityQueue` diimplementasikan dengan benar. Enqueue mempertahankan urutan prioritas. FIFO untuk prioritas sama terjaga. Semua test lulus.
- **Hasil Testing:** **PASSED** ✅ (100%)

### 2. Tugas 2: Implementasi Deque + Palindrome
- **Pengecekan Kode:** `Deque` dengan `add_front`, `add_rear`, `remove_front`, `remove_rear` benar. `is_palindrome()` menggunakan Deque lokal dengan benar. Semua 7 test lulus.
- **Hasil Testing:** **PASSED** ✅ (100%)

### 3. Tugas 3: Simulasi Antrian Bank
- **Pengecekan Kode:** 20 customers, 3 tellers, avg wait 0.30 menit — statistik akurat dan benar. Semua customer terlayani.
- **Hasil Testing:** **PASSED** ✅ (100%)

**NILAI MODUL 6: 100**

---

## Hasil Evaluasi Modul 7: Review & Studi Kasus (Persiapan UTS)

### 1. Tugas 1: Soal Teori (PDF)
- **Pengecekan:** PDF `Tugas7_10251056_Syahrina Aliyyu Tunggadewi.pdf` ada di folder Minggu 7.
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
- **Pengecekan Kode:** Berhasil menghitung height skewed tree n=10000 tanpa RecursionError. Tabel timing tercetak lengkap.
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
- **Pengecekan Kode:** Semua method baru lengkap, 7 test case lulus.
- **Hasil Testing Terminal:** **PASSED** ✅ (100%)

### 2. Tugas 2: Sistem Navigasi Kampus
- **Pengecekan Kode:** BFS route, shortest route (270m A→E), all_reachable berjalan benar.
- **Hasil Testing Terminal:** **PASSED** ✅ (100%)

### 3. Tugas 3: Analisis Kompleksitas Graph
- **Pengecekan Kode:** Perbandingan adjacency list vs matrix untuk 5 konfigurasi lengkap.
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

### **NILAI RATA-RATA (Modul 1-7, 9-13): 99.17**

| Modul | Nilai |
|-------|-------|
| Modul 1 | 100 |
| Modul 2 | 100 |
| Modul 3 | 100 |
| Modul 4 | 90 |
| Modul 5 | 100 |
| Modul 6 | 100 |
| Modul 7 | 100 |
| Modul 9 | 100 |
| Modul 10 | 100 |
| Modul 11 | 100 |
| Modul 12 | 100 |
| Modul 13 | 100 |
| **Rata-rata** | **99.17** |
