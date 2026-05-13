# Laporan Evaluasi Terperinci - Praktikum Struktur Data

---

## Data Mahasiswa
- **Nama:** Muhammad Azriel Al Fadhil
- **NIM:** 10251117
- **Kelas:** Struktur Data A
- **GitHub Username:** `strukturdata-a-azrilalfadhil-svg`

---

## Hasil Evaluasi Modul 1: Pengantar Struktur Data

### 1. Tugas 1: Pengembangan ADT Counter
- **Pengecekan Kode:**
  - Fungsi penambahan dan pemotongan aritmatika divalidasi dengan hati-hati. Operasi instansiasi `add` dan `multiply` berfungsi konsisten mematuhi *constraint* bilangan genap dan minimal. Pengecekan limit pengurang `subtract()` minimal 0 dibangun sangat cermat.
- **Hasil Testing Codelab:** **PASSED** ✅ (100%)

### 2. Tugas 2: Pengembangan ADT Stack - Aplikasi Reverse String
- **Pengecekan Kode:**
  - Metode instan `clear` dan string representasi `print_stack` dieksekusi sempurna mengandalkan *built-in methods* Python. Perjalanan iterasi *reverse_string* memanfaatkan pola *push-pop* LIFO secara tepat.
- **Hasil Testing Codelab:** **PASSED** ✅ (100%)

### 3. Tugas 3: Analisis Kompleksitas Lanjutan
- **Tabel Analisis Kompleksitas & Jawaban:**
  - Argumen Big-O terdefinisikan elegan. Jawaban teoritis yang menjabarkan mengapa $O(\log n)$ sangat unggul pada skala ekstrim dijelaskan mendalam secara kualitatif. Mahasiswa juga memberikan penjabaran $O(n²)$ terkait sistem rekomendasi film dengan triliunan operasi rasional.
- **Hasil Testing Codelab:** **PASSED** ✅ (100%)

**NILAI MODUL 1: 100**

---

## Hasil Evaluasi Modul 2: Array

### 1. Tugas 1: Pengembangan MyArray
- **Pengecekan Kode:**
  - Penyisipan indeks awal `insert_front` menggunakan method `insert_at(0, element)` menopang fungsionalitas rotasi data efisien. *reverse* swap diselesaikan dengan efisien membagi pertukaran elemen awal dan elemen n - 1.
- **Hasil Testing Codelab:** **PASSED** ✅ (100%)

### 2. Tugas 2: Aplikasi Array - Statistik Data
- **Pengecekan Kode:**
  - Pada penelusuran angka kedua ekstrem `find_second_largest`, mahasiswa memagari evaluasi indeks inisialisasi boolean Python yang dirangkai mandiri `-inf`, sehingga terhindar dari bias data terkompresi. Filter `remove_duplicates()` digabung mantap.
- **Hasil Testing Codelab:** **PASSED** ✅ (100%)

### 3. Tugas 3: Aplikasi Matrix - Operasi Dasar
- **Pengecekan Kode:**
  - Logika permutasi 2-dimensi dieksekusi handal, rotasi *transpose*, perkalian skalar, rotasi invers *is_symmetric*, dan *get_diagonal* dipasang lincah sesuai blok ukurannya dengan menggunakan pola iterasi berlapis *(nested loops)* yang tertumpuk presisi.
- **Hasil Testing Codelab:** **PASSED** ✅ (100%)

**NILAI MODUL 2: 100**

---

## Hasil Evaluasi Modul 3: Single Linked List

### 1. Tugas 1: Implementasi Single Linked List
- **Pengecekan Kode:**
  - `reverse()`, `find_min()`, `find_max()`, `remove_value()`, dan `to_list()` diimplementasikan dengan benar dan bersih. Semua assert test lulus dengan baik.
- **Hasil Testing:** **PASSED** ✅ (100%)

### 2. Tugas 2: Aplikasi Polinomial
- **Pengecekan Kode:**
  - `add_polynomials()` menggunakan copy-and-add, namun ada bug minor: koefisien dengan pangkat sama tidak digabung dalam hasil (`3x^2 + 2x^2` alih-alih `5x^2`). Test numerik `evaluate(1)` tetap lulus karena hasilnya sama (19). Bug hanya pada representasi display.
- **Hasil Testing:** **PASSED** ✅ (90%) — Test lulus namun terdapat bug display: koefisien pangkat sama tidak digabung pada fungsi `add_polynomials`.

### 3. Tugas 3: Aplikasi Music Playlist
- **Pengecekan Kode:**
  - Semua operasi playlist berjalan benar dengan Single Linked List. `add_song`, `remove_song`, `play`, `next_song`, `current_song`, `total_duration`, `song_count`, `search_by_artist` semua diimplementasikan dan divalidasi dengan assert.
- **Hasil Testing:** **PASSED** ✅ (100%)

**NILAI MODUL 3: 95**

---

## Hasil Evaluasi Modul 4: Double Linked List & Circular Linked List

