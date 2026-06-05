# Laporan Evaluasi Terperinci - Praktikum Struktur Data

---

## Data Mahasiswa
- **Nama:** Chelsea Angelika Velayati
- **NIM:** 10251104
- **Kelas:** Struktur Data A
- **GitHub Username:** `strukturdata-a-Chelsea-10251104`

---

## Hasil Evaluasi Modul 1: Pengantar Struktur Data

### 1. Tugas 1: Pengembangan ADT Counter
- **Pengecekan Kode:**
  - Metode `subtract()` berhasil dimodifikasi sesuai spesifikasi dengan membatasi agar tidak berada di bawah nol melalui metode kondisional bersarang (`if/else`). 
- **Hasil Testing Codelab:** **PASSED** ✅ (100%)

### 2. Tugas 2: Pengembangan ADT Stack - Aplikasi Reverse String
- **Pengecekan Kode:**
  - Fungsi iterasi string didalam metode pembalikan (*reverse_string*) diterapkan dengan struktur yang baik. Seluruh karakter berhasil ditambahkan denga `stack.push(char)` dan ditarik kembali secara LIFO dengan `result += stack.pop()`.
- **Hasil Testing Codelab:** **PASSED** ✅ (100%)

### 3. Tugas 3: Analisis Kompleksitas Lanjutan
- **Tabel Analisis Kompleksitas & Jawaban:**
  - Argumentasi yang diberikan cukup lengkap dan tepat sasaran. Penjelasan alasan dibalik efisiensi algoritma dihubungkan dengan prinsip operasi *Recursive Halving* serta perbandingan linear `O(n)`.
- **Hasil Testing Codelab:** **PASSED** ✅ (100%)

**NILAI MODUL 1: 100**

---

## Hasil Evaluasi Modul 2: Array

### 1. Tugas 1: Pengembangan MyArray
- **Pengecekan Kode:**
  - Logika modifikasi pointer kiri (*left*) dan kanan (*right*) dalam metode *reverse* diketik berbarengan dalam satu baris (*multiple assignment*) layaknya bahasa komputasi level lanjutan secara optimal `self._elements[left], self._elements[right] = self._elements[right], self._elements[left]`. Ini menghindari penggunaan variabel penampung sementara (`temp`).
- **Hasil Testing Codelab:** **PASSED** ✅ (100%)

### 2. Tugas 2: Aplikasi Array - Statistik Data
- **Pengecekan Kode:**
  - Penerapan `while` loop untuk seluruh fungsi membedakan kode mahasiswa ini dari yang lain yang mayoritas dominan menggunakan `for` iterasi ganda, sebuah nilai plus disisi variasi eksekusi tanpa mengubah kompleksitas aslinya `O(n)`.
- **Hasil Testing Codelab:** **PASSED** ✅ (100%)

### 3. Tugas 3: Aplikasi Matrix - Operasi Dasar
- **Pengecekan Kode:**
  - Konsep dimensi matriks berhasil direpresentasikan dalam algoritma iterasi *nested for-loop*.
- **Hasil Testing Codelab:** **PASSED** ✅ (100%)

**NILAI MODUL 2: 100**

---

## Hasil Evaluasi Modul 3: Single Linked List

### 1. Tugas 1: Implementasi Single Linked List
- **Pengecekan Kode:**
  - Terdapat duplikasi definisi kelas `Node.__init__` (ada dua blok `class Node` berturut-turut) dan terdapat **SyntaxError/IndentationError** pada method `reverse()`: baris komentar `Algoritma:` ditulis tanpa pembuka `"""` sehingga Python menginterpretasinya sebagai kode, bukan docstring. Logika `find_min`, `find_max`, `remove_value`, dan `to_list` secara substansi sudah benar.
- **Hasil Testing:** **FAILED** ❌ — `IndentationError: unexpected indent` pada baris 268 (`Algoritma:` tanpa triple-quote pembuka). File tidak dapat dieksekusi.

### 2. Tugas 2: Aplikasi Polinomial
- **Pengecekan Kode:**
  - `add_term()` mengimplementasikan penyisipan terurut dengan penggabungan koefisien duplikat secara lengkap, termasuk kasus penghapusan term berkoefisien nol. Metode tambahan `multiply_scalar()` dan `multiply_polynomials()` disertakan sebagai bonus. `add_polynomials()` menggunakan two-pointer merge yang efisien.
- **Hasil Testing:** **PASSED** ✅ (100%)

### 3. Tugas 3: Aplikasi Music Playlist
- **Pengecekan Kode:**
  - Playlist diimplementasikan dengan DLL-style (node `SongNode` memiliki atribut `prev` dan ada pointer `tail`), meskipun `SongNode` hanya didefinisikan dengan `next`. Hal ini berfungsi karena Python bersifat dinamis dan atribut `prev`/`tail` ditetapkan secara implisit. Semua operasi berjalan benar termasuk `prev_song()` sebagai fitur tambahan.
- **Hasil Testing:** **PASSED** ✅ (100%)

