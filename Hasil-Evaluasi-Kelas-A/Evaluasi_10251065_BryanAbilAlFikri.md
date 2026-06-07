# Laporan Evaluasi Terperinci - Praktikum Struktur Data

---

## Data Mahasiswa
- **Nama:** Bryan Abil Al-Fikri
- **NIM:** 10251065
- **Kelas:** Struktur Data A
- **GitHub Username:** `strukturdata-a-Bryan1065`

---

## Hasil Evaluasi Modul 1: Pengantar Struktur Data

### 1. Tugas 1: Pengembangan ADT Counter
- **Pengecekan Kode:**
  - Fungsi penambahan, pengurangan, hingga perkalian disusun solid menggunakan operator penugasan Python standar (`+=`, `-=`, `*=`). Terlihat pemahaman akan metode `reset` bawaan yang dieksekusi benar.
- **Hasil Testing Codelab:** **PASSED** ✅ (100%)

### 2. Tugas 2: Pengembangan ADT Stack - Aplikasi Reverse String
- **Pengecekan Kode:**
  - Metode operasional *stack stack.push()* dan *stack.pop()* dibalut rapi. Untuk fungsi ekstraksi pembalikan berjalan efisien mendayagunakan skema LIFO *last in first out* secara utuh.
- **Hasil Testing Codelab:** **PASSED** ✅ (100%)

### 3. Tugas 3: Analisis Kompleksitas Lanjutan
- **Tabel Analisis Kompleksitas & Jawaban:**
  - Pemahaman terhadap *Triple Nested Loop O(n³)* dan *Recursive Halving O(log n)* dijelaskan logis dan mudah dipahami. Contoh skenario dunia nyata untuk O(n²) diilustrasikan dengan valid.
- **Hasil Testing Codelab:** **PASSED** ✅ (100%)

**NILAI MODUL 1: 100**

---

## Hasil Evaluasi Modul 2: Array

### 1. Tugas 1: Pengembangan MyArray
- **Pengecekan Kode:**
  - Implementasi pertukaran nilai bolak-balik fitur *reverse* dijalankan aman menggunakan pendekatan `while left < right` yang efisien *in-place*. 
- **Hasil Testing Codelab:** **PASSED** ✅ (100%)

### 2. Tugas 2: Aplikasi Array - Statistik Data
- **Pengecekan Kode:**
  - *find_second_largest* tidak menggunakan angka literal statis tetapi *None* sebagai referensi inisiasi. Fitur logika duplikasi *remove_duplicates* menghindari pendobelan array element-by-element sukses.
- **Hasil Testing Codelab:** **PASSED** ✅ (100%)

### 3. Tugas 3: Aplikasi Matrix - Operasi Dasar
- **Pengecekan Kode:**
  - Transposisi matrix dan modifikasi per komponen melalui komputasi iteratif yang rapi dengan `zip()` yang menunjukkan penguasaan *built-in methods* Python dengan presisi tinggi.
- **Hasil Testing Codelab:** **PASSED** ✅ (100%)

**NILAI MODUL 2: 100**

---

## Hasil Evaluasi Modul 3: Single Linked List

### 1. Tugas 1: Implementasi Single Linked List
- **Pengecekan Kode:**
  - Semua method wajib (reverse, find_min, find_max, remove_value, to_list) diimplementasikan dengan benar dan lengkap. Algoritma reverse menggunakan tiga pointer efisien O(n). find_min dan find_max menggunakan traversal linear. remove_value menangani semua kasus edge dengan tepat.
- **Hasil Testing:** **PASSED** ✅ (100%)

### 2. Tugas 2: Aplikasi Polinomial
- **Pengecekan Kode:**
  - Polynomial menggunakan linked list terurut dari pangkat tertinggi ke terendah. add_term menangani insert terurut dan penggabungan koefisien pada pangkat yang sama. evaluate menggunakan kalkulasi pangkat dengan benar. add_polynomials menghasilkan polynomial baru hasil penjumlahan yang tepat.
- **Hasil Testing:** **PASSED** ✅ (100%)

### 3. Tugas 3: Aplikasi Music Playlist
- **Pengecekan Kode:**
  - Kelas Playlist dengan SongNode diimplementasikan lengkap. Semua method (add_song, remove_song, play, next_song, current_song, total_duration, song_count, display, search_by_artist) berfungsi dengan benar. File dikumpulkan tanpa ekstensi .py namun terdeteksi sebagai Python script yang valid.
- **Hasil Testing:** **PASSED** ✅ (100%)

**NILAI MODUL 3: 100**

---

## Hasil Evaluasi Modul 4: Double Linked List & Circular Linked List

### 1. Tugas 1: Implementasi Double Linked List
- **Pengecekan Kode:**
  - DLL dengan head dan tail diimplementasikan lengkap. reverse, find_min, find_max, swap_nodes, is_palindrome semuanya benar. is_palindrome menggunakan two-pointer approach dengan terminasi loop yang tepat. File dikumpulkan tanpa ekstensi .py namun valid sebagai Python script.
