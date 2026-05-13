# 📝 Laporan Evaluasi Terperinci - Praktikum Struktur Data

---

## 👤 Data Mahasiswa
- **Nama:** Jonatan Bagus Kristiawan
- **NIM:** 10251115
- **Kelas:** Struktur Data B
- **GitHub Username:** `strukturdata-b-JonatanBagusKristiawan`

---

## 🥇 Hasil Evaluasi Modul 1: Pengantar Struktur Data

### 1. Tugas 1: Pengembangan ADT Counter
- **Pengecekan Kode:**
  - Fungsi penambahan, pengurangan (`subtract`), dan eksekusi tes berjalan baik pada nilai tidak memunculkan output *error traceback*.
- **Hasil Testing Terminal:** **PASSED** ✅ (100%)

### 2. Tugas 2: Pengembangan ADT Stack - Aplikasi Reverse String
- **Pengecekan Kode:**
  - Kelas Stack dipanggil sesuai aturan dengan fitur parameter iterasi `append` dan `pop()` untuk merestorasi posisi karakter secara terbalik.
- **Hasil Testing Terminal:** **PASSED** ✅ (100%)

### 3. Tugas 3: Analisis Kompleksitas Lanjutan
- **Tabel Analisis Kompleksitas & Jawaban:**
  - Kode test mengeksekusi pengukuran loop tunggal, ganda bertumpuk, loop tripel secara dinamis terhadap nilai waktu *datetime*. Semuanya akurat terekam eksekusinya.
- **Hasil Testing Terminal:** **PASSED** ✅ (100%)

**✨ NILAI MODUL 1: 100 ✨**

---

## 🥈 Hasil Evaluasi Modul 2: Array

### 1. Tugas 1: Pengembangan MyArray
- **Pengecekan Kode:**
  - Metode insersi nilai di ujung `insert_end` maupun rotasi pembaharuan elemen (`update`), test fungsi *search* berhasil tanpa isu indeks luar jangkauan (Out of Range).
- **Hasil Testing Terminal:** **PASSED** ✅ (100%)

### 2. Tugas 2: Aplikasi Array - Statistik Data
- **Pengecekan Kode:**
  - Penjumlahan akumulatif statistik seperti operasi fungsi min/max, perhitungan rata, nilai largest array terkonfigurasi dengan tepat.
- **Hasil Testing Terminal:** **PASSED** ✅ (100%)

### 3. Tugas 3: Aplikasi Matrix - Operasi Dasar
- **Pengecekan Kode:**
  - Struktur logika perkalian nilai, penjabaran *addition*, validasi simetri diagonal untuk array/list matriks terselesaikan.
- **Hasil Testing Terminal:** **PASSED** ✅ (100%)

**✨ NILAI MODUL 2: 100 ✨**

---

## 🥉 Hasil Evaluasi Modul 3: Single Linked List

### 1. Tugas 1: Pengembangan LinkedList
- **Pengecekan Kode:** Implementasi sangat lengkap dengan semua method dasar praktikum. `reverse()`, `find_min()`, `find_max()`, `remove_value()`, dan `to_list()` diimplementasikan dengan benar menggunakan pola traverse standar. Test case identik dengan soal semuanya terpenuhi.
- **Hasil Testing Terminal:** **PASSED** ✅ (100%)

### 2. Tugas 2: Aplikasi Linked List - Polynomial
- **Pengecekan Kode:** Implementasi `Polynomial` lengkap. `add_term()` menjaga urutan pangkat dan menggabungkan koefisien menggunakan pendekatan merge sort-style dengan `current1`/`current2`. `evaluate()`, `degree()`, dan `add_polynomials()` benar. Display menggunakan format berbeda (`"3x^2"`, `"2x"`, `"5"`) — bersih dan valid. Semua assertion lulus.
- **Hasil Testing Terminal:** **PASSED** ✅ (100%)

