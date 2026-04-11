# Laporan Evaluasi Manual - Praktikum Struktur Data

---

## Data Mahasiswa
- **Nama:** Dina Gracella Apnel Lengkong
- **NIM:** 10251002
- **Kelas:** Struktur Data A
- **GitHub Username:** `strukturdata-a-10251002`

---

## Hasil Evaluasi Modul 1: Pengantar Struktur Data

### 1. Tugas 1: Pengembangan ADT Counter
- **Pengecekan Kode:**
  - `add(n)`: Diimplementasikan dengan benar. Terdapat pengecekan kondisi agar nilai `n` harus positif.
  - `subtract(n)`: Diimplementasikan dengan benar. Terdapat penanganan *error* jika `n` bernilai kurang dari nol, dan logika memastikan selisih tidak di bawah `0`.
  - `multiply(n)`: Diimplementasikan dengan benar. Terdapat *error handling* jika `n` negatif.
  - `__str__()`: Diimplementasikan dengan penulisan format string yang tepat.
- **Hasil Testing Codelab:** **PASSED** ✅ (100%)
- **Catatan:** Kode ditulis sangat bersih dan memperhatikan penanganan batasan *error* (*edge cases*).

### 2. Tugas 2: Pengembangan ADT Stack - Aplikasi Reverse String
- **Pengecekan Kode:**
  - `print_stack()`: Berhasil menampilkan daftar list/item stack dengan benar.
  - `clear()`: Method `clear()` di list berhasil meniadakan elemen stack.
  - Aplikasi `reverse_string(s)`: Logika memanfaatkan Stack LIFO berhasil membalikkan string sesuai diagram flowchart.
- **Hasil Testing Codelab:** **PASSED** ✅ (100%)

### 3. Tugas 3: Analisis Kompleksitas Lanjutan
- **Tabel Analisis Kompleksitas & Jawaban:**
  - Pengisian kompleksitas fungsi A sampai F seluruhnya **BENAR**. Alasan yang diberikan akurat. Jawaban atas pertanyaan 1-5 menunjukkan pemahaman yang sangat mendalam terkait konsep *Big-O Notation*, pengenalan eksponensial/logaritmik, dan implementasi kasus nyata.
- **Catatan:** Pemahaman konseptual sangat *solid*.

**NILAI MODUL 1: 100**

---

## Hasil Evaluasi Modul 2: Array

### 1. Tugas 1: Pengembangan MyArray
- **Pengecekan Kode:**
  - Fungsi `insert_front()`, `delete_front()`, `find_min()`, `find_max()`, `count()`, dan `reverse()` diimplementasikan dengan logika iterasi list Array yang kuat dan rapi sesuai flowchart.
- **Hasil Testing Codelab:** **PASSED** ✅ (100%)

### 2. Tugas 2: Aplikasi Array - Statistik Data
- **Pengecekan Kode:**
  - Mampu menggunakan Array buatan (`MyArray`) untuk melakukan penghitungan agregat (`sum`, `average`, `range`, pola duplikat `remove_duplicates`, dll.) dengan presisi tipe data `float`/`int` yang tepat.
- **Hasil Testing Codelab:** **PASSED** ✅ (100%)

### 3. Tugas 3: Aplikasi Matrix - Operasi Dasar
- **Pengecekan Kode:**
  - Pemahaman Array Multidimensi (Matrix) sudah sangat baik. Logika penjumlahan matriks (`add_matrices`), matriks perputaran transpose (`transpose_matrix`), matriks perkalian skalar, pembuktian simetris (`is_symmetric`), dan pengambilan diagonal matriks ter-implementasi sempurna.
- **Hasil Testing Codelab:** **PASSED** ✅ (100%)

**NILAI MODUL 2: 100**

---

## Hasil Evaluasi Modul 3: Single Linked List

### 1. Tugas 1: Implementasi Single Linked List
- **Pengecekan Kode:**
  - Method `reverse()`, `find_min()`, `find_max()`, `remove_value()`, dan `to_list()` semuanya diimplementasikan dengan benar menggunakan `None` sebagai sentinel (berbeda dengan Praktikum yang menggunakan class Node sebagai sentinel, Tugas sudah diperbaiki ke standar).
  - Semua method dari praktikum (insert_at_position, delete_at_position, get, count, clear, get_head, get_tail) diimplementasikan dengan lengkap dan benar.
- **Hasil Testing:** **PASSED** ✅ (100%)

### 2. Tugas 2: Aplikasi Polynomial
- **Pengecekan Kode:**
  - `add_term()` menyimpan term terurut dari pangkat tertinggi ke terendah dan menggabungkan koefisien saat pangkat sama. `evaluate()` dan `degree()` benar. `add_polynomials()` berfungsi dengan tepat.
  - Display menampilkan format `3x^2 + 2x^1 + 5x^0` (format konsisten menyertakan semua eksponen).
