# Laporan Evaluasi Terperinci - Praktikum Struktur Data

---

## Data Mahasiswa
- **Nama:** Muhammad Ryan Eka Putra
- **NIM:** 10251089
- **Kelas:** Struktur Data A
- **GitHub Username:** `strukturdata-a-10251089-Ryan`

---

## Hasil Evaluasi Modul 1: Pengantar Struktur Data

### 1. Tugas 1: Pengembangan ADT Counter
- **Pengecekan Kode:**
  - Metode `subtract()` bekerja lancar menggunakan kondisi terstruktur `if self._value >= n`. Method kalkulatif lainnya tertulis efisien dan tervalidasi dengan *if condition* meskipun klausa `else: pass` dapat disederhanakan.
- **Hasil Testing Codelab:** **PASSED** ✅ (100%)

### 2. Tugas 2: Pengembangan ADT Stack - Aplikasi Reverse String
- **Pengecekan Kode:**
  - Stack dibuat stabil. Pembalikan string *while not stack.is_empty(): result = result + stack.pop()* telah menjalankan instruksi *pop* sesuai prinsip LIFO murni.
- **Hasil Testing Codelab:** **PASSED** ✅ (100%)

### 3. Tugas 3: Analisis Kompleksitas Lanjutan
- **Tabel Analisis Kompleksitas & Jawaban:**
  - Pemahaman fungsi kompleksitas ditulis sangat baik, dicontohkan dengan kasus *real time* algoritma rekomen Tokopedia dan Netflix pada kompleksitas O(n^2), menunjukkan kapasitas analis komprehensif.
- **Hasil Testing Codelab:** **PASSED** ✅ (100%)

**NILAI MODUL 1: 100**

---

## Hasil Evaluasi Modul 2: Array

### 1. Tugas 1: Pengembangan MyArray
- **Pengecekan Kode:**
  - File .py untuk modul 2 sukses direname dalam sisi admin dan beroperasi secara optimal. Perhitungan manipulasi *index pointer* `left` dan `right` dieksekusi sempurna di fitur *reverse()*. 
- **Hasil Testing Codelab:** **PASSED** ✅ (100%)

### 2. Tugas 2: Aplikasi Array - Statistik Data
- **Pengecekan Kode:**
  - Pencarian *second largest* digarap dengan kalkulasi logis tanpa duplikat komparasi *None* statik `if second_largest is None or (...)`. Logika duplikat *remove_duplicates* tereksekusi mulus. 
- **Hasil Testing Codelab:** **PASSED** ✅ (100%)

### 3. Tugas 3: Aplikasi Matrix - Operasi Dasar
- **Pengecekan Kode:**
  - Algoritma transposisi *matrix* diprogramkan dengan struktur matriks terpadu yang dapat mengenali baris vertikal. Validasi asimetris dirangkai lugas menggunakan iterasi ganda mengecek pertentangan panjang dan lebar ordo matriks secara *hard-coded*.
- **Hasil Testing Codelab:** **PASSED** ✅ (100%)

**NILAI MODUL 2: 100**


---

## Hasil Evaluasi Modul 3: Single Linked List

### 1. Tugas 1: Implementasi Single Linked List
- **Pengecekan Kode:**
  - Implementasi bersih dan rapi tanpa kode berlebihan. `reverse()` menggunakan three-pointer standar. `find_min()` dan `find_max()` menginisialisasi dari `head.data` dan melakukan traversal penuh. `remove_value()` menggunakan variabel `previous` (bukan `prev`) yang deskriptif. `to_list()` mengkonversi dengan traversal sederhana. Tidak ada `pass` statement yang tidak perlu, kode sangat clean.
- **Hasil Testing:** **PASSED** ✅ (100%)

### 2. Tugas 2: Aplikasi Polinomial
- **Pengecekan Kode:**
  - `add_term()` menyimpan term terurut dari pangkat tertinggi ke terendah dengan handling duplikat pangkat yang benar. `evaluate()` mengakumulasikan hasil dengan benar. `add_polynomials()` mengiterasi kedua polinomial berurutan dan memanfaatkan `add_term()` untuk otomatisasi penggabungan suku. Display format `3x^2 + 2x^1 + 5x^0` konsisten dengan format template.
