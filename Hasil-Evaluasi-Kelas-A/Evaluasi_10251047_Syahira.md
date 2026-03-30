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
### **NILAI RATA-RATA SEMENTARA: 95.00 🌟**

*Penilaian ini adalah nilai sementara untuk Modul 1 hingga Modul 4, dievaluasi secara statis berdasarkan instruksi/flowchart dan divalidasi melalui unit test execution.*
