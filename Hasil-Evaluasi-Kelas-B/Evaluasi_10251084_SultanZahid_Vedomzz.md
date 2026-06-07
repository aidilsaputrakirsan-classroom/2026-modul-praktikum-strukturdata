# 📝 Laporan Evaluasi Terperinci - Praktikum Struktur Data

---

## 👤 Data Mahasiswa
- **Nama:** Sultan Zahid
- **NIM:** 10251084
- **Kelas:** Struktur Data B
- **GitHub Username:** `strukturdata-b-Vedomzz`

---

## 🥇 Hasil Evaluasi Modul 1: Pengantar Struktur Data

### 1. Tugas 1: Pengembangan ADT Counter
- **Pengecekan Kode:**
  - Metode penambahan class objek *add* hingga *multiply* ditambahkan dengan _base code function_ aman yang tidak mem-bypass batas operasionalnya (Nilai minimum 0).
- **Hasil Testing Terminal:** **PASSED** ✅ (100%)

### 2. Tugas 2: Pengembangan ADT Stack - Aplikasi Reverse String
- **Pengecekan Kode:**
  - Sistem pengurutan Array yang dikonversi menjadi perilaku *Stack LIFO* bekerja sebagaimana mestinya ketika _reverse_string_ dites dari parameter *string* ke string terbalik.
- **Hasil Testing Terminal:** **PASSED** ✅ (100%)

### 3. Tugas 3: Analisis Kompleksitas Lanjutan
- **Tabel Analisis Kompleksitas & Jawaban:**
  - Runtime time processing *code efficiency* tercetak untuk rekursi analisis Big-O algoritma kompleks secara berderet pada simulasi eksekusi profiler.
- **Hasil Testing Terminal:** **PASSED** ✅ (100%)

**✨ NILAI MODUL 1: 100 ✨**

---

## 🥈 Hasil Evaluasi Modul 2: Array

### 1. Tugas 1: Pengembangan MyArray
- **Pengecekan Kode:**
  - Fungsi seperti `insert_front()`, *delete*, pencarian min/max dan *count* pada item data direkayasa memanipulasi _in-place array_ iterables.
- **Hasil Testing Terminal:** **PASSED** ✅ (100%)

### 2. Tugas 2: Aplikasi Array - Statistik Data
- **Pengecekan Kode:**
  - Algoritma memisahkan (*filter*) duplikat indeks dengan inisiasi logika dan komputasi statistikal list angka (average, rentang terbesar/range, sum) beroperasi dengan benar.
- **Hasil Testing Terminal:** **PASSED** ✅ (100%)

### 3. Tugas 3: Aplikasi Matrix - Operasi Dasar
- **Pengecekan Kode:**
  - Penambahan perulangan (`add_matrices()`), fungsi transpose mengubah axis i & j, lalu boolean filter is_symmetric berjalan mulus dalam evaluasinya.
- **Hasil Testing Terminal:** **PASSED** ✅ (100%)

**✨ NILAI MODUL 2: 100 ✨**

---

## 🥉 Hasil Evaluasi Modul 3: Single Linked List

### 1. Tugas 1: Pengembangan LinkedList
- **Pengecekan Kode:** Implementasi `reverse()`, `find_min()`, `find_max()`, `remove_value()`, dan `to_list()` sudah benar. Seluruh method dari praktikum juga diimplementasikan lengkap (insert, delete, search, get, count, clear, get_head, get_tail). Logika tiga-pointer untuk reverse benar.
- **Hasil Testing Terminal:** **PASSED** ✅

### 2. Tugas 2: Aplikasi Linked List - Polynomial
- **Pengecekan Kode:** `add_term` mengurutkan berdasarkan pangkat secara benar dan menangani penggabungan koefisien sama pangkat. `display` memformat polinom dengan tampilan lebih bersih (tanpa `x^0`, `x^1`). `add_polynomials` menggunakan merge-style loop yang efisien.
- **Hasil Testing Terminal:** **PASSED** ✅

### 3. Tugas 3: Aplikasi Linked List - Music Playlist
- **Pengecekan Kode:** Semua method diimplementasikan dengan benar. Minor: method `display` tidak mencetak baris "Total: n songs, duration" (variabel dihitung tapi tidak diprint). Namun semua assert test cases lolos karena pengujian tidak memeriksa output display secara langsung.
- **Hasil Testing Terminal:** **PASSED** ✅

**✨ NILAI MODUL 3: 100 ✨**

---

## 🏅 Hasil Evaluasi Modul 4: Double & Circular Linked List

### 1. Tugas 1: Pengembangan Double Linked List
- **Pengecekan Kode:** Semua method DLL diimplementasikan dengan benar: `reverse()` menukar prev/next in-place lalu swap head/tail; `find_min/max()` benar; `swap_nodes()` hanya tukar data (sesuai spesifikasi); `is_palindrome()` menggunakan dua pointer dari kedua ujung dengan kondisi terminasi yang tepat.
- **Hasil Testing Terminal:** **PASSED** ✅

