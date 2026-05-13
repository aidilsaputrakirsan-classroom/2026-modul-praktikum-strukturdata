# Laporan Evaluasi Terperinci - Praktikum Struktur Data

---

## Data Mahasiswa
- **Nama:** Muhammad Rasya Al Khalifi
- **NIM:** 10251071
- **Kelas:** Struktur Data A
- **GitHub Username:** `strukturdata-a-MuhRasyaAlKhalifi`

---

## Hasil Evaluasi Modul 1: Pengantar Struktur Data

### 1. Tugas 1: Pengembangan ADT Counter
- **Pengecekan Kode:**
  - Metode penambahan `add()` dan pemotongan `subtract()` tersusun logis sesuai batasan. Blok verifikasi negatif pada operasi kurang (`if self._value < 0: self._value = 0`) menjamin angka absolut tidak menjadi nilai tak masuk akal. 
- **Hasil Testing Codelab:** **PASSED** ✅ (100%)

### 2. Tugas 2: Pengembangan ADT Stack - Aplikasi Reverse String
- **Pengecekan Kode:**
  - Pengembalian string terbalik (*reverse_string*) sukses dibangun dengan *stack* Python konvensional lewat pengulangan *pop* sampai objek himpunan kosong secara beruntun (`while not stack.is_empty():`).
- **Hasil Testing Codelab:** **PASSED** ✅ (100%)

### 3. Tugas 3: Analisis Kompleksitas Lanjutan
- **Tabel Analisis Kompleksitas & Jawaban:**
  - Penjelasan cukup definitif dan rasional, mampu mendeskripsikan setiap kode kompleksitas dan skenarionya, contoh relasi lambatnya `O(n²)` terhadap *sistem media sosial dengan 10 juta pengguna* diuraikan dengan matematis jelas.
- **Hasil Testing Codelab:** **PASSED** ✅ (100%)

**NILAI MODUL 1: 100**

---

## Hasil Evaluasi Modul 2: Array

### 1. Tugas 1: Pengembangan MyArray
- **Pengecekan Kode:** `insert_front`, `delete_front`, `find_min`, `find_max`, `count`, `reverse` diimplementasikan dengan benar. Semua test lulus.
- **Hasil Testing Codelab:** **PASSED** ✅ (100%)

### 2. Tugas 2: Aplikasi Array - Statistik Data
- **Pengecekan Kode:** `sum`, `average`, `range`, `find_second_largest`, `remove_duplicates` semua benar. Semua test lulus.
- **Hasil Testing Codelab:** **PASSED** ✅ (100%)

### 3. Tugas 3: Aplikasi Matrix - Operasi Dasar
- **Pengecekan Kode:** `add_matrices`, `transpose`, `scalar_multiply`, `is_symmetric`, `get_diagonal` semua benar. Semua test lulus.
- **Hasil Testing Codelab:** **PASSED** ✅ (100%)

**NILAI MODUL 2: 100**

---

## Hasil Evaluasi Modul 3: Single Linked List

### 1. Tugas 1: Implementasi Single Linked List
- **Pengecekan Kode:**
  - Semua method wajib (reverse, find_min, find_max, remove_value, to_list) diimplementasikan dengan benar dan lengkap. Algoritma reverse menggunakan tiga pointer efisien O(n). find_min/find_max dengan traversal linear. remove_value menangani semua kasus (head, tengah, tidak ditemukan) dengan tepat.
- **Hasil Testing:** **PASSED** ✅ (100%)

### 2. Tugas 2: Aplikasi Polinomial
- **Pengecekan Kode:**
  - Polynomial menggunakan linked list terurut dari pangkat tertinggi ke terendah. add_term menangani insert terurut dan penggabungan koefisien pada pangkat yang sama. evaluate menggunakan kalkulasi pangkat dengan benar. add_polynomials menghasilkan polynomial baru yang tepat.
- **Hasil Testing:** **PASSED** ✅ (100%)

### 3. Tugas 3: Aplikasi Music Playlist
- **Pengecekan Kode:**
  - Playlist dengan SongNode diimplementasikan lengkap. Semua method (add_song, remove_song, play, next_song, current_song, total_duration, song_count, display, search_by_artist) berfungsi dengan benar. Display menggunakan separator '=' 24 karakter.
- **Hasil Testing:** **PASSED** ✅ (100%)

**NILAI MODUL 3: 100**

---

## Hasil Evaluasi Modul 4: Double Linked List & Circular Linked List

