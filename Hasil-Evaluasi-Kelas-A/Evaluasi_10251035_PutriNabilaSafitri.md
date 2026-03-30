# Laporan Evaluasi Terperinci - Praktikum Struktur Data

---

## Data Mahasiswa
- **Nama:** Putri Nabila Safitri
- **NIM:** 10251035
- **Kelas:** Struktur Data A
- **GitHub Username:** `strukturdata-a-10251035-Putri`

---

## Hasil Evaluasi Modul 1: Pengantar Struktur Data

### 1. Tugas 1: Pengembangan ADT Counter
- **Pengecekan Kode:**
  - Metode `subtract()` dikontrol tepat untuk mencegah nilai negatif bersisa (`if self._value < 0: self._value = 0`). Seluruh implementasi kalkulatif beroperasi dengan sempurna.
- **Hasil Testing Codelab:** **PASSED** ✅ (100%)

### 2. Tugas 2: Pengembangan ADT Stack - Aplikasi Reverse String
- **Pengecekan Kode:**
  - Stack methods komplit. Pembalikan string (`reverse_string`) dilakukan via stack push per karakter yang ringkas, dengan *pop* di dalam *while loop* untuk penyesuaian string balasan.
- **Hasil Testing Codelab:** **PASSED** ✅ (100%)

### 3. Tugas 3: Analisis Kompleksitas Lanjutan
- **Tabel Analisis Kompleksitas & Jawaban:**
  - Pemahaman Notasi Big-O (termasuk kompleksitas kubik & logaritmik) dijawab dengan akurasi tinggi. Studi kasus yang digunakan logis, seperti sosial media skala jutaan *user* untuk O(n^2).
- **Hasil Testing Codelab:** **PASSED** ✅ (100%)

**NILAI MODUL 1: 100**

---

## Hasil Evaluasi Modul 2: Array

### 1. Tugas 1: Pengembangan MyArray
- **Pengecekan Kode:**
  - Modul pengecekan nilai min & max beroperasi efektif. Pergerakan loop array balikan `reverse(self)` diatur ringkas via variabel in-place swap tuple `self._elements[left], self._elements[right] = self._elements[right], self._elements[left]`.
- **Hasil Testing Codelab:** **PASSED** ✅ (100%)

### 2. Tugas 2: Aplikasi Array - Statistik Data
- **Pengecekan Kode:**
  - `remove_duplicates` ditangani via *search* untuk pengecekan elemen non-redundant. Metode *second largest* (mencari terbesar kedua) diformulasikan efisien menggunakan `float('-inf')` untuk pembanding awal.
- **Hasil Testing Codelab:** **PASSED** ✅ (100%)

### 3. Tugas 3: Aplikasi Matrix - Operasi Dasar
- **Pengecekan Kode:**
  - Pertahanan error handling diaplikasikan penuh (seperti memfilter *rows != len(matrix2)*). Implementasi diagonal dengan `range(min(rows, cols))` dinilai sebagai *best practice* keamanan memory.
- **Hasil Testing Codelab:** **PASSED** ✅ (100%)

**NILAI MODUL 2: 100**

---

## Hasil Evaluasi Modul 3: Single Linked List

### 1. Tugas 1: Implementasi Single Linked List
- **Pengecekan Kode:**
  - Implementasi `reverse()` menggunakan tiga pointer (`prev`, `current`, `next_node`) secara in-place dengan kompleksitas O(n). `find_min()` dan `find_max()` melakukan traversal penuh dimulai dari head. `remove_value()` menangani kasus penghapusan head maupun node di tengah/akhir. `to_list()` mengkonversi linked list ke Python list via traversal sederhana. Semua method baru terimplementasi dengan benar.
- **Hasil Testing:** **PASSED** ✅ (100%)

### 2. Tugas 2: Aplikasi Polinomial
- **Pengecekan Kode:**
  - `TermNode` menyimpan coefficient dan exponent. `add_term()` menjaga urutan dari pangkat tertinggi ke terendah dan menggabungkan koefisien jika pangkat sudah ada. `evaluate()` menghitung nilai polinomial dengan Horner-style traversal. `add_polynomials()` menggabungkan dua polinomial dengan benar.
- **Hasil Testing:** **PASSED** ✅ (100%)

### 3. Tugas 3: Aplikasi Music Playlist
- **Pengecekan Kode:**
  - `MusicPlaylist` berbasis linked list dengan `SongNode`. Operasi `song_count()`, `total_duration()`, `play()`, `next_song()`, `search_by_artist()`, dan `remove_song()` diimplementasi lengkap dan benar. Format tampilan playlist terstruktur rapi.
- **Hasil Testing:** **PASSED** ✅ (100%)

**NILAI MODUL 3: 100**

---

## Hasil Evaluasi Modul 4: Double Linked List & Circular Linked List

### 1. Tugas 1: Implementasi Double Linked List
- **Pengecekan Kode:**
  - `DoublyLinkedList` menggunakan `DNode` dengan pointer `prev` dan `next`. Method baru meliputi `reverse()` (membalik pointer prev/next setiap node), `find_min()`, `find_max()`, `swap_nodes()` (menukar data dua node berdasarkan nilai), dan `is_palindrome()` (memanfaatkan `to_list()` lalu membandingkan dengan reversal). Semua implementasi tepat dan terstruktur.
- **Hasil Testing:** **PASSED** ✅ (100%)

### 2. Tugas 2: Aplikasi Text Editor Undo/Redo
- **Pengecekan Kode:**
  - `TextEditor` menggunakan DLL sebagai riwayat (history). `type_text()` dan `append_text()` menambah state baru, `undo()` mundur ke state sebelumnya, `redo()` maju ke state berikutnya. Branching (mengetik ulang setelah undo) memotong redo chain dengan benar. Display history menunjukkan pointer `^current` pada posisi aktif.
- **Hasil Testing:** **PASSED** ✅ (100%)

### 3. Tugas 3: Aplikasi Round Robin Scheduler
- **Pengecekan Kode:**
  - `RoundRobinScheduler` menggunakan Circular Linked List. `add_process()` mempertahankan circular link, `remove_process()` menangani semua kasus (head, tail, tengah). `execute_one_cycle()` mengeksekusi proses head selama satu quantum, lalu berpindah ke proses berikutnya. Timeline eksekusi menampilkan interleaving yang benar sesuai Round Robin.
- **Hasil Testing:** **PASSED** ✅ (100%)

**NILAI MODUL 4: 100**

---
### **NILAI RATA-RATA SEMENTARA: 100.00 🌟**

*Penilaian ini adalah nilai sementara untuk Modul 1 hingga Modul 4, dievaluasi secara statis berdasarkan instruksi/flowchart dan divalidasi melalui unit test execution.*
