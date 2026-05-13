# 📝 Laporan Evaluasi Terperinci - Praktikum Struktur Data

---

## 👤 Data Mahasiswa
- **Nama:** Muh. Faizubaidillah H
- **NIM:** 10251018
- **Kelas:** Struktur Data B
- **GitHub Username:** `strukturdata-b-Faiz-codepy`

---

## 🥇 Hasil Evaluasi Modul 1: Pengantar Struktur Data

### 1. Tugas 1: Pengembangan ADT Counter
- **Pengecekan Kode:**
  - Fungsi penambahan, pengurangan (`subtract`), dan operasi skalar divalidasi dan menaati batas min/max.
- **Hasil Testing Terminal:** **PASSED** ✅ (100%)

### 2. Tugas 2: Pengembangan ADT Stack - Aplikasi Reverse String
- **Pengecekan Kode:**
  - Metode `pop()` pada stack digunakan secara tepat untuk menghasilkan *reverse order* tanpa bug.
- **Hasil Testing Terminal:** **PASSED** ✅ (100%)

### 3. Tugas 3: Analisis Kompleksitas Lanjutan
- **Tabel Analisis Kompleksitas & Jawaban:**
  - Pencatatan milidetik dari iterasi array profiler loop (O(n³)) berhasil dieksekusi dengan *performance benchmarking*.
- **Hasil Testing Terminal:** **PASSED** ✅ (100%)

**✨ NILAI MODUL 1: 100 ✨**

---

## 🥈 Hasil Evaluasi Modul 2: Array

### 1. Tugas 1: Pengembangan MyArray
- **Pengecekan Kode:**
  - Operasi insert/delete awal, pencarian elemen maksimal (`find_max`), komputasi kemunculan duplikat (`count`), serta array *reflection* dibuat *in-place*.
- **Hasil Testing Terminal:** **PASSED** ✅ (100%)

### 2. Tugas 2: Aplikasi Array - Statistik Data
- **Pengecekan Kode:**
  - Proses kalkulasi rerata/akumulasi dan deteksi *second largest array member* bekerja lurus tanpa IndexError/Traceback.
- **Hasil Testing Terminal:** **PASSED** ✅ (100%)

### 3. Tugas 3: Aplikasi Matrix - Operasi Dasar
- **Pengecekan Kode:**
  - Manipulasi baris-kolom array 2-dimensi sukses melewati test pengembalian _symmetric test_ dan operasi _transpose_.
- **Hasil Testing Terminal:** **PASSED** ✅ (100%)

**✨ NILAI MODUL 2: 100 ✨**

---

## 🥉 Hasil Evaluasi Modul 3: Single Linked List

### 1. Tugas 1: Pengembangan LinkedList
- **Pengecekan Kode:** Implementasi lengkap dan benar. `reverse()`, `find_min()`, `find_max()` semuanya menggunakan pola traverse yang tepat. `remove_value()` menangani kasus head dan non-head via pointer `prev`. `to_list()` benar. Ada variabel tak terpakai `Rev = None` di `find_min()` dan `find_max()` (sisa dari copy template), namun tidak mempengaruhi fungsionalitas. Semua test case lulus.
- **Hasil Testing Terminal:** **PASSED** ✅ (100%)

### 2. Tugas 2: Aplikasi Linked List - Polynomial
- **Pengecekan Kode:** Implementasi `add_term()` menangani penyisipan terurut dan penggabungan koefisien dengan benar. `add_polynomials()` menggunakan pendekatan merge dua list yang sudah terurut — efisien dan benar. `degree()` dan `evaluate()` benar. `display()` memformat output dengan notasi berbeda (`"3x^2"` untuk exp>1, `"2x"` untuk exp=1, `"5"` untuk exp=0) yang sedikit berbeda dari expected output soal tapi hasil kalkulasinya tepat.
- **Hasil Testing Terminal:** **PASSED** ✅ (100%)

### 3. Tugas 3: Aplikasi Linked List - Music Playlist
- **Pengecekan Kode:** Implementasi lengkap sesuai spesifikasi soal. `add_song()`, `remove_song()`, `play()`, `next_song()`, `current_song()`, `total_duration()`, `song_count()`, `display()`, dan `search_by_artist()` semuanya diimplementasikan dengan benar. Semua test case dengan 4 lagu Queen/Eagles/Led Zeppelin lulus.
- **Hasil Testing Terminal:** **PASSED** ✅ (100%)

**✨ NILAI MODUL 3: 100 ✨**

---

## 🏅 Hasil Evaluasi Modul 4: Double & Circular Linked List

