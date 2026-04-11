# Laporan Evaluasi Terperinci - Praktikum Struktur Data

---

## Data Mahasiswa
- **Nama:** Risna Andriani
- **NIM:** 10251077
- **Kelas:** Struktur Data A
- **GitHub Username:** `strukturdata-a-RisnaAndriani-10251077`

---

## Hasil Evaluasi Modul 1: Pengantar Struktur Data

### 1. Tugas 1: Pengembangan ADT Counter
- **Pengecekan Kode:**
  - Fungsi penambahan `add` dapat tereksekusi dengan baik. Pembatasan variabel negatif pada metode iterasi pengurangan `subtract()` dirangkai mantap dengan kondisi percabangan bersarang `if n > 0` dan `if self._value >= n`.
  - **Catatan Evaluator:** Ditemukan *Syntax Error* berupa kelebihan *whitespaces* dan simbol sama dengan (`assert counter.get_value() =    = 2`) pada saat test script dijalankan. Kesalahan telah diperbaiki secara manual oleh evaluator saat proses validasi agar kode bisa di *compile*.
- **Hasil Testing Codelab:** **PASSED** ✅ (96% - *Minor Deductions for Syntax Error*)

### 2. Tugas 2: Pengembangan ADT Stack - Aplikasi Reverse String
- **Pengecekan Kode:**
  - Metode `print_stack` sangat komprehensif mengandalkan inisialisasi list, namun terdapat kesalahan indentasi (*IndentationError*) pada blok pengembalian `return result` yang menghalangi simulasi kompilasi. Fungsi tersebut memuat 5 spasi dan bukan 4. Diperbaiki oleh evaluator saat proses pemeriksaan.
- **Hasil Testing Codelab:** **PASSED** ✅ (96% - *Minor Deductions for Indentation Error*)

### 3. Tugas 3: Analisis Kompleksitas Lanjutan
- **Tabel Analisis Kompleksitas & Jawaban:**
  - Menjabarkan efisiensi algoritma iteratif vs rekursif menggunakan rumusan $O(\log n)$ dan argumen yang sangat rasional (misalnya, membandingkan total loop iteratif berdasar Big-O ke total loop *recursive halving*).
  - Ditemukan minor *Syntax Error* berupa tanda kutip panjang multi-baris yang kurang satu tanda `"""` pada block docstring `fungsi_c()`. Telah diperbaiki manual.
- **Hasil Testing Codelab:** **PASSED** ✅ (96% - *Minor Deductions for Syntax Error*)

**NILAI MODUL 1: 96** *(Deduksi poin akibat beberapa Syntax Errors kecil yang menyebabkan kode gagal di compile saat awal pengujian)*

---

## Hasil Evaluasi Modul 2: Array

### 1. Tugas 1: Pengembangan MyArray
- **Pengecekan Kode:**
  - Logika pembalikan `reverse` dirakit stabil memakai konsep *two-pointer swapping* `while left < right` dipadu mutasi serentak variabel lokal. Pencarian nilai agregat max & min dirancang handal.
- **Hasil Testing Codelab:** **PASSED** ✅ (100%)

### 2. Tugas 2: Aplikasi Array - Statistik Data
- **Pengecekan Kode:**
  - Komparasi *second_largest* dieksekusi gesit dengan melandasi komparasinya menggunakan inisialisasi integer float tiada batas `float('-inf')` sehingga komparasi nilai bergeser dengan akurat. Filter elemen duplikat diisolasi murni menggunakan array lokal pencarian `-1`. Penulisan bersih tanpa *syntax error*.
- **Hasil Testing Codelab:** **PASSED** ✅ (100%)

### 3. Tugas 3: Aplikasi Matrix - Operasi Dasar
- **Pengecekan Kode:**
  - Matriks dirakit konsisten. Pembalikan rotasi *transpose* memanfaatkan *nested loop* baris-kolom array 2D secara sempurna `[matrix[j][i] for j in range(rows)]`. Perkalian dan pemeriksaan diagonal disusun tepat fungsi.
- **Hasil Testing Codelab:** **PASSED** ✅ (100%)

**NILAI MODUL 2: 100**


---

## Hasil Evaluasi Modul 3: Single Linked List

