# Laporan Evaluasi Terperinci - Praktikum Struktur Data

---

## Data Mahasiswa
- **Nama:** Arya Cahya Nugraha
- **NIM:** 10251023
- **Kelas:** Struktur Data A
- **GitHub Username:** `strukturdata-a-AryaCahyaNugraha22`

---

## Hasil Evaluasi Modul 1: Pengantar Struktur Data

### 1. Tugas 1: Pengembangan ADT Counter
- **Pengecekan Kode:**
  - Metode operasional `add()`, `subtract()`, dan `multiply()` berfungsi secara matematis dengan baik. Kondisi penjagaan _underflow_ `<0` berhasil di-construct memakai kontrol boolean rasional.
- **Hasil Testing Codelab:** **PASSED** ✅ (100%)

### 2. Tugas 2: Pengembangan ADT Stack - Aplikasi Reverse String
- **Pengecekan Kode:**
  - `Stack` terimplementasi natural menggunakan List. String reversal logic dengan `while not stack.is_empty(): result += stack.pop()` sesuai *flowchart*.
- **Hasil Testing Codelab:** **PASSED** ✅ (100%)

### 3. Tugas 3: Analisis Kompleksitas Lanjutan
- **Tabel Analisis Kompleksitas & Jawaban:**
  - Klasifikasi struktur _Big-O Notation_ (konstan, linier, kuadratik, logaritmik, kubik) sangat lugas. Definisi `O(n^3)` (delapan juta operasi) dan `O(log n)` (pembagian menjadi setengah) akurat. Argumentasi jawaban logis untuk kasus sistem nyata media sosial.
- **Hasil Testing Codelab:** **PASSED** ✅ (100%)

**NILAI MODUL 1: 100**

---

## Hasil Evaluasi Modul 2: Array

### 1. Tugas 1: Pengembangan MyArray
- **Pengecekan Kode:**
  - `insert_front` / `delete_front` di-approach menggunakan operasi list `insert(0)` dan `pop(0)`. In-place swap *reverse* array dibuat manual `while left < right` pertukaran variable tanpa function `reverse()` bawaan. Sangat bagus!
- **Hasil Testing Codelab:** **PASSED** ✅ (100%)

### 2. Tugas 2: Aplikasi Array - Statistik Data
- **Pengecekan Kode:**
  - Logika pengecekan _second largest_ elegan `-inf`. Algoritma untuk menghapus duplikasi loop di *remove_duplicates* dilakukan O(n^2) komparasi manual secara *pure* (bukan *built-in module module/set*). 
- **Hasil Testing Codelab:** **PASSED** ✅ (100%)

### 3. Tugas 3: Aplikasi Matrix - Operasi Dasar
- **Pengecekan Kode:**
  - Analisa dimensi saat `add_matrices` diaplikasikan dengan kokoh, menghindari kegagalan Index bila matrix *non-identik*. Fungsi simetri direpresentasi membandingkan *matrix* primer secara _boolean equal_ ke transponenya.
- **Hasil Testing Codelab:** **PASSED** ✅ (100%)

**NILAI MODUL 2: 100**


---

## Hasil Evaluasi Modul 3: Single Linked List

### 1. Tugas 1: Implementasi Single Linked List
- **Pengecekan Kode:**
  - `reverse()`, `find_min()`, `find_max()`, `remove_value()`, dan `to_list()` terimplementasi dengan benar dan berjalan sesuai test cases. File berisi duplikasi kode (Node dan LinkedList didefinisikan berulang kali karena penggabungan beberapa file Praktikum), namun Python menggunakan definisi kelas terakhir yang valid.
- **Hasil Testing:** **PASSED** ✅ (100%)

### 2. Tugas 2: Aplikasi Polynomial
- **Pengecekan Kode:**
  - **Tidak sesuai requirement:** File "Tugas Terstruktur 2" yang dikumpulkan berisi kode Praktikum 3.2 (Insert/Delete di Posisi), bukan Aplikasi Polynomial. Mahasiswa mengumpulkan file Praktikum sebagai Tugas Terstruktur.
- **Hasil Testing:** **FAILED** ❌ (Bukan implementasi Polynomial — file salah)

### 3. Tugas 3: Aplikasi Music Playlist
- **Pengecekan Kode:**
  - **Tidak sesuai requirement:** File "Tugas Terstruktur 3" yang dikumpulkan berisi kode Praktikum 3.3 (Operasi Tambahan), bukan Aplikasi Music Playlist. Mahasiswa mengumpulkan file Praktikum sebagai Tugas Terstruktur.
- **Hasil Testing:** **FAILED** ❌ (Bukan implementasi Music Playlist — file salah)