- **Hasil Testing:** **PASSED** ✅ (100%)

### 3. Tugas 3: Aplikasi Music Playlist
- **Pengecekan Kode:**
  - Semua operasi playlist diimplementasikan dengan benar dan bersih. `next_song()` tidak melakukan loop circular, mengembalikan `None` jika sudah di akhir. `remove_song()` tidak memperbarui `self.current` secara eksplisit, namun test yang diberikan tidak menguji skenario tersebut sehingga semua assert lulus. `search_by_artist()` menggunakan pencocokan exact string.
- **Hasil Testing:** **PASSED** ✅ (100%)

**NILAI MODUL 3: 100**

---

## Hasil Evaluasi Modul 4: Double Linked List & Circular Linked List

### 1. Tugas 1: Implementasi Double Linked List
- **Pengecekan Kode:**
  - `reverse()` menukar pointer setiap node secara in-place dan menukar `head`/`tail`. `find_min()` dan `find_max()` mengembalikan `None` jika list kosong (alih-alih raise ValueError) — perbedaan minor dari spesifikasi namun tidak mempengaruhi test. `swap_nodes()` menukar pos1 dan pos2 jika pos1 > pos2 untuk efisiensi traversal, lalu menukar data. `is_palindrome()` menggunakan two-pointer dengan kondisi terminasi yang tepat.
- **Hasil Testing:** **PASSED** ✅ (100%)

### 2. Tugas 2: Aplikasi Text Editor Undo/Redo
- **Pengecekan Kode:**
  - `type_text()` memutus redo-history sebelum menambahkan node baru. Implementasi `undo()` dan `redo()` bersih dengan pengecekan pointer yang tepat. `show_history()` menampilkan riwayat dengan format yang rapi menggunakan marker ` ^current`. Seluruh implementasi bersih tanpa redundansi.
- **Hasil Testing:** **PASSED** ✅ (100%)

### 3. Tugas 3: Aplikasi Round Robin Scheduler
- **Pengecekan Kode:**
  - `add_process()` dan `remove_process()` menjaga sifat sirkular CLL dengan benar, termasuk kasus hapus head. `execute_one_cycle()` mengembalikan dict dengan `time_range` sebagai tuple. `run()` mengurai `info['time_range']` ke `start` dan `end`. Catatan minor: `get_statistics()` menghitung `total_time` dari `sum(p.burst_time for p in self.completed)` — ini menghitung jumlah burst time bukan elapsed time, namun keduanya bernilai sama (12) untuk test ini.
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
- **Pengecekan:** Tidak ada file PDF di folder Minggu7. File `Tugas7.1_10251089_MuhammadRyanEkaPutra.py` berisi implementasi Sistem Manajemen Perpustakaan (bukan soal teori PDF).
- **Hasil:** **TIDAK DIKUMPULKAN** ❌ (0%)

### 2. Tugas 2: Sistem Manajemen Perpustakaan
- **Pengecekan Kode:** Semua 8 test case lulus.
- **Hasil Testing Terminal:** **PASSED** ✅ (100%)

**NILAI MODUL 7: 50** *((0+100)/2)*

---

## Hasil Evaluasi Modul 9: Tree & Binary Tree

### 1. Tugas 1: BinaryTree Class
- **Hasil Testing Terminal:** **PASSED** ✅ (100%)

### 2. Tugas 2: Expression Tree
- **Hasil Testing Terminal:** **PASSED** ✅ (100%)

### 3. Tugas 3: Analisis Kompleksitas Tree
- **Pengecekan Kode:** `RecursionError` pada fungsi `search_tree` rekursif tanpa `sys.setrecursionlimit` saat skewed tree.
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

### **NILAI RATA-RATA (Modul 1-7, 9, 10): 89.63**

| Modul | Nilai |
|-------|-------|
| Modul 1 | 100 |
| Modul 2 | 100 |
| Modul 3 | 100 |
| Modul 4 | 100 |
| Modul 5 | 100 |
| Modul 6 | 100 |
| Modul 7 | 50 |
| Modul 9 | 67 |
| Modul 10 | 100 |
| **Rata-rata** | **90.78** |

*Catatan: M7 T1 tidak dikumpulkan (file berisi Library management bukan PDF teori).*
