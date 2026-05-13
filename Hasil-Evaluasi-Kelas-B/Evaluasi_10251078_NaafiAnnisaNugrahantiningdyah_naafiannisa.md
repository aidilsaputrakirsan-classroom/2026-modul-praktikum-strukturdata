# 📝 Laporan Evaluasi Terperinci - Praktikum Struktur Data

---

## 👤 Data Mahasiswa
- **Nama:** Naafi' Annisa Nugrahantiningdyah
- **NIM:** 10251078
- **Kelas:** Struktur Data B
- **GitHub Username:** `strukturdata-b-naafiannisa`

---

## 🥇 Hasil Evaluasi Modul 1: Pengantar Struktur Data

### 1. Tugas 1: Pengembangan ADT Counter
- **Pengecekan Kode:**
  - Fungsi *add/subtract/multiply* dimodifikasi dan berfungsi memproses object perhitungan iterasi ganjil - genap tanpa terhenti *zero-value loop*.
- **Hasil Testing Terminal:** **PASSED** ✅ (100%)

### 2. Tugas 2: Pengembangan ADT Stack - Aplikasi Reverse String
- **Pengecekan Kode:**
  - Struktur logic pengolahan object `STACK` Array ditambahkan iterasi `reverse`. Method `pop()` / `push()` mengeksekusi iterasi karakter untuk dibalik dengan baik.
- **Hasil Testing Terminal:** **PASSED** ✅ (100%)

### 3. Tugas 3: Analisis Kompleksitas Lanjutan
- **Tabel Analisis Kompleksitas & Jawaban:**
  - Metode tes _Time Execution_ mem-profile detik eksekusi komputasi (contoh `triple nested loop` ke `find maximum`) secara berurutan. Detik komputasinya terlihat kecil (sangat optimal).
- **Hasil Testing Terminal:** **PASSED** ✅ (100%)

**✨ NILAI MODUL 1: 100 ✨**

---

## 🥈 Hasil Evaluasi Modul 2: Array

### 1. Tugas 1: Pengembangan MyArray
- **Pengecekan Kode:**
  - Algoritma delete awalan node `delete_front()` menghapus posisi start awal list. Validasi list `min-max` serta count / loop pencarian *length* valid.
- **Hasil Testing Terminal:** **PASSED** ✅ (100%)

### 2. Tugas 2: Aplikasi Array - Statistik Data
- **Pengecekan Kode:**
  - Metode pencabutan nilai kembar list dalam loop _remove duplicate_ ter-resolve. Modifikasi range *average*, hingga iterasi max-second berjalan efektif mencetak log array 1 elemen atau tak bernilai (*none*).
- **Hasil Testing Terminal:** **PASSED** ✅ (100%)

### 3. Tugas 3: Aplikasi Matrix - Operasi Dasar
- **Pengecekan Kode:**
  - Menerapkan iterasi komputasi tambah row dan cols Array ganda (matrix tambah *add_matrices*). Mempelajari simetri iterasi `for-loop` dalam *matrix addition*. Kalkulasi _Transpose_ normal.
- **Hasil Testing Terminal:** **PASSED** ✅ (100%)

**✨ NILAI MODUL 2: 100 ✨**

---

## 🥉 Hasil Evaluasi Modul 3: Single Linked List

### 1. Tugas 1: Pengembangan LinkedList
- **Pengecekan Kode:** Implementasi sangat bersih dan terstruktur. `reverse()` memperbarui `self.tail` secara eksplisit (kualitas lebih tinggi). `find_min()`, `find_max()`, `remove_value()` (juga memperbarui tail saat hapus tail), dan `to_list()` semuanya correct dan lengkap.
- **Hasil Testing Terminal:** **PASSED** ✅

### 2. Tugas 2: Aplikasi Linked List - Polynomial
- **Pengecekan Kode:** Implementasi `add_term()` menggunakan prev/current pointer yang rapi, menangani kasus edge (coefficient 0, exponent duplikat). `display()` memformat output polynomial dengan baik termasuk kasus koefisien -1. Uji tambahan polynomial kompleks juga lolos.
- **Hasil Testing Terminal:** **PASSED** ✅

### 3. Tugas 3: Aplikasi Linked List - Music Playlist
- **Pengecekan Kode:** Implementasi paling komprehensif di antara rekan-rekannya — menambahkan fitur case-insensitive search, menampilkan indikator lagu yang sedang diputar (▶️), dan mengelola update pointer `current` saat lagu dihapus.
- **Hasil Testing Terminal:** **PASSED** ✅

**✨ NILAI MODUL 3: 100 ✨**

---

## 🏅 Hasil Evaluasi Modul 4: Double & Circular Linked List

### 1. Tugas 1: Pengembangan Double Linked List
- **Pengecekan Kode:** Semua method baru DLL diimplementasikan identik dengan kualitas tinggi: `reverse()`, `find_min/max()`, `swap_nodes()`, `is_palindrome()`. Kode bersih dan well-commented.
- **Hasil Testing Terminal:** **PASSED** ✅

### 2. Tugas 2: Aplikasi DLL - Text Editor Undo/Redo
- **Pengecekan Kode:** `type_text()` memutus history setelah current dengan benar. `undo()`/`redo()` dan branching berjalan tepat. `show_history()` menampilkan history dengan offset posisi current yang dihitung akurat.
- **Hasil Testing Terminal:** **PASSED** ✅

