# 📝 Laporan Evaluasi Terperinci - Praktikum Struktur Data

---

## 👤 Data Mahasiswa
- **Nama:** Reihan Agil Wijaya
- **NIM:** 10251072
- **Kelas:** Struktur Data B
- **GitHub Username:** `strukturdata-b-reihan-agil-wijaya`

---

## 🥇 Hasil Evaluasi Modul 1: Pengantar Struktur Data

- **Pengecekan Kode:**
  - Evaluasi unit test Terminal Modul 1 terputus di **Tugas 1 (ADT Counter)**. Eksekusi tes memicu pesan *AssertionError: GAGAL: \_\_str\_\_*, yang mengindikasikan bahwa fungsi format output objek Counter `__str__` belum sesuai luaran yang dimandatkan.
- **Hasil Testing Terminal:** **FAILED** ❌ (0%)

**✨ NILAI MODUL 1: 0 ✨**

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
### **🏆 NILAI RATA-RATA SEMENTARA (Modul 1-4): 75.00 🏆**

*Penilaian ini adalah nilai sementara untuk Modul 1, 2, 3, dan 4, dievaluasi secara statis-manual berdasarkan kode program dan divalidasi melalui eksekusi unit test satu per satu.*
