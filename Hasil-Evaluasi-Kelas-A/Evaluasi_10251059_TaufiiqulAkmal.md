# Laporan Evaluasi Terperinci - Praktikum Struktur Data

---

## Data Mahasiswa
- **Nama:** Taufiiqul Akmal
- **NIM:** 10251059
- **Kelas:** Struktur Data A
- **GitHub Username:** `strukturdata-a-10251059-coder`

---

## Hasil Evaluasi Modul 1: Pengantar Struktur Data

### 1. Tugas 1: Pengembangan ADT Counter
- **Pengecekan Kode:**
  - Metode penambahan kalkulatif berjalan baik. Fungsi `subtract()` menggunakan pendekatan perbaikan kondisional tambahan yang menjamin proteksi data jika counter turun di bawah nol (`if self._value < 0: self._value = 0`).
- **Hasil Testing Codelab:** **PASSED** ✅ (100%)

### 2. Tugas 2: Pengembangan ADT Stack - Aplikasi Reverse String
- **Pengecekan Kode:**
  - `Stack` didesain sangat *clean* dengan konsep LIFO murni. `reverse_string()` menyusun string dengan operasi dorong/tarik yang disajikan dengan jelas pada skrip algoritma terstruktur di dalam komentar atas fungsinya.
- **Hasil Testing Codelab:** **PASSED** ✅ (100%)

### 3. Tugas 3: Analisis Kompleksitas Lanjutan
- **Tabel Analisis Kompleksitas & Jawaban:**
  - Pertanyaan dijawab dengan argumentasi rasional yang tepat sasaran. Contoh soal nomor 5 divisualisasikan dengan probabilitas kasus (1000000 pengguna -> 1 triliun loop pengecekan), memberikan gambaran Big-O konkrit pada realita pemodelan algoritma lamban $O(n^2)$.
- **Hasil Testing Codelab:** **PASSED** ✅ (100%)

**NILAI MODUL 1: 100**

---

## Hasil Evaluasi Modul 2: Array

### 1. Tugas 1: Pengembangan MyArray
- **Pengecekan Kode:**
  - Penyelesaian metode modifikasi letak internal terpusat aman dengan exception handler. *Reverse* array memanfaatkan metode *two pointer* konvensional dengan *assignment* sejajar `[left], [right] = [right], [left]`.
- **Hasil Testing Codelab:** **PASSED** ✅ (100%)

### 2. Tugas 2: Aplikasi Array - Statistik Data
- **Pengecekan Kode:**
  - Modul array `from tugas1... import MyArray` dikemas sebagai *dependency* yang modular. Metode deduplikasi melacak identitas variabel per indeks menggunakan sub-loop verifikasi yang valid.
- **Hasil Testing Codelab:** **PASSED** ✅ (100%)

### 3. Tugas 3: Aplikasi Matrix - Operasi Dasar
- **Pengecekan Kode:**
  - Validasi matrix tersusun apik sebelum melakukan eksekusi komputasional, mencegah ValueError sedini mungkin. Matrix symmetric berhasil diperiksa komparasi boolean dengan pengembalian statis.
- **Hasil Testing Codelab:** **PASSED** ✅ (100%)

**NILAI MODUL 2: 100**

---

## Hasil Evaluasi Modul 3: Single Linked List

### 1. Tugas 1: Implementasi Single Linked List
- **Pengecekan Kode:**
  - Semua method wajib (reverse, find_min, find_max, remove_value, to_list) diimplementasikan dengan benar dan lengkap. Reverse menggunakan iterasi tiga pointer yang efisien. find_min/find_max dengan traversal O(n). remove_value menangani semua kasus (head, tengah, tidak ditemukan) dengan benar.
- **Hasil Testing:** **PASSED** ✅ (100%)

### 2. Tugas 2: Aplikasi Polinomial
- **Pengecekan Kode:**
  - Kelas Polynomial diimplementasikan dengan baik menggunakan linked list terurut. add_term menangani insert terurut dan penggabungan koefisien duplikat. evaluate menggunakan traversal dengan perkalian pangkat. add_polynomials membangun polynomial hasil penjumlahan dengan benar.
- **Hasil Testing:** **PASSED** ✅ (100%)

