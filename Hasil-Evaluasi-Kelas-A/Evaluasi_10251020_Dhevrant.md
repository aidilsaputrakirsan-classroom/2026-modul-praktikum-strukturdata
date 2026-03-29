# Laporan Evaluasi Terperinci - Praktikum Struktur Data

---

## Data Mahasiswa
- **Nama:** Dhevrant Zhelynov Malelo
- **NIM:** 10251020
- **Kelas:** Struktur Data A
- **GitHub Username:** `strukturdata-a-Dhevrant`

---

## Hasil Evaluasi Modul 1: Pengantar Struktur Data

### 1. Tugas 1: Pengembangan ADT Counter
- **Pengecekan Kode:**
  - Metode penambahan `add()` dan perkalian `multiply()` berjalan mulus. Penggunaan block kondisional untuk memastikan nilai minimum `subtract()` berjalan dengan semestinya.
- **Hasil Testing Codelab:** **PASSED** ✅ (100%)

### 2. Tugas 2: Pengembangan ADT Stack - Aplikasi Reverse String
- **Pengecekan Kode:**
  - Fungsi Stack aman, dan iterasi `while not stack.is_empty()` diterapkan sesuai flowchart pembalikan string.
- **Hasil Testing Codelab:** **PASSED** ✅ (100%)

### 3. Tugas 3: Analisis Kompleksitas Lanjutan
- **Tabel Analisis Kompleksitas & Jawaban:**
  - **Minor Note:** Ada sedikit anomali/bias teoritis dalam penulisan notasi Big-O asimtotik. Notasi komputasi yang dituliskan adalah *O(2n)* (untuk O(n²)) dan *O(3n)* (untuk O(n³)), yang mana merepresentasikan konstanta alih-alih bentuk pemangkatan algoritma kuadratik/kubik. Namun pemahaman tentang algoritma secara bahasa (seperti lambatnya n³) dapat dimengerti dengan baik.
- **Hasil Testing Codelab:** **PASSED** ✅ (100%)

**NILAI MODUL 1: 90**

---

## Hasil Evaluasi Modul 2: Array

### 1. Tugas 1: Pengembangan MyArray
- **Pengecekan Kode:**
  - Proses modifikasi array in-place `reverse` menggunakan fitur native Python yang solid (`self._elements.reverse()`). Linear counting and minimum/maximum logic terkomposisi dengan sangat baik.
- **Hasil Testing Codelab:** **PASSED** ✅ (100%)

### 2. Tugas 2: Aplikasi Array - Statistik Data
- **Pengecekan Kode:**
  - Penggunaan `average` yang divalidasi manual untuk list elemen berjumlah 0 (zero division escape rule). Perhitungan nilai `second_largest` dan modifikasi array terhindar dari duplikat berjalan apik.
- **Hasil Testing Codelab:** **PASSED** ✅ (100%)

### 3. Tugas 3: Aplikasi Matrix - Operasi Dasar
- **Pengecekan Kode:**
  - Modul matriks diselesaikan dengan *logic testing* untuk perbandingan `matrix[i][j] != matrix[j][i]` saat validasi *is_symmetric*. Efisien tanpa harus load *transpose* yang berat.
- **Hasil Testing Codelab:** **PASSED** ✅ (100%)

**NILAI MODUL 2: 100**


---

## Hasil Evaluasi Modul 3: Single Linked List

### 1. Tugas 1: Implementasi Single Linked List
- **Pengecekan Kode:**
  - Implementasi `reverse()` menggunakan iterasi prev/current/next_node yang solid. `find_min()` dan `find_max()` menangani kasus empty dengan `raise ValueError`. `remove_value()` menangani kasus head dan middle dengan bersih menggunakan variabel `previous`. `to_list()` mengonversi seluruh isi list ke Python list dengan tepat. Kode terstruktur rapi dengan dokumentasi docstring yang lengkap.
- **Hasil Testing:** **PASSED** ✅ (100%)

### 2. Tugas 2: Aplikasi Polynomial
- **Pengecekan Kode:**
  - `Polynomial` menggunakan linked list berurutan eksponen menurun. `add_term()` memasukkan term di posisi yang benar dan menggabungkan term dengan pangkat sama. `add_polynomials()` bekerja dengan mengiterasi kedua polynomial dan memanggil `add_term()` untuk menggabungkan koefisien secara otomatis.
- **Hasil Testing:** **PASSED** ✅ (100%)

### 3. Tugas 3: Aplikasi Music Playlist
- **Pengecekan Kode:**
  - Semua method playlist (`add_song`, `remove_song`, `play`, `next_song`, `current_song`, `total_duration`, `song_count`, `search_by_artist`) diimplementasikan dengan benar dan bersih. Navigasi lagu menggunakan pointer `current` yang diperbarui saat `play()` dan `next_song()`.
- **Hasil Testing:** **PASSED** ✅ (100%)

**NILAI MODUL 3: 100**

---

## Hasil Evaluasi Modul 4: Double Linked List & Circular Linked List

### 1. Tugas 1: Implementasi Double Linked List
- **Pengecekan Kode:**
  - `reverse()` menggunakan pendekatan swap prev/next setiap node secara in-place, kemudian memperbarui head dan tail. `swap_nodes()` menelusuri list dua kali untuk menemukan node di posisi yang diminta. `is_palindrome()` menggunakan dua pointer dari kedua ujung. Semua method lengkap dengan docstring dan error handling.
- **Hasil Testing:** **PASSED** ✅ (100%)

### 2. Tugas 2: Aplikasi Text Editor Undo/Redo
- **Pengecekan Kode:**
  - `TextEditor` menggunakan DLL state-based. `type_text()` memutus redo chain sebelum menyisipkan state baru (branching). `undo()` dan `redo()` berfungsi dengan memeriksa `prev`/`next`. `show_history()` menampilkan seluruh chain dengan marker `^current` yang tepat.
- **Hasil Testing:** **PASSED** ✅ (100%)

### 3. Tugas 3: Aplikasi Round Robin Scheduler
- **Pengecekan Kode:**
  - `RoundRobinScheduler` menggunakan Circular Linked List dengan manajemen head yang tepat. `remove_process()` menangani kasus single-node, head-node, dan non-head. `execute_one_cycle()` memisahkan tracking waktu mulai/akhir dari metode `run()` dan mengembalikan info detail. Output timeline sesuai ekspektasi.
- **Hasil Testing:** **PASSED** ✅ (100%)

**NILAI MODUL 4: 100**

---
### **NILAI RATA-RATA SEMENTARA: 97.50 🌟**

*Penilaian ini adalah nilai sementara untuk Modul 1 hingga Modul 4, dievaluasi secara statis berdasarkan instruksi/flowchart dan divalidasi melalui unit test execution.*
