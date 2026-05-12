# 📝 Laporan Evaluasi Terperinci - Praktikum Struktur Data

---

## 👤 Data Mahasiswa
- **Nama:** Taufiq Erik Herliansyah
- **NIM:** 10251009
- **Kelas:** Struktur Data B
- **GitHub Username:** `strukturdata-b-Taufiqerikhrl`

---

## 🥇 Hasil Evaluasi Modul 1: Pengantar Struktur Data

### 1. Tugas 1: Pengembangan ADT Counter
- **Pengecekan Kode:**
  - Metode penambahan fungsi baru (`add`, `subtract`, `multiply`) telah dioperasikan dengan baik tanpa mengganggu bawaannya. Substraksi bekerja memvalidasi minimum result `0`.
- **Hasil Testing Terminal:** **PASSED** ✅ (100%)

### 2. Tugas 2: Pengembangan ADT Stack - Aplikasi Reverse String
- **Pengecekan Kode:**
  - `Stack` memori ditambahkan iterasi method *push/pop* LIFO untuk membalik *reverse strings*. Program berjalan baik tanpa cacat.
- **Hasil Testing Terminal:** **PASSED** ✅ (100%)

### 3. Tugas 3: Analisis Kompleksitas Lanjutan
- **Pengecekan Kode:**
  - File ini tidak mengeksekusi tes Python, melainkan berisi dokumentasi text langsung (via Python triple quotes `"""`) tentang analisis tabel _Time Execution_ (A, B, C, D, E, dan F) dan pertanyaan terkait fungsi-nya dan dijabarkan dengan lumayan lengkap.
- **Hasil Pemeriksaan Langsung:** **PASSED** ✅ (100%)

**✨ NILAI MODUL 1: 100 ✨**

---

## 🥈 Hasil Evaluasi Modul 2: Array

### 1. Tugas 1: Pengembangan MyArray
- **Pengecekan Kode:**
  - List logic Array dari *insert_front*, delete list terdepan dan rekursi *reverse* mereset struktur indeks array berjalan secara statikal.
- **Hasil Testing Terminal:** **PASSED** ✅ (100%)

### 2. Tugas 2: Aplikasi Array - Statistik Data
- **Pengecekan Kode:**
  - Kode program merespon komputasi _range_ fungsi avg/mean list, fungsi second maximum element dan fungsi `sum` statistik.
- **Hasil Testing Terminal:** **PASSED** ✅ (100%)

### 3. Tugas 3: Aplikasi Matrix - Operasi Dasar
- **Pengecekan Kode:**
  - Method penambahan array dimensi matrix (`add_matrices()`), rotasi *transpose*, pengecekan is_symmetric, dijalankan stabil.
- **Hasil Testing Terminal:** **PASSED** ✅ (100%)

**✨ NILAI MODUL 2: 100 ✨**

---

## 🥉 Hasil Evaluasi Modul 3: Single Linked List

### 1. Tugas 1: Pengembangan LinkedList
- **Pengecekan Kode:** Implementasi `reverse()`, `find_min()`, `find_max()`, `remove_value()`, dan `to_list()` seluruhnya bersih dan efisien. Algoritma reverse menggunakan teknik tiga-pointer (prev, current, next_node) secara benar. `remove_value` menangani kasus node pertama dan node tidak ditemukan (return False).
- **Hasil Testing Terminal:** **PASSED** ✅

### 2. Tugas 2: Aplikasi Linked List - Polynomial
- **Pengecekan Kode:** `add_term` mengurutkan suku dari pangkat tertinggi ke terendah dan menggabungkan koefisien jika pangkat sudah ada. `evaluate(x)` menggunakan formula polinom benar. `add_polynomials` mengiterasi kedua list dan menggabungkan dengan `add_term`.
- **Hasil Testing Terminal:** **PASSED** ✅

### 3. Tugas 3: Aplikasi Linked List - Music Playlist
- **Pengecekan Kode:** Semua method (`add_song`, `remove_song`, `play`, `next_song`, `current_song`, `total_duration`, `song_count`, `search_by_artist`, `display`) diimplementasikan dengan benar. `remove_song` menangani kasus `current` song yang dihapus.
- **Hasil Testing Terminal:** **PASSED** ✅

**✨ NILAI MODUL 3: 100 ✨**

---

## 🏅 Hasil Evaluasi Modul 4: Double & Circular Linked List

- **Pengecekan Kode:** Tidak ditemukan folder atau file submission terkait Modul 4 (minggu4 / tugas4) di repositori mahasiswa ini.
- **Hasil Testing Terminal:** **TIDAK ADA SUBMISSION** ❌

