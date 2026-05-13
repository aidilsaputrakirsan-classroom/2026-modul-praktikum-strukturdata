# Laporan Evaluasi Terperinci - Praktikum Struktur Data

---

## Data Mahasiswa
- **Nama:** Noel Natalian Somba
- **NIM:** 10251053
- **Kelas:** Struktur Data A
- **GitHub Username:** `strukturdata-a-N3CH0`

---

## Hasil Evaluasi Modul 1: Pengantar Struktur Data

### 1. Tugas 1: Pengembangan ADT Counter
- **Pengecekan Kode:**
  - Metode penambahan dan perkalian tersusun secara fungsional. Pada metode *subtract()*, pembatasan ke tingkat operasional nihil telah divalidasi dengan lancar `if self._value < 0: self._value = 0` guna proteksi kalkulasi.
- **Hasil Testing Codelab:** **PASSED** ✅ (100%)

### 2. Tugas 2: Pengembangan ADT Stack - Aplikasi Reverse String
- **Pengecekan Kode:**
  - Fungsi balik string dirancang memakai pengulangan standard Python melalui iterasi dan mekanisme `pop`, mematuhi pakem tata cara Stack secara efisien.
- **Hasil Testing Codelab:** **PASSED** ✅ (100%)

### 3. Tugas 3: Analisis Kompleksitas Lanjutan
- **Tabel Analisis Kompleksitas & Jawaban:**
  - Mahasiswa memahami betul teori analisis komparatif performa algoritma (Big-O). Pembuktian matematis serta penjelasan di contoh iterasi sangat lugas. Penjabaran untuk *bubble sort* dengan algoritma $O(n^2)$ pada 1 juta data logis karena membutuhkan operasi sangat masif senilai $10^{12}$.
- **Hasil Testing Codelab:** **PASSED** ✅ (100%)

**NILAI MODUL 1: 100**

---

## Hasil Evaluasi Modul 2: Array

### 1. Tugas 1: Pengembangan MyArray
- **Pengecekan Kode:**
  - Semua metode esensial (`insert_front`, `delete_front`, `find_min`, `find_max`, `reverse`, dan `count`) berfungsi sempurna tanpa cacat kompilasi atau kesalahan runtime. Teknik `reverse` *in-place swap* diimplementasikan dengan presisi yang mantul.
- **Hasil Testing Codelab:** **PASSED** ✅ (100%)

### 2. Tugas 2: Aplikasi Array - Statistik Data
- **Pengecekan Kode:**
  - Pencarian elemen unik dan penyisihan terduplikat dimodelkan menggunakan class *MyArray* dari tugas sebelumnya. Fungsi `find_second_largest` dan rentang dieksekusi efisien karena mahasiswa meletakkan conditional pointer logic tanpa fungsi library sort Python sama sekali.
- **Hasil Testing Codelab:** **PASSED** ✅ (100%)

### 3. Tugas 3: Aplikasi Matrix - Operasi Dasar
- **Pengecekan Kode:**
  - *Nested loops* matriks untuk kalkulasi aljabar linier ditangani solid dengan pemantauan panjang index baris/kolom `len(matrix[0])`. Perulangan pada rotasi transpose matrix dibuat efisien. 
- **Hasil Testing Codelab:** **PASSED** ✅ (100%)

**NILAI MODUL 2: 100**

---

## Hasil Evaluasi Modul 3: Single Linked List

### 1. Tugas 1: Implementasi Single Linked List
- **Pengecekan Kode:**
  - Implementasi `reverse()`, `find_min()`, `find_max()`, `remove_value()`, dan `to_list()` semuanya benar dan bersih. `remove_value()` menangani kasus empty list dengan `if self.is_empty(): return False`. Kode terstruktur dengan pemisah jelas antara method praktikum dan method tugas baru.
- **Hasil Testing:** **PASSED** ✅ (100%)

### 2. Tugas 2: Aplikasi Polinomial
- **Pengecekan Kode:**
  - `Polynomial` menggunakan `TermNode`. `add_term()` menjaga urutan pangkat tertinggi ke terendah dengan penggabungan koefisien jika pangkat sudah ada. Format display menggunakan notasi `x^n` eksplisit. `add_polynomials()` menggabungkan dua polinomial dengan benar.
- **Hasil Testing:** **PASSED** ✅ (100%)

### 3. Tugas 3: Aplikasi Music Playlist
- **Pengecekan Kode:**
  - `MusicPlaylist` diimplementasikan lengkap. Seluruh operasi (`song_count`, `total_duration`, `play`, `next_song`, `search_by_artist`, `remove_song`) berfungsi dengan tepat dan terstruktur baik.
- **Hasil Testing:** **PASSED** ✅ (100%)

**NILAI MODUL 3: 100**

---

## Hasil Evaluasi Modul 4: Double Linked List & Circular Linked List

### 1. Tugas 1: Implementasi Double Linked List
- **Pengecekan Kode:**
  - `DoublyLinkedList` menggunakan `DNode` dengan pointer `prev` dan `next`. Method baru `reverse()`, `find_min()`, `find_max()`, `swap_nodes()`, dan `is_palindrome()` semuanya diimplementasikan dengan benar. Kode bersih dan terstruktur dengan komentar yang memadai.
- **Hasil Testing:** **PASSED** ✅ (100%)

### 2. Tugas 2: Aplikasi Text Editor Undo/Redo
- **Pengecekan Kode:**
  - `TextEditor` berbasis DLL berfungsi sempurna. `type_text()`, `append_text()`, `undo()`, `redo()`, dan branching semuanya diimplementasi dan lolos semua test. Display history menampilkan posisi `^current` dengan alignment yang tepat di bawah state aktif.
- **Hasil Testing:** **PASSED** ✅ (100%)

### 3. Tugas 3: Aplikasi Round Robin Scheduler
- **Pengecekan Kode:**
  - `RoundRobinScheduler` menggunakan Circular Linked List. `add_process()` menjaga circular link, `remove_process()` menangani semua kasus penghapusan. `execute_one_cycle()` mengeksekusi quantum dan berpindah ke proses berikutnya. Timeline menampilkan interleaving Round Robin yang benar. Bonus: statistik rata-rata turnaround time dan waiting time per proses ditambahkan di output, menunjukkan pemahaman lebih dalam tentang CPU scheduling.
- **Hasil Testing:** **PASSED** ✅ (100%)

**NILAI MODUL 4: 100**

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
- **Pengecekan:** Tidak ada PDF di folder Minggu 7. File `Tugas_7.1_10251053_Noel_Natalian_Somba.py` berisi implementasi Sistem Manajemen Perpustakaan (bukan soal teori PDF).
- **Hasil:** **TIDAK DIKUMPULKAN** ❌ (0%)

### 2. Tugas 2: Sistem Manajemen Perpustakaan
- **Pengecekan Kode:** File `Tugas_7.1` berisi Library management. Semua 8 test case lulus.
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

### **NILAI RATA-RATA (Modul 1-7, 9, 10): 89.63**

| Modul | Nilai |
|-------|-------|
| Modul 1 | 100 |
| Modul 2 | 100 |
| Modul 3 | 100 |
| Modul 4 | 100 |
| Modul 5 | 100 |
| Modul 6 | 100 |
| Modul 7 | 50 |
| Modul 9 | 67 |
| Modul 10 | 100 |
| **Rata-rata** | **90.78** |

*Catatan: M6 dikumpulkan terlambat (setelah evaluasi pertama), sudah dievaluasi. M7 T1 tidak dikumpulkan (file tugas berisi Library bukan PDF teori).*