### 3. Tugas 3: Aplikasi Music Playlist
- **Pengecekan Kode:**
  - Kelas Playlist dengan SongNode lengkap. Semua method (add_song, remove_song, play, next_song, current_song, total_duration, song_count, display, search_by_artist) diimplementasikan dengan benar. search_by_artist menggunakan exact case match yang konsisten dengan test case.
- **Hasil Testing:** **PASSED** ✅ (100%)

**NILAI MODUL 3: 100**

---

## Hasil Evaluasi Modul 4: Double Linked List & Circular Linked List

### 1. Tugas 1: Implementasi Double Linked List
- **Pengecekan Kode:**
  - DLL dengan head dan tail diimplementasikan lengkap. reverse menggunakan swap pointer prev/next setiap node secara efisien lalu swap head/tail. find_min, find_max, swap_nodes (tukar data), is_palindrome (two-pointer dari head dan tail) semuanya benar. is_palindrome menggunakan kondisi left != right dan left.prev != right untuk terminasi tengah.
- **Hasil Testing:** **PASSED** ✅ (100%)

### 2. Tugas 2: Aplikasi Text Editor Undo/Redo
- **Pengecekan Kode:**
  - TextEditor menggunakan DLL dengan StateNode. type_text menghapus future history sebelum menambah state baru (branching). undo/redo bergerak mundur/maju dengan benar. can_undo/can_redo memeriksa pointer prev/next. show_history menampilkan seluruh chain dari head dengan marker current yang ditempel pada node saat ini.
- **Hasil Testing:** **PASSED** ✅ (100%)

### 3. Tugas 3: Aplikasi Round Robin Scheduler
- **Pengecekan Kode:**
  - RoundRobinScheduler menggunakan Circular Linked List. add_process membangun CLL dengan benar. execute_one_cycle mengeksekusi quantum, memindahkan head ke next untuk rotasi, dan menghapus proses yang selesai. run menghasilkan timeline eksekusi yang tepat sesuai algoritma Round Robin.
- **Hasil Testing:** **PASSED** ✅ (100%)

**NILAI MODUL 4: 100**

---

## Hasil Evaluasi Modul 5: Stack

### 1. Tugas 1: Pengembangan Stack dengan Method Baru
- **Pengecekan Kode:** Semua method baru (`get_min`, `get_max`, `clear`, `to_list`, `copy`, `reverse`) diimplementasikan dengan benar. Semua test lulus.
- **Hasil Testing:** **PASSED** ✅ (100%)

### 2. Tugas 2: Konversi dan Evaluasi Ekspresi
- **Pengecekan Kode:** `infix_to_postfix()` benar termasuk right-associativity `^`. `evaluate_postfix()` dan `calculate()` benar. Semua test lulus.
- **Hasil Testing:** **PASSED** ✅ (100%)

### 3. Tugas 3: Aplikasi Browser History
- **Pengecekan Kode:** `BrowserHistory` menggunakan dua stack. `visit()`, `back()`, `forward()`, dan `current_page()` benar. Semua test lulus.
- **Hasil Testing:** **PASSED** ✅ (100%)

**NILAI MODUL 5: 100**

---

## Hasil Evaluasi Modul 6: Queue

> ❌ **Semua file Modul 6 kosong** saat evaluasi dilakukan (per April 2026). File `Tugas6.1`, `Tugas6.2`, dan `Tugas6.3` ada di repository namun berisi hanya baris kosong tanpa kode apapun.

### 1. Tugas 1: Implementasi Priority Queue
- **Hasil Testing:** **TIDAK ADA KODE** ❌ (0%)

### 2. Tugas 2: Implementasi Deque + Palindrome
- **Hasil Testing:** **TIDAK ADA KODE** ❌ (0%)

### 3. Tugas 3: Simulasi Antrian Bank
- **Hasil Testing:** **TIDAK ADA KODE** ❌ (0%)

**NILAI MODUL 6: 0** *(semua file kosong)*

---

### **NILAI RATA-RATA SEMENTARA: 83 🌟**

| Modul | Nilai |
|-------|-------|
| Modul 1 | 100 |
| Modul 2 | 100 |
| Modul 3 | 100 |
| Modul 4 | 100 |
| Modul 5 | 100 |
| Modul 6 | 0 |
| **Rata-rata** | **83** |