### 1. Tugas 1: Implementasi Double Linked List
- **Pengecekan Kode:**
  - DLL dengan head dan tail diimplementasikan lengkap. reverse, find_min, find_max, swap_nodes, is_palindrome semuanya diimplementasikan dengan benar. is_palindrome menggunakan two-pointer approach dengan terminasi loop yang tepat. Semua test case palindrome dan non-palindrome lulus.
- **Hasil Testing:** **PASSED** ✅ (100%)

### 2. Tugas 2: Aplikasi Text Editor Undo/Redo
- **Pengecekan Kode:**
  - TextEditor menggunakan DLL dengan StateNode. type_text, append_text, undo, redo, get_text, can_undo, can_redo semuanya berfungsi benar. Branching saat pengetikan setelah undo ditangani dengan tepat. show_history menampilkan chain dengan marker ^current yang jelas.
- **Hasil Testing:** **PASSED** ✅ (100%)

### 3. Tugas 3: Aplikasi Round Robin Scheduler
- **Pengecekan Kode:**
  - RoundRobinScheduler menggunakan CLL. execute_one_cycle mengeksekusi quantum dan melakukan rotasi head ke proses berikutnya dengan benar. Output timeline menunjukkan rotasi round-robin yang akurat: A->B->C->A->B->C->A dengan quantum 2. Display queue menampilkan format yang informatif dengan burst time dan remaining time.
- **Hasil Testing:** **PASSED** ✅ (100%)

**NILAI MODUL 4: 100**

---
## Hasil Evaluasi Modul 5: Stack

### 1. Tugas 1: Pengembangan Stack dengan Method Baru
- **Pengecekan Kode:** Semua method (`get_min`, `get_max`, `clear`, `to_list`, `copy`, `reverse`) diimplementasikan dengan benar. Semua test lulus.
- **Hasil Testing:** **PASSED** ✅ (100%)

### 2. Tugas 2: Konversi dan Evaluasi Ekspresi
- **Pengecekan Kode:** `infix_to_postfix()` benar termasuk right-associativity `^`. `evaluate_postfix()` dan `calculate()` benar. Semua test lulus.
- **Hasil Testing:** **PASSED** ✅ (100%)

### 3. Tugas 3: Aplikasi Browser History
- **Pengecekan Kode:** `BrowserHistory` menggunakan dua stack. `visit()`, `back()`, `forward()`, dan `current_page()` benar. Semua test lulus.
- **Hasil Testing:** **PASSED** ✅ (100%)

**NILAI MODUL 5: 100**

---

## Hasil Evaluasi Modul 6: Queue

### 1. Tugas 1: Implementasi Priority Queue
- **Pengecekan Kode:** `PriorityQueue` benar, urutan prioritas terjaga. Semua test lulus.
- **Hasil Testing:** **PASSED** ✅ (100%)

### 2. Tugas 2: Implementasi Deque + Palindrome
- **Pengecekan Kode:** `Deque` benar. Namun `is_palindrome()` tidak mengembalikan nilai apapun (return `None`) — fungsi melakukan pengecekan namun tidak ada `return True/False`. Akibatnya semua pemanggilan `is_palindrome()` mengembalikan `None`.
- **Hasil Testing:** **FAILED** ❌ — `is_palindrome()` selalu return `None` (50%)

### 3. Tugas 3: Simulasi Antrian Bank
- **Pengecekan Kode:** 20 customers, 3 tellers, avg wait 0.30 menit — statistik benar.
- **Hasil Testing:** **PASSED** ✅ (100%)

**NILAI MODUL 6: 83** *(T1:100 + T2:50 + T3:100) / 3 ≈ 83*

---

## Hasil Evaluasi Modul 7: Review & Studi Kasus (Persiapan UTS)

### 1. Tugas 1: Soal Teori (PDF)
- **Pengecekan:** PDF `Tugas1_10251071_MuhammadRasyaAlKhalifi.pdf` ada di folder minggu7.
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

### **NILAI RATA-RATA (Modul 1-7, 9, 10): 93.75**

| Modul | Nilai |
|-------|-------|
| Modul 1 | 100 |
| Modul 2 | 100 |
| Modul 3 | 100 |
| Modul 4 | 100 |
| Modul 5 | 100 |
| Modul 6 | 83 |
| Modul 7 | 100 |
| Modul 9 | 67 |
| Modul 10 | 100 |
| **Rata-rata** | **94.44** |