### 1. Tugas 1: Pengembangan Double Linked List
- **Pengecekan Kode:** Tidak ada file.
- **Hasil Testing Terminal:** **FAILED** ❌

### 2. Tugas 2: Aplikasi DLL - Text Editor Undo/Redo
- **Pengecekan Kode:** Tidak ada file.
- **Hasil Testing Terminal:** **FAILED** ❌

### 3. Tugas 3: Aplikasi CLL - Round Robin Scheduler
- **Pengecekan Kode:** Tidak ada file.
- **Hasil Testing Terminal:** **FAILED** ❌

**✨ NILAI MODUL 4: 0 ✨**

---

## 🔢 Hasil Evaluasi Modul 5: Stack

### 1. Tugas 1: Pengembangan Stack
- **Pengecekan Kode:** Implementasi semua method baru (`get_min`, `get_max`, `clear`, `to_list`, `copy`, `reverse`) benar secara logika. File tidak mengandung kode test (tidak ada output saat dijalankan).
- **Hasil Testing Terminal:** **PASSED** ✅ (100%) — review statis

### 2. Tugas 2: Infix → Postfix + Evaluasi Ekspresi
- **Pengecekan Kode:** Kondisi right-associativity `^` di while loop benar: `token != '^'` ✅. `A^B^C` → `A B C ^ ^` benar. File tidak mengandung kode test.
- **Hasil Testing Terminal:** **PASSED** ✅ (100%) — review statis

### 3. Tugas 3: Browser History
- **Pengecekan Kode:** `BrowserHistory` dengan dua stack, `visit()` clear forward, `back()`/`forward()` benar. File tidak mengandung kode test.
- **Hasil Testing Terminal:** **PASSED** ✅ (100%) — review statis

**✨ NILAI MODUL 5: 100 ✨**

---

## 🔢 Hasil Evaluasi Modul 6: Queue

### 1. Tugas 1: Priority Queue
- **Pengecekan Kode:** File `minggu6/Tugas1` berisi konten **Modul 5 T1 (Stack)** — duplikat minggu5. Bukan Priority Queue yang diminta.
- **Hasil Testing Terminal:** **FAILED** ❌ (0%) — salah konten

### 2. Tugas 2: Deque + is_palindrome()
- **Pengecekan Kode:** File `minggu6/Tugas2` berisi konten **Modul 5 T2 (Infix-Postfix)** — duplikat minggu5. Bukan Deque yang diminta.
- **Hasil Testing Terminal:** **FAILED** ❌ (0%) — salah konten

### 3. Tugas 3: Simulasi Antrian Bank
- **Pengecekan Kode:** File `minggu6/Tugas3` berisi konten **Modul 5 T3 (Browser History)** — duplikat minggu5. Bukan simulasi bank yang diminta.
- **Hasil Testing Terminal:** **FAILED** ❌ (0%) — salah konten

**✨ NILAI MODUL 6: 0 ✨**

---
## 🔢 Hasil Evaluasi Modul 7: Review & Studi Kasus (Persiapan UTS)

### 1. Tugas 1: Soal Teori (PDF)
- **Pengecekan Kode:** PDF `TUGAS1_10251009_...pdf` ada di folder `minggu 7/` (folder dievaluasi via `git show` karena ada spasi di nama).
- **Hasil:** **DIKUMPULKAN** ✅ (100%)

### 2. Tugas 2: Sistem Manajemen Perpustakaan
- **Pengecekan Kode:** `Library` lengkap (linked list, stack, queue, priority queue). Semua 8 test lulus via `git show ... | python`.
- **Hasil Testing Terminal:** **PASSED** ✅ (100%)

**✨ NILAI MODUL 7: 100 ✨**

---

## 🔢 Hasil Evaluasi Modul 9: Tree & Binary Tree

### 1-3. Semua Tugas
- **Pengecekan Kode:** Tidak ada folder `minggu 9` / `Minggu9`. File `Tugas1/2/3_10251009_...py` di root repo adalah tugas terstruktur lama (ADT Counter, Reverse String, Analisis Kompleksitas — di-commit Maret 2026 sebelum modul 9), bukan submission BinaryTree/Expression Tree.
- **Hasil:** **TIDAK DIKUMPULKAN** ❌ (0%)

**✨ NILAI MODUL 9: 0 ✨**

---
### **🏆 NILAI RATA-RATA (Modul 1-7, 9): 62.50 🏆**

*Penilaian dievaluasi secara statis-manual berdasarkan kode program dan divalidasi melalui eksekusi unit test satu per satu.*