### 3. Tugas 3: Aplikasi Linked List - Music Playlist
- **Pengecekan Kode:** Implementasi `Playlist` lengkap sesuai spesifikasi soal. `add_song()`, `remove_song()`, `play()`, `next_song()`, `current_song()`, `total_duration()`, `song_count()`, `display()`, dan `search_by_artist()` semuanya benar. `format_duration()` helper tersedia. Semua test case lulus.
- **Hasil Testing Terminal:** **PASSED** ✅ (100%)

**✨ NILAI MODUL 3: 100 ✨**

---

## 🏅 Hasil Evaluasi Modul 4: Double & Circular Linked List

### 1. Tugas 1: Pengembangan Double Linked List
- **Pengecekan Kode:** Ada duplikasi definisi `class DNode` (dua kali) di file — Python hanya menggunakan definisi terakhir, tidak menyebabkan error. `reverse()` menggunakan pendekatan berbeda: menyimpan `next_node`, lalu set `current.next = prev_node` dan `current.prev = next_node`, kemudian advance via `next_node`. Setelah loop, swap `head`/`tail`. Logika ini benar. `find_min()`, `find_max()`, `swap_nodes()`, `is_palindrome()`, `to_list()` semuanya benar. Semua test case lulus.
- **Hasil Testing Terminal:** **PASSED** ✅ (100%)

### 2. Tugas 2: Aplikasi DLL - Text Editor Undo/Redo
- **Pengecekan Kode:** Implementasi `TextEditor` benar secara fungsional. `type_text()` menggunakan loop `while current.next is not None: current.next = current.next.next` untuk menghapus semua node setelah current — pendekatan ini benar karena `current` tidak bergeser, tiap iterasi mempersingkat chain. Setelah loop, disambungkan ke `new_node`. `undo()`, `redo()`, branching semuanya benar. Semua test case lulus.
- **Hasil Testing Terminal:** **PASSED** ✅ (100%)

### 3. Tugas 3: Aplikasi CLL - Round Robin Scheduler
- **Pengecekan Kode:** Terdapat bug kritis pada `execute_one_cycle()`: ketika proses **belum selesai** (remaining > 0), tidak ada penggeseran `self.head = self.head.next`. Akibatnya `run()` akan **infinite loop** pada proses pertama yang belum selesai, karena proses yang sama terus-menerus dieksekusi tanpa berganti ke proses berikutnya. Logika CLL round-robin yang benar mengharuskan head digeser ke proses berikutnya setelah tiap cycle. `get_statistics()` hanya mengembalikan `total_time`.
- **Hasil Testing Terminal:** **FAILED** ❌ (infinite loop — head tidak diadvance untuk proses yang belum selesai)

**✨ NILAI MODUL 4: 80 ✨**

---

## 🥇 Hasil Evaluasi Modul 5: Stack

> Catatan: semua file dikumpulkan tanpa ekstensi `.py` (-15 per tugas).

### 1. Tugas 1: Pengembangan Stack
- **Pengecekan Kode:** Stack dengan `get_min/max`, `to_list`, `copy`, `reverse`, `clear` benar. File tanpa ekstensi `.py`.
- **Hasil Testing Terminal:** **PASSED** ✅ (85% — dikurangi 15 karena tidak ada ekstensi `.py`)

### 2. Tugas 2: Konversi dan Evaluasi Ekspresi
- **Pengecekan Kode:** Infix to postfix dengan right-associativity `^` benar. Full calculation lulus semua. File tanpa ekstensi `.py`.
- **Hasil Testing Terminal:** **PASSED** ✅ (85% — dikurangi 15 karena tidak ada ekstensi `.py`)

### 3. Tugas 3: Aplikasi Stack - Browser History
- **Pengecekan Kode:** BrowserHistory dengan 2 stack, visit/back/forward benar. File tanpa ekstensi `.py`.
- **Hasil Testing Terminal:** **PASSED** ✅ (85% — dikurangi 15 karena tidak ada ekstensi `.py`)

