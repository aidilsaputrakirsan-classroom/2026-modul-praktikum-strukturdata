# Laporan Evaluasi Terperinci - Praktikum Struktur Data

---

## Data Mahasiswa
- **Nama:** Mosses Restu Nugroho
- **NIM:** 10251083
- **Kelas:** Struktur Data A
- **GitHub Username:** `strukturdata-a-MossesRestuN`

---

## Hasil Evaluasi Modul 1: Pengantar Struktur Data

### 1. Tugas 1: Pengembangan ADT Counter
- **Pengecekan Kode:**
  - Metode `subtract()` dikerjakan dengan solid di mana batas nilai bawah 0 diamankan menggunakan validasi tambahan `if self._value < 0: self._value = 0` sehingga kondisi anomali tertangani dengan rapi. Konsep pemrograman berorientasi objek yang kuat.
- **Hasil Testing Codelab:** **PASSED** ✅ (100%)

### 2. Tugas 2: Pengembangan ADT Stack - Aplikasi Reverse String
- **Pengecekan Kode:**
  - Fungsi pembalikan *reverse_string* memanfaatkan mekanisme penambahan iteratif pada string baru, mengambil keluaran *stack.pop()* sehingga pola *Last In First Out* (LIFO) tereksekusi murni.
- **Hasil Testing Codelab:** **PASSED** ✅ (100%)

### 3. Tugas 3: Analisis Kompleksitas Lanjutan
- **Tabel Analisis Kompleksitas & Jawaban:**
  - Penjelasan cukup lugas, mahasiswa bisa mendeskripsikan Big O notation ke dalam bahasa awam yang ringkas seperti "tiap rekursi membagi n jadi n/2". Contoh kegagalan algoritma `O(n²)` (sistem perbandingan data jutaan pengguna) tepat sasaran dan rasional.
- **Hasil Testing Codelab:** **PASSED** ✅ (100%)

**NILAI MODUL 1: 100**

---

## Hasil Evaluasi Modul 2: Array

### 1. Tugas 1: Pengembangan MyArray
- **Pengecekan Kode:**
  - Pendefinisian fitur pada class `MyArray` stabil. `find_min()` dan `find_max()` dilengkapi pemblokiran `self.is_empty()` sebagai gerbang batas error *ValueError*. Fungsi `reverse` cukup padat dijalankan melalui fungsi bawaan python (*self._elements.reverse()*).
- **Hasil Testing Codelab:** **PASSED** ✅ (100%)

### 2. Tugas 2: Aplikasi Array - Statistik Data
- **Pengecekan Kode:**
  - Penerapan `find_second_largest` dijalin apik melalui penyelesaian dalam sekali melintas (*one pass O(n)*), menggunakan inisialisasi infinity negatif `float('-inf')` yang mendemonstrasikan keluwesan penguasaan Python tingkat menengah.
- **Hasil Testing Codelab:** **PASSED** ✅ (100%)

### 3. Tugas 3: Aplikasi Matrix - Operasi Dasar
- **Pengecekan Kode:**
  - Mahasiswa mampu menulis komputasi matriks dua dimensi (`add_matrices` dan `transpose_matrix`) secara stabil menggunakan iterasi baris-kolom mendasar tanpa ketergantungan *libraries* eksternal tambahan.
- **Hasil Testing Codelab:** **PASSED** ✅ (100%)

**NILAI MODUL 2: 100**


---

## Hasil Evaluasi Modul 3: Single Linked List

### 1. Tugas 1: Implementasi Single Linked List
- **Pengecekan Kode:**
  - `reverse()` menggunakan three-pointer (`prev`, `current`, `next_node`) yang efisien. `find_min()` dan `find_max()` menginisialisasi dari `head.data` dan menggunakan variabel `minimum`/`maximum` yang deskriptif. `remove_value()` menggunakan `prev` pointer untuk menangani semua kasus penghapusan. `to_list()` mengkonversi linked list ke Python list dengan traversal bersih. Catatan minor: `display()` menggunakan `"-> NULL"` tanpa spasi sebelum `->`, berbeda dari format standar, namun tidak mempengaruhi logika.
- **Hasil Testing:** **PASSED** ✅ (100%)

### 2. Tugas 2: Aplikasi Polinomial
- **Pengecekan Kode:**
  - `add_term()` mengabaikan koefisien 0 dan menyimpan term terurut. Penanganan duplikat pangkat dengan penambahan koefisien langsung pada node yang ada. `evaluate()` menggunakan `result` sebagai akumulator. `add_polynomials()` mengiterasi kedua polinomial secara berurutan. `display()` menggunakan format yang lebih ringkas: `3x^2 + 2x + 5` (tanpa `^1` dan `^0` untuk pangkat 1 dan 0).
- **Hasil Testing:** **PASSED** ✅ (100%)

