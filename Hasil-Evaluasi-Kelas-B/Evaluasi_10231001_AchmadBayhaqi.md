# 📝 Laporan Evaluasi Terperinci - Praktikum Struktur Data

---

## 👤 Data Mahasiswa
- **Nama:** Achmad Bayhaqi
- **NIM:** 10231001
- **Kelas:** Struktur Data B
- **GitHub Username:** `strukturdata-b-AchmadLyraa`

---

## 🥇 Hasil Evaluasi Modul 1: Pengantar Struktur Data

### 1. Tugas 1: Pengembangan ADT Counter
- **Pengecekan Kode:**
  - Metode penambahan fungsi baru (`add`, `subtract`, `multiply`) telah dioperasikan dengan baik tanpa mendestruksi nilai bawaan. Validasi minimum 0 pada method *subtract* terperhatikan dan terimplementasi dengan baik.
- **Hasil Testing Terminal:** **PASSED** ✅ (100%)

### 2. Tugas 2: Pengembangan ADT Stack - Aplikasi Reverse String
- **Pengecekan Kode:**
  - Konsep LIFO digunakan saat iterasi push and pop string per karakter terimplementasikan secara tepat.
- **Hasil Testing Terminal:** **PASSED** ✅ (100%)

### 3. Tugas 3: Analisis Kompleksitas Lanjutan
- **Tabel Analisis Kompleksitas & Jawaban:**
  - Analisis *execution time measurement* dan Profiler membandingkan metode rekursi dengan iterasi loop telah berhasil dieksekusi memetakan ukuran waktu (detik) sesuai.
- **Hasil Testing Terminal:** **PASSED** ✅ (100%)

**✨ NILAI MODUL 1: 100 ✨**

---

## 🥈 Hasil Evaluasi Modul 2: Array

### 1. Tugas 1: Pengembangan MyArray
- **Pengecekan Kode:**
  - Fungsi insersi array, delete depan (pengurangan list length) iterasi limit list hingga reverse diatur secara rapi.
- **Hasil Testing Terminal:** **PASSED** ✅ (100%)

### 2. Tugas 2: Aplikasi Array - Statistik Data
- **Pengecekan Kode:**
  - Method perhitungan data dari Rata-rata, deteksi largest maximum element dan second maximum serta range limit dikelola menggunakan algoritma for in-place secara komprehensif.
- **Hasil Testing Terminal:** **PASSED** ✅ (100%)

### 3. Tugas 3: Aplikasi Matrix - Operasi Dasar
- **Pengecekan Kode:**
  - Pengoperasian perhitungan matrix dua dimensi (add, product scalar, hingga transpos sumbu koordinator i/j) dikelola dengan menggunakan double level array dengan mulus.
- **Hasil Testing Terminal:** **PASSED** ✅ (100%)

**✨ NILAI MODUL 2: 100 ✨**

---

## 🥉 Hasil Evaluasi Modul 3: Single Linked List

### 1. Tugas 1: Pengembangan LinkedList
- **Pengecekan Kode:** Implementasi lengkap dan bersih. Method `reverse()` menggunakan three-pointer traversal yang benar (`prev`, `current`, `next_node`). `find_min()` dan `find_max()` meng-traverse seluruh list dengan inisialisasi dari `head.data`. `remove_value()` menangani kasus head dengan benar dan mengembalikan `True/False`. `to_list()` mengonversi ke Python list. Semua test case yang disertakan dalam file pass sempurna.
- **Hasil Testing Terminal:** **PASSED** ✅ (100%)

### 2. Tugas 2: Aplikasi Linked List - Polynomial
- **Pengecekan Kode:** Class `Polynomial` dan `TermNode` diimplementasikan dengan baik. `add_term()` menjaga urutan pangkat tertinggi ke terendah, menangani penggabungan koefisien pada pangkat yang sama (termasuk menghapus term jika koefisien jadi 0 via `remove_exponent`). `evaluate()` menghitung dengan `x**exponent` secara benar. `add_polynomials()` menggabungkan semua term dari dua polinomial. Semua assertion lulus.
- **Hasil Testing Terminal:** **PASSED** ✅ (100%)

### 3. Tugas 3: Aplikasi Linked List - Music Playlist
- **Pengecekan Kode:** Class `Playlist` dan `SongNode` diimplementasikan lengkap dengan `duration`. Method `add_song()`, `remove_song()`, `play()`, `next_song()`, `current_song()`, `total_duration()`, `song_count()`, `display()`, dan `search_by_artist()` semuanya benar. `remove_song()` menangani kasus `current` yang sedang diputar saat dihapus. Semua test case dengan playlist Queen/Eagles/Led Zeppelin lulus.
- **Hasil Testing Terminal:** **PASSED** ✅ (100%)

**✨ NILAI MODUL 3: 100 ✨**

---