**✨ NILAI MODUL 5: 85 ✨** *((85+85+85)/3)*

---

## 🥈 Hasil Evaluasi Modul 6: Queue

> Catatan: semua file dikumpulkan tanpa ekstensi `.py` (-15 per tugas).

### 1. Tugas 1: Priority Queue
- **Pengecekan Kode:** PriorityQueue dengan enqueue/dequeue/peek dan FIFO prioritas sama benar. File tanpa `.py`.
- **Hasil Testing Terminal:** **PASSED** ✅ (85%)

### 2. Tugas 2: Deque dan Palindrome
- **Pengecekan Kode:** Deque add/remove/peek benar. `is_palindrome()` benar. File tanpa `.py`.
- **Hasil Testing Terminal:** **PASSED** ✅ (85%)

### 3. Tugas 3: Simulasi Antrian Bank
- **Pengecekan Kode:** Simulasi 20 customers, 3 tellers. Avg waiting time 0.30 menit (positif). File tanpa `.py`.
- **Hasil Testing Terminal:** **PASSED** ✅ (85%)

**✨ NILAI MODUL 6: 85 ✨** *((85+85+85)/3)*

---
## 🔢 Hasil Evaluasi Modul 7: Review & Studi Kasus (Persiapan UTS)

### 1. Tugas 1: Soal Teori (PDF)
- **Pengecekan:** PDF `Tugas7.1_10251115_Jonatan Bagus Kristiawan.pdf` ada di `minggu 7/`. Sekarang file Python sudah pakai ekstensi `.py`.
- **Hasil:** **DIKUMPULKAN** ✅ (100%)

### 2. Tugas 2: Sistem Manajemen Perpustakaan
- **Hasil Testing Terminal:** **PASSED** ✅ (100%)

**✨ NILAI MODUL 7: 100 ✨**

---

## 🔢 Hasil Evaluasi Modul 9: Tree & Binary Tree

### 1. Tugas 1: BinaryTree Class
- **Hasil Testing Terminal:** **PASSED** ✅ (100%)

### 2. Tugas 2: Expression Tree
- **Hasil Testing Terminal:** **PASSED** ✅ (100%)

### 3. Tugas 3: Analisis Kompleksitas Tree
- **Pengecekan Kode:** `height()` rekursif tanpa `sys.setrecursionlimit` → `RecursionError` pada skewed tree.
- **Hasil Testing Terminal:** **FAILED** ❌ (0%)

**✨ NILAI MODUL 9: 67 ✨**

---
## Hasil Evaluasi Modul 10: Binary Search Tree (BST)

### 1. Tugas 1: Pengembangan BST Class
- **Pengecekan Kode:** Semua test lulus. File menggunakan nama dengan trailing space sebelum .py (dapat dieksekusi).
- **Hasil Testing Terminal:** **PASSED** ✅ (100%)

### 2. Tugas 2: Sistem Phonebook dengan BST
- **Pengecekan Kode:** Semua test lulus.
- **Hasil Testing Terminal:** **PASSED** ✅ (100%)

### 3. Tugas 3: Analisis Performa BST
- **Pengecekan Kode:** Sorted BST height n-1 benar. Analisis lengkap n=50000.
- **Hasil Testing Terminal:** **PASSED** ✅ (100%)

**NILAI MODUL 10: 100**

---
### **NILAI RATA-RATA (Modul 1-7, 9, 10): 90.78**

| Modul | Nilai |
|-------|-------|
| Modul 1 | 100 |
| Modul 2 | 100 |
| Modul 3 | 100 |
| Modul 4 | 80 |
| Modul 5 | 85 |
| Modul 6 | 85 |
| Modul 7 | 100 |
| Modul 9 | 67 |
| Modul 10 | 100 |
| **Rata-rata** | **90.78** |

*Penilaian dievaluasi secara statis-manual berdasarkan kode program dan divalidasi melalui eksekusi unit test satu per satu.*
