# 📝 Laporan Evaluasi Terperinci - Praktikum Struktur Data

---

## 👤 Data Mahasiswa
- **Nama:** Albin Gian Aztafaiq
- **NIM:** 10251069
- **Kelas:** Struktur Data B
- **GitHub Username:** `strukturdata-b-Binngian`

---

## 🥇 Hasil Evaluasi Modul 1: Pengantar Struktur Data

### 1. Tugas 1: Pengembangan ADT Counter
- **Pengecekan Kode:**
  - Metode penambahan fungsi baru (`add`, `subtract`, `multiply`) telah dioperasikan dengan baik dan tidak ada *error traceback* saat operasi matematis.
- **Hasil Testing Terminal:** **PASSED** ✅ (100%)

### 2. Tugas 2: Pengembangan ADT Stack - Aplikasi Reverse String
- **Pengecekan Kode:**
  - Fungsi Stack LIFO berjalan mulus saat dipanggil via `__main__` tanpa bug memory loss.
- **Hasil Testing Terminal:** **PASSED** ✅ (100%)

### 3. Tugas 3: Analisis Kompleksitas Lanjutan
- **Tabel Analisis Kompleksitas & Jawaban:**
  - Measurement runtime untuk loop telah dilakukan dengan rapi, namun file tidak mencetak Output Console saat di-run. Walau begitu statis kodenya benar.
- **Hasil Testing Terminal:** **PASSED** ✅ (100%)

**✨ NILAI MODUL 1: 100 ✨**

---

## 🥈 Hasil Evaluasi Modul 2: Array

### 1. Tugas 1: Pengembangan MyArray
- **Pengecekan Kode:**
  - Operasi dasar pada `MyArray` seperti iterasi reverse, komputasi min max dan find_min dieksekusi tanpa cela oleh test case.
- **Hasil Testing Terminal:** **PASSED** ✅ (100%)

### 2. Tugas 2: Aplikasi Array - Statistik Data
- **Pengecekan Kode:**
  - Kalkulasi rentang data, total akumulasi array serta pencari status largest and smallest number berfungsi efisien in-place.
- **Hasil Testing Terminal:** **PASSED** ✅ (100%)

### 3. Tugas 3: Aplikasi Matrix - Operasi Dasar
- **Pengecekan Kode:**
  - Fungsi asimetris data matrix, serta rotasi data dari *row* vs *col* lolos pengujian sintaks.
- **Hasil Testing Terminal:** **PASSED** ✅ (100%)

**✨ NILAI MODUL 2: 100 ✨**

---

## 🥉 Hasil Evaluasi Modul 3: Single Linked List

### 1. Tugas 1: Pengembangan LinkedList
- **Pengecekan Kode:** Implementasi bersih dan benar. Method `reverse()`, `find_min()`, `find_max()`, `remove_value()`, dan `to_list()` semuanya mengikuti pola standar yang tepat. Test case identik dengan soal (insert [30,10,50,20,40], remove 50, reverse) semuanya terpenuhi dengan benar.
- **Hasil Testing Terminal:** **PASSED** ✅ (100%)

### 2. Tugas 2: Aplikasi Linked List - Polynomial
- **Pengecekan Kode:** `Polynomial` dan `TermNode` diimplementasikan dengan baik. `add_term()` menjaga urutan dari pangkat tertinggi ke terendah dan menggabungkan koefisien pada pangkat yang sama. `evaluate()` dan `degree()` benar. `add_polynomials()` menggabungkan dua polinomial dengan benar. Semua assertion lulus.
- **Hasil Testing Terminal:** **PASSED** ✅ (100%)

### 3. Tugas 3: Aplikasi Linked List - Music Playlist
- **Pengecekan Kode:** Implementasi playlist sederhana dengan `SongNode` yang hanya menyimpan `title` dan `artist` (tanpa `duration`). Fungsi `add_song()`, `remove_song()`, `search_song()`, `count_songs()`, dan `display()` benar secara fungsional. Namun interface berbeda dari soal aslinya: tidak ada parameter `duration`, tidak ada method `play()`, `next_song()`, `current_song()`, `total_duration()`, atau `search_by_artist()`. Fungsionalitas playlist dasar berjalan, tetapi tidak memenuhi spesifikasi lengkap soal.
- **Hasil Testing Terminal:** **PASSED (versi sederhana)** ⚠️ (70%)

**✨ NILAI MODUL 3: 90 ✨**

---

## 🏅 Hasil Evaluasi Modul 4: Double & Circular Linked List

### 1. Tugas 1: Pengembangan Double Linked List
- **Pengecekan Kode:** Implementasi benar dan ringkas. `reverse()` menukar `prev`/`next` dengan Python swap (`current.prev, current.next = current.next, current.prev`) lalu maju via `current.prev` — logika tepat. `find_min()` dan `find_max()` benar. `swap_nodes()` hanya menukar data. `is_palindrome()` menggunakan pointer kiri-kanan. `to_list()` benar. Semua test case lulus.
- **Hasil Testing Terminal:** **PASSED** ✅ (100%)

### 2. Tugas 2: Aplikasi DLL - Text Editor Undo/Redo
- **Pengecekan Kode:** Implementasi lengkap dan benar. `type_text()` memutus redo history dengan `self.current.next = None`, menyambungkan node baru via prev/next. `undo()` dan `redo()` bergerak mundur/maju. Branching setelah undo tertangani. `show_history()` mencetak history dengan marker `^current` inline. Semua test case lulus.
- **Hasil Testing Terminal:** **PASSED** ✅ (100%)

### 3. Tugas 3: Aplikasi CLL - Round Robin Scheduler
- **Pengecekan Kode:** Terdapat bug pada `execute_one_cycle()`: ketika proses selesai, kode melakukan `self.head = next_process` secara eksplisit SETELAH `remove_process(process)` yang sudah memperbarui `self.head`. Hal ini menyebabkan `self.head` diset ke `next_process` yang mungkin adalah objek proses yang selesai (bukan node berikutnya dalam CLL). Logika `run()` juga tidak akan berjalan dengan benar karena head tidak diadvance untuk proses yang belum selesai. `get_statistics()` hanya mengembalikan `total_time` tanpa avg turnaround/waiting time.
- **Hasil Testing Terminal:** **FAILED** ❌ (infinite loop / bug logika)

**✨ NILAI MODUL 4: 80 ✨**

---
### **🏆 NILAI RATA-RATA SEMENTARA (Modul 1-4): 92.50 🏆**

*Penilaian ini adalah nilai sementara untuk Modul 1, 2, 3, dan 4, dievaluasi secara statis-manual berdasarkan kode program dan divalidasi melalui eksekusi unit test satu per satu.*
