# Laporan Evaluasi Terperinci - Praktikum Struktur Data

---

## Data Mahasiswa
- **Nama:** Devi Gustiani
- **NIM:** 10251017
- **Kelas:** Struktur Data A
- **GitHub Username:** `strukturdata-a-devigustiani`

---

## Hasil Evaluasi Modul 1: Pengantar Struktur Data

### 1. Tugas 1: Pengembangan ADT Counter
- **Pengecekan Kode:**
  - Metode penambahan dan pengurangan bekerja sesuai requirement. `subtract()` memverifikasi batas minimum `< 0` dengan solid.
- **Hasil Testing Codelab:** **PASSED** ✅ (100%)

### 2. Tugas 2: Pengembangan ADT Stack - Aplikasi Reverse String
- **Pengecekan Kode:**
  - Penggunaan `stack.push()` dan iterasi pembalikan `while not stack.is_empty(): result += stack.pop()` sesuai algoritma.
- **Hasil Testing Codelab:** **PASSED** ✅ (100%)

### 3. Tugas 3: Analisis Kompleksitas Lanjutan
- **Tabel Analisis Kompleksitas & Jawaban:**
  - Tabel analisa time complexity tepat. Argumentasi yang dilampirkan logis, terkhusus soal n log n dan logaritmik tree halving. 
- **Hasil Testing Codelab:** **PASSED** ✅ (100%)

**NILAI MODUL 1: 100**

---

## Hasil Evaluasi Modul 2: Array

### 1. Tugas 1: Pengembangan MyArray
- **Pengecekan Kode:**
  - **Minor Bugs:** Terdapat kesalahan *indentation* `return` variabel di dalam scope perulangan `for` pada method `find_min`, `find_max`, dan `count`. Hal ini menyebabkan *test execution* berhenti dan membalikkan nilai saat perulangan loop pertama selesai.
  - **Typo Pointer:** Di dalam fungsi `reverse()`, pemanggilan indeks array memiliki kesalahan ketik pointer `self._elements[1]` (angka satu) alih-alih `self._elements[i]` yang menyebabkan *logic overwrite* indeks 1 terus-menerus.
- **Hasil Testing Codelab:** **FAILED** ❌ (Beberapa syntax error & indeks bug).

### 2. Tugas 2: Aplikasi Array - Statistik Data
- **Pengecekan Kode:**
  - Perbaikan pada method *find_min* / *find_max* dilakukan pada baris kode di tugas ini (identasi benar). Fungsionalitas data analitik linear dan pencarian `second_largest` berjalan baik.
- **Hasil Testing Codelab:** **PASSED** ✅ (100%)

### 3. Tugas 3: Aplikasi Matrix - Operasi Dasar
- **Pengecekan Kode:**
  - Implementasi komparasi matriks 2D, enumerasi ordo (baris x kolom), boolean simetri serta kalkulasi matriks berhasil dienkapsulasi dengan rapi di skrip ini.
- **Hasil Testing Codelab:** **PASSED** ✅ (100%)

**NILAI MODUL 2: 80**


---

## Hasil Evaluasi Modul 3: Single Linked List

### 1. Tugas 1: Implementasi Single Linked List
- **Pengecekan Kode:**
  - Implementasi `reverse()` menggunakan pendekatan iteratif tiga pointer (prev/curr/nxt) yang bersih dan benar. `find_min()` dan `find_max()` melakukan traversal O(n) dengan inisialisasi nilai awal dari head. `remove_value()` menangani kasus head dan middle node dengan baik. `to_list()` mengonversi linked list ke Python list secara tepat. Terdapat duplikasi definisi class `Node` dan `LinkedList` dalam satu file (akibat copy dari file Praktikum sebelumnya), namun Python menggunakan definisi terakhir sehingga kode fungsional berjalan normal.
- **Hasil Testing:** **PASSED** ✅ (100%)

