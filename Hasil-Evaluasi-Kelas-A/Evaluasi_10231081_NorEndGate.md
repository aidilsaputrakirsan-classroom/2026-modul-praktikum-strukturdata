# Laporan Evaluasi Terperinci - Praktikum Struktur Data

---

## Data Mahasiswa
- **Nama:** Rendy
- **NIM:** 10231081
- **Kelas:** Struktur Data A
- **GitHub Username:** `strukturdata-a-NorEndGate`

---

## Hasil Evaluasi Modul 1: Pengantar Struktur Data

### 1. Tugas 1: Pengembangan ADT Counter
- **Pengecekan Kode:**
  - `add(n)`: Diimplementasikan dengan pengkondisian nilai minimum (harus positif).
  - `subtract(n)`: Pengecekan *boundary* berhasil dieksekusi agar selisihnya tidak menyebabkan defisit mutlak di bawah `0`.
  - `multiply(n)`: Dikerjakan dengan baik. Terdapat pengecekan jika nilai minus/negatif.
  - `__str__()`: Pembuatan representasi format string terimplementasi.
- **Hasil Testing Codelab:** **PASSED** ✅ (100%)

### 2. Tugas 2: Pengembangan ADT Stack - Aplikasi Reverse String
- **Pengecekan Kode:**
  - Fitur `print_stack` menampilkan elemen LIFO dari array stack (`self._items`).
  - Fitur `clear` menghapus list *items* seluruh instansiasi Object.
  - Implementasi reverse_string berjalan tepat memanfaatkan sifat LIFO stack buatan mahasiswa.
- **Hasil Testing Codelab:** **PASSED** ✅ (100%)

### 3. Tugas 3: Analisis Kompleksitas Lanjutan
- **Tabel Analisis Kompleksitas & Jawaban:**
  - Prediksi operasi Big-O akurat (A-F). Mahasiswa mengerti korelasi waktu terhadap tipe eksekusi *iterative* versus rekurens. Secara inisiatif menyesuaikan variabel unit test `n` lebih kecil saat algoritma bersifat log(n³). Jawaban dan penjabaran narasi juga sangat baik dan komprehensif.
- **Hasil Testing Codelab:** **PASSED** ✅ (100%)

**NILAI MODUL 1: 100**

---

## Hasil Evaluasi Modul 2: Array

### 1. Tugas 1: Pengembangan MyArray
- **Pengecekan Kode:**
  - Metode penambahan maupun pengurangan node awal `insert_front` / `delete_front` berjalan valid melalui manipulasi index array internal Python. Pengecekan minimaks dan pemutaran arah array diimplementasikan sesuai *flowchart*.
- **Hasil Testing Codelab:** **PASSED** ✅ (100%)

### 2. Tugas 2: Aplikasi Array - Statistik Data
- **Pengecekan Kode:**
  - Berhasil menyusun pengolahan analitik dari angka *floating point* / *integer*. Fungsi aggregasi seperti sum, filter unit ganda (*remove duplicates*), perankingan rata-rata tereksekusi tanpa hambatan.
- **Hasil Testing Codelab:** **PASSED** ✅ (100%)

### 3. Tugas 3: Aplikasi Matrix - Operasi Dasar
- **Pengecekan Kode:**
  - Mahasiswa memahami *multi-dimensional arrays*. Mahasiswa mengimplementasikan fungsi ekstra untuk komparasi validasi dan representasi matriks *printing* (tugas yang melebihi standar baseline). *Output* komparasi dan kalkulasi skalar sangat stabil.
- **Hasil Testing Codelab:** **PASSED** ✅ (100%)

**NILAI MODUL 2: 100**

---

## Hasil Evaluasi Modul 3: Single Linked List

### 1. Tugas 1: Implementasi Single Linked List
- **Pengecekan Kode:**
  - Semua method baru diimplementasikan dengan benar: `reverse()` menggunakan three-pointer technique (O(n)), `find_min()` dan `find_max()` melakukan traversal penuh, `remove_value()` menghapus node pertama dengan nilai yang cocok, `to_list()` mengkonversi ke Python list.
  - Method dari praktikum (insert, delete, search, size, dll) semuanya lengkap dan benar.
- **Hasil Testing:** **PASSED** ✅ (100%)

### 2. Tugas 2: Aplikasi Polynomial
- **Pengecekan Kode:**
  - Class `Polynomial` dan `TermNode` diimplementasikan dengan baik. `add_term()` menjaga urutan dari pangkat tertinggi ke terendah dan menangani koefisien sama (merge). `evaluate()` dan `degree()` benar. `add_polynomials()` menghasilkan hasil penjumlahan yang tepat.
  - Bonus: menangani koefisien 0, auto-sort pangkat, dan display dengan format matematika yang rapi.
- **Hasil Testing:** **PASSED** ✅ (100%)

### 3. Tugas 3: Aplikasi Music Playlist
- **Pengecekan Kode:**
  - Class `Playlist` dan `SongNode` lengkap. Semua fitur diimplementasikan: `add_song()`, `remove_song()`, `play()`, `next_song()`, `current_song()`, `total_duration()`, `song_count()`, `display()`, `search_by_artist()`. Helper `format_duration()` mengkonversi detik ke format mm:ss.
  - `remove_song()` menangani update `self.current` saat lagu aktif dihapus.
