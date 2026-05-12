# 📝 Laporan Evaluasi Terperinci - Praktikum Struktur Data

---

## 👤 Data Mahasiswa
- **Nama:** Reihan Agil Wijaya
- **NIM:** 10251072
- **Kelas:** Struktur Data B
- **GitHub Username:** `strukturdata-b-reihan-agil-wijaya`

---

## 🥇 Hasil Evaluasi Modul 1: Pengantar Struktur Data

### 1. Tugas 1: Pengembangan ADT Counter
- **Pengecekan Kode:** `__str__` mengembalikan `f"counter: {self._value}"` (huruf kecil) sedangkan test mengharapkan `"Counter: 10"` (huruf kapital) — AssertionError pada baris 98.
- **Hasil Testing Terminal:** **FAILED** ❌ (0%)

### 2. Tugas 2: Pengembangan ADT Stack - Aplikasi Reverse String
- **Pengecekan Kode:** Push/pop LIFO untuk reverse string benar. Semua test lulus.
- **Hasil Testing Terminal:** **PASSED** ✅ (100%)

### 3. Tugas 3: Analisis Kompleksitas Lanjutan
- **Pengecekan Kode:** Profiling eksekusi triple nested loop, recursive halving, dan find_max berjalan dengan output waktu yang benar.
- **Hasil Testing Terminal:** **PASSED** ✅ (100%)

**✨ NILAI MODUL 1: 67 ✨** *((0+100+100)/3)*

---

## 🥈 Hasil Evaluasi Modul 2: Array

### 1. Tugas 1: Pengembangan MyArray
- **Pengecekan Kode:**
  - Menghapus method statis di baris pertama `delete_front()` berfungsi baik. Index algoritma list di-_reverse_, *minimum & maximum* berjalan wajar.
- **Hasil Testing Terminal:** **PASSED** ✅ (100%)

### 2. Tugas 2: Aplikasi Array - Statistik Data
- **Pengecekan Kode:**
  - Logic algoritma iterasi filter list index duplikasi value dengan fungsi loop ganda `remove_duplicates` sukses dieksekusi test case. Terusan fungsi _range_ math maupun filter angka *second_largest* tidak ada bugs.
- **Hasil Testing Terminal:** **PASSED** ✅ (100%)

### 3. Tugas 3: Aplikasi Matrix - Operasi Dasar
- **Pengecekan Kode:**
  - Metode row dan dot array terstruktur melalui matriks iterabel iterasi dimensi ganda (tambah/ add dan transpose) dengan kalkulator simetris. Berjalan mulus di console.
- **Hasil Testing Terminal:** **PASSED** ✅ (100%)

**✨ NILAI MODUL 2: 100 ✨**

---

## 🥉 Hasil Evaluasi Modul 3: Single Linked List

### 1. Tugas 1: Pengembangan LinkedList
- **Pengecekan Kode:** Implementasi bersih dan profesional. `reverse()`, `find_min()`, `find_max()`, `remove_value()` (menggunakan prev pointer elegantly), dan `to_list()` semuanya diimplementasikan dengan benar tanpa komentar TODO.
- **Hasil Testing Terminal:** **PASSED** ✅

### 2. Tugas 2: Aplikasi Linked List - Polynomial
- **Pengecekan Kode:** `add_term()` menggunakan pola sorted insertion. `add_polynomials()` menggunakan merge-style algorithm yang efisien. `display()` memformat ekspresi polynomial dengan menghilangkan `^1` dan `^0` untuk tampilan lebih natural.
- **Hasil Testing Terminal:** **PASSED** ✅

### 3. Tugas 3: Aplikasi Linked List - Music Playlist
- **Pengecekan Kode:** Semua method Playlist diimplementasikan lengkap dan clean tanpa komentar TODO. Kode paling ringkas dan profesional untuk Tugas 3.
- **Hasil Testing Terminal:** **PASSED** ✅

**✨ NILAI MODUL 3: 100 ✨**

---

## 🏅 Hasil Evaluasi Modul 4: Double & Circular Linked List

### 1. Tugas 1: Pengembangan Double Linked List
- **Pengecekan Kode:** `reverse()`, `find_min/max()`, `swap_nodes()`, `is_palindrome()` semuanya benar. Minor: terdapat duplikasi definisi class `DNode` (baris 12 dan 18) namun Python hanya menggunakan definisi terakhir sehingga tidak berpengaruh pada eksekusi.
- **Hasil Testing Terminal:** **PASSED** ✅

### 2. Tugas 2: Aplikasi DLL - Text Editor Undo/Redo
- **Pengecekan Kode:** `type_text()` menggunakan loop untuk menghapus semua node setelah current sebelum menambah node baru (pendekatan berbeda namun hasilnya sama). `undo()`/`redo()` dan branching berjalan tepat. `show_history()` menampilkan history dengan marker current yang jelas.
- **Hasil Testing Terminal:** **PASSED** ✅

### 3. Tugas 3: Aplikasi CLL - Round Robin Scheduler
- **Pengecekan Kode:** Implementasi lengkap dengan statistik detail (waiting time, completion time, turnaround time). `remove_process()` menangani semua kasus dengan benar. Timeline eksekusi sesuai ekspektasi.
- **Hasil Testing Terminal:** **PASSED** ✅

**✨ NILAI MODUL 4: 100 ✨**

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
- **Pengecekan Kode:** File `tugas3` di folder `minggu 6` berisi kode Browser History (aplikasi Stack dari M5), bukan simulasi antrian bank. File salah konten.
- **Hasil Testing Terminal:** **FAILED** ❌ (0% — konten salah, bukan Queue/Bank simulation)

**✨ NILAI MODUL 6: 67 ✨** *((100+100+0)/3)*

---
## 🔢 Hasil Evaluasi Modul 7: Review & Studi Kasus (Persiapan UTS)

### 1. Tugas 1: Soal Teori (PDF)
- **Pengecekan:** PDF `Tugas7_10251072_ReihanAgilWijaya.pdf` ada di `minggu 7/`.
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
### **🏆 NILAI RATA-RATA (Modul 1-7, 9): 87.63 🏆**

*Penilaian dievaluasi secara statis-manual berdasarkan kode program dan divalidasi melalui eksekusi unit test satu per satu.*