- **Hasil Testing:** **PASSED** ✅ (100%)

### 2. Tugas 2: Aplikasi Text Editor Undo/Redo
- **Pengecekan Kode:**
  - TextEditor menggunakan DLL dengan StateNode. type_text menghapus future history (branching) sebelum menambah state baru. undo/redo bernavigasi mundur/maju dengan benar. show_history menampilkan seluruh chain history dengan marker current yang jelas menggunakan format kurung kotak.
- **Hasil Testing:** **PASSED** ✅ (100%)

### 3. Tugas 3: Aplikasi Round Robin Scheduler
- **Pengecekan Kode:**
  - RoundRobinScheduler menggunakan CLL. execute_one_cycle mengeksekusi quantum dan melakukan rotasi `self.head = self.head.next` dengan tepat. remove_process menangani penghapusan node dari CLL dengan benar. run menghasilkan timeline Round Robin yang akurat sesuai output yang diharapkan.
- **Hasil Testing:** **PASSED** ✅ (100%)

**NILAI MODUL 4: 100**

---

## Hasil Evaluasi Modul 5: Stack

### 1. Tugas 1: Pengembangan Stack dengan Method Baru
- **Pengecekan Kode:** Semua method baru (`get_min`, `get_max`, `clear`, `to_list`, `copy`, `reverse`) diimplementasikan dengan benar. Semua test lulus.
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

### 1. Tugas 1: Priority Queue
- **Hasil Testing Terminal:** **PASSED** ✅ (100%)

### 2. Tugas 2: Deque dan Palindrome
- **Hasil Testing Terminal:** **PASSED** ✅ (100%)

### 3. Tugas 3: Simulasi Antrian Bank
- **Hasil Testing Terminal:** **PASSED** ✅ (100%)

**NILAI MODUL 6: 100**

---

## Hasil Evaluasi Modul 7: Review & Studi Kasus (Persiapan UTS)

### 1. Tugas 1: Soal Teori (PDF)
- **Pengecekan:** PDF `Tugas7_10251065_Bryan Abil Al-Fikri.pdf` ada di folder Minggu 7.
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
- **Pengecekan Kode:** Perbandingan adjacency list vs matrix berjalan untuk 5 konfigurasi.
- **Hasil Testing Terminal:** **PASSED** ✅ (100%)

**NILAI MODUL 11: 100**

---

## Hasil Evaluasi Modul 12: Algoritma Searching

> **Catatan:** M12 di-push tanggal 24 Mei 2026 (beberapa jam setelah evaluasi awal). Setelah pull ulang dari repo, M12 lengkap dan semua test PASSED.

### 1. Tugas 1: Binary Search Lanjutan
- **Pengecekan Kode:** Semua fungsi (`lower_bound`, `upper_bound`, `count_occurrences`, `find_closest`, `search_rotated`) benar dan lulus 5 test case.
- **Hasil Testing Terminal:** **PASSED** ✅ (100%)

### 2. Tugas 2: Hash Table - Open Addressing
- **Pengecekan Kode:** Linear probing + tombstone, resize & rehash bekerja sempurna.
- **Hasil Testing Terminal:** **PASSED** ✅ (100%)

### 3. Tugas 3: Sistem Kamus Digital
- **Pengecekan Kode:** Bidirectional dictionary dengan multiple translations dan prefix search benar.
- **Hasil Testing Terminal:** **PASSED** ✅ (100%)

**NILAI MODUL 12: 100**

---

## Hasil Evaluasi Modul 13: Sorting Dasar

- **Catatan:** Tidak ada folder/file Modul 13 di repositori (commit terakhir hanya sampai Modul 12).

**NILAI MODUL 13: 0**

---

## Hasil Evaluasi Modul 14: Sorting Lanjutan

- Tidak ada folder/file Modul 14 di repositori.

**NILAI MODUL 14: 0**

---

### **NILAI RATA-RATA (Modul 1-7, 9-14): 82.08**

| Modul | Nilai |
|-------|-------|
| Modul 1 | 100 |
| Modul 2 | 100 |
| Modul 3 | 100 |
| Modul 4 | 100 |
| Modul 5 | 100 |
| Modul 6 | 100 |
| Modul 7 | 100 |
| Modul 9 | 67 |
| Modul 10 | 100 |
| Modul 11 | 100 |
| Modul 12 | 100 |
| Modul 13 | 0 |
| Modul 14 | 0 |
| **Rata-rata** | **82.08** |

*Catatan: M6 dikumpulkan terlambat (setelah evaluasi pertama), sudah dievaluasi. M12 di-push 24 Mei 2026, dievaluasi pada pull ulang — semua test PASSED.*
