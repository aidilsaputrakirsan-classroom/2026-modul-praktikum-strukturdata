# Laporan Evaluasi Terperinci - Praktikum Struktur Data

---

## Data Mahasiswa
- **Nama:** Muhammad Fajri Ikhsan
- **NIM:** 10251068
- **Kelas:** Struktur Data A
- **GitHub Username:** `strukturdata-a-Fajri-ITK`

---

## Hasil Evaluasi Modul 1: Pengantar Struktur Data

### 1. Tugas 1: Pengembangan ADT Counter
- **Pengecekan Kode:**
  - Metode `subtract()` disusun dengan struktur *if/elif* yang memagari operasi decrement agar hasil akhir absolut tidak pernah berada di bawah nilai nol. 
- **Hasil Testing Codelab:** **PASSED** ✅ (100%)

### 2. Tugas 2: Pengembangan ADT Stack - Aplikasi Reverse String
- **Pengecekan Kode:**
  - Metode pembalikan (*reverse_string*) beraksi valid dengan metode pengumpulan per karakter kembali (*string concatenation*) setelah dilempar satu per satu (*pop*) memastikan skema komputas LIFO berjalan konsisten.
- **Hasil Testing Codelab:** **PASSED** ✅ (100%)

### 3. Tugas 3: Analisis Kompleksitas Lanjutan
- **Tabel Analisis Kompleksitas & Jawaban:**
  - Ketajaman analisa nampak kuat di bagian algoritma skala besar `O(n²)`. Contoh *real case* pencocokan satu juta pengguna di platform digital memperterang konsekuensi dari *nested loop* secara faktual.
- **Hasil Testing Codelab:** **PASSED** ✅ (100%)

**NILAI MODUL 1: 100**

---

## Hasil Evaluasi Modul 2: Array

### 1. Tugas 1: Pengembangan MyArray
- **Pengecekan Kode:**
  - Operasi manipulasi standar terenkapsulasi secara wajar. Fungsi `reverse` cukup minimalis dan langsung mengandalkan *built-in function* `reverse()` dasar Python, efisien secara fungsi internal namun perlu ditekankan pada konsep algoritmanya (`two pointer`) kedepannya.
- **Hasil Testing Codelab:** **PASSED** ✅ (100%)

### 2. Tugas 2: Aplikasi Array - Statistik Data
- **Pengecekan Kode:**
  - `remove_duplicates` diformulasikan kreatif mengandalkan properti struktur data *dictionary keys* (`dict.fromkeys()`) untuk pemastian keunikan elemen, suatu bentuk solusi yang langka di level perkenalan pemrograman, memperlihatkan usaha eksploratif eksternal.
- **Hasil Testing Codelab:** **PASSED** ✅ (100%)

### 3. Tugas 3: Aplikasi Matrix - Operasi Dasar
- **Pengecekan Kode:**
  - Penggunaan *list comprehension* dominan digunakan di setiap blok metode tugas matriks terstruktur (`add_matrices`, `transpose_matrix`, dll), merefleksikan alur yang padat alias *one-liner Pythonic way*. Sangat mahir memanfaatkan fungsionalitas lanjutan seperti eksekusi *zip()*.
- **Hasil Testing Codelab:** **PASSED** ✅ (100%)

**NILAI MODUL 2: 100**

---

## Hasil Evaluasi Modul 3: Single Linked List

### 1. Tugas 1: Implementasi Single Linked List
- **Pengecekan Kode:**
  - Semua method wajib (reverse, find_min, find_max, remove_value, to_list) diimplementasikan dengan benar. Algoritma reverse menggunakan tiga pointer efisien. find_min/find_max dengan traversal linear O(n). remove_value menangani semua kasus dengan tepat. Display menggunakan format sedikit berbeda (tanpa spasi sebelum "-> NULL") namun fungsionalitas tetap benar.
- **Hasil Testing:** **PASSED** ✅ (100%)

### 2. Tugas 2: Aplikasi Polinomial
- **Pengecekan Kode:**
  - Polynomial diimplementasikan dengan linked list terurut. add_term menangani insert terurut dan penggabungan koefisien. Display menampilkan format `3x^2 + 2x^1 + 5` (untuk x^0 ditampilkan sebagai konstanta saja). evaluate dan add_polynomials berfungsi dengan benar.
- **Hasil Testing:** **PASSED** ✅ (100%)

### 3. Tugas 3: Aplikasi Music Playlist
- **Pengecekan Kode:**
  - Playlist dengan SongNode diimplementasikan lengkap. Semua method (add_song, remove_song, play, next_song, current_song, total_duration, song_count, display, search_by_artist) diimplementasikan dan berfungsi dengan benar. Format display menggunakan separator 30 karakter '='.
- **Hasil Testing:** **PASSED** ✅ (100%)

**NILAI MODUL 3: 100**

---

## Hasil Evaluasi Modul 4: Double Linked List & Circular Linked List

