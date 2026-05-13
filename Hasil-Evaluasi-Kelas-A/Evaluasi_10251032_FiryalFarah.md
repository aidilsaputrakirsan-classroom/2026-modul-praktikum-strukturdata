# Laporan Evaluasi Terperinci - Praktikum Struktur Data

---

## Data Mahasiswa
- **Nama:** Firyal Farah Khulaidah
- **NIM:** 10251032
- **Kelas:** Struktur Data A
- **GitHub Username:** `strukturdata-a-FiryalFarah`

---

## Hasil Evaluasi Modul 1: Pengantar Struktur Data

### 1. Tugas 1: Pengembangan ADT Counter
- **Pengecekan Kode:**
  - Metode operasional kalkulasi statis Counter (`add()`, `subtract()`, `multiply()`) terimplementasi mulus dengan validasi `< 0` yang aman dan sesuai flowchart.
- **Hasil Testing Codelab:** **PASSED** ✅ (100%)

### 2. Tugas 2: Pengembangan ADT Stack - Aplikasi Reverse String
- **Pengecekan Kode:**
  - Stack pop terlindungi validasi _is_empty()_. Pemisahan method _print_stack_ di-coding tepat sasaran dan operasi *reverse string* via inersi stack (`pop()` dan _concatenation_) sangat bersih.
- **Hasil Testing Codelab:** **PASSED** ✅ (100%)

### 3. Tugas 3: Analisis Kompleksitas Lanjutan
- **Tabel Analisis Kompleksitas & Jawaban:**
  - Pemaparan notasi Big-O (konstan, linear, logaritmik, kuadratik, kubik) pada tabel cukup singkat namun jelas intisarinya. Simulasi waktu eksekusi dipahami dengan baik (ex: kasus sorting ecommerce untuk Big-O $O(n^2)$).
- **Hasil Testing Codelab:** **PASSED** ✅ (100%)

**NILAI MODUL 1: 100**

---

## Hasil Evaluasi Modul 2: Array

### 1. Tugas 1: Pengembangan MyArray
- **Pengecekan Kode:**
  - Error Handling tertangani ideal dengan menaikkan argumen `ValueError` atau `IndexError` pada posisi list kosong. Pemutaran array *reverse()* in-place `self._elements[left], self._elements[right] = self._elements[right], self._elements[left]` ditangani secara ringkas.
- **Hasil Testing Codelab:** **PASSED** ✅ (100%)

### 2. Tugas 2: Aplikasi Array - Statistik Data
- **Pengecekan Kode:**
  - Penghapusan duplikat *remove_duplicates* mendelegasikan iterasi perbandingan O(n^2) melalui panggilan linear dari instance method pencarian (`result.search() == -1`), ini *best practice* yang dianjurkan.
- **Hasil Testing Codelab:** **PASSED** ✅ (100%)

### 3. Tugas 3: Aplikasi Matrix - Operasi Dasar
- **Pengecekan Kode:**
  - Fungsi iteratif matriks mengelola komputasi *matrix operations* secara natural. Algoritma perbandingan transposisi (*is_symmetric*) dikembangkan elegan membedakan dimensi `matrix[i][j] != matrix[j][i]` untuk menghindari nested memori yang boros.
- **Hasil Testing Codelab:** **PASSED** ✅ (100%)

**NILAI MODUL 2: 100**


---

## Hasil Evaluasi Modul 3: Single Linked List

### 1. Tugas 1: Implementasi Single Linked List
- **Pengecekan Kode:**
  - `reverse()`, `find_min()`, `find_max()`, `remove_value()`, dan `to_list()` terimplementasi dengan tepat dan terstruktur. Error handling menggunakan `raise ValueError/IndexError` sudah sesuai. Kode bersih tanpa duplikasi.
- **Hasil Testing:** **PASSED** ✅ (100%)

### 2. Tugas 2: Aplikasi Polynomial
- **Pengecekan Kode:**
  - Implementasi `Polynomial` menggunakan linked list berurutan eksponen menurun. `add_term()` menangani penggabungan term dengan eksponen sama. `evaluate()` menghitung nilai polynomial dengan benar. `add_polynomials()` melakukan merge dengan tepat.
- **Hasil Testing:** **PASSED** ✅ (100%)

### 3. Tugas 3: Aplikasi Music Playlist
- **Pengecekan Kode:**
  - Semua operasi playlist lengkap dan berfungsi. `search_by_artist()`, `total_duration()`, `song_count()` diimplementasikan secara benar. Navigasi lagu menggunakan pointer `current` yang dikelola dengan tepat.
- **Hasil Testing:** **PASSED** ✅ (100%)

**NILAI MODUL 3: 100**

---

## Hasil Evaluasi Modul 4: Double Linked List & Circular Linked List

### 1. Tugas 1: Implementasi Double Linked List
- **Pengecekan Kode:**
  - `reverse()` membalik pointer in-place dengan benar. `find_min()`, `find_max()`, `swap_nodes()`, dan `is_palindrome()` berfungsi sesuai spesifikasi.
- **Hasil Testing:** **PASSED** ✅ (100%)

