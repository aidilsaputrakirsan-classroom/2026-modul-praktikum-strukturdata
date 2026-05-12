# 📝 Laporan Evaluasi Terperinci - Praktikum Struktur Data

---

## 👤 Data Mahasiswa
- **Nama:** Muhammad Nabil Fadhilla
- **NIM:** 10251087
- **Kelas:** Struktur Data B
- **GitHub Username:** `strukturdata-b-nabilfdl`

---

## 🥇 Hasil Evaluasi Modul 1: Pengantar Struktur Data

### 1. Tugas 1: Pengembangan ADT Counter
- **Pengecekan Kode:**
  - Fungsi ADT ditambah list properti *add*, *subtract* yang mampu mengisolir limit nilainya dari `0`. Dan method iterasi fungsi *multiply* diimplementasikan dengan sangat baik pada unit test terminal.
- **Hasil Testing Terminal:** **PASSED** ✅ (100%)

### 2. Tugas 2: Pengembangan ADT Stack - Aplikasi Reverse String
- **Pengecekan Kode:**
  - Metode LIFO dari encapsulation Class `Stack` menampung array string teks untuk dicetak / dikonversi urutannya dari posisi akhir string (berhasil di _reverse_).
- **Hasil Testing Terminal:** **PASSED** ✅ (100%)

### 3. Tugas 3: Analisis Kompleksitas Lanjutan
- **Tabel Analisis Kompleksitas & Jawaban:**
  - Big O kompleksitas iterasi dari range data minimum ke besar mencetak record eksekusi profilernya `microsecond`. Berjalan sangat ringan di memori test.
- **Hasil Testing Terminal:** **PASSED** ✅ (100%)

**✨ NILAI MODUL 1: 100 ✨**

---

## 🥈 Hasil Evaluasi Modul 2: Array

### 1. Tugas 1: Pengembangan MyArray
- **Pengecekan Kode:**
  - Array statis dimanipulasi sesuai dengan rutin fungsionalitas insert data node dan remove first row (`delete_front()`). Serta program reset count perulangan reverse dapat berjalan sempurna.
- **Hasil Testing Terminal:** **PASSED** ✅ (100%)

### 2. Tugas 2: Aplikasi Array - Statistik Data
- **Pengecekan Kode:**
  - Kalkulasi manual _range_ dari object filter list index min max, pencarian _second maximum_ value index, fungsi `average` dan iterasi menghapus node ganda dieksekusi normal.
- **Hasil Testing Terminal:** **PASSED** ✅ (100%)

### 3. Tugas 3: Aplikasi Matrix - Operasi Dasar
- **Pengecekan Kode:**
  - Perhitungan matrix `add_matrices` dikomputasi berdasar kolom dan dot length, `boolean` matrix *Symmetry* di-_declare_, serta matrix row perulangan *transpose* berjalan mulus.
- **Hasil Testing Terminal:** **PASSED** ✅ (100%)

**✨ NILAI MODUL 2: 100 ✨**

---

## 🥉 Hasil Evaluasi Modul 3: Single Linked List

### 1. Tugas 1: Pengembangan LinkedList
- **Pengecekan Kode:** Semua method baru (`reverse()`, `find_min()`, `find_max()`, `remove_value()`, `to_list()`) diimplementasikan dengan benar menggunakan logika traversal yang tepat. Kode mengikuti pola yang konsisten dengan modul sebelumnya.
- **Hasil Testing Terminal:** **PASSED** ✅

### 2. Tugas 2: Aplikasi Linked List - Polynomial
- **Pengecekan Kode:** `add_term()` menggunakan pendekatan sorted insertion dengan penanganan koefisien duplikat. `add_polynomials()` menggunakan pendekatan merge-sort-style yang efisien (bukan simple copy seperti template). Logika benar dan kompak.
- **Hasil Testing Terminal:** **PASSED** ✅

### 3. Tugas 3: Aplikasi Linked List - Music Playlist
- **Pengecekan Kode:** Implementasi lengkap semua method Playlist. `add_song()` menginisialisasi `self.current` ke node pertama saat list kosong (minor: berbeda dari template yang tidak langsung set current, tapi tidak menyebabkan bug pada test case).
- **Hasil Testing Terminal:** **PASSED** ✅

**✨ NILAI MODUL 3: 100 ✨**

---

## 🏅 Hasil Evaluasi Modul 4: Double & Circular Linked List

### 1. Tugas 1: Pengembangan Double Linked List
- **Pengecekan Kode:** *(Pengumpulan terlambat)* DLL dengan `reverse()`, `is_palindrome()` benar. Semua test lulus.
- **Hasil Testing Terminal:** **PASSED** ✅ (50% — terlambat, maks 50)

### 2. Tugas 2: Aplikasi DLL - Text Editor Undo/Redo
- **Pengecekan Kode:** *(Pengumpulan terlambat)* Text editor branching, undo/redo benar. Semua test lulus.
- **Hasil Testing Terminal:** **PASSED** ✅ (50% — terlambat, maks 50)

### 3. Tugas 3: Aplikasi CLL - Round Robin Scheduler
- **Pengecekan Kode:** *(Pengumpulan terlambat)* Round Robin bergantian per quantum benar, total execution time 12 benar.
- **Hasil Testing Terminal:** **PASSED** ✅ (50% — terlambat, maks 50)

**✨ NILAI MODUL 4: 50 ✨** *(pengumpulan terlambat)*

---

## 🥇 Hasil Evaluasi Modul 5: Stack

### 1. Tugas 1: Pengembangan Stack
- **Pengecekan Kode:** Stack dengan `get_min/max`, `to_list`, `copy`, `reverse`, `clear` diimplementasikan benar.
- **Hasil Testing Terminal:** **PASSED** ✅ (100%)

### 2. Tugas 2: Konversi dan Evaluasi Ekspresi
- **Pengecekan Kode:** Infix to postfix dengan right-associativity `^` benar. Full calculation lulus semua.
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
- **Pengecekan Kode:** Deque add/remove/peek benar. `is_palindrome()` benar.
- **Hasil Testing Terminal:** **PASSED** ✅ (100%)

### 3. Tugas 3: Simulasi Antrian Bank
- **Pengecekan Kode:** Simulasi 20 customers, 3 tellers. Avg waiting time 0.30 menit (positif), semua customers terlayani.
- **Hasil Testing Terminal:** **PASSED** ✅ (100%)

**✨ NILAI MODUL 6: 100 ✨**

---
## 🔢 Hasil Evaluasi Modul 7: Review & Studi Kasus (Persiapan UTS)

### 1. Tugas 1: Soal Teori (PDF)
- **Pengecekan:** PDF `Tugas_10251087_Muhammad Nabil Fadhilla.pdf` ada di `minggu 7/`.
- **Hasil:** **DIKUMPULKAN** ✅ (100%)

### 2. Tugas 2: Sistem Manajemen Perpustakaan
- **Hasil Testing Terminal:** **PASSED** ✅ (100%)

**✨ NILAI MODUL 7: 100 ✨**

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
### **🏆 NILAI RATA-RATA (Modul 1-7, 9): 89.63 🏆**

*Penilaian dievaluasi secara statis-manual berdasarkan kode program dan divalidasi melalui eksekusi unit test satu per satu.*