## 🏅 Hasil Evaluasi Modul 4: Double & Circular Linked List

### 1. Tugas 1: Pengembangan Double Linked List
- **Pengecekan Kode:** Implementasi sangat lengkap dengan DLL beserta `head` dan `tail`. `reverse()` menukar `prev`/`next` tiap node lalu swap `head`/`tail` — benar secara logika. `find_min()` dan `find_max()` benar. `swap_nodes(pos1, pos2)` hanya menukar data (bukan pointer) — efisien dan tepat. `is_palindrome()` menggunakan pointer kiri-kanan yang bertemu di tengah — logika boundary `left != right and left.prev != right` sudah tepat. `to_list()` benar.
- **Hasil Testing Terminal:** **PASSED** ✅ (100%)

### 2. Tugas 2: Aplikasi DLL - Text Editor Undo/Redo
- **Pengecekan Kode:** `TextEditor` menggunakan DLL dengan `head` dan `current`. `type_text()` memutus semua node setelah `current` dengan `current.next = None` lalu menyambungkan node baru — branching tertangani dengan benar. `append_text()` memanggil `type_text(current + text)`. `undo()` dan `redo()` bergerak mundur/maju dengan return `True/False`. `can_undo()` / `can_redo()` benar. Semua test termasuk branching setelah undo lulus.
- **Hasil Testing Terminal:** **PASSED** ✅ (100%)

### 3. Tugas 3: Aplikasi CLL - Round Robin Scheduler
- **Pengecekan Kode:** `RoundRobinScheduler` menggunakan Circular Linked List. `add_process()` menjaga circular dengan `last.next = self.head`. `remove_process()` menangani kasus head (update last.next) dan non-head dengan benar. `execute_one_cycle()` memotong waktu dengan `min(quantum, remaining)`, menghapus proses yang selesai, dan menggeser head ke `head.next` untuk proses yang belum selesai. `run()` menjalankan semua proses dan menampilkan timeline. `get_statistics()` menghitung rata-rata turnaround dan waiting time.
- **Hasil Testing Terminal:** **PASSED** ✅ (100%)

**✨ NILAI MODUL 4: 100 ✨**

---

## 🔢 Hasil Evaluasi Modul 5: Stack

### 1. Tugas 1: Pengembangan Stack (get_min, get_max, clear, to_list, copy, reverse)
- **Pengecekan Kode:** Semua method baru diimplementasikan dengan benar. `get_min()`/`get_max()` men-traverse stack, `to_list()` mengonversi ke list, `copy()` membuat salinan, `reverse()` membalik urutan, `clear()` mengosongkan stack.
- **Hasil Testing Terminal:** **PASSED** ✅ (100%)

### 2. Tugas 2: Infix → Postfix + Evaluasi Ekspresi
- **Pengecekan Kode:** Konversi infix-to-postfix benar termasuk right-associativity `^`: `A^B^C` → `A B C ^ ^` ✅. Evaluasi postfix benar untuk semua operator termasuk pangkat.
- **Hasil Testing Terminal:** **PASSED** ✅ (100%)

### 3. Tugas 3: Browser History (dua stack)
- **Pengecekan Kode:** `BrowserHistory` menggunakan dua stack (back/forward). `visit()` membersihkan forward stack. `back()`/`forward()` memindahkan halaman antar stack dengan benar.
- **Hasil Testing Terminal:** **PASSED** ✅ (100%)

**✨ NILAI MODUL 5: 100 ✨**

---

## 🔢 Hasil Evaluasi Modul 6: Queue

### 1. Tugas 1: Priority Queue
- **Pengecekan Kode:** `dequeue()` mengeluarkan item dengan prioritas tertinggi. Penanganan prioritas sama benar. `peek()` tidak mengubah isi antrian.
- **Hasil Testing Terminal:** **PASSED** ✅ (100%)

### 2. Tugas 2: Deque + is_palindrome()
- **Pengecekan Kode:** Operasi `add_front`, `add_rear`, `remove_front`, `remove_rear` benar. `is_palindrome()` mengembalikan `True`/`False` dengan benar untuk semua kasus termasuk string kosong dan satu karakter.
- **Hasil Testing Terminal:** **PASSED** ✅ (100%)

### 3. Tugas 3: Simulasi Antrian Bank
- **Pengecekan Kode:** 20 customer, 3 teller, avg waiting time positif (0.30 menit) — logika `service_start_time` benar (tidak negatif). Statistik lengkap.
- **Hasil Testing Terminal:** **PASSED** ✅ (100%)

**✨ NILAI MODUL 6: 100 ✨**

---
### **🏆 NILAI RATA-RATA (Modul 1-6): 100.00 🏆**

*Penilaian dievaluasi secara statis-manual berdasarkan kode program dan divalidasi melalui eksekusi unit test satu per satu.*