### 3. Tugas 3: Aplikasi CLL - Round Robin Scheduler
- **Pengecekan Kode:** Implementasi lengkap dengan pencatatan statistik detail (waiting time, turnaround time, throughput). `remove_process()` menangani semua kasus (1 node, hapus head, hapus tengah/akhir). Timeline eksekusi sesuai ekspektasi.
- **Hasil Testing Terminal:** **PASSED** ✅

**✨ NILAI MODUL 4: 100 ✨**

---

## 🥇 Hasil Evaluasi Modul 5: Stack

### 1. Tugas 1: Pengembangan Stack
- **Pengecekan Kode:** Stack dengan `get_min/max`, `to_list`, `copy`, `reverse`, `clear` diimplementasikan benar. Edge case ValueError pada stack kosong juga ditangani.
- **Hasil Testing Terminal:** **PASSED** ✅ (100%)

### 2. Tugas 2: Konversi dan Evaluasi Ekspresi
- **Pengecekan Kode:** Infix to postfix dengan right-associativity `^` benar. Test case tambahan seperti `(5+3)*2^2` dan `10-3^2` juga lulus.
- **Hasil Testing Terminal:** **PASSED** ✅ (100%)

### 3. Tugas 3: Aplikasi Stack - Browser History
- **Pengecekan Kode:** BrowserHistory dengan 2 stack, visit/back/forward benar.
- **Hasil Testing Terminal:** **PASSED** ✅ (100%)

**✨ NILAI MODUL 5: 100 ✨**

---

## 🥈 Hasil Evaluasi Modul 6: Queue

### 1. Tugas 1: Priority Queue
- **Pengecekan Kode:** PriorityQueue dengan enqueue/dequeue/peek dan FIFO prioritas sama benar.
- **Hasil Testing Terminal:** **PASSED** ✅ (100%)

### 2. Tugas 2: Deque dan Palindrome
- **Pengecekan Kode:** Deque add/remove/peek benar. Test palindrome diperluas dengan "kasur rusak" dan "ibu ratna antar ubi", semua benar.
- **Hasil Testing Terminal:** **PASSED** ✅ (100%)

### 3. Tugas 3: Simulasi Antrian Bank
- **Pengecekan Kode:** Simulasi berjalan namun **avg waiting time = -7.15 menit (negatif)**, menandakan logika perhitungan waktu tunggu tidak benar.
- **Hasil Testing Terminal:** **FAILED** ❌ (0% — avg waiting time negatif)

**✨ NILAI MODUL 6: 67 ✨** *((100+100+0)/3)*

---
## 🔢 Hasil Evaluasi Modul 7: Review & Studi Kasus (Persiapan UTS)

### 1. Tugas 1: Soal Teori (PDF)
- **Pengecekan:** PDF `Tugas7_10251078_...pdf` ada di `Minggu 7/`.
- **Hasil:** **DIKUMPULKAN** ✅ (100%)

### 2. Tugas 2: Sistem Manajemen Perpustakaan
- **Hasil Testing Terminal:** **PASSED** ✅ (100%)

**✨ NILAI MODUL 7: 100 ✨**

---

## 🔢 Hasil Evaluasi Modul 9: Tree & Binary Tree

### Catatan: Semua 3 file tugas TANPA ekstensi `.py` → penalti -15 per tugas.

### 1. Tugas 1: BinaryTree Class
- **Hasil Testing Terminal:** **PASSED** ✅ (100% → **85** setelah penalti)

### 2. Tugas 2: Expression Tree
- **Hasil Testing Terminal:** **PASSED** ✅ (100% → **85**)

### 3. Tugas 3: Analisis Kompleksitas Tree
- **Pengecekan Kode:** Tabel kompleksitas + rekomendasi B-Tree/AVL/Red-Black ditampilkan. Tidak ada `RecursionError` (memang menggunakan `sys.setrecursionlimit` atau iteratif).
- **Hasil Testing Terminal:** **PASSED** ✅ (100% → **85**)

**✨ NILAI MODUL 9: 85 ✨**

---
## Hasil Evaluasi Modul 10: Binary Search Tree (BST)

### 1. Tugas 1: Pengembangan BST Class
- **Pengecekan Kode:** Semua test lulus (termasuk Test 8 tambahan). File tanpa ekstensi .py, penalti -15.
- **Hasil Testing Terminal:** **PASSED** ✅ (85%)

### 2. Tugas 2: Sistem Phonebook dengan BST
- **Pengecekan Kode:** Semua test lulus. File tanpa ekstensi .py, penalti -15.
- **Hasil Testing Terminal:** **PASSED** ✅ (85%)

### 3. Tugas 3: Analisis Performa BST
- **Pengecekan Kode:** Sorted BST height n-1 benar. Analisis lengkap n=50000. File tanpa ekstensi .py, penalti -15.
- **Hasil Testing Terminal:** **PASSED** ✅ (85%)

**NILAI MODUL 10: 85** *(T1:85 + T2:85 + T3:85) / 3 = 85*

---
### **NILAI RATA-RATA (Modul 1-7, 9, 10): 93.00**

| Modul | Nilai |
|-------|-------|
| Modul 1 | 100 |
| Modul 2 | 100 |
| Modul 3 | 100 |
| Modul 4 | 100 |
| Modul 5 | 100 |
| Modul 6 | 67 |
| Modul 7 | 100 |
| Modul 9 | 85 |
| Modul 10 | 85 |
| **Rata-rata** | **93.00** |

*Penilaian dievaluasi secara statis-manual berdasarkan kode program dan divalidasi melalui eksekusi unit test satu per satu.*
