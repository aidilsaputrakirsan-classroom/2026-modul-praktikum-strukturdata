# Laporan Evaluasi Terperinci - Praktikum Struktur Data

---

## Data Mahasiswa
- **Nama:** Nurul Syahira A
- **NIM:** 10251047
- **Kelas:** Struktur Data A
- **GitHub Username:** `strukturdata-a-syahira10251047`

---

## Hasil Evaluasi Modul 1: Pengantar Struktur Data

### 1. Tugas 1: Pengembangan ADT Counter
- **Pengecekan Kode:**
  - Metode `subtract()` bekerja lancar menggunakan kondisi terstruktur `if self._value >= n`. Method kalkulatif lainnya tertulis efisien. 
- **Hasil Testing Codelab:** **PASSED** ✅ (100%)

### 2. Tugas 2: Pengembangan ADT Stack - Aplikasi Reverse String
- **Pengecekan Kode:**
  - Struktur Stack menggunakan prinsip LIFO tanpa kompromi. Loop `for` dikombinasikan secara proporsional dengan `while` loop pada `reverse_string()`.
- **Hasil Testing Codelab:** **PASSED** ✅ (100%)

### 3. Tugas 3: Analisis Kompleksitas Lanjutan
- **Tabel Analisis Kompleksitas & Jawaban:**
  - Alasan di balik penentuan kompleksitas ditulis singkat dan tepat sasaran. Penjelasan O(log n) berpusat pada rekursi *halving*, membuktikan penguasaan algoritma pencarian lanjutan.
- **Hasil Testing Codelab:** **PASSED** ✅ (100%)

**NILAI MODUL 1: 100**

---

## Hasil Evaluasi Modul 2: Array

### 1. Tugas 1: Pengembangan MyArray
- **Pengecekan Kode:**
  - Method `find_min()` dan `find_max()` dilengkapi error exception standar jika array kosong. Operasi array dasar ditangani baik.
- **Hasil Testing Codelab:** **PASSED** ✅ (100%)

### 2. Tugas 2: Aplikasi Array - Statistik Data
- **Pengecekan Kode:**
  - *Logic* pada `calculate_sum` sangat padat dan ringkas: memanggil `self._elements[i]` menghindari *overhead* akses get(). `remove_duplicates` dioptimalkan dengan iterasi bertingkat.
- **Hasil Testing Codelab:** **PASSED** ✅ (100%)

### 3. Tugas 3: Aplikasi Matrix - Operasi Dasar
- **Pengecekan Kode:**
  - Validasi *is_symmetric* dipermudah menggunakan komparasi langsung: `t = transpose_matrix(matrix); return matrix == t`. Strategi pengkodean yang sangat "Pythonic" dan *clean*.
- **Hasil Testing Codelab:** **PASSED** ✅ (100%)

**NILAI MODUL 2: 100**

---

## Hasil Evaluasi Modul 3: Single Linked List

### 1. Tugas 1: Implementasi Single Linked List
- **Pengecekan Kode:**
  - Implementasi `reverse()`, `find_min()`, `find_max()`, `remove_value()`, dan `to_list()` semuanya benar. `remove_value()` menangani kasus penghapusan head dengan pengecekan `self.head.data == value` secara langsung. Method praktikum dilengkapi komentar TODO yang masih tersisa namun tidak memengaruhi fungsionalitas.
- **Hasil Testing:** **PASSED** ✅ (100%)

### 2. Tugas 2: Aplikasi Polinomial
- **Pengecekan Kode:**
  - `Polynomial` menggunakan `TermNode` dengan urutan dari pangkat tertinggi ke terendah. `add_term()` menggabungkan koefisien untuk pangkat yang sama. Format display menggunakan notasi `x` (tanpa pangkat eksplisit untuk exp=1). Semua operasi polinomial berfungsi dengan benar.
- **Hasil Testing:** **PASSED** ✅ (100%)

### 3. Tugas 3: Aplikasi Music Playlist
- **Pengecekan Kode:**
  - Semua operasi playlist diimplementasikan lengkap dan benar: `song_count()`, `total_duration()`, `play()`, `next_song()`, `search_by_artist()`, dan `remove_song()`. Output playlist rapi dan terstruktur.
- **Hasil Testing:** **PASSED** ✅ (100%)

**NILAI MODUL 3: 100**

---

## Hasil Evaluasi Modul 4: Double Linked List & Circular Linked List

