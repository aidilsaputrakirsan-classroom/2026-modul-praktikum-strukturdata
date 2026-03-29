# Laporan Evaluasi Terperinci - Praktikum Struktur Data

---

## Data Mahasiswa
- **Nama:** Salsabila Yulianti Salim
- **NIM:** 10251026
- **Kelas:** Struktur Data A
- **GitHub Username:** `strukturdata-a-Salsabilaayees`

---

## Hasil Evaluasi Modul 1: Pengantar Struktur Data

### 1. Tugas 1: Pengembangan ADT Counter
- **Pengecekan Kode:**
  - Fungsi penambahan `add()`, `subtract()`, dan perkalian matematis `multiply()` ditulis dengan *if kondisional* pencegahan *underflow* yang jelas. Logic algoritma aman dan berjalan mulus.
- **Hasil Testing Codelab:** **PASSED** ✅ (100%)

### 2. Tugas 2: Pengembangan ADT Stack - Aplikasi Reverse String
- **Pengecekan Kode:**
  - Metode Stack diproteksi dengan `if not self.is_empty():` sebelum memodifikasi `self._items`. Implementasi string pembalikan terkomposisi dengan baik.
- **Hasil Testing Codelab:** **PASSED** ✅ (100%)

### 3. Tugas 3: Analisis Kompleksitas Lanjutan
- **Tabel Analisis Kompleksitas & Jawaban:**
  - Memberikan argumen konkrit terhadap setiap nilai *Time Complexity* di tabel. Untuk `O(log n)` (fungsi E), disertakan simulasi runut *tree* (10000 -> 5000 -> 2500 -> ...), merefleksikan pamahaman rekursif yang prima. Analisa kasus nyatanya sangat dalam dan detail.
- **Hasil Testing Codelab:** **PASSED** ✅ (100%)

**NILAI MODUL 1: 100**

---

## Hasil Evaluasi Modul 2: Array

### 1. Tugas 1: Pengembangan MyArray
- **Pengecekan Kode:**
  - Kode solid dilengkapi mitigasi error (Raising ValueError/IndexError) jika array kosong. Penggunaan dua variabel swap pada fungsi *reverse()* array *in-place* bekerja secara efisien.
- **Hasil Testing Codelab:** **PASSED** ✅ (100%)

### 2. Tugas 2: Aplikasi Array - Statistik Data
- **Pengecekan Kode:**
  - Fungsi iterasi saat penghitungan data kuantitatif tidak menggunakan fungsi instan/bawaan python (seperti min/max), mencerminkan adopsi kompetensi Algoritma. Algoritma `remove_duplicates` dibuat secara murni mengitari elemen array O(n^2).
- **Hasil Testing Codelab:** **PASSED** ✅ (100%)

### 3. Tugas 3: Aplikasi Matrix - Operasi Dasar
- **Pengecekan Kode:**
  - Komparasi ordo dan nilai matriks ditangani rapi. *is_symmetric* menggunakan komparator presisi dengan baris `matrix[i][j] != matrix[j][i]` untuk check kelayakan identitas tanpa merombak memori untuk replikasi transpose penuh. 
- **Hasil Testing Codelab:** **PASSED** ✅ (100%)

**NILAI MODUL 2: 100**


---

## Hasil Evaluasi Modul 3: Single Linked List

### 1. Tugas 1: Implementasi Single Linked List
- **Pengecekan Kode:**
  - `reverse()`, `find_min()`, `find_max()`, `remove_value()`, dan `to_list()` terimplementasi dengan solid dan bersih. Error handling dengan `raise IndexError/ValueError` pada kondisi kosong sudah tepat. Kode terstruktur dengan baik tanpa duplikasi.
- **Hasil Testing:** **PASSED** ✅ (100%)

### 2. Tugas 2: Aplikasi Polynomial
- **Pengecekan Kode:**
  - Implementasi `Polynomial` menggunakan linked list berurutan eksponen menurun. `add_term()` menangani penggabungan term dengan eksponen sama. Tampilan polynomial menggunakan format `3x^2 + 2x + 5` (tanpa eksponen untuk x^1 dan x^0 saat nilai 1, berbeda sedikit dengan referensi). `add_polynomials()` berfungsi benar.
- **Hasil Testing:** **PASSED** ✅ (100%)

### 3. Tugas 3: Aplikasi Music Playlist
- **Pengecekan Kode:**
  - Semua operasi playlist diimplementasikan dengan lengkap. Navigasi lagu (`play`, `next_song`, `current_song`) berfungsi dengan pointer `current`. `search_by_artist()` mengembalikan list judul lagu dengan benar.
- **Hasil Testing:** **PASSED** ✅ (100%)

**NILAI MODUL 3: 100**

---

## Hasil Evaluasi Modul 4: Double Linked List & Circular Linked List

### 1. Tugas 1: Implementasi Double Linked List
- **Pengecekan Kode:**
  - `reverse()` membalik pointer prev/next seluruh node in-place dan memperbarui head/tail. `find_min()`, `find_max()` berjalan dengan benar. `swap_nodes()` menukar data dua node berdasarkan posisi. `is_palindrome()` menggunakan pointer kiri-kanan untuk membandingkan dari kedua ujung.
- **Hasil Testing:** **PASSED** ✅ (100%)

### 2. Tugas 2: Aplikasi Text Editor Undo/Redo
- **Pengecekan Kode:**
  - `TextEditor` mengelola state teks menggunakan DLL. `type_text()` memotong redo chain sebelum menyisipkan state baru. `undo()`/`redo()` bergerak melalui chain. `show_history()` menampilkan seluruh riwayat dengan marker `^current` yang jelas.
- **Hasil Testing:** **PASSED** ✅ (100%)

### 3. Tugas 3: Aplikasi Round Robin Scheduler
- **Pengecekan Kode:**
  - `RoundRobinScheduler` menggunakan CLL. `add_process()` menyisipkan di akhir circular list. `remove_process()` menangani semua kasus secara benar. `execute_one_cycle()` dan `run()` menghasilkan timeline eksekusi yang tepat dengan output detail per proses.
- **Hasil Testing:** **PASSED** ✅ (100%)

**NILAI MODUL 4: 100**

---
### **NILAI RATA-RATA SEMENTARA: 100.00 🌟**

*Penilaian ini adalah nilai sementara untuk Modul 1 hingga Modul 4, dievaluasi secara statis berdasarkan instruksi/flowchart dan divalidasi melalui unit test execution.*