**NILAI MODUL 3: 90**

---

## Hasil Evaluasi Modul 4: Double Linked List & Circular Linked List

### 1. Tugas 1: Implementasi Double Linked List
- **Pengecekan Kode:**
  - `reverse()` mengimplementasikan algoritma tukar pointer prev/next per node lalu menukar `head` dan `tail` — benar dan efisien O(n). `is_palindrome()` menggunakan counter setengah panjang list untuk membandingkan dari kedua ujung. Semua method berjalan sesuai spesifikasi.
- **Hasil Testing:** **PASSED** ✅ (100%)

### 2. Tugas 2: Aplikasi Text Editor Undo/Redo
- **Pengecekan Kode:**
  - `type_text()` memotong cabang redo (`self.current.next = None`) sebelum membuat node baru. Semua operasi undo/redo/branching berjalan dengan benar. `show_history()` menampilkan posisi ^current di tengah label node.
- **Hasil Testing:** **PASSED** ✅ (100%)

### 3. Tugas 3: Aplikasi Round Robin Scheduler
- **Pengecekan Kode:**
  - `add_process()` menggunakan pointer `tail` untuk O(1) insertion. Terdapat **bug pada `remove_process`**: ketika Process A (remaining=1) menjadi head dan Process B/C selesai, proses A tidak pernah dieksekusi — scheduler berhenti dengan hanya 2 proses selesai (`processes_completed: 2`). Total waktu 11 (harusnya 12). Logika `remove_process` tidak memindahkan `head` dengan benar setelah B dan C selesai dalam urutan.
- **Hasil Testing:** **FAILED** ❌ — Process A (remaining: 1) tidak pernah dieksekusi. Hanya 2/3 proses selesai.

**NILAI MODUL 4: 90**

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
- **Pengecekan:** PDF ditemukan di folder minggu7.
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

## Hasil Evaluasi Modul 11: Graph

### 1. Tugas 1: Pengembangan Graph Class
- **Pengecekan Kode:** Method baru lengkap, 7 test case lulus.
- **Hasil Testing Terminal:** **PASSED** ✅ (100%)

### 2. Tugas 2: Sistem Navigasi Kampus
- **Pengecekan Kode:** BFS route, shortest route (270m A→E), all_reachable berjalan benar.
- **Hasil Testing Terminal:** **PASSED** ✅ (100%)

### 3. Tugas 3: Analisis Kompleksitas Graph
- **Pengecekan Kode:** Perbandingan adjacency list vs matrix lengkap.
- **Hasil Testing Terminal:** **PASSED** ✅ (100%)

**NILAI MODUL 11: 100**

---

## Hasil Evaluasi Modul 12: Algoritma Searching

### 1. Tugas 1: Binary Search Lanjutan
- **Pengecekan Kode:** Semua fungsi lulus 5 test case.
- **Hasil Testing Terminal:** **PASSED** ✅ (100%)

### 2. Tugas 2: Hash Table - Open Addressing
- **Pengecekan Kode:** Linear probing + tombstone, resize & rehash bekerja.
- **Hasil Testing Terminal:** **PASSED** ✅ (100%)

### 3. Tugas 3: Sistem Kamus Digital
- **Pengecekan Kode:** Bidirectional dictionary dengan multiple translations dan prefix search benar.
- **Hasil Testing Terminal:** **PASSED** ✅ (100%)

**NILAI MODUL 12: 100**

---

## Hasil Evaluasi Modul 13: Sorting Dasar

### 1. Tugas 1: Sorting dengan Custom Comparator
- **Pengecekan Kode:** `bubble_sort_custom`, `selection_sort_custom`, `insertion_sort_custom` dengan parameter `key` & `reverse` benar.
- **Hasil Testing Terminal:** **PASSED** ✅ (100%)

### 2. Tugas 2: Sistem Ranking Mahasiswa
- **Pengecekan Kode:** `RankingSystem` (`sort_by_nama`, `sort_by_nilai_akhir`, `sort_by_grade_then_nama`, `get_top_n`, `grade_distribution`) benar.
- **Hasil Testing Terminal:** **PASSED** ✅ (100%)

### 3. Tugas 3: Analisis dan Visualisasi Sorting
- **Pengecekan Kode:** Trace verbose, uji stabilitas, tabel observasi & 5 jawaban analisis lengkap.
- **Hasil Testing Terminal:** **PASSED** ✅ (100%)

**NILAI MODUL 13: 100**

---

### **NILAI RATA-RATA (Modul 1-7, 9-13): 95.58**

| Modul | Nilai |
|-------|-------|
| Modul 1 | 100 |
| Modul 2 | 100 |
| Modul 3 | 90 |
| Modul 4 | 90 |
| Modul 5 | 100 |
| Modul 6 | 100 |
| Modul 7 | 100 |
| Modul 9 | 67 |
| Modul 10 | 100 |
| Modul 11 | 100 |
| Modul 12 | 100 |
| Modul 13 | 100 |
| **Rata-rata** | **95.58** |