### 1. Tugas 1: Implementasi Single Linked List
- **Pengecekan Kode:**
  - Implementasi `reverse()` menggunakan three-pointer (`prev`, `current`, `next_node`) yang benar dan efisien. `find_min()` dan `find_max()` memulai dari `head.next` setelah inisialisasi dari `head.data`. `remove_value()` menangani semua kasus dengan menggunakan variabel `prev` pointer. `to_list()` mengkonversi linked list ke Python list dengan traversal bersih. Catatan minor: `insert_at_position()` menggunakan `ImportError` alih-alih `IndexError` untuk validasi posisi, namun tidak mempengaruhi test cases yang diberikan.
- **Hasil Testing:** **PASSED** ✅ (100%)

### 2. Tugas 2: Aplikasi Polinomial
- **Pengecekan Kode:**
  - `add_term()` mengabaikan koefisien nol di awal dan menyimpan term terurut dari pangkat tertinggi ke terendah. Penanganan duplikat pangkat menambahkan koefisien secara langsung pada node yang ada. `evaluate()` menghitung nilai dengan iterasi penuh. `add_polynomials()` mengiterasi kedua polinomial dan memanfaatkan `add_term()` untuk penggabungan otomatis. Format display menggunakan `3x^2 + 2x^1 + 5x^0` konsisten.
- **Hasil Testing:** **PASSED** ✅ (100%)

### 3. Tugas 3: Aplikasi Music Playlist
- **Pengecekan Kode:**
  - `add_song()` dan `remove_song()` diimplementasikan dengan benar menggunakan traversal linked list. `next_song()` mengembalikan `None` jika sudah di akhir (tanpa loop circular). `remove_song()` menangani pembaruan `self.current` jika lagu yang dihapus sedang diputar. `search_by_artist()` melakukan pencocokan exact string (case-sensitive). `display()` dan `format_duration()` menampilkan informasi playlist dengan rapi.
- **Hasil Testing:** **PASSED** ✅ (100%)

**NILAI MODUL 3: 100**

---

## Hasil Evaluasi Modul 4: Double Linked List & Circular Linked List

### 1. Tugas 1: Implementasi Double Linked List
- **Pengecekan Kode:**
  - `reverse()` menukar pointer `prev` dan `next` setiap node secara in-place menggunakan variabel `temp`, lalu menukar `head` dan `tail` di akhir. `find_min()` dan `find_max()` melakukan traversal dengan inisialisasi dari `head.data`. `swap_nodes()` memvalidasi batas posisi dengan `n = self.size()` sebelum menukar data. `is_palindrome()` membandingkan dari kedua ujung menggunakan kondisi terminasi `left != right and left.prev != right`.
- **Hasil Testing:** **PASSED** ✅ (100%)

### 2. Tugas 2: Aplikasi Text Editor Undo/Redo
- **Pengecekan Kode:**
  - Implementasi `type_text()` memotong redo-history dengan benar sebelum menambahkan node baru. `undo()` dan `redo()` bernavigasi melalui pointer DLL. `append_text()` menggabungkan teks saat ini dengan teks baru sebelum memanggil `type_text()`. `show_history()` menampilkan riwayat dengan marker `^current` langsung setelah teks node saat ini.
- **Hasil Testing:** **PASSED** ✅ (100%)

### 3. Tugas 3: Aplikasi Round Robin Scheduler
- **Pengecekan Kode:**
  - `add_process()` menjaga sifat sirkular CLL dengan benar. `remove_process()` menangani kasus single-node, hapus head (dengan mencari tail terlebih dahulu), dan hapus non-head. `execute_one_cycle()` mengembalikan tuple `(start_time, end_time, result_dict)` yang diurai oleh `run()`. Output timeline A(5)+B(3)+C(4) dengan quantum=2 menghasilkan total waktu 12 sesuai ekspektasi.
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

### **NILAI RATA-RATA SEMENTARA: 99 🌟**

| Modul | Nilai |
|-------|-------|
| Modul 1 | 96 |
| Modul 2 | 100 |
| Modul 3 | 100 |
| Modul 4 | 100 |
| Modul 5 | 100 |
| Modul 6 | 100 |
| **Rata-rata** | **99** |
