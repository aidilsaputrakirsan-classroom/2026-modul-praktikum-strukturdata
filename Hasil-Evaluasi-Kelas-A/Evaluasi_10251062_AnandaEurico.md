# Laporan Evaluasi Terperinci - Praktikum Struktur Data

---

## Data Mahasiswa
- **Nama:** Ananda Eurico Rhiva Rifqia Salim
- **NIM:** 10251062
- **Kelas:** Struktur Data A
- **GitHub Username:** `strukturdata-a-AnandaEurico`

---

## Hasil Evaluasi Modul 1: Pengantar Struktur Data

### 1. Tugas 1: Pengembangan ADT Counter
- **Pengecekan Kode:**
  - Metode `subtract()` bekerja sangat baik menggunakan struktur kendali kondisional ganda `if n > 0 and self._value >= n:` dan varian penempatan ke 0 agar *value* tidak kurang dari 0.
- **Hasil Testing Codelab:** **PASSED** ✅ (100%)

### 2. Tugas 2: Pengembangan ADT Stack - Aplikasi Reverse String
- **Pengecekan Kode:**
  - Logika pembalikan String *while not stack.is_empty(): reversed_str += stack.pop()* dieksekusi elegan sesuai implementasi kerangka teori LIFO.
- **Hasil Testing Codelab:** **PASSED** ✅ (100%)

### 3. Tugas 3: Analisis Kompleksitas Lanjutan
- **Tabel Analisis Kompleksitas & Jawaban:**
  - Analisis dijawab dengan tepat, rapi, dan padat. Menyertakan contoh kasus sorting dengan bubble sort (O(n²)) sebagai implementasi *real world* kompleksitas yang tak diinginkan pada skala data besar.
- **Hasil Testing Codelab:** **PASSED** ✅ (100%)

**NILAI MODUL 1: 100**

---

## Hasil Evaluasi Modul 2: Array

### 1. Tugas 1: Pengembangan MyArray
- **Pengecekan Kode:**
  - Fitur `reverse` mengadopsi standar komputasi dengan `left, right = 0, len(self._elements) - 1` hingga ke titik temu antar iterator, metode eksekusi algoritma *in-place* optimal.
- **Hasil Testing Codelab:** **PASSED** ✅ (100%)

### 2. Tugas 2: Aplikasi Array - Statistik Data
- **Pengecekan Kode:**
  - Implementasi *second_largest* tidak menggunakan metode filter manual *range default*, pencarian iteratif ganda di set dengan variabel nilai awal ke `float('-inf')` yang efektif untuk merujuk perbandingan angka minimum dasar.
- **Hasil Testing Codelab:** **PASSED** ✅ (100%)

### 3. Tugas 3: Aplikasi Matrix - Operasi Dasar
- **Pengecekan Kode:**
  - Operasi manipulasi matriks bebas kendala secara dimensional. Struktur validasi yang disiapkan telah diimplementasikan dengan `ValueError` guna menghindari kerusakan kalkulasi.
- **Hasil Testing Codelab:** **PASSED** ✅ (100%)

**NILAI MODUL 2: 100**

---

## Hasil Evaluasi Modul 3: Single Linked List

### 1. Tugas 1: Implementasi Single Linked List
- **Pengecekan Kode:**
  - Semua method wajib (reverse, find_min, find_max, remove_value, to_list) diimplementasikan dengan benar. Logika reverse menggunakan iterasi tiga pointer yang tepat. find_min/find_max dengan traversal O(n). remove_value menangani semua kasus dengan benar.
- **Hasil Testing:** **PASSED** ✅ (100%)

### 2. Tugas 2: Aplikasi Polinomial
- **Pengecekan Kode:**
  - Polynomial diimplementasikan menggunakan linked list terurut. add_term menangani insert terurut dan penggabungan koefisien pada pangkat sama. display menggunakan format `3x^2 + 2x + 5` (tanpa eksponen untuk x^1 dan x^0). evaluate dan add_polynomials berfungsi dengan benar.
- **Hasil Testing:** **PASSED** ✅ (100%)

### 3. Tugas 3: Aplikasi Music Playlist
- **Pengecekan Kode:**
  - Playlist dengan SongNode lengkap. Semua method diimplementasikan dengan benar termasuk add_song, remove_song, play, next_song, current_song, total_duration, song_count, display, dan search_by_artist. Format display menggunakan separator 30 karakter '='.