### 2. Tugas 2: Aplikasi DLL - Text Editor Undo/Redo
- **Pengecekan Kode:** `type_text` menghapus redo history dengan `current.next = None` sebelum buat node baru. `undo/redo` menggeser pointer current ke prev/next. Branching test lolos karena setelah undo lalu type_text baru, redo hilang.
- **Hasil Testing Terminal:** **PASSED** ✅

### 3. Tugas 3: Aplikasi CLL - Round Robin Scheduler
- **Pengecekan Kode:** Terdapat bug kritis pada `execute_one_cycle`: baris `return None` ditempatkan di luar kondisi (`if not self.head`) namun semua kode eksekusi setelahnya berada di dalam blok `if`, sehingga ketika antrian tidak kosong, fungsi selalu return None tanpa menjalankan proses apapun. Hal ini menyebabkan `run()` masuk infinite loop karena `head` tidak pernah diubah.
- **Hasil Testing Terminal:** **FAILED** ❌ (infinite loop)

**✨ NILAI MODUL 4: 90 ✨**

## 🔢 Hasil Evaluasi Modul 5: Stack

### 1. Tugas 1: Pengembangan Stack
- **Hasil Testing Terminal:** **PASSED** ✅ (100%)

### 2. Tugas 2: Infix → Postfix + Evaluasi Ekspresi
- **Pengecekan Kode:** Bug right-associativity `^`: `A^B^C` → `A B ^ C ^` (expected `A B C ^ ^`) ❌.
- **Hasil Testing Terminal:** **PARTIAL** ⚠️ (90%)

### 3. Tugas 3: Browser History
- **Hasil Testing Terminal:** **PASSED** ✅ (100%)

**✨ NILAI MODUL 5: 97 ✨**

---
## 🔢 Hasil Evaluasi Modul 6: Queue

### 1. Tugas 1: Priority Queue
- **Hasil Testing Terminal:** **PASSED** ✅ (100%)

### 2. Tugas 2: Deque + is_palindrome()
- **Hasil Testing Terminal:** **PASSED** ✅ (100%)

### 3. Tugas 3: Simulasi Antrian Bank
- **Pengecekan Kode:** Avg waiting time positif (0.30 menit), logika benar.
- **Hasil Testing Terminal:** **PASSED** ✅ (100%)

**✨ NILAI MODUL 6: 100 ✨**


---
## 🔢 Hasil Evaluasi Modul 7: Review & Studi Kasus (Persiapan UTS)

### 1. Tugas 1: Soal Teori (PDF)
- **Pengecekan:** PDF `Tugas7_10251084_Sultan Zahid.pdf` ada di `minggu 7/`.
- **Hasil:** **DIKUMPULKAN** ✅ (100%)

### 2. Tugas 2: Sistem Manajemen Perpustakaan
- **Pengecekan Kode:** `return_book()` mengembalikan `None` (bukan tuple `(success, fine)`) → `TypeError: cannot unpack non-iterable NoneType object` pada Test 5. Implementation tidak lengkap.
- **Hasil Testing Terminal:** **FAILED** ❌ (0%)

**✨ NILAI MODUL 7: 50 ✨**

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
- **Pengecekan Kode:** Tidak ada folder/file Modul 10 di repo.
- **Hasil Testing Terminal:** **TIDAK DIKUMPULKAN** ❌ (0%)

### 2. Tugas 2: Sistem Phonebook dengan BST
- **Pengecekan Kode:** Tidak ada folder/file Modul 10 di repo.
- **Hasil Testing Terminal:** **TIDAK DIKUMPULKAN** ❌ (0%)

### 3. Tugas 3: Analisis Performa BST
- **Pengecekan Kode:** Tidak ada folder/file Modul 10 di repo.
- **Hasil Testing Terminal:** **TIDAK DIKUMPULKAN** ❌ (0%)

**NILAI MODUL 10: 0**

---

## Hasil Evaluasi Modul 11: Graph

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

- **Catatan:** Hanya mengumpulkan file **Praktikum** (`praktikum13_code1/2/3`), tidak ada Tugas Terstruktur 13.

**NILAI MODUL 13: 0**

---

## Hasil Evaluasi Modul 14: Sorting Lanjutan

- Hanya mengumpulkan file Praktikum 14 (Implementasi Merge/Quick/Heap Sort), tidak ada Tugas Terstruktur 14.

**NILAI MODUL 14: 0**

---

### **NILAI RATA-RATA (Modul 1-7, 9-14): 69.54**

| Modul | Nilai |
|-------|-------|
| Modul 1 | 100 |
| Modul 2 | 100 |
| Modul 3 | 100 |
| Modul 4 | 90 |
| Modul 5 | 97 |
| Modul 6 | 100 |
| Modul 7 | 50 |
| Modul 9 | 67 |
| Modul 10 | 0 |
| Modul 11 | 100 |
| Modul 12 | 100 |
| Modul 13 | 0 |
| Modul 14 | 0 |
| **Rata-rata** | **69.54** |

*Penilaian dievaluasi secara statis-manual berdasarkan kode program dan divalidasi melalui eksekusi unit test satu per satu.*