### 2. Tugas 2: Aplikasi Polynomial
- **Pengecekan Kode:**
  - Kelas `Polynomial` menggunakan linked list untuk menyimpan term dalam urutan pangkat menurun. `add_term()` menangani koefisien 0, memasukkan di posisi tepat berdasarkan eksponen, dan menggabungkan term dengan pangkat sama. `evaluate()` menghitung nilai polinomial dengan benar. `add_polynomials()` melakukan merge dua polynomial secara efisien.
- **Hasil Testing:** **PASSED** ✅ (100%)

### 3. Tugas 3: Aplikasi Music Playlist
- **Pengecekan Kode:**
  - Kelas `Playlist` berbasis linked list mengimplementasikan `add_song()`, `remove_song()`, `play()`, `next_song()`, `current_song()`, `total_duration()`, `song_count()`, `search_by_artist()` dengan benar. Helper `format_duration()` mengkonversi detik ke format mm:ss dengan tepat.
- **Hasil Testing:** **PASSED** ✅ (100%)

**NILAI MODUL 3: 100**

---

## Hasil Evaluasi Modul 4: Double Linked List & Circular Linked List

### 1. Tugas 1: Implementasi Double Linked List
- **Pengecekan Kode:**
  - `reverse()` melakukan swap pointer prev/next secara in-place dengan benar dan memperbarui `self.head`. `find_min()` dan `find_max()` berjalan baik. `swap_nodes()` menukar data dua node di posisi yang ditentukan. `is_palindrome()` membandingkan dari kedua ujung menggunakan `head` dan `tail`.
- **Hasil Testing:** **PASSED** ✅ (100%)

### 2. Tugas 2: Aplikasi Text Editor Undo/Redo
- **Pengecekan Kode:**
  - `TextEditor` menggunakan DLL untuk menyimpan state teks. `type_text()` menghapus redo history (branching), `append_text()` menambahkan teks ke state saat ini. `undo()` dan `redo()` bergerak melalui chain dengan benar. `can_undo()`/`can_redo()` berfungsi semestinya.
- **Hasil Testing:** **PASSED** ✅ (100%)

### 3. Tugas 3: Aplikasi Round Robin Scheduler
- **Pengecekan Kode:**
  - `RoundRobinScheduler` menggunakan Circular Linked List. `add_process()` menyisipkan di akhir circular list dengan benar. `remove_process()` menangani berbagai kasus (single node, head node, non-head). `execute_one_cycle()` menghitung waktu eksekusi dengan quantum dan melakukan rotasi head ke proses berikutnya. Total execution time 12 sesuai ekspektasi.
- **Hasil Testing:** **PASSED** ✅ (100%)

**NILAI MODUL 4: 100**

---

## Hasil Evaluasi Modul 5: Stack

> ⚠️ **Catatan Format:** File Modul 5 dikumpulkan **tanpa ekstensi `.py`** (`Tugas 5.1`, `Tugas 5.2`, `Tugas 5.3`). Meskipun konten Python valid dan dapat dieksekusi, format pengumpulan tidak sesuai ketentuan. **Pengurangan nilai 15 poin diterapkan.**

### 1. Tugas 1: Pengembangan Stack dengan Method Baru
- **Pengecekan Kode:** Semua method baru benar, semua test lulus.
- **Hasil Testing:** **PASSED** ✅

### 2. Tugas 2: Konversi dan Evaluasi Ekspresi
- **Pengecekan Kode:** `infix_to_postfix()` benar termasuk right-associativity `^`. Semua test lulus.
- **Hasil Testing:** **PASSED** ✅

### 3. Tugas 3: Aplikasi Browser History
- **Pengecekan Kode:** Browser history benar.
- **Hasil Testing:** **PASSED** ✅

**NILAI MODUL 5: 85** *(100 - 15 penalti format file tanpa `.py`)*

---

## Hasil Evaluasi Modul 6: Queue

