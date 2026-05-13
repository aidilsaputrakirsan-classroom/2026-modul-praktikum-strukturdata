# Laporan Evaluasi Terperinci - Praktikum Struktur Data

---

## Data Mahasiswa
- **Nama:** Rifat Adlyjuliandra
- **NIM:** 10251005
- **Kelas:** Struktur Data A
- **GitHub Username:** `strukturdata-a-rifatadlyjuliandra`

---

## Hasil Evaluasi Modul 1: Pengantar Struktur Data

### 1. Tugas 1: Pengembangan ADT Counter
- **Pengecekan Kode:**
  - Metode `add()`, `subtract()`, `multiply()` dan `__str__()` dibuat dengan benar dengan *exception* batas minimal nilai/negatif yang tepat.
- **Hasil Testing Codelab:** **PASSED** ✅ (100%)

### 2. Tugas 2: Pengembangan ADT Stack - Aplikasi Reverse String
- **Pengecekan Kode:**
  - `print_stack` & `clear` terimplementasi. 
  - Iterasi pop seluruh elemen *stack* untuk *reverse_string* berjalan sangat akurat.
- **Hasil Testing Codelab:** **PASSED** ✅ (100%)

### 3. Tugas 3: Analisis Kompleksitas Lanjutan
- **Tabel Analisis Kompleksitas & Jawaban:**
  - Seluruh algoritma O(n) hingga O(n³) dijelaskan dengan alasan yang tepat di blok *docstring*. Mahasiswa membuktikan performa rekursi `E` log(n) yang efisien dibarengi studi kasus linear `F` (O(n)).
- **Hasil Testing Codelab:** **PASSED** ✅ (100%)

**NILAI MODUL 1: 100**

---

## Hasil Evaluasi Modul 2: Array

### 1. Tugas 1: Pengembangan MyArray
- **Pengecekan Kode:**
  - `insert_front` / `delete_front` memanggil delegasi `insert_at` dengan indeks `0`, ini metode refaktorisasi kelas yang sangat rapi dan OOP-*friendly*.
- **Hasil Testing Codelab:** **PASSED** ✅ (100%)

### 2. Tugas 2: Aplikasi Array - Statistik Data
- **Pengecekan Kode:**
  - Menghitung rentang (range), rata-rata, penjumlahan, *second largest*, hingga *remove_duplicates* (O(n²)) beroperasi tanpa *bug*.
- **Hasil Testing Codelab:** **PASSED** ✅ (100%)

### 3. Tugas 3: Aplikasi Matrix - Operasi Dasar
- **Pengecekan Kode:**
  - Seluruh struktur iterasi multiline (*nested arrays*) digunakan dengan baik untuk penjumlahan, perkalian matriks-skalar, hingga properti matriks (diagonal & simetri).
- **Hasil Testing Codelab:** **PASSED** ✅ (100%)

**NILAI MODUL 2: 100**

---

## Hasil Evaluasi Modul 3: Single Linked List

### 1. Tugas 1: Implementasi Single Linked List
- **Pengecekan Kode:**
  - Implementasi method `reverse()`, `find_min()`, `find_max()`, `remove_value()`, dan `to_list()` secara logika sudah benar. Namun, file **terpotong/tidak lengkap**: bagian test section hanya berisi komentar `# Test to` tanpa assertion apapun (file berakhir di baris 135).
  - Saat dijalankan, program hanya menampilkan output `display()` dan berakhir tanpa error, namun juga tanpa validasi assertion.
- **Hasil Testing:** **PARTIAL** ⚠️ (90%) — Implementasi benar secara logika, namun test tidak lengkap

### 2. Tugas 2: Aplikasi Polynomial
- **Pengecekan Kode:**
  - Implementasi `Polynomial`, `add_term()`, `display()`, `evaluate()`, `degree()`, dan `add_polynomials()` secara logika sudah benar. Test section **terpotong** di baris 150 — assertion untuk `evaluate(1)==19` dan pesan PASSED tidak ada.
  - Saat dijalankan, degree dan evaluate berhasil divalidasi sebagian (`degree PASSED`, `evaluate PASSED`), namun test untuk penjumlahan polynomial tidak memiliki assertion akhir.
- **Hasil Testing:** **PARTIAL** ⚠️ (90%) — Implementasi benar, test tidak lengkap sepenuhnya

### 3. Tugas 3: Aplikasi Music Playlist
- **Pengecekan Kode:**
  - File memiliki **SyntaxError**: method `search_by_artist()` terpotong di baris 135 dengan kurung yang tidak ditutup (`result.append(current.title` — kurung `(` tidak pernah ditutup).
  - Saat dijalankan: `SyntaxError: '(' was never closed` — program tidak dapat dieksekusi sama sekali.
