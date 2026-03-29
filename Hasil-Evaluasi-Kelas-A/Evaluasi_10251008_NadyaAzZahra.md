# Laporan Evaluasi Terperinci - Praktikum Struktur Data

---

## Data Mahasiswa
- **Nama:** Nadya Az-Zahra
- **NIM:** 10251008
- **Kelas:** Struktur Data A
- **GitHub Username:** `strukturdata-a-nadyaazzahra`

---

## Hasil Evaluasi Modul 1: Pengantar Struktur Data

### 1. Tugas 1: Pengembangan ADT Counter
- **Pengecekan Kode:**
  - Metode penambahan maupun pengurangan di bawah 0 sudah dirancang rapi dengan percabangan `if n > 0`. Algoritma untuk `add()`, `subtract()`, dan `multiply()` dibuat sangat efisien.
- **Hasil Testing Codelab:** **PASSED** ✅ (100%)

### 2. Tugas 2: Pengembangan ADT Stack - Aplikasi Reverse String
- **Pengecekan Kode:**
  - Method stack dan reverse_string diimplementasikan dengan list operations Python tanpa mendegradasi performa. Stack iterasi dibongkar perlahan dengan `.pop()`.
- **Hasil Testing Codelab:** **PASSED** ✅ (100%)

### 3. Tugas 3: Analisis Kompleksitas Lanjutan
- **Tabel Analisis Kompleksitas & Jawaban:**
  - Jawaban tertulis sangat rinci dan runut. Mulai dari relasi algoritma O(n³) terhadap waktu pengeksekusian hingga logika bubble sort linear vs kuadratik yang disinggung di akhir pembahasan. Semua kode berhasil mencatat eksekusi yang konsisten.
- **Hasil Testing Codelab:** **PASSED** ✅ (100%)

**NILAI MODUL 1: 100**

---

## Hasil Evaluasi Modul 2: Array

### 1. Tugas 1: Pengembangan MyArray
- **Pengecekan Kode:**
  - Reverse swap in-place dieksekusi solid (`left` & `right` logic pointer pivot valid). Pencarian minimaks valid O(n).
- **Hasil Testing Codelab:** **PASSED** ✅ (100%)

### 2. Tugas 2: Aplikasi Array - Statistik Data
- **Pengecekan Kode:**
  - Fungsionalitas pencarian urutan terbesar kedua berjalan mulus dengan float negative infinity `float('-inf')`, menunjukkan pemahaman *edge-case pointer replacement* yang cemerlang.
- **Hasil Testing Codelab:** **PASSED** ✅ (100%)

### 3. Tugas 3: Aplikasi Matrix - Operasi Dasar
- **Pengecekan Kode:**
  - Logika determinasi linear pada `is_symmetric` disatukan dengan inisiasi `transpose_matrix`. Hasil perhitungan di dalam `for-loops` sangat rapi.
- **Hasil Testing Codelab:** **PASSED** ✅ (100%)

**NILAI MODUL 2: 100**

---

## Hasil Evaluasi Modul 3: Single Linked List

### 1. Tugas 1: Implementasi Single Linked List
- **Pengecekan Kode:**
  - Terdapat **bug kritis** pada method `reverse()` di baris 183: `prev = currentcurrent = next_node` — ini adalah chained assignment yang menetapkan nilai ke variabel `currentcurrent` (bukan `current`). Akibatnya, variable `current` tidak pernah diperbarui dalam loop, menyebabkan **infinite loop** saat `reverse()` dipanggil.
  - Method lain (`find_min()`, `find_max()`, `remove_value()`, `to_list()`) diimplementasikan dengan benar.
  - Saat dijalankan: program **infinite loop** pada saat test `ll.reverse()` dipanggil, tidak dapat selesai.
- **Hasil Testing:** **FAILED** ❌ (0%) — Infinite loop akibat bug typo pada `reverse()`

### 2. Tugas 2: Aplikasi Polynomial
- **Pengecekan Kode:**
  - Implementasi `Polynomial`, `add_term()`, `evaluate()`, `degree()`, dan `add_polynomials()` semuanya benar dan lengkap. Display menggunakan format `3x^2 + 2x^1 + 5x^0` yang konsisten.
- **Hasil Testing:** **PASSED** ✅ (100%)

### 3. Tugas 3: Aplikasi Music Playlist
- **Pengecekan Kode:**
  - Semua fitur playlist diimplementasikan dengan benar dan lengkap: `add_song()`, `remove_song()`, `play()`, `next_song()`, `current_song()`, `total_duration()`, `song_count()`, `display()`, `search_by_artist()`.
  - `remove_song()` juga mengupdate `self.current` jika lagu yang sedang diputar dihapus.
- **Hasil Testing:** **PASSED** ✅ (100%)

**NILAI MODUL 3: 67**

---

## Hasil Evaluasi Modul 4: Double Linked List & Circular Linked List

### 1. Tugas 1: Implementasi Double Linked List
- **Pengecekan Kode:**
  - `reverse()` diimplementasikan dengan benar (swap prev/next + swap head/tail). `find_min()`, `find_max()`, `swap_nodes()`, `is_palindrome()`, dan `to_list()` semuanya benar dan lengkap.
- **Hasil Testing:** **PASSED** ✅ (100%)

### 2. Tugas 2: Aplikasi Text Editor Undo/Redo
- **Pengecekan Kode:**
  - `type_text()` menghapus redo history dengan benar. `undo()`/`redo()` berfungsi baik. `show_history()` menampilkan history dengan penanda `^current` pada state aktif.
- **Hasil Testing:** **PASSED** ✅ (100%)

### 3. Tugas 3: Aplikasi Round Robin Scheduler
- **Pengecekan Kode:**
  - Terdapat **bug pada `remove_process()`**: saat proses yang dihapus adalah head, `prev` telah diset ke `self.head` sebelum loop sehingga `prev.next = current.next` memodifikasi pointer head yang lama secara salah, yang dapat menyebabkan inkonsistensi struktur circular. Bug ini mengakibatkan **infinite loop** saat scheduler berjalan.
  - Saat dijalankan: program **tidak selesai** (infinite loop/timeout) ketika menjalankan `scheduler.run()`.
- **Hasil Testing:** **FAILED** ❌ (0%) — Infinite loop akibat bug pada `remove_process()`

**NILAI MODUL 4: 67**

---
### **NILAI RATA-RATA SEMENTARA: 84 🌟**

*Penilaian ini adalah nilai sementara untuk Modul 1 hingga Modul 4, dievaluasi secara statis berdasarkan instruksi/flowchart dan divalidasi melalui unit test execution.*