### 1. Tugas 1: Implementasi Double Linked List
- **Pengecekan Kode:**
  - Seluruh method DLL (`reverse`, `find_min`, `find_max`, `swap_nodes`, `is_palindrome`, `to_list`) diimplementasikan dengan benar. `reverse()` menukar pointer prev/next per node dan memperbarui head/tail. Semua assert test lulus.
- **Hasil Testing:** **PASSED** ✅ (100%)

### 2. Tugas 2: Aplikasi Text Editor Undo/Redo
- **Pengecekan Kode:**
  - Semua operasi text editor (`type_text`, `append_text`, `undo`, `redo`, branching) berjalan benar. `show_history()` menampilkan history dengan label `(current)` di akhir entri yang aktif. Semua assert test lulus.
- **Hasil Testing:** **PASSED** ✅ (100%)

### 3. Tugas 3: Aplikasi Round Robin Scheduler
- **Pengecekan Kode:**
  - Terdapat **bug pada logika rotasi**: scheduler mengeksekusi Process A secara berturut-turut hingga selesai, kemudian B, kemudian C — bukan pola Round Robin bergantian per quantum. Output menunjukkan `A→A→A(selesai)→B→B(selesai)→C→C(selesai)` alih-alih `A→B→C→A→B(selesai)→C(selesai)→A(selesai)`. `head` tidak dirotasi setelah tiap quantum — proses tidak berpindah ke antrian berikutnya setelah dieksekusi.
- **Hasil Testing:** **FAILED** ❌ — Round Robin tidak berjalan bergantian: proses dieksekusi sequential bukan circular per quantum.

**NILAI MODUL 4: 85**

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
- **Pengecekan Kode:** `PriorityQueue` benar, urutan prioritas terjaga. Semua test lulus. Catatan: urutan FIFO untuk prioritas sama tidak terjaga (Normal sebelum Medium).
- **Hasil Testing:** **PASSED** ✅ (100%)

### 2. Tugas 2: Implementasi Deque + Palindrome
- **Pengecekan Kode:** File T2 tidak ditemukan di folder Minggu 6 — tidak ada file Tugas 6.2 yang dikumpulkan.
- **Hasil Testing:** **TIDAK DIKUMPULKAN** ❌ (0%)

### 3. Tugas 3: Simulasi Antrian Bank
- **Pengecekan Kode:** File T3 tidak ditemukan di folder Minggu 6 — tidak ada file Tugas 6.3 yang dikumpulkan.
- **Hasil Testing:** **TIDAK DIKUMPULKAN** ❌ (0%)

**NILAI MODUL 6: 33** *(T1:100 + T2:0 + T3:0) / 3 ≈ 33*

---

## Hasil Evaluasi Modul 7: Review & Studi Kasus (Persiapan UTS)

### 1. Tugas 1: Soal Teori (PDF)
- **Pengecekan:** Tidak ada file PDF di folder minggu7.
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
- **Pengecekan Kode:** Menggunakan `sys.setrecursionlimit` sehingga `height()` pada skewed tree n=10000 berhasil dieksekusi tanpa RecursionError. Nama file menggunakan koma (`tugas9,3_...`) sebagai pemisah namun tetap valid dieksekusi.
- **Hasil Testing Terminal:** **PASSED** ✅ (100%)

**NILAI MODUL 9: 100**

---

## Hasil Evaluasi Modul 10: Binary Search Tree (BST)

### 1. Tugas 1: Pengembangan BST Class
- **Hasil Testing Terminal:** **PASSED** ✅ (100%)

### 2. Tugas 2: Sistem Phonebook dengan BST
- **Pengecekan Kode:** File menggunakan `input()` di akhir (menyebabkan `EOFError` saat dijalankan non-interaktif, namun diakali dengan piping). Hanya mengimplementasikan 3 test (Size, Search, Delete) vs 7 test standar template. Test prefix search tidak ada. Semua 3 test yang ada lulus.
- **Hasil Testing Terminal:** **PASSED** ✅ (70%) — 3/7 test standar diimplementasikan

### 3. Tugas 3: Analisis Performa BST
- **Pengecekan Kode:** File menggunakan `input()` di akhir namun tetap bisa dijalankan dengan piping. Analisis BST (height comparison Random/Sorted/Balanced dan timing search) lengkap hingga n=50000.
- **Hasil Testing Terminal:** **PASSED** ✅ (100%)

**NILAI MODUL 10: 90** *((100+70+100)/3 ≈ 90)*

---

### **NILAI RATA-RATA (Modul 1-7, 9, 10): 83.67**

| Modul | Nilai | Keterangan |
|-------|-------|------------|
| Modul 1 | 100 | |
| Modul 2 | 100 | |
| Modul 3 | 95 | |
| Modul 4 | 85 | |
| Modul 5 | 100 | |
| Modul 6 | 33 | T2/T3 tidak dikumpulkan |
| Modul 7 | 50 | T1 tidak ada PDF |
| Modul 9 | 100 | |
| Modul 10 | 90 | T2 hanya 3 dari 7 test standar |
| **Rata-rata** | **83.67** | |
