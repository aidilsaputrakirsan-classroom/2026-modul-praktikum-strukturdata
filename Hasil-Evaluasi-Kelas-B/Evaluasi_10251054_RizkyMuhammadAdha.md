# 📝 Laporan Evaluasi Terperinci - Praktikum Struktur Data

---

## 👤 Data Mahasiswa
- **Nama:** Rizky Muhammad Adha
- **NIM:** 10251054
- **Kelas:** Struktur Data B
- **GitHub Username:** `strukturdata-b-Rizi-54`

---

## 🥇 Hasil Evaluasi Modul 1: Pengantar Struktur Data

### 1. Tugas 1: Pengembangan ADT Counter
- **Pengecekan Kode:**
  - Fungsi penambahan, pengurangan, operasi iterasi modifikasi kali sudah bekerja. Validasi pengurangan `< 0` bekerja mulus menangkal *error math* menjadi `0`.
- **Hasil Testing Terminal:** **PASSED** ✅ (100%)

### 2. Tugas 2: Pengembangan ADT Stack - Aplikasi Reverse String
- **Pengecekan Kode:**
  - Operasi LIFO stack `reverse_string()` membalik list urutan elemen alfabet dengan _push()_ dan perulangan `pop()` secara efisien.
- **Hasil Testing Terminal:** **PASSED** ✅ (100%)

### 3. Tugas 3: Analisis Kompleksitas Lanjutan
- **Tabel Analisis Kompleksitas & Jawaban:**
  - Metode tes analisis Big-O O(n³) eksekusi test Python berhasil diamati dengan *profiler timestamp recording* pada terminal.
- **Hasil Testing Terminal:** **PASSED** ✅ (100%)

**✨ NILAI MODUL 1: 100 ✨**

---

## 🥈 Hasil Evaluasi Modul 2: Array

### 1. Tugas 1: Pengembangan MyArray
- **Pengecekan Kode:**
  - Algoritma kelas `MyArray` yang mengakomodasi _min/max find()_, *insert_front()* hingga *reverse* array memodifikasi index beroperasi dengan efisien *in-place*.
- **Hasil Testing Terminal:** **PASSED** ✅ (100%)

### 2. Tugas 2: Aplikasi Array - Statistik Data
- **Pengecekan Kode:**
  - Range array dinamis di-search memproduksi avg yang spesifik. Validasi elemen list array menghapus object *duplicate* tidak mendatangkan Error exception.
- **Hasil Testing Terminal:** **PASSED** ✅ (100%)

### 3. Tugas 3: Aplikasi Matrix - Operasi Dasar
- **Pengecekan Kode:**
  - Eksekusi _loop iteration_ *row+columns* pada perhitungan `matrix_multiplication` mapun validasi logis dua-matrik lolos validasi `PASSED`.
- **Hasil Testing Terminal:** **PASSED** ✅ (100%)

**✨ NILAI MODUL 2: 100 ✨**

---

## 🥉 Hasil Evaluasi Modul 3: Single Linked List

### 1. Tugas 1: Pengembangan LinkedList
- **Pengecekan Kode:** Semua method baru (`reverse()`, `find_min()`, `find_max()`, `remove_value()`, `to_list()`) diimplementasikan benar. Logika iteratif dan kondisi edge case sudah ditangani dengan baik.
- **Hasil Testing Terminal:** **PASSED** ✅

### 2. Tugas 2: Aplikasi Linked List - Polynomial
- **Pengecekan Kode:** Terdapat bug pada fungsi `add_polynomials()`: saat menjumlahkan term dari p2 ke result, method `add_term()` tidak menggabungkan koefisien dengan pangkat yang sama yang sudah ada di list. Kondisi merge hanya mengecek `current.next.exponent == exponent` tetapi melewatkan kasus di mana node dengan pangkat yang sama adalah head. Akibatnya output `add_polynomials(p1, p2)` menampilkan `3x^2 + 2x^2 + 6x + 8` (tidak tergabung) alih-alih `5x^2 + 6x + 8`. Namun karena assert hanya menguji `evaluate(1) == 19` (yang tetap benar secara numerik), test tetap lulus.
- **Hasil Testing Terminal:** **PASSED** ✅ (assert numerik lulus, namun display polynomial salah - term x^2 tidak tergabung)

### 3. Tugas 3: Aplikasi Linked List - Music Playlist
- **Pengecekan Kode:** Semua method playlist diimplementasikan benar termasuk `format_duration()` dengan format `mm:ss`. Logika navigasi dan pencarian artis berjalan sesuai spesifikasi.
- **Hasil Testing Terminal:** **PASSED** ✅

**✨ NILAI MODUL 3: 90 ✨**

---

## 🏅 Hasil Evaluasi Modul 4: Double & Circular Linked List

### 1. Tugas 1: Pengembangan Double Linked List
- **Pengecekan Kode:** Implementasi `reverse()`, `find_min()`, `find_max()`, `swap_nodes()`, dan `is_palindrome()` semuanya benar. Semua test case lulus termasuk skenario palindrome dan non-palindrome.
- **Hasil Testing Terminal:** **PASSED** ✅

### 2. Tugas 2: Aplikasi DLL - Text Editor Undo/Redo
- **Pengecekan Kode:** Text editor berbasis DLL mengimplementasikan seluruh operasi editing dan history management. Branching history (overwrite redo history saat text baru diketik) berjalan benar. Semua test case lulus.
- **Hasil Testing Terminal:** **PASSED** ✅

### 3. Tugas 3: Aplikasi CLL - Round Robin Scheduler
- **Pengecekan Kode:** Round Robin Scheduler dengan CLL mengeksekusi proses dengan quantum time. Timeline eksekusi ditampilkan dengan detail waktu awal-akhir beserta status remaining time. Proses selesai dengan tepat saat remaining = 0. Total waktu eksekusi benar (12).
- **Hasil Testing Terminal:** **PASSED** ✅

**✨ NILAI MODUL 4: 100 ✨**

---
### **🏆 NILAI RATA-RATA SEMENTARA (Modul 1-4): 97.50 🏆**

*Penilaian ini adalah nilai sementara untuk Modul 1, 2, 3, dan 4, dievaluasi secara statis-manual berdasarkan kode program dan divalidasi melalui eksekusi unit test satu per satu.*
