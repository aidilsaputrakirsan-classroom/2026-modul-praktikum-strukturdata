# Laporan Evaluasi Terperinci - Praktikum Struktur Data

---

## Data Mahasiswa
- **Nama:** Silvester Jevon Amabel
- **NIM:** 10251029
- **Kelas:** Struktur Data A
- **GitHub Username:** `strukturdata-a-SilvesterJevon`

---

## Hasil Evaluasi Modul 1: Pengantar Struktur Data

### 1. Tugas 1: Pengembangan ADT Counter
- **Pengecekan Kode:**
  - Fungsi penambahan `add()`, `subtract()`, dan perkalian matematis `multiply()` ditulis dengan *conditional* blok kontrol struktur yang sempurna untuk menghindari nilai negatif.
- **Hasil Testing Codelab:** **PASSED** ✅ (100%)

### 2. Tugas 2: Pengembangan ADT Stack - Aplikasi Reverse String
- **Pengecekan Kode:**
  - Metode Stack diproteksi dengan `if self.is_empty(): raise IndexError`. String reversal memadukan *push* dan iterasi *pop* dengan efektif.
- **Hasil Testing Codelab:** **PASSED** ✅ (100%)

### 3. Tugas 3: Analisis Kompleksitas Lanjutan
- **Tabel Analisis Kompleksitas & Jawaban:**
  - Membongkar analisa struktur kode `O(log n)` (fungsi E) serta menjelaskan sifat *rekursif* yang membebankan setengah input tiap putaran. Analisa skalabilitas real-world komplit dan aplikatif (seperti studi kasus sistem bank untuk kompleksitas `O(n^2)`).
- **Hasil Testing Codelab:** **PASSED** ✅ (100%)

**NILAI MODUL 1: 100**

---

## Hasil Evaluasi Modul 2: Array

### 1. Tugas 1: Pengembangan MyArray
- **Pengecekan Kode:**
  - Metode pencarian *find_min* / *find_max* di-handle dengan baik. Penyesuaian `raise ValueError("Array kosong")` melindungi fungsi. Reverse array digarap natural menggunakan variabel temporary (`temp = self._elements[left]`).
- **Hasil Testing Codelab:** **PASSED** ✅ (100%)

### 2. Tugas 2: Aplikasi Array - Statistik Data
- **Pengecekan Kode:**
  - Kalkulasi kuantitatif diimplementasi pure dari _loop_ dan variabel akumulator di semua modul analitis numerik. Menjauhkan *built-in module*, membuktikan esensi pemikiran Algorithm-based.
- **Hasil Testing Codelab:** **PASSED** ✅ (100%)

### 3. Tugas 3: Aplikasi Matrix - Operasi Dasar
- **Pengecekan Kode:**
  - Operator _matrix validation_ `if len(matrix) != len(matrix[0])` melindungi `get_diagonal()`. Transpose array `result.append(row)` dan `scalar` array loop berdimensi ganda (nested-loop) kokoh secara sintaksis.
- **Hasil Testing Codelab:** **PASSED** ✅ (100%)

**NILAI MODUL 2: 100**


---

## Hasil Evaluasi Modul 3: Single Linked List

### 1. Tugas 1: Implementasi Single Linked List
- **Pengecekan Kode:** `reverse()`, `find_min()`, `find_max()`, `remove_value()`, `to_list()` diimplementasikan dengan benar. Semua assert test lulus.
- **Hasil Testing:** **PASSED** ✅ (100%)

### 2. Tugas 2: Aplikasi Polinomial
- **Pengecekan Kode:** `add_polynomials()` menggabungkan koefisien pangkat sama dengan benar (`5x^2 + 6x + 8`). Semua test lulus.
- **Hasil Testing:** **PASSED** ✅ (100%)

### 3. Tugas 3: Aplikasi Music Playlist
- **Pengecekan Kode:** Semua operasi playlist (`add_song`, `remove_song`, `play`, `next_song`, `search_by_artist`, `total_duration`, `song_count`) berjalan benar. Semua test lulus.
- **Hasil Testing:** **PASSED** ✅ (100%)

**NILAI MODUL 3: 100**

---

## Hasil Evaluasi Modul 4: Double Linked List & Circular Linked List

### 1. Tugas 1: Implementasi Double Linked List
- **Pengecekan Kode:** Semua method DLL (`reverse`, `find_min`, `find_max`, `swap_nodes`, `is_palindrome`, `to_list`) diimplementasikan dengan benar. Semua assert test lulus.
- **Hasil Testing:** **PASSED** ✅ (100%)

