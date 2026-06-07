# Laporan Evaluasi Terperinci - Praktikum Struktur Data

---

## Data Mahasiswa
- **Nama:** Andre Adi Ruhaya
- **NIM:** 10251114
- **Kelas:** Struktur Data A
- **GitHub Username:** `strukturdata-a-Andre10251114`

---

## Hasil Evaluasi Modul 1: Pengantar Struktur Data

### 1. Tugas 1: Pengembangan ADT Counter
- **Pengecekan Kode:**
  - Fungsi beroperasi stabil secara menyeluruh. Struktur kondisional disempurnakan dengan penanganan batas nol yang efisien: `if self._value < 0: self._value = 0`.
- **Hasil Testing Codelab:** **PASSED** ✅ (100%)

### 2. Tugas 2: Pengembangan ADT Stack - Aplikasi Reverse String
- **Pengecekan Kode:**
  - Metode `pop` dan `peek` terlindungi dengan *safety check* `if not self.is_empty():` yang menghindarkan program dari `IndexError`. Logika eksekusi berjalan stabil pada kalkulasi LIFO *string*.
- **Hasil Testing Codelab:** **PASSED** ✅ (100%)

### 3. Tugas 3: Analisis Kompleksitas Lanjutan
- **Tabel Analisis Kompleksitas & Jawaban:**
  - Tabel kompleksitas ditulis sesuai. Jawaban atas pertanyaan-pertanyaan spesifik tentang efisiensi pencarian maksimum dan kelemahan O(n²) diuraikan dengan argumentasi nyata terhadapat sistem pengguna jaringan.
- **Hasil Testing Codelab:** **PASSED** ✅ (100%)

**NILAI MODUL 1: 100**

---

## Hasil Evaluasi Modul 2: Array

### 1. Tugas 1: Pengembangan MyArray
- **Pengecekan Kode:**
  - Fitur `insert_front` dan `delete_front` memakai metode `insert(0, ...)` dan `pop(0)` bawaan array *list* dengan benar. Sayangnya baris komentar *TODO* tidak dihilangkan, namun tidak memengaruhi jalannya fungsi fundamental.
- **Hasil Testing Codelab:** **PASSED** ✅ (100%)

### 2. Tugas 2: Aplikasi Array - Statistik Data
- **Pengecekan Kode:**
  - Kode program *error* (ModuleNotFoundError) di awal lantaran nama *file* pustaka import di-set menjadi _"tugas1_10251114_Andre"_ padahal penamaan aktualnya _"Tugas1_10251114_Andre_Adi_Ruhaya"_. Setelah disunting, kode statistik tereksekusi mulus tanpa hambatan.
- **Hasil Testing Codelab:** **PASSED** ✅ (90%) - Pengurangan 10 poin atas *error* penamaan modul.

### 3. Tugas 3: Aplikasi Matrix - Operasi Dasar
- **Pengecekan Kode:**
  - Validasi asimetris dirangkai lugas menggunakan klausa pengujian `ValueError` dimensi di metode penjumlahan. Matrix berjalan sempurna.
- **Hasil Testing Codelab:** **PASSED** ✅ (100%)

**NILAI MODUL 2: 96**

---

## Hasil Evaluasi Modul 3: Single Linked List

### 1. Tugas 1: Implementasi Single Linked List
- **Pengecekan Kode:**
  - `reverse()`, `find_min()`, `find_max()`, `remove_value()`, dan `to_list()` diimplementasikan dengan benar. Semua assert test berhasil dilalui dengan baik.
- **Hasil Testing:** **PASSED** ✅ (100%)

### 2. Tugas 2: Aplikasi Polinomial
- **Pengecekan Kode:**
  - `add_polynomials()` menggunakan copy-and-add, namun `add_term()` tidak menggabungkan koefisien saat pangkat sudah ada dalam hasil intermediate. Output menampilkan `3x^2 + 2x^2 + 6x + 8` alih-alih `5x^2 + 6x + 8` — bug minor display pada penggabungan koefisien. Test `evaluate(1)` tetap lulus secara numerik.
- **Hasil Testing:** **PASSED** ✅ (90%) — Test numerik lulus namun representasi polinomial hasil penjumlahan tidak dimerge dengan benar.

### 3. Tugas 3: Aplikasi Music Playlist
- **Pengecekan Kode:**
  - Semua operasi playlist (`add_song`, `remove_song`, `play`, `next_song`, `current_song`, `total_duration`, `song_count`, `search_by_artist`) berjalan dengan benar secara fungsional. Tidak menggunakan assert-based test (hanya print demo), namun output menampilkan hasil yang sesuai ekspektasi.
- **Hasil Testing:** **PASSED** ✅ (90%) — Fungsional benar namun tidak menggunakan assert statements untuk validasi otomatis.

**NILAI MODUL 3: 90**

---

## Hasil Evaluasi Modul 4: Double Linked List & Circular Linked List

### 1. Tugas 1: Implementasi Double Linked List
- **Pengecekan Kode:**
  - Semua method DLL (`reverse`, `find_min`, `find_max`, `swap_nodes`, `is_palindrome`, `to_list`) benar. `reverse()` menggunakan teknik tukar pointer yang tepat. Semua assert test lulus.
- **Hasil Testing:** **PASSED** ✅ (100%)

