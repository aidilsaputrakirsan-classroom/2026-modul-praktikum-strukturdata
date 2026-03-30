# Laporan Evaluasi Terperinci - Praktikum Struktur Data

---

## Data Mahasiswa
- **Nama:** Muhammad Rasya Al Khalifi
- **NIM:** 10251071
- **Kelas:** Struktur Data A
- **GitHub Username:** `strukturdata-a-MuhRasyaAlKhalifi`

---

## Hasil Evaluasi Modul 1: Pengantar Struktur Data

### 1. Tugas 1: Pengembangan ADT Counter
- **Pengecekan Kode:**
  - Metode penambahan `add()` dan pemotongan `subtract()` tersusun logis sesuai batasan. Blok verifikasi negatif pada operasi kurang (`if self._value < 0: self._value = 0`) menjamin angka absolut tidak menjadi nilai tak masuk akal. 
- **Hasil Testing Codelab:** **PASSED** ✅ (100%)

### 2. Tugas 2: Pengembangan ADT Stack - Aplikasi Reverse String
- **Pengecekan Kode:**
  - Pengembalian string terbalik (*reverse_string*) sukses dibangun dengan *stack* Python konvensional lewat pengulangan *pop* sampai objek himpunan kosong secara beruntun (`while not stack.is_empty():`).
- **Hasil Testing Codelab:** **PASSED** ✅ (100%)

### 3. Tugas 3: Analisis Kompleksitas Lanjutan
- **Tabel Analisis Kompleksitas & Jawaban:**
  - Penjelasan cukup definitif dan rasional, mampu mendeskripsikan setiap kode kompleksitas dan skenarionya, contoh relasi lambatnya `O(n²)` terhadap *sistem media sosial dengan 10 juta pengguna* diuraikan dengan matematis jelas.
- **Hasil Testing Codelab:** **PASSED** ✅ (100%)

**NILAI MODUL 1: 100**

---

## Hasil Evaluasi Modul 2: Array

- **Pengecekan Kode:**
  - Folder `minggu2` atau `Minggu2` tidak ditemukan pada repositori GitHub mahasiswa. Tidak ada submission (pengumpulan tugas) untuk Modul 2.
- **Hasil Testing Codelab:** **FAILED** ❌ (0%)

**NILAI MODUL 2: 0**

---

## Hasil Evaluasi Modul 3: Single Linked List

### 1. Tugas 1: Implementasi Single Linked List
- **Pengecekan Kode:**
  - Semua method wajib (reverse, find_min, find_max, remove_value, to_list) diimplementasikan dengan benar dan lengkap. Algoritma reverse menggunakan tiga pointer efisien O(n). find_min/find_max dengan traversal linear. remove_value menangani semua kasus (head, tengah, tidak ditemukan) dengan tepat.
- **Hasil Testing:** **PASSED** ✅ (100%)

### 2. Tugas 2: Aplikasi Polinomial
- **Pengecekan Kode:**
  - Polynomial menggunakan linked list terurut dari pangkat tertinggi ke terendah. add_term menangani insert terurut dan penggabungan koefisien pada pangkat yang sama. evaluate menggunakan kalkulasi pangkat dengan benar. add_polynomials menghasilkan polynomial baru yang tepat.
- **Hasil Testing:** **PASSED** ✅ (100%)

### 3. Tugas 3: Aplikasi Music Playlist
- **Pengecekan Kode:**
  - Playlist dengan SongNode diimplementasikan lengkap. Semua method (add_song, remove_song, play, next_song, current_song, total_duration, song_count, display, search_by_artist) berfungsi dengan benar. Display menggunakan separator '=' 24 karakter.
- **Hasil Testing:** **PASSED** ✅ (100%)

**NILAI MODUL 3: 100**

---

## Hasil Evaluasi Modul 4: Double Linked List & Circular Linked List

### 1. Tugas 1: Implementasi Double Linked List
- **Pengecekan Kode:**
  - DLL dengan head dan tail diimplementasikan lengkap. reverse, find_min, find_max, swap_nodes, is_palindrome semuanya diimplementasikan dengan benar. is_palindrome menggunakan two-pointer approach dengan terminasi loop yang tepat. Semua test case palindrome dan non-palindrome lulus.
- **Hasil Testing:** **PASSED** ✅ (100%)

### 2. Tugas 2: Aplikasi Text Editor Undo/Redo
- **Pengecekan Kode:**
  - TextEditor menggunakan DLL dengan StateNode. type_text, append_text, undo, redo, get_text, can_undo, can_redo semuanya berfungsi benar. Branching saat pengetikan setelah undo ditangani dengan tepat. show_history menampilkan chain dengan marker ^current yang jelas.
- **Hasil Testing:** **PASSED** ✅ (100%)

### 3. Tugas 3: Aplikasi Round Robin Scheduler
- **Pengecekan Kode:**
  - RoundRobinScheduler menggunakan CLL. execute_one_cycle mengeksekusi quantum dan melakukan rotasi head ke proses berikutnya dengan benar. Output timeline menunjukkan rotasi round-robin yang akurat: A->B->C->A->B->C->A dengan quantum 2. Display queue menampilkan format yang informatif dengan burst time dan remaining time.
- **Hasil Testing:** **PASSED** ✅ (100%)

**NILAI MODUL 4: 100**

---
### **NILAI RATA-RATA SEMENTARA: 75.00 ⚠️**

*Penilaian ini adalah nilai sementara untuk Modul 1 hingga Modul 4, dievaluasi secara statis berdasarkan instruksi/flowchart dan divalidasi melalui unit test execution. Harap perhatikan nilai nol akibat absensi pengumpulan tugas Modul 2.*
