# 📝 Laporan Evaluasi Terperinci - Praktikum Struktur Data

---

## 👤 Data Mahasiswa
- **Nama:** Heldawati ilham
- **NIM:** 10251042
- **Kelas:** Struktur Data B
- **GitHub Username:** `strukturdata-b-heldaa127`

---

## 🥇 Hasil Evaluasi Modul 1: Pengantar Struktur Data

- **Pengecekan Kode:**
  - Fungsi iterasi penambahan gagal jalan karena memanggil properti attribute `self.value` alangkah baiknya `self._value`. Hal ini teridentifikasi pada AttributeError di **Tugas 1**.
  - Objek *Stack* di **Tugas 2** memunculkan `AttributeError` karena pemanggilan `self.items` keliru dari yang seharusnya `self._items`.
- **Hasil Testing Terminal:** **FAILED** ❌ (0%)

**✨ NILAI MODUL 1: 0 ✨**

---

## 🥈 Hasil Evaluasi Modul 2: Array

- **Pengecekan Kode:**
  - **Tugas 1** gagal. Penulisan nama method `arr.insert_end` padahal yang dibuat dan dicari adalah rutin `arr.insert_front()`.
  - **Tugas 2** mencetak error fatal. Objek `MyArray` yang mendefinisikan class statistik Array tak-terdefinisikan (`NameError`).
  - **Tugas 3** gagal. Program `add_matrices` salah mengkalkulasikan variabel hingga me-return *NoneType* yang akhirnya bukan index/subscriptable value.
- **Hasil Testing Terminal:** **FAILED** ❌ (0%)

**✨ NILAI MODUL 2: 0 ✨**

---

## 🥉 Hasil Evaluasi Modul 3: Single Linked List

### 1. Tugas 1: Pengembangan LinkedList
- **Pengecekan Kode:** Implementasi `reverse()`, `find_min()`, `find_max()`, `remove_value()`, dan `to_list()` semuanya benar dan berjalan mulus. Terdapat typo minor pada `display()` yang mencetak `"LingkedList:"` (seharusnya `"LinkedList:"`), namun tidak memengaruhi logika dan test assertion. Semua test case lulus.
- **Hasil Testing Terminal:** **PASSED** ✅

### 2. Tugas 2: Aplikasi Linked List - Polynomial
- **Pengecekan Kode:** `add_term()` menangani insertion terurut dan merge koefisien dengan benar. Terdapat edge case penghapusan node saat koefisien jadi 0. `evaluate()` dan `degree()` benar. `add_polynomials()` menggunakan merge pointer dua arah.
- **Hasil Testing Terminal:** **PASSED** ✅

### 3. Tugas 3: Aplikasi Linked List - Music Playlist
- **Pengecekan Kode:** Semua method `Playlist` berjalan dengan benar. `search_by_artist()` menggunakan `lower()` untuk case-insensitive matching (bonus), namun test menggunakan string yang sudah cocok. `remove_song()` dan navigasi current benar.
- **Hasil Testing Terminal:** **PASSED** ✅

**✨ NILAI MODUL 3: 100 ✨**

---

## 🏅 Hasil Evaluasi Modul 4: Double & Circular Linked List

### 1. Tugas 1: Pengembangan Double Linked List
- **Pengecekan Kode:** `reverse()` swap prev/next in-place, `find_min()`/`find_max()` traversal dari head, `swap_nodes()` tukar data, `is_palindrome()` dua pointer. Semua implementasi benar dan test lulus.
- **Hasil Testing Terminal:** **PASSED** ✅

### 2. Tugas 2: Aplikasi DLL - Text Editor Undo/Redo
- **Pengecekan Kode:** `type_text()` memutus redo history saat mengetik baru, undo/redo berjalan benar dengan pointer `current`. `show_history()` menampilkan riwayat dengan tanda `<== current`. Test branching lulus.
- **Hasil Testing Terminal:** **PASSED** ✅

### 3. Tugas 3: Aplikasi CLL - Round Robin Scheduler
- **Pengecekan Kode:** CLL Round Robin diimplementasi lengkap. `execute_one_cycle()` menggunakan `max(..., 0)` untuk keamanan remaining_time. `run()` mencetak timeline dengan format yang sedikit berbeda dari template (tidak ada "All processes completed!" dengan tanda seru) namun fungsional benar.
- **Hasil Testing Terminal:** **PASSED** ✅

**✨ NILAI MODUL 4: 100 ✨**

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

- **Pengecekan Kode:** Tidak ada submission Modul 6 saat evaluasi dilakukan.

**✨ NILAI MODUL 6: 0 ✨**


---
## 🔢 Hasil Evaluasi Modul 7: Review & Studi Kasus (Persiapan UTS)

### 1. Tugas 1: Soal Teori (PDF)
- **Pengecekan:** PDF `Tugas7_10251042_Heldawati ilham.pdf` ada di `minggu 7/`.
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
- **Pengecekan Kode:** Tidak ada folder/file Modul 10 di repo.
- **Hasil Testing Terminal:** **TIDAK DIKUMPULKAN** ❌ (0%)

### 2. Tugas 2: Sistem Phonebook dengan BST
- **Pengecekan Kode:** Tidak ada folder/file Modul 10 di repo.
- **Hasil Testing Terminal:** **TIDAK DIKUMPULKAN** ❌ (0%)

### 3. Tugas 3: Analisis Performa BST
- **Pengecekan Kode:** Tidak ada folder/file Modul 10 di repo.
- **Hasil Testing Terminal:** **TIDAK DIKUMPULKAN** ❌ (0%)

**NILAI MODUL 10: 0**

---
### **NILAI RATA-RATA (Modul 1-7, 9, 10): 51.89**

| Modul | Nilai |
|-------|-------|
| Modul 1 | 0 |
| Modul 2 | 0 |
| Modul 3 | 100 |
| Modul 4 | 100 |
| Modul 5 | 100 |
| Modul 6 | 0 |
| Modul 7 | 100 |
| Modul 9 | 67 |
| Modul 10 | 0 |
| **Rata-rata** | **51.89** |

*Penilaian dievaluasi secara statis-manual berdasarkan kode program dan divalidasi melalui eksekusi unit test satu per satu.*
