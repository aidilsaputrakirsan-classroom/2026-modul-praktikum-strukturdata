# 📝 Laporan Evaluasi Terperinci - Praktikum Struktur Data

---

## 👤 Data Mahasiswa
- **Nama:** Firni Fauziah Ramadhini
- **NIM:** 10231038
- **Kelas:** Struktur Data B
- **GitHub Username:** `strukturdata-b-firnifziah`

---

## 🥇 Hasil Evaluasi Modul 1: Pengantar Struktur Data

### 1. Tugas 1: Pengembangan ADT Counter
- **Pengecekan Kode:**
  - Metode penambahan fungsi baru (`add`, `subtract`, `multiply`) telah dioperasikan dengan baik tanpa mengganggu bawaannya. Substraksi bekerja memvalidasi kondisi minimum result `0`.
- **Hasil Testing Terminal:** **PASSED** ✅ (100%)

### 2. Tugas 2: Pengembangan ADT Stack - Aplikasi Reverse String
- **Pengecekan Kode:**
  - `Stack` memori ditambahkan iterasi method *push/pop* LIFO untuk membalik *reverse strings*. Program berjalan baik tanpa cacat pada compiler.
- **Hasil Testing Terminal:** **PASSED** ✅ (100%)

### 3. Tugas 3: Analisis Kompleksitas Lanjutan
- **Pengecekan Kode:**
  - Print logic profiler eksekusi untuk Time komputasi (triple array, rekursi `n/2`, iterasi max array value) berjalan sangat cepat dalam sekian _microsecond_.
- **Hasil Testing Terminal:** **PASSED** ✅ (100%)

**✨ NILAI MODUL 1: 100 ✨**

---

## 🥈 Hasil Evaluasi Modul 2: Array

### 1. Tugas 1: Pengembangan MyArray
- **Pengecekan Kode:**
  - Fungsi iterabel _indexing_ List `insert_front()`, *delete*, komputasi loop max dan min `count()` direkayasa memanipulasi _in-place array_ logic.
- **Hasil Testing Terminal:** **PASSED** ✅ (100%)

### 2. Tugas 2: Aplikasi Array - Statistik Data
- **Pengecekan Kode:**
  - Filter logic _second maximum array list_, menghapus baris duplikasi elemen iterasi ganda dan kalkulator `range` - mean dirangkai komputasinya.
- **Hasil Testing Terminal:** **PASSED** ✅ (100%)

### 3. Tugas 3: Aplikasi Matrix - Operasi Dasar
- **Pengecekan Kode:**
  - Logic matrix penjumlahan matriks array sum (`add_matrices()`), transpose matrix logic baris menjadi index sumbu kolom, beserta validasi matrix _Symmetric_ berjalan stabil.
- **Hasil Testing Terminal:** **PASSED** ✅ (100%)

**✨ NILAI MODUL 2: 100 ✨**

---

## 🥉 Hasil Evaluasi Modul 3: Single Linked List

### 1. Tugas 1: Pengembangan LinkedList
- **Pengecekan Kode:** Implementasi `reverse()`, `find_min()`, `find_max()`, `remove_value()`, dan `to_list()` lengkap dan benar. Terdapat artefak minor berupa deklarasi `class LinkedList:` bersarang di baris komentar dalam kelas yang sama (baris 18), namun tidak memengaruhi fungsionalitas karena seluruh method ada di kelas outer. Semua test case dari soal terpenuhi.
- **Hasil Testing Terminal:** **PASSED** ✅

### 2. Tugas 2: Aplikasi Linked List - Polynomial
- **Pengecekan Kode:** Implementasi `add_term()` (terurut descending, merge koefisien jika pangkat sama), `evaluate()`, `degree()`, dan `add_polynomials()` benar. Pengujian `P1+P2` menghasilkan `5x^2 + 6x^1 + 8x^0` dan `evaluate(1)=19` sesuai ekspektasi.
- **Hasil Testing Terminal:** **PASSED** ✅