### 2. Tugas 2: Aplikasi Text Editor Undo/Redo
- **Pengecekan Kode:**
  - Semua operasi text editor berjalan dengan benar. `type_text()`, `append_text()`, `undo()`, `redo()`, dan branching semuanya lulus. `show_history()` menampilkan history dengan marker `^current`.
- **Hasil Testing:** **PASSED** ✅ (100%)

### 3. Tugas 3: Aplikasi Round Robin Scheduler
- **Pengecekan Kode:**
  - Terdapat **bug kritis pada `remove_process`**: setelah proses selesai (remaining=0), node tidak benar-benar dihapus dari circular list sehingga proses yang sudah "selesai" tetap ada di antrian. Ini menyebabkan **infinite loop** — program terus mencetak `"Time 12-12: Process B/C/A completed"` tanpa batas waktu. Eksekusi dihentikan paksa oleh timeout 10 detik.
- **Hasil Testing:** **FAILED** ❌ — Infinite loop akibat bug pada remove_process: proses yang sudah selesai tidak dihapus dari circular list dengan benar. TIMEOUT.

**NILAI MODUL 4: 70**

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
- **Pengecekan Kode:** File T2 tidak ditemukan di folder Minggu 6 — tidak ada file Tugas2 yang dikumpulkan.
- **Hasil Testing:** **TIDAK DIKUMPULKAN** ❌ (0%)

### 3. Tugas 3: Simulasi Antrian Bank
- **Pengecekan Kode:** File T3 tidak ditemukan di folder Minggu 6 — tidak ada file Tugas3 yang dikumpulkan.
- **Hasil Testing:** **TIDAK DIKUMPULKAN** ❌ (0%)

**NILAI MODUL 6: 33** *(T1:100 + T2:0 + T3:0) / 3 ≈ 33*

---

## Hasil Evaluasi Modul 7: Review & Studi Kasus (Persiapan UTS)

### 1. Tugas 1: Soal Teori (PDF)
- **Pengecekan:** Tidak ada file PDF di folder minggu7.
- **Hasil:** **TIDAK DIKUMPULKAN** ❌ (0%)

### 2. Tugas 2: Sistem Manajemen Perpustakaan
- **Pengecekan Kode:** File berisi definisi class saja tanpa blok test/main — tidak ada kode yang dieksekusi saat dijalankan. Output kosong, tidak ada assert yang diuji.
- **Hasil Testing Terminal:** **TIDAK ADA TEST** ❌ (0%)

**NILAI MODUL 7: 0** *((0+0)/2)*

---

## Hasil Evaluasi Modul 9: Tree & Binary Tree

### 1. Tugas 1: BinaryTree Class
- **Pengecekan Kode:** File berisi definisi class tanpa test execution — output kosong.
- **Hasil Testing Terminal:** **TIDAK ADA TEST** ❌ (0%)

### 2. Tugas 2: Expression Tree
- **Pengecekan Kode:** File berisi definisi class tanpa test execution — output kosong.
- **Hasil Testing Terminal:** **TIDAK ADA TEST** ❌ (0%)

### 3. Tugas 3: Analisis Kompleksitas Tree
- **Pengecekan Kode:** `height()` rekursif tanpa `sys.setrecursionlimit` → `RecursionError` pada skewed tree.
- **Hasil Testing Terminal:** **FAILED** ❌ (0%)

**NILAI MODUL 9: 0**

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
- **Pengecekan:** Filename `Tugas1_10251114_Andre_Adi_Ruhaya,py` menggunakan koma `,` bukan titik `.` sebelum `py` — file tidak memiliki ekstensi `.py` yang valid. Saat dijalankan via interpreter Python, semua 7 test case lulus.
- **Hasil Testing Terminal:** **PASSED** ✅ (85%) — penalti -15 karena tanpa ekstensi `.py`

### 2. Tugas 2: Sistem Navigasi Kampus
- **Pengecekan Kode:** BFS route, shortest route (270m A→E), all_reachable berjalan benar.
- **Hasil Testing Terminal:** **PASSED** ✅ (100%)

### 3. Tugas 3: Analisis Kompleksitas Graph
- **Pengecekan Kode:** Perbandingan adjacency list vs matrix lengkap.
- **Hasil Testing Terminal:** **PASSED** ✅ (100%)

**NILAI MODUL 11: 95** *((85+100+100)/3 ≈ 95)*

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
- **Pengecekan Kode:** `RankingSystem` (`sort_by_nama`, `sort_by_nilai_akhir`, `sort_by_grade_then_nama`, `get_top_n`, `grade_distribution`) benar. *(test harness diganti dataset custom; method `RankingSystem` benar — divalidasi dengan test standar)*
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

### **NILAI RATA-RATA (Modul 1-7, 9-14): 75.69**

| Modul | Nilai | Keterangan |
|-------|-------|------------|
| Modul 1 | 100 | |
| Modul 2 | 96 | |
| Modul 3 | 90 | |
| Modul 4 | 70 | |
| Modul 5 | 100 | |
| Modul 6 | 33 | T2/T3 tidak dikumpulkan |
| Modul 7 | 0 | T1 tidak ada PDF, T2 tidak ada kode test |
| Modul 9 | 0 | T1/T2 class-only (no test), T3 RecursionError |
| Modul 10 | 100 | |
| Modul 11 | 95 | T1 filename `,py` bukan `.py` (-15) |
| Modul 12 | 100 | |
| Modul 13 | 100 |
| Modul 14 | 100 |
| **Rata-rata** | **75.69** | |