- **Hasil Testing:** **PASSED** ✅ (100%)

### 3. Tugas 3: Aplikasi Music Playlist
- **Pengecekan Kode:**
  - Semua fitur playlist diimplementasikan: `add_song()`, `remove_song()`, `play()`, `next_song()`, `current_song()`, `total_duration()`, `song_count()`, `display()`, `search_by_artist()` semuanya berfungsi dengan benar.
- **Hasil Testing:** **PASSED** ✅ (100%)

**NILAI MODUL 3: 100**

---

## Hasil Evaluasi Modul 4: Double Linked List & Circular Linked List

### 1. Tugas 1: Implementasi Double Linked List
- **Pengecekan Kode:**
  - Terdapat duplikasi definisi `__init__` dalam class (dua blok `__init__` dan dua blok method dasar), namun Python menggunakan definisi terakhir sehingga tidak menyebabkan error. Method `reverse()`, `find_min()`, `find_max()`, `swap_nodes()`, `is_palindrome()`, `to_list()` semuanya diimplementasikan dengan benar.
  - Semua test assertions berhasil dipenuhi.
- **Hasil Testing:** **PASSED** ✅ (100%)

### 2. Tugas 2: Aplikasi Text Editor Undo/Redo
- **Pengecekan Kode:**
  - `type_text()` menghapus forward history (branching) dengan benar. `undo()`/`redo()` memindahkan pointer current. `show_history()` menampilkan history dengan penanda `^current` langsung di samping state aktif.
- **Hasil Testing:** **PASSED** ✅ (100%)

### 3. Tugas 3: Aplikasi Round Robin Scheduler
- **Pengecekan Kode:**
  - Implementasi CLL untuk scheduler Round Robin berjalan dengan benar. `add_process()` mempertahankan struktur circular. `remove_process()` menangani semua kasus (satu node, head, tengah). `execute_one_cycle()` dan `run()` menghasilkan timeline yang tepat.
- **Hasil Testing:** **PASSED** ✅ (100%)

**NILAI MODUL 4: 100**

---

## Hasil Evaluasi Modul 5: Stack

### 1. Tugas 1: Pengembangan Stack dengan Method Baru
- **Pengecekan Kode:**
  - `get_min()` dan `get_max()` menggunakan `min(self.items)` / `max(self.items)` — benar.
  - `clear()`, `to_list()`, `copy()`, dan `reverse()` semuanya terimplementasi dan lulus test.
- **Hasil Testing:** **PASSED** ✅ (100%)

### 2. Tugas 2: Konversi dan Evaluasi Ekspresi
- **Pengecekan Kode:**
  - Fungsi `infix_to_postfix()`, `evaluate_postfix()`, dan `calculate()` seluruhnya `pass` — tidak diimplementasikan.
  - Semua 16 test case menghasilkan `None`.
- **Hasil Testing:** **GAGAL** ❌ (0%) — tidak diimplementasikan

### 3. Tugas 3: Aplikasi Browser History
- **Pengecekan Kode:**
  - `BrowserHistory` dengan dua stack berjalan benar. `visit()`, `back()`, `forward()`, `can_go_back()`, `can_go_forward()` semua sesuai spesifikasi.
- **Hasil Testing:** **PASSED** ✅ (100%)

**NILAI MODUL 5: 67** *(T1:100 + T2:0 + T3:100) / 3 ≈ 67*

---

## Hasil Evaluasi Modul 6: Queue

### 1. Tugas 1: Implementasi Priority Queue
- **Pengecekan Kode:**
  - List of tuples terurut descending. Enqueue insertion sort, FIFO untuk prioritas sama terjaga.
- **Hasil Testing:** **PASSED** ✅ (100%)

### 2. Tugas 2: Implementasi Deque + Palindrome
- **Pengecekan Kode:**
  - Deque dengan operasi front/rear benar. Palindrome checker lulus semua 7 test case.
- **Hasil Testing:** **PASSED** ✅ (100%)

### 3. Tugas 3: Simulasi Antrian Bank
- **Pengecekan Kode:**
  - Simulasi 3 teller, 20 customers — semua terlayani. Statistik waktu tunggu & servis terhitung benar.
- **Hasil Testing:** **PASSED** ✅ (100%)

**NILAI MODUL 6: 100**

---

### **NILAI RATA-RATA SEMENTARA: 94 🌟**

| Modul | Nilai |
|-------|-------|
| Modul 1 | 100 |
| Modul 2 | 100 |
| Modul 3 | 100 |
| Modul 4 | 100 |
| Modul 5 | 67 |
| Modul 6 | 100 |
| **Rata-rata** | **94** |

*Catatan: Modul 5 Tugas 2 (Konversi Infix→Postfix) tidak diimplementasikan.*
