# Laporan Evaluasi Terperinci - Praktikum Struktur Data

---

## Data Mahasiswa
- **Nama:** Julian Zaky Saputra
- **NIM:** 10251080
- **Kelas:** Struktur Data A
- **GitHub Username:** `strukturdata-a-Julian-Zaky-Saputra`

---

## Hasil Evaluasi Modul 1: Pengantar Struktur Data

### 1. Tugas 1: Pengembangan ADT Counter
- **Pengecekan Kode:**
  - Metode `subtract()` diimplementasikan menahan value counter untuk tak jatuh di bawah nol `if self._value < 0: self._value = 0` setelah dilakukan pengurangan. Langkah yang ringkas dan fungsional.
- **Hasil Testing Codelab:** **PASSED** ✅ (100%)

### 2. Tugas 2: Pengembangan ADT Stack - Aplikasi Reverse String
- **Pengecekan Kode:**
  - Fungsi penumpukan dan pengeluaran berlapis dari *stack* untuk *reverse_string* dieksekusi benar.
- **Hasil Testing Codelab:** **PASSED** ✅ (100%)

### 3. Tugas 3: Analisis Kompleksitas Lanjutan
- **Tabel Analisis Kompleksitas & Jawaban:**
  - Mahasiswa mendeskripsikan secara awam namun cukup deskriptif, misal *Triple nested loop* dilambangkan "Angka diulang tiga kali bertingkat" membuktikan pemahaman inti materi, walau disarankan menggunakan terminologi ilmiah di lingkungan akademis. Contoh pencarian duplikasi data dari 5 juta nasabah bank (skala triliun operasi) untuk kasus batas toleransi `O(n²)` diuraikan sangat brilian.
- **Hasil Testing Codelab:** **PASSED** ✅ (100%)

**NILAI MODUL 1: 100**

---

## Hasil Evaluasi Modul 2: Array

### 1. Tugas 1: Pengembangan MyArray
- **Pengecekan Kode:**
  - Terdapat deteksi tambahan pada blok *find_min* dan *find_max* yang memeriksa via `len() == 0` dan kemudian melakukan eksekusi inisasial. Fungsi `reverse` telah berjalan aman menggunakan *two pointer strategy*.
- **Hasil Testing Codelab:** **PASSED** ✅ (100%)

### 2. Tugas 2: Aplikasi Array - Statistik Data
- **Pengecekan Kode:**
  - Mahkamah kode menemukan sebuah praktik impresif di mana perhitungan elemen terbesar kedua *find_second_largest* tidak memakai sorting sama sekali (memenuhi kompleksitas `O(n)` sejati) tetapi menginisiasi dua angka variabel bantuan paling kecil dari Python `float("-inf")` (*infinity* negatif), algoritma yang brilian dan tingkat tinggi.
- **Hasil Testing Codelab:** **PASSED** ✅ (100%)

### 3. Tugas 3: Aplikasi Matrix - Operasi Dasar
- **Pengecekan Kode:**
  - Pemeriksaan ukuran matriks dipertahankan aman, struktur for bersarang (*nested-for loop*) standar beroperasi untuk melakukan modifikasi nilai *matrix*, sesuai algoritma dasar perkalian dan penjumlahan matriks.
- **Hasil Testing Codelab:** **PASSED** ✅ (100%)

**NILAI MODUL 2: 100**


---

## Hasil Evaluasi Modul 3: Single Linked List

### 1. Tugas 1: Implementasi Single Linked List
- **Pengecekan Kode:**
  - Implementasi lengkap dari template praktikum. `reverse()` menggunakan three-pointer idiomatik. `find_min()` dan `find_max()` menginisialisasi dari `head.data` dan melakukan traversal penuh. `remove_value()` menangani kasus head dan non-head dengan benar. `to_list()` mengumpulkan semua data ke Python list. Catatan minor: banyak `pass` statement setelah `return` yang redundan namun tidak mengganggu eksekusi. File tugas3.3 tidak memiliki ekstensi `.py` namun merupakan file Python yang valid.
- **Hasil Testing:** **PASSED** ✅ (100%)

