# 📝 Laporan Evaluasi Terperinci - Praktikum Struktur Data

---

## 👤 Data Mahasiswa
- **Nama:** Enjelin Hartini
- **NIM:** 10251015
- **Kelas:** Struktur Data B
- **GitHub Username:** `strukturdata-b-enjelinhartini`

---

## 🥇 Hasil Evaluasi Modul 1: Pengantar Struktur Data

- **Pengecekan Kode:**
  - Terjadi serangkaian isu sintaksis struktural dan indentasi bahasa skrip. Tugas 1 mengalami error pada properti indentasi nilai saat pengurangan (`self._value -= 1`). Tugas 2 mendapati AttributeError karena salah merujuk `self.items` alih-alih `self._items` seperti fungsi bawaannya. Selanjutnya, tugas 3 mengalami `SyntaxError: invalid character '→' (U+2192)` karena salah pencetakan string langsung di baris kode.
- **Hasil Testing Terminal:** **FAILED** ❌ (0%)

**✨ NILAI MODUL 1: 0 ✨**

---

## 🥈 Hasil Evaluasi Modul 2: Array

### 1. Tugas 1: Pengembangan MyArray
- **Pengecekan Kode:**
  - Metode `insert_front()`, *delete*, iterasi *find min/max* hingga array counter telah memanipulasi _in-place list_ array yang berjalan _bug-free_.
- **Hasil Testing Terminal:** **PASSED** ✅ (100%)

### 2. Tugas 2: Aplikasi Array - Statistik Data
- **Pengecekan Kode:**
  - Skrip komputasional rentang `range`, perhitungan max _element kedua_, sampai filter _remove duplicates_ tidak mendatangkan IndexError.
- **Hasil Testing Terminal:** **PASSED** ✅ (100%)

### 3. Tugas 3: Aplikasi Matrix - Operasi Dasar
- **Pengecekan Kode:**
  - Tambahan _looping matrix addition_, modifikasi sumbu x&y matriks pada `transpose`, dan loop bool `is_symmetric` lancar ter-kompilasi _True_.
- **Hasil Testing Terminal:** **PASSED** ✅ (100%)

**✨ NILAI MODUL 2: 100 ✨**

---

## 🥉 Hasil Evaluasi Modul 3: Single Linked List

### 1. Tugas 1: Pengembangan LinkedList
- **Pengecekan Kode:** Implementasi `reverse()`, `find_min()`, `find_max()`, `remove_value()`, dan `to_list()` benar dan lengkap. Digunakan folder `Tugas3` yang memiliki file tugas terstruktur lengkap.
- **Hasil Testing Terminal:** **PASSED** ✅

### 2. Tugas 2: Aplikasi Linked List - Polynomial
- **Pengecekan Kode:** `add_term` mengurutkan suku polinom dan menangani penggabungan koefisien. `display` memformat dengan gaya `coeff*x^n`. `evaluate` dan `add_polynomials` benar.
- **Hasil Testing Terminal:** **PASSED** ✅

### 3. Tugas 3: Aplikasi Linked List - Music Playlist
- **Pengecekan Kode:** Semua method playlist diimplementasikan dengan benar: `add_song`, `remove_song`, `play`, `next_song`, `current_song`, `total_duration`, `song_count`, `search_by_artist`, `display`.
- **Hasil Testing Terminal:** **PASSED** ✅

**✨ NILAI MODUL 3: 100 ✨**

---

## 🏅 Hasil Evaluasi Modul 4: Double & Circular Linked List

### 1. Tugas 1: Pengembangan Double Linked List
- **Pengecekan Kode:** Semua method DLL (`reverse`, `find_min/max`, `swap_nodes`, `is_palindrome`, `to_list`) diimplementasikan dengan benar. Digunakan folder `Tugas4` yang memiliki file tugas terstruktur lengkap.
- **Hasil Testing Terminal:** **PASSED** ✅

### 2. Tugas 2: Aplikasi DLL - Text Editor Undo/Redo
- **Pengecekan Kode:** `type_text`, `append_text`, `undo`, `redo`, `get_text`, `can_undo`, `can_redo` semuanya benar. `show_history` diimplementasikan dan menampilkan riwayat dengan penanda posisi current.
- **Hasil Testing Terminal:** **PASSED** ✅

### 3. Tugas 3: Aplikasi CLL - Round Robin Scheduler
- **Pengecekan Kode:** Implementasi Round Robin Scheduler berjalan sempurna. `add_process` dan `remove_process` mempertahankan struktur circular dengan benar untuk semua kasus. `execute_one_cycle` mengeksekusi proses dan mengembalikan dict hasil. Output timeline eksekusi sesuai dengan ekspektasi.
- **Hasil Testing Terminal:** **PASSED** ✅

**✨ NILAI MODUL 4: 100 ✨**

---

## 🥇 Hasil Evaluasi Modul 5: Stack

- **Pengecekan Kode:** Repositori diperiksa, **tidak ada file tugas untuk Modul 5**. ⚠️
- **Hasil Testing Terminal:** **FAILED** ❌ (0%)

**✨ NILAI MODUL 5: 0 ✨**

---

## 🥈 Hasil Evaluasi Modul 6: Queue

- **Pengecekan Kode:** Repositori diperiksa, **tidak ada file tugas untuk Modul 6**. ⚠️
- **Hasil Testing Terminal:** **FAILED** ❌ (0%)

**✨ NILAI MODUL 6: 0 ✨**

---
### **🏆 NILAI RATA-RATA (Modul 1-6): 50.00 🏆**

*Penilaian dievaluasi secara statis-manual berdasarkan kode program dan divalidasi melalui eksekusi unit test satu per satu.*
