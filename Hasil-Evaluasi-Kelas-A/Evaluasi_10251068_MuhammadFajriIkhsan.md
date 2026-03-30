# Laporan Evaluasi Terperinci - Praktikum Struktur Data

---

## Data Mahasiswa
- **Nama:** Muhammad Fajri Ikhsan
- **NIM:** 10251068
- **Kelas:** Struktur Data A
- **GitHub Username:** `strukturdata-a-Fajri-ITK`

---

## Hasil Evaluasi Modul 1: Pengantar Struktur Data

### 1. Tugas 1: Pengembangan ADT Counter
- **Pengecekan Kode:**
  - Metode `subtract()` disusun dengan struktur *if/elif* yang memagari operasi decrement agar hasil akhir absolut tidak pernah berada di bawah nilai nol. 
- **Hasil Testing Codelab:** **PASSED** ✅ (100%)

### 2. Tugas 2: Pengembangan ADT Stack - Aplikasi Reverse String
- **Pengecekan Kode:**
  - Metode pembalikan (*reverse_string*) beraksi valid dengan metode pengumpulan per karakter kembali (*string concatenation*) setelah dilempar satu per satu (*pop*) memastikan skema komputas LIFO berjalan konsisten.
- **Hasil Testing Codelab:** **PASSED** ✅ (100%)

### 3. Tugas 3: Analisis Kompleksitas Lanjutan
- **Tabel Analisis Kompleksitas & Jawaban:**
  - Ketajaman analisa nampak kuat di bagian algoritma skala besar `O(n²)`. Contoh *real case* pencocokan satu juta pengguna di platform digital memperterang konsekuensi dari *nested loop* secara faktual.
- **Hasil Testing Codelab:** **PASSED** ✅ (100%)

**NILAI MODUL 1: 100**

---

## Hasil Evaluasi Modul 2: Array

### 1. Tugas 1: Pengembangan MyArray
- **Pengecekan Kode:**
  - Operasi manipulasi standar terenkapsulasi secara wajar. Fungsi `reverse` cukup minimalis dan langsung mengandalkan *built-in function* `reverse()` dasar Python, efisien secara fungsi internal namun perlu ditekankan pada konsep algoritmanya (`two pointer`) kedepannya.
- **Hasil Testing Codelab:** **PASSED** ✅ (100%)

### 2. Tugas 2: Aplikasi Array - Statistik Data
- **Pengecekan Kode:**
  - `remove_duplicates` diformulasikan kreatif mengandalkan properti struktur data *dictionary keys* (`dict.fromkeys()`) untuk pemastian keunikan elemen, suatu bentuk solusi yang langka di level perkenalan pemrograman, memperlihatkan usaha eksploratif eksternal.
- **Hasil Testing Codelab:** **PASSED** ✅ (100%)

### 3. Tugas 3: Aplikasi Matrix - Operasi Dasar
- **Pengecekan Kode:**
  - Penggunaan *list comprehension* dominan digunakan di setiap blok metode tugas matriks terstruktur (`add_matrices`, `transpose_matrix`, dll), merefleksikan alur yang padat alias *one-liner Pythonic way*. Sangat mahir memanfaatkan fungsionalitas lanjutan seperti eksekusi *zip()*.
- **Hasil Testing Codelab:** **PASSED** ✅ (100%)

**NILAI MODUL 2: 100**

---

## Hasil Evaluasi Modul 3: Single Linked List

### 1. Tugas 1: Implementasi Single Linked List
- **Pengecekan Kode:**
  - Semua method wajib (reverse, find_min, find_max, remove_value, to_list) diimplementasikan dengan benar. Algoritma reverse menggunakan tiga pointer efisien. find_min/find_max dengan traversal linear O(n). remove_value menangani semua kasus dengan tepat. Display menggunakan format sedikit berbeda (tanpa spasi sebelum "-> NULL") namun fungsionalitas tetap benar.
- **Hasil Testing:** **PASSED** ✅ (100%)

### 2. Tugas 2: Aplikasi Polinomial
- **Pengecekan Kode:**
  - Polynomial diimplementasikan dengan linked list terurut. add_term menangani insert terurut dan penggabungan koefisien. Display menampilkan format `3x^2 + 2x^1 + 5` (untuk x^0 ditampilkan sebagai konstanta saja). evaluate dan add_polynomials berfungsi dengan benar.
- **Hasil Testing:** **PASSED** ✅ (100%)

### 3. Tugas 3: Aplikasi Music Playlist
- **Pengecekan Kode:**
  - Playlist dengan SongNode diimplementasikan lengkap. Semua method (add_song, remove_song, play, next_song, current_song, total_duration, song_count, display, search_by_artist) diimplementasikan dan berfungsi dengan benar. Format display menggunakan separator 30 karakter '='.
- **Hasil Testing:** **PASSED** ✅ (100%)

**NILAI MODUL 3: 100**

---

## Hasil Evaluasi Modul 4: Double Linked List & Circular Linked List

### 1. Tugas 1: Implementasi Double Linked List
- **Pengecekan Kode:**
  - DLL dengan head dan tail diimplementasikan lengkap. reverse, find_min, find_max, swap_nodes (tukar data), is_palindrome semuanya diimplementasikan dengan benar. is_palindrome menggunakan two-pointer dari head dan tail dengan terminasi loop yang tepat.
- **Hasil Testing:** **PASSED** ✅ (100%)

### 2. Tugas 2: Aplikasi Text Editor Undo/Redo
- **Pengecekan Kode:**
  - TextEditor menggunakan DLL dengan StateNode. Semua method (type_text, append_text, undo, redo, get_text, can_undo, can_redo, show_history) berfungsi dengan benar. Branching saat mengetik setelah undo menghapus future history dengan tepat. show_history menampilkan chain dengan marker ^current di akhir node saat ini.
- **Hasil Testing:** **PASSED** ✅ (100%)

### 3. Tugas 3: Aplikasi Round Robin Scheduler
- **Pengecekan Kode:**
  - RoundRobinScheduler menggunakan CLL. execute_one_cycle mengeksekusi quantum dan melakukan rotasi head ke proses berikutnya dengan benar. remove_process menghapus node dari CLL dengan tepat. Output timeline menunjukkan rotasi round-robin yang akurat antar Process A, B, C.
- **Hasil Testing:** **PASSED** ✅ (100%)

**NILAI MODUL 4: 100**

---
### **NILAI RATA-RATA SEMENTARA: 100.00 🌟**

*Penilaian ini adalah nilai sementara untuk Modul 1 hingga Modul 4, dievaluasi secara statis berdasarkan instruksi/flowchart dan divalidasi melalui unit test execution.*