### 3. Tugas 3: Aplikasi Music Playlist
- **Pengecekan Kode:**
  - Semua operasi playlist diimplementasikan dengan benar. `next_song()` mengembalikan `None` jika sudah di akhir list. `remove_song()` memperbarui `self.current` jika lagu yang dihapus sedang diputar. Catatan minor: `display()` tidak mencetak header `=== Playlist: [nama] ===`, langsung ke nomor lagu; namun fungsi `format_duration()` dan `total_duration()` bekerja dengan benar dan semua assert test berhasil.
- **Hasil Testing:** **PASSED** ✅ (100%)

**NILAI MODUL 3: 100**

---

## Hasil Evaluasi Modul 4: Double Linked List & Circular Linked List

### 1. Tugas 1: Implementasi Double Linked List
- **Pengecekan Kode:**
  - `reverse()` menukar pointer setiap node dan menukar head/tail hanya jika `temp` (node terakhir sebelum None) tidak None — pengecekan defensif yang baik. `find_min()` dan `find_max()` melakukan traversal lengkap. `swap_nodes()` menggunakan dua loop terpisah untuk menemukan node1 dan node2, lalu menukar data. `is_palindrome()` menggunakan two-pointer dari head dan tail. Catatan minor: `delete_at_beginning()` tidak mengembalikan `deleted` untuk kasus single-node, namun tidak mempengaruhi test yang diberikan.
- **Hasil Testing:** **PASSED** ✅ (100%)

### 2. Tugas 2: Aplikasi Text Editor Undo/Redo
- **Pengecekan Kode:**
  - `type_text()` memutus redo-history dengan benar. `undo()` dan `redo()` berfungsi dengan pengecekan pointer yang tepat. `show_history()` menampilkan riwayat dengan marker ` ^current` pada node aktif. Implementasi bersih dan ringkas tanpa kode berlebihan.
- **Hasil Testing:** **PASSED** ✅ (100%)

### 3. Tugas 3: Aplikasi Round Robin Scheduler
- **Pengecekan Kode:**
  - `execute_one_cycle()` mencetak output timeline secara langsung di dalam method (berbeda dari mahasiswa lain yang mengembalikan info ke `run()`), lalu `run()` memanggil tanpa perlu memparsing dict. Pendekatan ini valid dan menghasilkan output yang identik. `add_process()`, `remove_process()`, dan semua operasi CLL berfungsi dengan benar. Output A(5)+B(3)+C(4) dengan quantum=2 menghasilkan total waktu 12.
- **Hasil Testing:** **PASSED** ✅ (100%)

**NILAI MODUL 4: 100**

---
## Hasil Evaluasi Modul 5: Stack

### 1. Tugas 1: Pengembangan Stack dengan Method Baru
- **Pengecekan Kode:** Semua method baru diimplementasikan dengan benar. Semua test lulus.
- **Hasil Testing:** **PASSED** ✅ (100%)

### 2. Tugas 2: Konversi dan Evaluasi Ekspresi
- **Pengecekan Kode:** `infix_to_postfix()` benar termasuk right-associativity `^`. Semua test lulus.
- **Hasil Testing:** **PASSED** ✅ (100%)

### 3. Tugas 3: Aplikasi Browser History
- **Pengecekan Kode:** `BrowserHistory` benar. Semua test lulus.
- **Hasil Testing:** **PASSED** ✅ (100%)

**NILAI MODUL 5: 100**

---

## Hasil Evaluasi Modul 6: Queue

### 1. Tugas 1: Implementasi Priority Queue
- **Pengecekan Kode:** `PriorityQueue` benar, urutan prioritas terjaga. Semua test lulus.
- **Hasil Testing:** **PASSED** ✅ (100%)

### 2. Tugas 2: Implementasi Deque + Palindrome
- **Pengecekan Kode:** `Deque` dan `is_palindrome()` benar. Semua 7 test lulus.
- **Hasil Testing:** **PASSED** ✅ (100%)

### 3. Tugas 3: Simulasi Antrian Bank
- **Pengecekan Kode:** 20 customers, 3 tellers, avg wait 0.30 menit — statistik benar.
- **Hasil Testing:** **PASSED** ✅ (100%)

**NILAI MODUL 6: 100**

---

## Hasil Evaluasi Modul 7: Review & Studi Kasus (Persiapan UTS)

### 1. Tugas 1: Soal Teori (PDF)
- **Pengecekan:** PDF `Tugas7_10251083_MossesRestuNugroho.pdf` ada di folder minggu7.
- **Hasil:** **DIKUMPULKAN** ✅ (100%)

### 2. Tugas 2: Sistem Manajemen Perpustakaan
- **Pengecekan Kode:** Semua 8 test case lulus.
- **Hasil Testing Terminal:** **PASSED** ✅ (100%)

**NILAI MODUL 7: 100**

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

### **NILAI RATA-RATA (Modul 1-7, 9, 10): 95.88**

| Modul | Nilai |
|-------|-------|
| Modul 1 | 100 |
| Modul 2 | 100 |
| Modul 3 | 100 |
| Modul 4 | 100 |
| Modul 5 | 100 |
| Modul 6 | 100 |
| Modul 7 | 100 |
| Modul 9 | 67 |
| Modul 10 | 100 |
| **Rata-rata** | **96.33** |