- **Hasil Testing:** **PASSED** ✅ (100%)

**NILAI MODUL 3: 100**

---

## Hasil Evaluasi Modul 4: Double Linked List & Circular Linked List

### 1. Tugas 1: Implementasi Double Linked List
- **Pengecekan Kode:**
  - DLL diimplementasikan lengkap dengan head dan tail. reverse, find_min, find_max, swap_nodes, is_palindrome semuanya diimplementasikan dengan benar. is_palindrome menggunakan two-pointer approach yang tepat dengan loop termination yang benar.
- **Hasil Testing:** **PASSED** ✅ (100%)

### 2. Tugas 2: Aplikasi Text Editor Undo/Redo
- **Pengecekan Kode:**
  - TextEditor menggunakan DLL dengan StateNode. Semua fungsi (type_text, append_text, undo, redo, get_text, can_undo, can_redo, show_history) berfungsi dengan benar. Branching saat pengetikan setelah undo ditangani dengan tepat.
- **Hasil Testing:** **PASSED** ✅ (100%)

### 3. Tugas 3: Aplikasi Round Robin Scheduler
- **Pengecekan Kode:**
  - RoundRobinScheduler diimplementasikan menggunakan CLL. Terdapat bug pada method execute_one_cycle: setelah mengeksekusi quantum untuk proses yang belum selesai, `self.head` tidak diperbarui ke proses berikutnya (tidak ada `self.head = self.head.next`). Akibatnya scheduler tidak melakukan rotasi antar proses dan memproses setiap proses sampai selesai secara berurutan, bukan round-robin.
- **Hasil Testing:** **FAILED** ❌ - Scheduler tidak melakukan rotasi antar proses (sequential processing bukan round-robin). Output menunjukkan Process A selesai terlebih dahulu, lalu B, lalu C.

**NILAI MODUL 4: 80**

---

## Hasil Evaluasi Modul 5: Stack

### 1. Tugas 1: Pengembangan Stack dengan Method Baru
- **Pengecekan Kode:** Semua method baru (`get_min`, `get_max`, `clear`, `to_list`, `copy`, `reverse`) diimplementasikan dengan benar. Semua test lulus.
- **Hasil Testing:** **PASSED** ✅ (100%)

### 2. Tugas 2: Konversi dan Evaluasi Ekspresi
- **Pengecekan Kode:** `infix_to_postfix()` benar termasuk right-associativity `^`. `evaluate_postfix()` dan `calculate()` benar. Semua test lulus.
- **Hasil Testing:** **PASSED** ✅ (100%)

### 3. Tugas 3: Aplikasi Browser History
- **Pengecekan Kode:** `BrowserHistory` menggunakan dua stack. `visit()`, `back()`, `forward()`, dan `current_page()` benar. Semua test lulus.
- **Hasil Testing:** **PASSED** ✅ (100%)

**NILAI MODUL 5: 100**

---

## Hasil Evaluasi Modul 6: Queue

### 1. Tugas 1: Implementasi Priority Queue
- **Pengecekan Kode:** `PriorityQueue` benar dengan urutan prioritas yang tepat. Semua test lulus.
- **Hasil Testing:** **PASSED** ✅ (100%)

### 2. Tugas 2: Implementasi Deque + Palindrome
- **Pengecekan Kode:** `Deque` benar. `is_palindrome()` menggunakan Deque lokal dengan benar. Semua 7 test lulus.
- **Hasil Testing:** **PASSED** ✅ (100%)

### 3. Tugas 3: Simulasi Antrian Bank
- **Pengecekan Kode:** Semua 20 customers terlayani, namun rata-rata waktu tunggu negatif (-6.15 menit) — bug logika pada perhitungan `waiting_time`. Nilai `service_start_time` dihitung sebelum pelanggan tiba, menyebabkan selisih negatif.
- **Hasil Testing:** **BUG LOGIKA** ⚠️ (60%)

**NILAI MODUL 6: 87** *(T1:100 + T2:100 + T3:60) / 3 ≈ 87*

---

### **NILAI RATA-RATA SEMENTARA: 95 🌟**

| Modul | Nilai |
|-------|-------|
| Modul 1 | 100 |
| Modul 2 | 100 |
| Modul 3 | 100 |
| Modul 4 | 80 |
| Modul 5 | 100 |
| Modul 6 | 87 |
| **Rata-rata** | **95** |