### 2. Tugas 2: Aplikasi Text Editor Undo/Redo
- **Pengecekan Kode:**
  - `TextEditor` mengelola state teks menggunakan DLL. Semua operasi (`type_text`, `append_text`, `undo`, `redo`, `can_undo`, `can_redo`, `show_history`) berfungsi dengan benar termasuk branching.
- **Hasil Testing:** **PASSED** ✅ (100%)

### 3. Tugas 3: Aplikasi Round Robin Scheduler
- **Pengecekan Kode:**
  - **Bug Moderat:** Terdapat bug pada `execute_one_cycle()` — setelah `remove_process(process)` menghapus proses yang selesai dan otomatis meng-update `self.head` ke node berikutnya, kode kemudian kembali mengeksekusi `self.head = self.head.next` pada baris 113-114, menyebabkan head maju dua langkah dan melewatkan satu proses. Akibatnya urutan eksekusi setelah Process B selesai menjadi tidak sesuai ekspektasi (Process A selesai sebelum Process C). Total waktu 12 tetap benar namun urutan completion berbeda dari standar Round Robin.
- **Hasil Testing:** **FAILED** ❌ (Bug logika rotasi head setelah proses selesai — urutan completion salah)

**NILAI MODUL 4: 90**

---

## Hasil Evaluasi Modul 5: Stack

### 1. Tugas 1: Pengembangan Stack dengan Method Baru
- **Pengecekan Kode:** Semua method benar, semua test lulus.
- **Hasil Testing:** **PASSED** ✅ (100%)

### 2. Tugas 2: Konversi dan Evaluasi Ekspresi
- **Pengecekan Kode:** `infix_to_postfix()` benar termasuk right-associativity `^`. Semua test lulus.
- **Hasil Testing:** **PASSED** ✅ (100%)

### 3. Tugas 3: Aplikasi Browser History
- **Pengecekan Kode:** Browser history benar.
- **Hasil Testing:** **PASSED** ✅ (100%)

**NILAI MODUL 5: 100**

---

## Hasil Evaluasi Modul 6: Queue

### 1. Tugas 1: Implementasi Priority Queue
- **Pengecekan Kode:** Priority Queue benar, semua test lulus.
- **Hasil Testing:** **PASSED** ✅ (100%)

### 2. Tugas 2: Implementasi Deque + Palindrome
- **Pengecekan Kode:** Deque dan palindrome benar, semua 7 test palindrome lulus.
- **Hasil Testing:** **PASSED** ✅ (100%)

### 3. Tugas 3: Simulasi Antrian Bank
- **Pengecekan Kode:** 20 customers, 3 tellers, avg wait 0.30 menit, max wait 2 menit. Semua terlayani.
- **Hasil Testing:** **PASSED** ✅ (100%)

**NILAI MODUL 6: 100**

---

## Hasil Evaluasi Modul 7: Review & Studi Kasus (Persiapan UTS)

### 1. Tugas 1: Soal Teori (PDF)
- **Pengecekan:** PDF `Tugas 7.1_10251032_Firyal Farah Khulaidah.pdf` ada di folder Minggu 7.
- **Hasil:** **DIKUMPULKAN** ✅ (100%)

### 2. Tugas 2: Sistem Manajemen Perpustakaan
- **Pengecekan Kode:** Implementasi hanya mencakup 4 dari 8 test case (Test 1–4: add books, register users, borrow books, borrow queue). Test 5–8 tidak diimplementasikan.
- **Hasil Testing Terminal:** **PASSED SEBAGIAN** ⚠️ (50% — 4/8 test)

**NILAI MODUL 7: 75** *((100+50)/2)*

---

## Hasil Evaluasi Modul 9: Tree & Binary Tree

### 1. Tugas 1: BinaryTree Class
- **Hasil Testing Terminal:** **PASSED** ✅ (100%)

### 2. Tugas 2: Expression Tree
- **Hasil Testing Terminal:** **PASSED** ✅ (100%)

### 3. Tugas 3: Analisis Kompleksitas Tree
- **Pengecekan Kode:** `height()` rekursif tanpa `sys.setrecursionlimit` → `RecursionError` pada skewed tree.
- **Hasil Testing Terminal:** **FAILED** ❌ (0%)

**NILAI MODUL 9: 67**

---

## Hasil Evaluasi Modul 10: Binary Search Tree (BST)

### 1. Tugas 1: Pengembangan BST Class
- **Hasil Testing Terminal:** **PASSED** ✅ (100%)

### 2. Tugas 2: Sistem Phonebook dengan BST
- **Hasil Testing Terminal:** **PASSED** ✅ (100%)

### 3. Tugas 3: Analisis Performa BST
- **Hasil Testing Terminal:** **PASSED** ✅ (100%)

**NILAI MODUL 10: 100**

---

### **NILAI RATA-RATA (Modul 1-7, 9, 10): 91.5**

| Modul | Nilai |
|-------|-------|
| Modul 1 | 100 |
| Modul 2 | 100 |
| Modul 3 | 100 |
| Modul 4 | 90 |
| Modul 5 | 100 |
| Modul 6 | 100 |
| Modul 7 | 75 |
| Modul 9 | 67 |
| Modul 10 | 100 |
| **Rata-rata** | **92.44** |

*Catatan: M7 T2 hanya 4/8 test case diimplementasikan.*
