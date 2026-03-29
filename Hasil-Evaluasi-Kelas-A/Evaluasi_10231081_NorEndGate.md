# Laporan Evaluasi Terperinci - Praktikum Struktur Data

---

## Data Mahasiswa
- **Nama:** Rendy
- **NIM:** 10231081
- **Kelas:** Struktur Data A
- **GitHub Username:** `strukturdata-a-NorEndGate`

---

## Hasil Evaluasi Modul 1: Pengantar Struktur Data

### 1. Tugas 1: Pengembangan ADT Counter
- **Pengecekan Kode:**
  - `add(n)`: Diimplementasikan dengan pengkondisian nilai minimum (harus positif).
  - `subtract(n)`: Pengecekan *boundary* berhasil dieksekusi agar selisihnya tidak menyebabkan defisit mutlak di bawah `0`.
  - `multiply(n)`: Dikerjakan dengan baik. Terdapat pengecekan jika nilai minus/negatif.
  - `__str__()`: Pembuatan representasi format string terimplementasi.
- **Hasil Testing Codelab:** **PASSED** ✅ (100%)

### 2. Tugas 2: Pengembangan ADT Stack - Aplikasi Reverse String
- **Pengecekan Kode:**
  - Fitur `print_stack` menampilkan elemen LIFO dari array stack (`self._items`).
  - Fitur `clear` menghapus list *items* seluruh instansiasi Object.
  - Implementasi reverse_string berjalan tepat memanfaatkan sifat LIFO stack buatan mahasiswa.
- **Hasil Testing Codelab:** **PASSED** ✅ (100%)

### 3. Tugas 3: Analisis Kompleksitas Lanjutan
- **Tabel Analisis Kompleksitas & Jawaban:**
  - Prediksi operasi Big-O akurat (A-F). Mahasiswa mengerti korelasi waktu terhadap tipe eksekusi *iterative* versus rekurens. Secara inisiatif menyesuaikan variabel unit test `n` lebih kecil saat algoritma bersifat log(n³). Jawaban dan penjabaran narasi juga sangat baik dan komprehensif.
- **Hasil Testing Codelab:** **PASSED** ✅ (100%)

**NILAI MODUL 1: 100**

---

## Hasil Evaluasi Modul 2: Array

### 1. Tugas 1: Pengembangan MyArray
- **Pengecekan Kode:**
  - Metode penambahan maupun pengurangan node awal `insert_front` / `delete_front` berjalan valid melalui manipulasi index array internal Python. Pengecekan minimaks dan pemutaran arah array diimplementasikan sesuai *flowchart*.
- **Hasil Testing Codelab:** **PASSED** ✅ (100%)

### 2. Tugas 2: Aplikasi Array - Statistik Data
- **Pengecekan Kode:**
  - Berhasil menyusun pengolahan analitik dari angka *floating point* / *integer*. Fungsi aggregasi seperti sum, filter unit ganda (*remove duplicates*), perankingan rata-rata tereksekusi tanpa hambatan.
- **Hasil Testing Codelab:** **PASSED** ✅ (100%)

### 3. Tugas 3: Aplikasi Matrix - Operasi Dasar
- **Pengecekan Kode:**
  - Mahasiswa memahami *multi-dimensional arrays*. Mahasiswa mengimplementasikan fungsi ekstra untuk komparasi validasi dan representasi matriks *printing* (tugas yang melebihi standar baseline). *Output* komparasi dan kalkulasi skalar sangat stabil.
- **Hasil Testing Codelab:** **PASSED** ✅ (100%)

**NILAI MODUL 2: 100**

---

## Hasil Evaluasi Modul 3: Single Linked List

### 1. Tugas 1: Implementasi Single Linked List
- **Pengecekan Kode:**
  - Semua method baru diimplementasikan dengan benar: `reverse()` menggunakan three-pointer technique (O(n)), `find_min()` dan `find_max()` melakukan traversal penuh, `remove_value()` menghapus node pertama dengan nilai yang cocok, `to_list()` mengkonversi ke Python list.
  - Method dari praktikum (insert, delete, search, size, dll) semuanya lengkap dan benar.
- **Hasil Testing:** **PASSED** ✅ (100%)

### 2. Tugas 2: Aplikasi Polynomial
- **Pengecekan Kode:**
  - Class `Polynomial` dan `TermNode` diimplementasikan dengan baik. `add_term()` menjaga urutan dari pangkat tertinggi ke terendah dan menangani koefisien sama (merge). `evaluate()` dan `degree()` benar. `add_polynomials()` menghasilkan hasil penjumlahan yang tepat.
  - Bonus: menangani koefisien 0, auto-sort pangkat, dan display dengan format matematika yang rapi.
- **Hasil Testing:** **PASSED** ✅ (100%)

### 3. Tugas 3: Aplikasi Music Playlist
- **Pengecekan Kode:**
  - Class `Playlist` dan `SongNode` lengkap. Semua fitur diimplementasikan: `add_song()`, `remove_song()`, `play()`, `next_song()`, `current_song()`, `total_duration()`, `song_count()`, `display()`, `search_by_artist()`. Helper `format_duration()` mengkonversi detik ke format mm:ss.
  - `remove_song()` menangani update `self.current` saat lagu aktif dihapus.
- **Hasil Testing:** **PASSED** ✅ (100%)

**NILAI MODUL 3: 100**

---

## Hasil Evaluasi Modul 4: Double Linked List & Circular Linked List

### 1. Tugas 1: Implementasi Double Linked List
- **Pengecekan Kode:**
  - `reverse()` menukar prev/next setiap node dan memperbarui head/tail dengan benar. `find_min()` dan `find_max()` melakukan traversal O(n). `swap_nodes()` menukar data dua node berdasarkan posisi. `is_palindrome()` membandingkan dari kedua ujung menggunakan pointer head dan tail secara bersamaan. `to_list()` untuk konversi ke Python list.
- **Hasil Testing:** **PASSED** ✅ (100%)

### 2. Tugas 2: Aplikasi Text Editor Undo/Redo
- **Pengecekan Kode:**
  - Class `TextEditor` menggunakan DLL (`StateNode` dengan prev/next). `type_text()` memutus redo history saat mengetik baru (branching). `append_text()` menambahkan ke state saat ini. `undo()` dan `redo()` memindahkan current pointer. `show_history()` menampilkan seluruh history dengan posisi current yang akurat.
- **Hasil Testing:** **PASSED** ✅ (100%)

### 3. Tugas 3: Aplikasi Round Robin Scheduler
- **Pengecekan Kode:**
  - Class `RoundRobinScheduler` menggunakan Circular Linked List. `add_process()` menambah proses ke CLL dengan pointer circular yang benar. `remove_process()` menangani kasus satu proses maupun proses di head/tengah. `execute_one_cycle()` menjalankan quantum atau sisa burst, mencatat statistik. `run()` menjalankan semua proses hingga selesai dengan timeline yang tepat (A=5, B=3, C=4, quantum=2 → total 12).
- **Hasil Testing:** **PASSED** ✅ (100%)

**NILAI MODUL 4: 100**

---
### **NILAI RATA-RATA SEMENTARA: 100 🌟**

*Penilaian ini adalah nilai sementara untuk Modul 1 hingga Modul 4, dievaluasi secara statis berdasarkan instruksi/flowchart dan divalidasi melalui unit test execution.*