### 1. Tugas 1: Pengembangan Double Linked List
- **Pengecekan Kode:** Implementasi DLL sangat lengkap dengan semua method praktikum disertakan. `reverse()` menggunakan Python swap `current.prev, current.next = current.next, current.prev` lalu maju via `current.prev` — benar. `find_min()` mulai dari `head.next` setelah inisialisasi dari `head.data` — benar. `swap_nodes()` hanya tukar data. `is_palindrome()` menggunakan pointer kiri-kanan. Semua test case DLL lulus.
- **Hasil Testing Terminal:** **PASSED** ✅ (100%)

### 2. Tugas 2: Aplikasi DLL - Text Editor Undo/Redo
- **Pengecekan Kode:** Implementasi `TextEditor` benar. `type_text()` memutus history redo dengan mengatur `current.next.prev = None` lalu `current.next = None`, kemudian menyambungkan node baru. `undo()` dan `redo()` bergerak mundur/maju dengan return `True/False`. Branching setelah undo tertangani dengan benar. Semua test case lulus.
- **Hasil Testing Terminal:** **PASSED** ✅ (100%)

### 3. Tugas 3: Aplikasi CLL - Round Robin Scheduler
- **Pengecekan Kode:** Terdapat bug serius pada `execute_one_cycle()`: fungsi melakukan `return result` pada baris 106 SEBELUM blok `if process.remaining_time <= 0` di baris 112-117. Seluruh logika penghapusan proses dan penggeseran head menjadi **dead code** (tidak pernah dieksekusi). Akibatnya, `run()` akan mengalami **infinite loop** karena proses tidak pernah dihapus dari antrian. `run()` juga memanggil `self.remove_process(self.head)` secara terpisah yang akan menghapus proses yang salah.
- **Hasil Testing Terminal:** **FAILED** ❌ (infinite loop karena dead code setelah return)

**✨ NILAI MODUL 4: 80 ✨**

## 🔢 Hasil Evaluasi Modul 5: Stack

### 1. Tugas 1: Pengembangan Stack
- **Hasil Testing Terminal:** **PASSED** ✅ (100%)

### 2. Tugas 2: Infix → Postfix + Evaluasi Ekspresi
- **Pengecekan Kode:** Right-associativity `^`: `A^B^C` → `A B C ^ ^` ✅.
- **Hasil Testing Terminal:** **PASSED** ✅ (100%)

### 3. Tugas 3: Browser History
- **Hasil Testing Terminal:** **PASSED** ✅ (100%)

**✨ NILAI MODUL 5: 100 ✨**

---
## 🔢 Hasil Evaluasi Modul 6: Queue

### 1. Tugas 1: Priority Queue
- **Hasil Testing Terminal:** **PASSED** ✅ (100%)

### 2. Tugas 2: Deque + is_palindrome()
- **Pengecekan Kode:** `is_palindrome()` mengembalikan `True`/`False` benar untuk semua kasus.
- **Hasil Testing Terminal:** **PASSED** ✅ (100%)

### 3. Tugas 3: Simulasi Antrian Bank
- **Pengecekan Kode:** 20 customer, 3 teller, avg waiting time 0.30 menit (positif, logika benar).
- **Hasil Testing Terminal:** **PASSED** ✅ (100%)

**✨ NILAI MODUL 6: 100 ✨**


---
## 🔢 Hasil Evaluasi Modul 7: Review & Studi Kasus (Persiapan UTS)

### 1. Tugas 1: Soal Teori (PDF)
- **Pengecekan:** PDF + DOCX ada di `Tugas/Minggu 7/`.
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
- **Pengecekan Kode:** Semua test lulus.
- **Hasil Testing Terminal:** **PASSED** ✅ (100%)

### 2. Tugas 2: Sistem Phonebook dengan BST
- **Pengecekan Kode:** Semua test lulus.
- **Hasil Testing Terminal:** **PASSED** ✅ (100%)

### 3. Tugas 3: Analisis Performa BST
- **Pengecekan Kode:** Sorted BST height n-1 benar. Analisis lengkap n=50000.
- **Hasil Testing Terminal:** **PASSED** ✅ (100%)

**NILAI MODUL 10: 100**

---
### **NILAI RATA-RATA (Modul 1-7, 9, 10): 94.11**

| Modul | Nilai |
|-------|-------|
| Modul 1 | 100 |
| Modul 2 | 100 |
| Modul 3 | 100 |
| Modul 4 | 80 |
| Modul 5 | 100 |
| Modul 6 | 100 |
| Modul 7 | 100 |
| Modul 9 | 67 |
| Modul 10 | 100 |
| **Rata-rata** | **94.11** |

*Penilaian dievaluasi secara statis-manual berdasarkan kode program dan divalidasi melalui eksekusi unit test satu per satu.*