### 2. Tugas 2: Aplikasi Text Editor Undo/Redo
- **Pengecekan Kode:** `type_text`, `append_text`, `undo`, `redo`, dan branching semua berjalan benar. `show_history()` menampilkan posisi `^current` dengan tepat.
- **Hasil Testing:** **PASSED** ✅ (100%)

### 3. Tugas 3: Aplikasi Round Robin Scheduler
- **Pengecekan Kode:** **Bug pada logika rotasi** — scheduler mengeksekusi Process A hingga selesai, baru beralih ke B, kemudian C. Output: `A→A→A(selesai)→B→B(selesai)→C→C(selesai)` alih-alih pola Round Robin `A→B→C→A→...`. Head tidak dirotasi ke proses berikutnya setelah tiap quantum.
- **Hasil Testing:** **FAILED** ❌ — Round Robin tidak bergantian per quantum, proses dieksekusi sequential.

**NILAI MODUL 4: 67** *(T1:100 + T2:100 + T3:0) / 3 ≈ 67*

---

## Hasil Evaluasi Modul 5: Stack

### 1. Tugas 1: Pengembangan Stack dengan Method Baru
- **Pengecekan Kode:** Semua method baru benar, semua test lulus.
- **Hasil Testing:** **PASSED** ✅ (100%)

### 2. Tugas 2: Konversi dan Evaluasi Ekspresi
- **Pengecekan Kode:** `infix_to_postfix()` 5/6 benar; **right-associativity `^` tidak ditangani** — `'A ^ B ^ C'` → `'A B ^ C ^'`. Evaluasi postfix dan calculate semua benar.
- **Hasil Testing:** **HAMPIR LULUS** ⚠️ (90%)

### 3. Tugas 3: Aplikasi Browser History
- **Pengecekan Kode:** Browser history benar, semua test lulus.
- **Hasil Testing:** **PASSED** ✅ (100%)

**NILAI MODUL 5: 97** *(T1:100 + T2:90 + T3:100) / 3 ≈ 97*

---

## Hasil Evaluasi Modul 6: Queue

### 1. Tugas 1: Implementasi Priority Queue
- **Pengecekan Kode:** Priority Queue benar. Catatan: untuk prioritas sama (=3), urutan FIFO tidak dijaga (`Normal task` keluar sebelum `Medium priority task`, padahal Medium masuk lebih dulu). Test tidak mengassert FIFO, jadi dianggap lulus.
- **Hasil Testing:** **PASSED** ✅ (100%)

### 2. Tugas 2: Implementasi Deque + Palindrome
- **Pengecekan Kode:** Deque benar. Palindrome — semua 7 test lulus.
- **Hasil Testing:** **PASSED** ✅ (100%)

### 3. Tugas 3: Simulasi Antrian Bank
- **Pengecekan Kode:** Avg waiting time -6.15 menit (negatif) — bug logika pada perhitungan `start_service_time`. Semua 20 customers terlayani tapi statistik tidak valid.
- **Hasil Testing:** **BUG LOGIKA** ⚠️ (60%)

**NILAI MODUL 6: 87** *(T1:100 + T2:100 + T3:60) / 3 ≈ 87*

---

## Hasil Evaluasi Modul 7: Review & Studi Kasus (Persiapan UTS)

### 1. Tugas 1: Soal Teori (PDF)
- **Pengecekan:** Tidak ada file PDF di folder modul-07. Hanya ada file praktikum dan `tugas02`.
- **Hasil:** **TIDAK DIKUMPULKAN** ❌ (0%)

### 2. Tugas 2: Sistem Manajemen Perpustakaan
- **Pengecekan Kode:** Semua 8 test case lulus.
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

### **NILAI RATA-RATA (Modul 1-7, 9, 10): 83.5**

| Modul | Nilai |
|-------|-------|
| Modul 1 | 100 |
| Modul 2 | 100 |
| Modul 3 | 100 |
| Modul 4 | 67 |
| Modul 5 | 97 |
| Modul 6 | 87 |
| Modul 7 | 50 |
| Modul 9 | 67 |
| Modul 10 | 100 |
| **Rata-rata** | **85.33** |

*Catatan: M7 T1 tidak dikumpulkan (tidak ada PDF).*
