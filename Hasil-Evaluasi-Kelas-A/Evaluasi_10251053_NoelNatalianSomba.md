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
### **NILAI RATA-RATA SEMENTARA: 100.00 🌟**

*Penilaian ini adalah nilai sementara untuk Modul 1 hingga Modul 4, dievaluasi secara statis berdasarkan instruksi/flowchart dan divalidasi melalui unit test execution.*
