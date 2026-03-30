# Laporan Evaluasi Terperinci - Praktikum Struktur Data

---

## Data Mahasiswa
- **Nama:** Muh. Asrul Syam
- **NIM:** 10251044
- **Kelas:** Struktur Data A
- **GitHub Username:** `strukturdata-a-Asrul-6`

---

## Hasil Evaluasi Modul 1: Pengantar Struktur Data

### 1. Tugas 1: Pengembangan ADT Counter
- **Pengecekan Kode:**
  - Metode `subtract()` bekerja baik dengan *if-else statement* yang memastikan nilai kembali ke `0` saat pengurang > nilai asli. Keseluruhan modul ADT Counter diimplementasi sesuai instruksi.
- **Hasil Testing Codelab:** **PASSED** ✅ (100%)

### 2. Tugas 2: Pengembangan ADT Stack - Aplikasi Reverse String
- **Pengecekan Kode:**
  - Penggunaan struktur class `Stack` diaplikasikan cermat. Pembalikan string (`reverse_string()`) mengandalkan push dan pop konvensional yang bersih.
- **Hasil Testing Codelab:** **PASSED** ✅ (100%)

### 3. Tugas 3: Analisis Kompleksitas Lanjutan
- **Tabel Analisis Kompleksitas & Jawaban:**
  - Definisi tiap Big-O dijelaskan *to the point*. Jawaban terkait Big-O O(n) mencari data maksimal serta limitasi O(n^2) rasional dengan referensi sistem media sosial raksasa.
- **Hasil Testing Codelab:** **PASSED** ✅ (100%)

**NILAI MODUL 1: 100**

---

## Hasil Evaluasi Modul 2: Array

### 1. Tugas 1: Pengembangan MyArray
- **Pengecekan Kode:**
  - Validasi panjang list kosong `len(self._elements) == 0` melindungi akses `IndexError`. Metode pencarian (*find*) dibungkus solid dengan pembanding awal `self._elements[0]`.
- **Hasil Testing Codelab:** **PASSED** ✅ (100%)

### 2. Tugas 2: Aplikasi Array - Statistik Data
- **Pengecekan Kode:**
  - Pengembangan method `calculate_average` sangat unik dan menarik di mana *while loop* diinisiasi secara mandiri, sedikit mengingatkan pada style bahasa C yang diadaptasi secara *Pythonic*.
- **Hasil Testing Codelab:** **PASSED** ✅ (100%)

### 3. Tugas 3: Aplikasi Matrix - Operasi Dasar
- **Pengecekan Kode:**
  - Pengecekan simetris matrix direalisasikan cermat dengan cara memanggil internal *function* `transpose = transpose_matrix(matrix)` dan mencocokkan nilainya pada *looping check*, sangat *reusable*.
- **Hasil Testing Codelab:** **PASSED** ✅ (100%)

**NILAI MODUL 2: 100**

---

## Hasil Evaluasi Modul 3: Single Linked List

### 1. Tugas 1: Implementasi Single Linked List
- **Pengecekan Kode:**
  - Implementasi `reverse()`, `find_min()`, `find_max()`, `remove_value()`, dan `to_list()` semuanya benar. Kode dibagi menjadi dua bagian yang jelas: method dari praktikum dan method baru (tugas). `find_min()` dan `find_max()` dimulai dari `self.head.next` dengan nilai awal dari `self.head` — efisien karena tidak mengecek head dua kali.
- **Hasil Testing:** **PASSED** ✅ (100%)

### 2. Tugas 2: Aplikasi Polinomial
- **Pengecekan Kode:**
  - Implementasi `Polynomial` menggunakan `TermNode`. `add_term()` mengurutkan dari pangkat tertinggi ke terendah dan menggabungkan koefisien dengan pangkat yang sama. Format display menggunakan notasi `x^n` eksplisit. Semua operasi matematika polinomial berfungsi dengan benar.
- **Hasil Testing:** **PASSED** ✅ (100%)

### 3. Tugas 3: Aplikasi Music Playlist
- **Pengecekan Kode:**
  - Aplikasi Music Playlist diimplementasikan lengkap dengan `SongNode`. Semua operasi utama (`song_count`, `total_duration`, `play`, `next_song`, `search_by_artist`, `remove_song`) berfungsi dengan tepat. Output memiliki pemisah baris ekstra yang membuat display lebih terbaca.
- **Hasil Testing:** **PASSED** ✅ (100%)

**NILAI MODUL 3: 100**

---

## Hasil Evaluasi Modul 4: Double Linked List & Circular Linked List

### 1. Tugas 1: Implementasi Double Linked List
- **Pengecekan Kode:**
  - `DoublyLinkedList` diimplementasikan lengkap dengan `DNode`. Method baru `reverse()` (membalik pointer prev/next in-place), `find_min()`, `find_max()` (traversal dari head), `swap_nodes()` (swap data, tidak swap node), dan `is_palindrome()` semuanya benar dan efisien.
- **Hasil Testing:** **PASSED** ✅ (100%)

### 2. Tugas 2: Aplikasi Text Editor Undo/Redo
- **Pengecekan Kode:**
  - `TextEditor` berbasis DLL dengan pointer `current` untuk posisi aktif. `type_text()` dan `append_text()` memotong redo chain saat ada input baru. `undo()` dan `redo()` berfungsi dengan benar. Display history menggunakan `<- current` sebagai penanda posisi.
- **Hasil Testing:** **PASSED** ✅ (100%)

### 3. Tugas 3: Aplikasi Round Robin Scheduler
- **Pengecekan Kode:**
  - `RoundRobinScheduler` menggunakan Circular Linked List. `add_process()` mempertahankan circular link dengan traversal ke tail. `execute_one_cycle()` menjalankan satu quantum dan berpindah ke proses berikutnya (`self.head = self.head.next`). Timeline eksekusi menampilkan interleaving Round Robin yang benar. Tampilan antrian (`[Process A:5]`) unik dan informatif.
- **Hasil Testing:** **PASSED** ✅ (100%)

**NILAI MODUL 4: 100**

---
### **NILAI RATA-RATA SEMENTARA: 100.00 🌟**

*Penilaian ini adalah nilai sementara untuk Modul 1 hingga Modul 4, dievaluasi secara statis berdasarkan instruksi/flowchart dan divalidasi melalui unit test execution.*