> ⚠️ **Catatan Format:** File Modul 6 juga dikumpulkan **tanpa ekstensi `.py`** (`Tugas 6.1`, `Tugas 6.2`, `Tugas 6.3`). Pengurangan nilai 15 poin diterapkan.

### 1. Tugas 1: Implementasi Priority Queue
- **Pengecekan Kode:** Priority Queue benar, semua test lulus.
- **Hasil Testing:** **PASSED** ✅

### 2. Tugas 2: Implementasi Deque + Palindrome
- **Pengecekan Kode:** Deque dan palindrome benar, semua 7 test palindrome lulus.
- **Hasil Testing:** **PASSED** ✅

### 3. Tugas 3: Simulasi Antrian Bank
- **Pengecekan Kode:** Simulasi benar, statistik akurat.
- **Hasil Testing:** **PASSED** ✅

**NILAI MODUL 6: 85** *(100 - 15 penalti format file tanpa `.py`)*

---

## Hasil Evaluasi Modul 7: Review & Studi Kasus (Persiapan UTS)

### 1. Tugas 1: Soal Teori (PDF)
- **Pengecekan:** PDF `Tugas 7.1_10251017_Devi Gustiani (1).pdf` ada di folder Minggu 7.
- **Hasil:** **DIKUMPULKAN** ✅ (100%)

### 2. Tugas 2: Sistem Manajemen Perpustakaan
- **Pengecekan Kode:** Implementasi hanya mencakup 4 dari 8 test case (Test 1–4: add books, register users, borrow books, borrow queue). Test 5–8 (return book, user history, search, statistics) tidak diimplementasikan.
- **Hasil Testing Terminal:** **PASSED SEBAGIAN** ⚠️ (50% — 4/8 test)

**NILAI MODUL 7: 75** *((100+50)/2)*

---

## Hasil Evaluasi Modul 9: Tree & Binary Tree

### 1. Tugas 1: BinaryTree Class
- **Hasil Testing Terminal:** **PASSED** ✅ (100%)

### 2. Tugas 2: Expression Tree
- **Hasil Testing Terminal:** **PASSED** ✅ (100%)

### 3. Tugas 3: Analisis Kompleksitas Tree
- **Pengecekan Kode:** `SyntaxError: invalid character '≈' (U+2248)` pada baris 21 — file tidak dapat dijalankan.
- **Hasil Testing Terminal:** **FAILED** ❌ (0%)

**NILAI MODUL 9: 67**

---

## Hasil Evaluasi Modul 10: Binary Search Tree (BST)

### 1. Tugas 1: Pengembangan BST Class
- **Hasil Testing Terminal:** **PASSED** ✅ (100%)

### 2. Tugas 2: Sistem Phonebook dengan BST
- **Hasil Testing Terminal:** **PASSED** ✅ (100%)

### 3. Tugas 3: Analisis Performa BST
- **Pengecekan Kode:** Analisis hanya mencakup hingga n=10000 (tidak ada n=50000 seperti template). Data height comparison dan search timing sudah benar namun kurang lengkap.
- **Hasil Testing Terminal:** **PASSED** ✅ (90%) — analisis benar namun hanya hingga n=10000

**NILAI MODUL 10: 97** *((100+100+90)/3 ≈ 97)*

---

### **NILAI RATA-RATA (Modul 1-7, 9, 10): 87.67**

| Modul | Nilai |
|-------|-------|
| Modul 1 | 100 |
| Modul 2 | 80 |
| Modul 3 | 100 |
| Modul 4 | 100 |
| Modul 5 | 85 |
| Modul 6 | 85 |
| Modul 7 | 75 |
| Modul 9 | 67 |
| Modul 10 | 97 |
| **Rata-rata** | **87.67** |

*Catatan: M5/M6 file tanpa ekstensi `.py` (-15 per tugas). M7 T2 hanya 4/8 test case diimplementasikan. M9 T3 SyntaxError karakter unicode. M10 T3 hanya hingga n=10000.*