**NILAI MODUL 3: 60**

---

## Hasil Evaluasi Modul 4: Double Linked List & Circular Linked List

### 1. Tugas 1: Implementasi Double Linked List
- **Pengecekan Kode:** Semua method DLL (`reverse`, `find_min`, `find_max`, `swap_nodes`, `is_palindrome`, `to_list`) diimplementasikan dengan benar. Semua assert test lulus.
- **Hasil Testing:** **PASSED** ✅ (100%)

### 2. Tugas 2: Aplikasi Text Editor Undo/Redo
- **Pengecekan Kode:** `type_text`, `append_text`, `undo`, `redo`, dan branching semua berjalan benar. `show_history()` menampilkan posisi `^current` dengan tepat.
- **Hasil Testing:** **PASSED** ✅ (100%)

### 3. Tugas 3: Aplikasi Round Robin Scheduler
- **Pengecekan Kode:** Logika rotasi Round Robin **benar** — proses bergantian per quantum (A→B→C→A→B selesai→C selesai→A selesai). Namun setelah semua proses selesai, program tidak berhenti — infinite loop `"Time 12-12: Process X completed"` karena `remove_process` tidak menghapus node dari circular list dengan benar.
- **Hasil Testing:** **INFINITE LOOP** ⚠️ (50%) — Rotasi benar, tapi terminasi gagal.

**NILAI MODUL 4: 83** *(T1:100 + T2:100 + T3:50) / 3 ≈ 83*

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
- **Pengecekan Kode:** Priority Queue benar, semua test lulus.
- **Hasil Testing:** **PASSED** ✅ (100%)

### 2. Tugas 2: Implementasi Deque + Palindrome
- **Pengecekan Kode:** Deque dan palindrome benar, semua 7 test lulus.
- **Hasil Testing:** **PASSED** ✅ (100%)

### 3. Tugas 3: Simulasi Antrian Bank
- **Pengecekan Kode:** Simulasi benar, statistik akurat.
- **Hasil Testing:** **PASSED** ✅ (100%)

**NILAI MODUL 6: 100**

---

## Hasil Evaluasi Modul 7: Review & Studi Kasus (Persiapan UTS)

### 1. Tugas 1: Soal Teori (PDF)
- **Pengecekan:** Tidak ada PDF di folder minggu 7. File `Tugas Terstruktur 1_10251023_Arya Cahya Nugraha.py` berisi jawaban teori (Pilihan Ganda) dalam format .py.
- **Hasil:** **TIDAK VALID** ❌ (0%) — tugas teori harus berupa PDF

### 2. Tugas 2: Sistem Manajemen Perpustakaan
- **Pengecekan Kode:** `Tugas Terstruktur 2` berisi implementasi Library. Semua test lulus.
- **Hasil Testing Terminal:** **PASSED** ✅ (100%)

**NILAI MODUL 7: 50** *((0+100)/2)*

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

### 1. Tugas 1: Pengembangan Graph Class (file: `Tugas Terstruktur 1`)
- **Pengecekan Kode:** Implementasi method baru lengkap, 7 test case lulus.
- **Hasil Testing Terminal:** **PASSED** ✅ (100%)

### 2. Tugas 2: Sistem Navigasi Kampus (file: `Tugas Terstruktur 2`)
- **Pengecekan Kode:** BFS route, shortest route (270m A→E), dan all_reachable berjalan benar.
- **Hasil Testing Terminal:** **PASSED** ✅ (100%)

### 3. Tugas 3: Analisis Kompleksitas Graph (file: `Tugas Terstruktur 3`)
- **Pengecekan Kode:** Perbandingan adjacency list vs matrix berjalan untuk 5 konfigurasi.
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

- **Catatan:** Hanya mengumpulkan file **Praktikum** (`Tugas Praktikum 13.1/2/3` berisi kode Praktikum 13.1/2/3), **tidak ada Tugas Terstruktur** 13.1/13.2/13.3.

**NILAI MODUL 13: 0**

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

### **NILAI RATA-RATA (Modul 1-7, 9-14): 73.85**

| Modul | Nilai |
|-------|-------|
| Modul 1 | 100 |
| Modul 2 | 100 |
| Modul 3 | 60 |
| Modul 4 | 83 |
| Modul 5 | 100 |
| Modul 6 | 100 |
| Modul 7 | 50 |
| Modul 9 | 67 |
| Modul 10 | 100 |
| Modul 11 | 100 |
| Modul 12 | 0 |
| Modul 13 | 0 |
| Modul 14 | 100 |
| **Rata-rata** | **73.85** |

*Catatan: M7 T1 dikumpulkan sebagai .py bukan PDF. Modul 12 tidak dikumpulkan.*