### 1. Tugas 1: Implementasi Double Linked List
- **Pengecekan Kode:**
  - `DoublyLinkedList` menggunakan `DNode` dengan pointer `prev` dan `next`. Method baru `reverse()`, `find_min()`, `find_max()`, `swap_nodes()`, dan `is_palindrome()` diimplementasikan dengan benar. Penggunaan `previous = None` dan traversal dua pointer untuk reverse sudah tepat.
- **Hasil Testing:** **PASSED** ✅ (100%)

### 2. Tugas 2: Aplikasi Text Editor Undo/Redo
- **Pengecekan Kode:**
  - `TextEditor` berbasis DLL berfungsi dengan baik. `type_text()`, `append_text()`, `undo()`, `redo()`, dan branching semuanya diimplementasi dan lolos semua test. Display history menampilkan `^current` di baris terpisah di bawah posisi aktif, memberikan visual yang jelas.
- **Hasil Testing:** **PASSED** ✅ (100%)

### 3. Tugas 3: Aplikasi Round Robin Scheduler
- **Pengecekan Kode:**
  - File `Tugas4.3_10251047_Nurul Syahira.py` berisi konten Praktikum 4.3 (Insert dan Delete di Posisi DLL), bukan implementasi Round Robin Scheduler yang diminta. File yang disubmit adalah file praktikum yang salah diunggah ke slot tugas.
- **Hasil Testing:** **FAILED** ❌ — file yang disubmit adalah Praktikum 4.3 (DLL insert/delete), bukan Round Robin Scheduler

**NILAI MODUL 4: 80**

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
- **Pengecekan Kode:** Priority Queue benar, FIFO untuk prioritas sama terjaga.
- **Hasil Testing:** **PASSED** ✅ (100%)

### 2. Tugas 2: Implementasi Deque + Palindrome
- **Pengecekan Kode:** Deque benar. Palindrome — format output berbeda (`radar -> True`) tapi semua hasil benar.
- **Hasil Testing:** **PASSED** ✅ (100%)

### 3. Tugas 3: Simulasi Antrian Bank
- **Pengecekan Kode:** 20 customers, 3 tellers, avg wait 0.30 — benar. Output tanpa label "minutes" tapi nilai benar.
- **Hasil Testing:** **PASSED** ✅ (100%)

**NILAI MODUL 6: 100**

---

## Hasil Evaluasi Modul 7: Review & Studi Kasus (Persiapan UTS)

### 1. Tugas 1: Soal Teori (PDF)
- **Pengecekan:** PDF `Tugas7_10251047_Nurul Syahira A.pdf` ada di folder Minggu7.
- **Hasil:** **DIKUMPULKAN** ✅ (100%)

### 2. Tugas 2: Sistem Manajemen Perpustakaan
- **Pengecekan Kode:** Implementasi berjalan (operasi borrow/queue/display tercetak) namun tidak menggunakan format test case terstruktur (tidak ada marker "Test 1 PASSED" dll). Fungsionalitas partial.
- **Hasil Testing Terminal:** **PARTIAL** ⚠️ (50%)

**NILAI MODUL 7: 75** *((100+50)/2)*

---

## Hasil Evaluasi Modul 9: Tree & Binary Tree

### 1. Tugas 1: BinaryTree Class
- **Hasil Testing Terminal:** **PASSED** ✅ (100%)

### 2. Tugas 2: Expression Tree
- **Hasil Testing Terminal:** **PASSED** ✅ (100%)

### 3. Tugas 3: Analisis Kompleksitas Tree
- **Pengecekan Kode:** File berisi analisis teks (tabel kompleksitas + Q&A) tanpa implementasi kode pengukuran. Tidak ada RecursionError, tapi tidak ada output pengukuran. Konten analisis benar.
- **Hasil Testing Terminal:** **PARTIAL** ⚠️ (50% — analisis benar, tidak ada kode pengukuran)

**NILAI MODUL 9: 83** *((100+100+50)/3)*

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

### **NILAI RATA-RATA (Modul 1-7, 9, 10): 92.25**

| Modul | Nilai |
|-------|-------|
| Modul 1 | 100 |
| Modul 2 | 100 |
| Modul 3 | 100 |
| Modul 4 | 80 |
| Modul 5 | 100 |
| Modul 6 | 100 |
| Modul 7 | 75 |
| Modul 9 | 83 |
| Modul 10 | 100 |
| **Rata-rata** | **93.11** |

*Catatan: M7 T2 tidak menggunakan format test terstruktur. M9 T3 hanya berisi analisis teks, tanpa kode pengukuran.*