### 2. Tugas 2: Aplikasi Polinomial
- **Pengecekan Kode:**
  - `add_term()` menyimpan term terurut dari pangkat tertinggi ke terendah. Duplikat pangkat ditangani dengan menambahkan koefisien pada node yang ada. `evaluate()` menggunakan variabel `count` (nama alternatif untuk `result`) yang berfungsi dengan benar. `add_polynomials()` mengiterasi kedua polinomial dan memanfaatkan `add_term()`. Display menggunakan format `3x^2 + 2x^1 + 5x^0` yang konsisten.
- **Hasil Testing:** **PASSED** ✅ (100%)

### 3. Tugas 3: Aplikasi Music Playlist
- **Pengecekan Kode:**
  - `add_song()`, `remove_song()`, `play()`, `next_song()`, dan `current_song()` diimplementasikan dengan benar. `search_by_artist()` menggunakan pencocokan exact case-sensitive. `display()` menampilkan playlist dengan format yang tepat termasuk header `=== Playlist: [nama] ===` dan total durasi.
- **Hasil Testing:** **PASSED** ✅ (100%)

**NILAI MODUL 3: 100**

---

## Hasil Evaluasi Modul 4: Double Linked List & Circular Linked List

### 1. Tugas 1: Implementasi Double Linked List
- **Pengecekan Kode:**
  - `reverse()` menukar pointer `prev` dan `next` setiap node secara in-place lalu menukar `head` dan `tail`. `find_min()` dan `find_max()` menggunakan traversal dengan inisialisasi dari `head.data`. `swap_nodes()` memvalidasi posisi dengan `self.size()` dan hanya menukar data. `is_palindrome()` menggunakan two-pointer dari head dan tail dengan kondisi terminasi yang tepat. Catatan minor: banyak `pass` setelah `return` yang redundan namun tidak berpengaruh.
- **Hasil Testing:** **PASSED** ✅ (100%)

### 2. Tugas 2: Aplikasi Text Editor Undo/Redo
- **Pengecekan Kode:**
  - `type_text()` memutus redo-history dengan `self.current.next = None` sebelum menambahkan state baru. `undo()` dan `redo()` bernavigasi dengan cek pointer yang tepat. `show_history()` menampilkan riwayat dari head dengan marker ` ^current` pada node saat ini.
- **Hasil Testing:** **PASSED** ✅ (100%)

### 3. Tugas 3: Aplikasi Round Robin Scheduler
- **Pengecekan Kode:**
  - `add_process()` dan `remove_process()` menjaga sifat sirkular CLL dengan benar. `execute_one_cycle()` mengembalikan dict lengkap dengan `start`, `end`, dan status completion. `run()` membaca `result['completed']` dan `result['start']`/`result['end']` untuk menampilkan timeline. Output A(5)+B(3)+C(4) dengan quantum=2 menghasilkan total waktu 12 sesuai ekspektasi.
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
- **Pengecekan Kode:** `Deque` benar. Namun `is_palindrome()` tidak mengembalikan nilai apapun (return `None`) — fungsi melakukan pengecekan namun tidak ada `return True/False`. Akibatnya semua pemanggilan `is_palindrome()` mengembalikan `None`.
- **Hasil Testing:** **FAILED** ❌ — `is_palindrome()` selalu return `None` (50%)

### 3. Tugas 3: Simulasi Antrian Bank
- **Pengecekan Kode:** 20 customers, 3 tellers, avg wait 0.30 menit — statistik benar.
- **Hasil Testing:** **PASSED** ✅ (100%)

**NILAI MODUL 6: 83** *(T1:100 + T2:50 + T3:100) / 3 ≈ 83*

---

## Hasil Evaluasi Modul 7: Review & Studi Kasus (Persiapan UTS)

### 1. Tugas 1: Soal Teori (PDF)
- **Pengecekan:** Tidak ada file PDF di folder minggu7. Hanya ada `tugas7.2_10251080.py`.
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

### **NILAI RATA-RATA (Modul 1-7, 9, 10): 87.5**

| Modul | Nilai |
|-------|-------|
| Modul 1 | 100 |
| Modul 2 | 100 |
| Modul 3 | 100 |
| Modul 4 | 100 |
| Modul 5 | 100 |
| Modul 6 | 83 |
| Modul 7 | 50 |
| Modul 9 | 67 |
| Modul 10 | 100 |
| **Rata-rata** | **88.89** |

*Catatan: M7 T1 tidak dikumpulkan (tidak ada PDF).*