- **Hasil Testing:** **FAILED** ❌ (0%) — SyntaxError, file tidak lengkap/terpotong

**NILAI MODUL 3: 60**

---

## Hasil Evaluasi Modul 4: Double Linked List & Circular Linked List

### 1. Tugas 1: Implementasi Double Linked List
- **Pengecekan Kode:**
  - Semua method baru (`reverse()`, `find_min()`, `find_max()`, `swap_nodes()`, `is_palindrome()`, `to_list()`) diimplementasikan dengan benar dan lengkap. Tidak ada method praktikum yang menyebabkan konflik.
- **Hasil Testing:** **PASSED** ✅ (100%)

### 2. Tugas 2: Aplikasi Text Editor Undo/Redo
- **Pengecekan Kode:**
  - `type_text()` menghapus forward history dengan benar (iterasi node untuk cleanup memory). `undo()`/`redo()` berfungsi dengan baik. `show_history()` menampilkan history dengan posisi current.
- **Hasil Testing:** **PASSED** ✅ (100%)

### 3. Tugas 3: Aplikasi Round Robin Scheduler
- **Pengecekan Kode:**
  - Implementasi CLL Round Robin Scheduler lengkap dan benar. `execute_one_cycle()` mencetak langsung saat eksekusi (berbeda dari yang lain tapi fungsional). Timeline yang dihasilkan tepat sesuai ekspektasi.
- **Hasil Testing:** **PASSED** ✅ (100%)

**NILAI MODUL 4: 100**

---

## Hasil Evaluasi Modul 5: Stack

### 1. Tugas 1: Pengembangan Stack dengan Method Baru
- **Pengecekan Kode:** `get_min()`, `get_max()`, `clear()`, `to_list()`, `copy()`, `reverse()` semuanya terimplementasi dan benar.
- **Hasil Testing:** **PASSED** ✅ (100%)

### 2. Tugas 2: Konversi dan Evaluasi Ekspresi
- **Pengecekan Kode:**
  - `infix_to_postfix()` diimplementasikan dengan benar menggunakan stack — termasuk right-associativity untuk operator `^`.
  - `evaluate_postfix()` dan `calculate()` benar, seluruh test case lulus.
- **Hasil Testing:** **PASSED** ✅ (100%)

### 3. Tugas 3: Aplikasi Browser History
- **Pengecekan Kode:** Implementasi dua stack untuk back/forward. Semua operasi benar.
- **Hasil Testing:** **PASSED** ✅ (100%)

**NILAI MODUL 5: 100**

---

## Hasil Evaluasi Modul 6: Queue

### 1. Tugas 1: Implementasi Priority Queue
- **Pengecekan Kode:** List terurut descending, insertion sort, FIFO untuk prioritas sama. Semua test lulus.
- **Hasil Testing:** **PASSED** ✅ (100%)

### 2. Tugas 2: Implementasi Deque + Palindrome
- **Pengecekan Kode:** Deque semua operasi benar. Palindrome checker menggunakan Deque lokal — semua 7 test case lulus.
- **Hasil Testing:** **PASSED** ✅ (100%)

### 3. Tugas 3: Simulasi Antrian Bank
- **Pengecekan Kode:** Simulasi 20 customers, 3 tellers — semua terlayani. Statistik akurat.
- **Hasil Testing:** **PASSED** ✅ (100%)

**NILAI MODUL 6: 100**

---

## Hasil Evaluasi Modul 7: Review & Studi Kasus (Persiapan UTS)

### Semua Tugas
- **Pengecekan:** Folder `minggu 7/` hanya berisi `Praktikum1_10251005_RifatAdlyjuliandra.py` dan `Praktikum2_10251005_RifatAdlyjuliandra.py` — tidak ada file tugas (PDF maupun .py untuk T7.2).
- **Hasil:** **TIDAK DIKUMPULKAN** ❌ (0%)

**NILAI MODUL 7: 0**

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

### Semua Tugas
- **Pengecekan:** Tidak ditemukan folder atau file Modul 10 di repositori.
- **Hasil:** **TIDAK DIKUMPULKAN** ❌ (0%)

**NILAI MODUL 10: 0**

---

### **NILAI RATA-RATA (Modul 1-7, 9, 10): 69.67**

| Modul | Nilai |
|-------|-------|
| Modul 1 | 100 |
| Modul 2 | 100 |
| Modul 3 | 60 |
| Modul 4 | 100 |
| Modul 5 | 100 |
| Modul 6 | 100 |
| Modul 7 | 0 |
| Modul 9 | 67 |
| Modul 10 | 0 |
| **Rata-rata** | **69.67** |

*Catatan: Modul 3 T2 terdapat bug pengurutan polynomial. Modul 7 tidak dikumpulkan.*