- **Hasil Testing:** **PASSED** ✅ (100%)

**NILAI MODUL 3: 100**

---

## Hasil Evaluasi Modul 4: Double Linked List & Circular Linked List

### 1. Tugas 1: Implementasi Double Linked List
- **Pengecekan Kode:**
  - `reverse()` menukar prev/next setiap node dan memperbarui head/tail dengan benar. `find_min()` dan `find_max()` melakukan traversal O(n). `swap_nodes()` menukar data dua node berdasarkan posisi. `is_palindrome()` membandingkan dari kedua ujung menggunakan pointer head dan tail secara bersamaan. `to_list()` untuk konversi ke Python list.
- **Hasil Testing:** **PASSED** ✅ (100%)

### 2. Tugas 2: Aplikasi Text Editor Undo/Redo
- **Pengecekan Kode:**
  - Class `TextEditor` menggunakan DLL (`StateNode` dengan prev/next). `type_text()` memutus redo history saat mengetik baru (branching). `append_text()` menambahkan ke state saat ini. `undo()` dan `redo()` memindahkan current pointer. `show_history()` menampilkan seluruh history dengan posisi current yang akurat.
- **Hasil Testing:** **PASSED** ✅ (100%)

### 3. Tugas 3: Aplikasi Round Robin Scheduler
- **Pengecekan Kode:**
  - Class `RoundRobinScheduler` menggunakan Circular Linked List. `add_process()` menambah proses ke CLL dengan pointer circular yang benar. `remove_process()` menangani kasus satu proses maupun proses di head/tengah. `execute_one_cycle()` menjalankan quantum atau sisa burst, mencatat statistik. `run()` menjalankan semua proses hingga selesai dengan timeline yang tepat (A=5, B=3, C=4, quantum=2 → total 12).
- **Hasil Testing:** **PASSED** ✅ (100%)

**NILAI MODUL 4: 100**

---

## Hasil Evaluasi Modul 5: Stack

### 1. Tugas 1: Pengembangan Stack dengan Method Baru
- **Pengecekan Kode:**
  - `get_min()` dan `get_max()` menggunakan `min(self.items)` / `max(self.items)` — efisien dan benar O(n).
  - `clear()` mengeset `self.items = []` — bersih dan benar.
  - `to_list()` mengembalikan `list(self.items)` — copy yang benar (bottom→top).
  - `copy()` membuat Stack baru dengan elemen yang sama — independent copy terbukti lulus test.
  - `reverse()` menggunakan auxiliary stack (pop semua ke temp stack, pop kembali) — logika benar.
- **Hasil Testing:** **PASSED** ✅ (100%)

### 2. Tugas 2: Konversi dan Evaluasi Ekspresi
- **Pengecekan Kode:**
  - Fungsi `infix_to_postfix()`, `evaluate_postfix()`, dan `calculate()` seluruhnya dibiarkan sebagai `pass` tanpa implementasi apapun.
  - Semua 16 test case menghasilkan `None`.
- **Hasil Testing:** **GAGAL** ❌ (0%) — tidak diimplementasikan

### 3. Tugas 3: Aplikasi Browser History
- **Pengecekan Kode:**
  - `BrowserHistory` menggunakan dua Stack (`back_stack`, `forward_stack`). Logika `visit()` → push current ke back_stack lalu clear forward_stack sudah benar.
  - `back()` dan `forward()` memindahkan halaman antar stack secara tepat.
  - `can_go_back()` dan `can_go_forward()` mengembalikan boolean berdasarkan keadaan stack.
- **Hasil Testing:** **PASSED** ✅ (100%)

**NILAI MODUL 5: 67** *(T1:100 + T2:0 + T3:100) / 3 ≈ 67*

---

## Hasil Evaluasi Modul 6: Queue

### 1. Tugas 1: Implementasi Priority Queue
- **Pengecekan Kode:**
  - `PriorityQueue` menyimpan elemen sebagai list of tuples `(priority, item)` terurut descending.
  - `enqueue()` melakukan insertion sort berdasarkan prioritas — FIFO untuk prioritas sama terjaga.
  - `dequeue()` mengembalikan item (bukan tuple) dari posisi pertama.
  - `display()` menampilkan format `PriorityQueue: [(p, item), ...]`.
- **Hasil Testing:** **PASSED** ✅ (100%)

### 2. Tugas 2: Implementasi Deque + Palindrome
- **Pengecekan Kode:**
  - `Deque` menggunakan list Python. `add_front()` pakai `insert(0, item)`, `add_rear()` pakai `append()`.
  - `remove_front()` dan `remove_rear()` benar dengan penanganan empty check.
  - `is_palindrome()` menggunakan Deque — semua 7 test case lulus termasuk string kosong.
- **Hasil Testing:** **PASSED** ✅ (100%)

### 3. Tugas 3: Simulasi Antrian Bank
- **Pengecekan Kode:**
  - `BankSimulation` dengan 3 teller melayani 20 customers secara lengkap.
  - Statistik: rata-rata waktu tunggu 0.30 menit, semua customer terlayani.
  - Logika assignment teller (mencari teller available) berjalan benar.
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

*Catatan: Modul 5 Tugas 2 (Konversi Infix→Postfix) tidak diimplementasikan sama sekali.*