### 3. Tugas 3: Aplikasi Linked List - Music Playlist
- **Pengecekan Kode:** Kelas `Playlist` mengimplementasikan `add_song()`, `remove_song()`, `play()`, `next_song()`, `current_song()`, `total_duration()`, `song_count()`, `display()`, dan `search_by_artist()` dengan benar. Penanganan current pointer saat remove_song sudah tepat.
- **Hasil Testing Terminal:** **PASSED** ✅

**✨ NILAI MODUL 3: 100 ✨**

---

## 🏅 Hasil Evaluasi Modul 4: Double & Circular Linked List

### 1. Tugas 1: Pengembangan Double Linked List
- **Pengecekan Kode:** `reverse()` menggunakan swap prev/next in-place dengan benar, `find_min()`/`find_max()` benar, `swap_nodes()` menukar data (bukan node), `is_palindrome()` menggunakan dua pointer dari head dan tail yang bertemu di tengah. Semua method berjalan sempurna.
- **Hasil Testing Terminal:** **PASSED** ✅

### 2. Tugas 2: Aplikasi DLL - Text Editor Undo/Redo
- **Pengecekan Kode:** `type_text()` memutus redo history dengan benar (branching), `append_text()` menggabungkan teks lama+baru, `undo()`/`redo()` menggeser pointer current, `can_undo()`/`can_redo()` benar. Branching test juga lulus.
- **Hasil Testing Terminal:** **PASSED** ✅

### 3. Tugas 3: Aplikasi CLL - Round Robin Scheduler
- **Pengecekan Kode:** `add_process()` membangun CLL dengan benar, `remove_process()` menangani kasus head dan non-head, `execute_one_cycle()` mengurangi `remaining_time` dan memindahkan head ke proses berikutnya. Output timeline sesuai ekspektasi (total 12 satuan waktu).
- **Hasil Testing Terminal:** **PASSED** ✅

**✨ NILAI MODUL 4: 100 ✨**

---

## 🔢 Hasil Evaluasi Modul 5: Stack

### 1. Tugas 1: Pengembangan Stack
- **Hasil Testing Terminal:** **PASSED** ✅ (100%)

### 2. Tugas 2: Infix → Postfix + Evaluasi Ekspresi
- **Pengecekan Kode:** Right-associativity `^`: `A^B^C` → `A B C ^ ^` ✅. Semua test case lulus.
- **Hasil Testing Terminal:** **PASSED** ✅ (100%)

### 3. Tugas 3: Browser History
- **Hasil Testing Terminal:** **PASSED** ✅ (100%)

**✨ NILAI MODUL 5: 100 ✨**

---

## 🔢 Hasil Evaluasi Modul 6: Queue

### 1. Tugas 1: Priority Queue
- **Hasil Testing Terminal:** **PASSED** ✅ (100%)

### 2. Tugas 2: Deque + is_palindrome()
- **Pengecekan Kode:** File yang dikumpulkan adalah file **praktikum** (`PRAKTIKUM 6.2: Implementasi Circular Queue`) — bukan implementasi Deque + `is_palindrome()` yang diminta. Konten tidak sesuai tugas.
- **Hasil Testing Terminal:** **FAILED** ❌ (0%) — salah konten

### 3. Tugas 3: Simulasi Antrian Bank
- **Pengecekan Kode:** File yang dikumpulkan adalah file **praktikum** (`PRAKTIKUM 6.3: Implementasi Queue dengan Linked List`) — bukan simulasi antrian bank 20 customer 3 teller. Konten tidak sesuai tugas.
- **Hasil Testing Terminal:** **FAILED** ❌ (0%) — salah konten

**✨ NILAI MODUL 6: 33 ✨**

---
### **🏆 NILAI RATA-RATA (Modul 1-6): 88.83 🏆**

*Penilaian dievaluasi secara statis-manual berdasarkan kode program dan divalidasi melalui eksekusi unit test satu per satu.*