### 1. Tugas 1: Implementasi Double Linked List
- **Pengecekan Kode:**
  - DLL dengan head dan tail diimplementasikan lengkap. reverse, find_min, find_max, swap_nodes (tukar data), is_palindrome semuanya diimplementasikan dengan benar. is_palindrome menggunakan two-pointer dari head dan tail dengan terminasi loop yang tepat.
- **Hasil Testing:** **PASSED** ✅ (100%)

### 2. Tugas 2: Aplikasi Text Editor Undo/Redo
- **Pengecekan Kode:**
  - TextEditor menggunakan DLL dengan StateNode. Semua method (type_text, append_text, undo, redo, get_text, can_undo, can_redo, show_history) berfungsi dengan benar. Branching saat mengetik setelah undo menghapus future history dengan tepat. show_history menampilkan chain dengan marker ^current di akhir node saat ini.
- **Hasil Testing:** **PASSED** ✅ (100%)

### 3. Tugas 3: Aplikasi Round Robin Scheduler
- **Pengecekan Kode:**
  - RoundRobinScheduler menggunakan CLL. execute_one_cycle mengeksekusi quantum dan melakukan rotasi head ke proses berikutnya dengan benar. remove_process menghapus node dari CLL dengan tepat. Output timeline menunjukkan rotasi round-robin yang akurat antar Process A, B, C.
- **Hasil Testing:** **PASSED** ✅ (100%)

**NILAI MODUL 4: 100**

---

## Hasil Evaluasi Modul 5: Stack

### 1. Tugas 1: Pengembangan Stack dengan Method Baru
- **Pengecekan Kode:** Semua method baru (`get_min`, `get_max`, `clear`, `to_list`, `copy`, `reverse`) diimplementasikan dengan benar. Semua test lulus.
- **Hasil Testing:** **PASSED** ✅ (100%)

### 2. Tugas 2: Konversi dan Evaluasi Ekspresi
- **Pengecekan Kode:** `infix_to_postfix()` **tidak menangani right-associativity `^`** — `2^3^2` menghasilkan `23^2^` (left-assoc) bukan `232^^` (right-assoc). Selain itu, `back_stack` pada `BrowserHistory` tidak digunakan dengan benar untuk menampilkan halaman terakhir saat `back()`. Test `^` gagal.
- **Hasil Testing:** **HAMPIR LULUS** ⚠️ (80%)

### 3. Tugas 3: Aplikasi Browser History
- **Pengecekan Kode:** `BrowserHistory` menggunakan dua stack. Logika dasar `visit()`, `back()`, `forward()` benar. Semua test lulus.
- **Hasil Testing:** **PASSED** ✅ (100%)

**NILAI MODUL 5: 93** *(T1:100 + T2:80 + T3:100) / 3 ≈ 93*

---

## Hasil Evaluasi Modul 6: Queue

### 1. Tugas 1: Implementasi Priority Queue
- **Pengecekan Kode:** `PriorityQueue` diimplementasikan dengan benar. Enqueue mempertahankan urutan prioritas. Semua test lulus.
- **Hasil Testing:** **PASSED** ✅ (100%)

### 2. Tugas 2: Implementasi Deque + Palindrome
- **Pengecekan Kode:** `Deque` benar. Namun `is_palindrome()` tidak mengembalikan nilai apapun (return `None`) — fungsi melakukan pengecekan namun tidak ada statement `return True/False`. Akibatnya semua pemanggilan `is_palindrome()` mengembalikan `None` bukan boolean.
- **Hasil Testing:** **FAILED** ❌ — `is_palindrome()` selalu return `None` (50%)

### 3. Tugas 3: Simulasi Antrian Bank
- **Pengecekan Kode:** Semua 20 customers terlayani, namun rata-rata waktu tunggu negatif — bug logika pada perhitungan `waiting_time`. `service_start_time` dihitung sebelum customer tiba sehingga menghasilkan selisih negatif.
- **Hasil Testing:** **BUG LOGIKA** ⚠️ (60%)

**NILAI MODUL 6: 70** *(T1:100 + T2:50 + T3:60) / 3 ≈ 70*

---

## Hasil Evaluasi Modul 7: Review & Studi Kasus (Persiapan UTS)

### 1. Tugas 1: Soal Teori (PDF)
- **Pengecekan:** PDF `TUGAS7_10251068_MuhammadFajriIkhsan.pdf` ada di folder minggu7.
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

### Semua Tugas
- **Pengecekan:** Tidak ditemukan folder atau file Modul 12 di repositori.
- **Hasil:** **TIDAK DIKUMPULKAN** ❌ (0%)

**NILAI MODUL 12: 0**

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

### **NILAI RATA-RATA (Modul 1-7, 9-13): 85.83**

| Modul | Nilai |
|-------|-------|
| Modul 1 | 100 |
| Modul 2 | 100 |
| Modul 3 | 100 |
| Modul 4 | 100 |
| Modul 5 | 93 |
| Modul 6 | 70 |
| Modul 7 | 100 |
| Modul 9 | 67 |
| Modul 10 | 100 |
| Modul 11 | 100 |
| Modul 12 | 0 |
| Modul 13 | 100 |
| **Rata-rata** | **85.83** |

*Catatan: Modul 12 tidak dikumpulkan.*
