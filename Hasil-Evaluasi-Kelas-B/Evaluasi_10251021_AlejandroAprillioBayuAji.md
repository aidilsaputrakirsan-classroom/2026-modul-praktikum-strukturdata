# 📝 Laporan Evaluasi Terperinci - Praktikum Struktur Data

---

## 👤 Data Mahasiswa
- **Nama:** Alejandro Aprillio Bayu Aji
- **NIM:** 10251021
- **Kelas:** Struktur Data B
- **GitHub Username:** `strukturdata-b-alejandroaprillio`

---

## 🥇 Hasil Evaluasi Modul 1: Pengantar Struktur Data

### 1. Tugas 1: Pengembangan ADT Counter
- **Pengecekan Kode:**
  - Metode penambahan kalkulasi nilai matematis seperti iterasi *add*, *multiply*, dan *subtract* dengan filter minimal bernilai 0, diimplementasikan aman dengan parameter yang sesuai.
- **Hasil Testing Terminal:** **PASSED** ✅ (100%)

### 2. Tugas 2: Pengembangan ADT Stack - Aplikasi Reverse String
- **Pengecekan Kode:**
  - Fungsi Stack LIFO berjalan baik. Iterasi push() karakter array ke parameter pembalik `pop()` berjalan mulus mengeksekusi *reverse_string* list kata secara *in-place*.
- **Hasil Testing Terminal:** **PASSED** ✅ (100%)

### 3. Tugas 3: Analisis Kompleksitas Lanjutan
- **Tabel Analisis Kompleksitas & Jawaban:**
  - Fungsi profil komputasi pada tes `code execution` rekursi hingga loop array berjalan logis men-trace iterasi limit komputasi program.
- **Hasil Testing Terminal:** **PASSED** ✅ (100%)

**✨ NILAI MODUL 1: 100 ✨**

---

## 🥈 Hasil Evaluasi Modul 2: Array

### 1. Tugas 1: Pengembangan MyArray
- **Pengecekan Kode:**
  - Logic penghapusan (*delete_front()*), *insert_front()* awal, *count()* max array length dan modifikasi iterasi max/min list nilai direspon sesuai fungsi yang ditugaskan.
- **Hasil Testing Terminal:** **PASSED** ✅ (100%)

### 2. Tugas 2: Aplikasi Array - Statistik Data
- **Pengecekan Kode:**
  - Logic kalkulator range, filtering duplikasi angka hingga akumulasi sum untuk nilai statistik avg beroperasi efektif pada uji coba parameter index out of range exception.
- **Hasil Testing Terminal:** **PASSED** ✅ (100%)

### 3. Tugas 3: Aplikasi Matrix - Operasi Dasar
- **Pengecekan Kode:**
  - Tambahan kalkulasi _matrix addition_, loop index rotasi baris_i dan kolom_j *transpose*, identifikasi array _symmetric_ bebas debug code failure.
- **Hasil Testing Terminal:** **PASSED** ✅ (100%)

**✨ NILAI MODUL 2: 100 ✨**

---

## 🥉 Hasil Evaluasi Modul 3: Single Linked List

### 1. Tugas 1: Pengembangan LinkedList
- **Pengecekan Kode:** Implementasi `reverse()`, `find_min()`, `find_max()`, `remove_value()`, dan `to_list()` benar dan efisien. Logika reverse menggunakan tiga pointer standar. `remove_value` menangani edge case head dan node tidak ditemukan.
- **Hasil Testing Terminal:** **PASSED** ✅

### 2. Tugas 2: Aplikasi Linked List - Polynomial
- **Pengecekan Kode:** `add_term` mengurutkan suku dari pangkat tertinggi, menggabungkan koefisien jika eksponen sama. `display` memformat polinom secara dinamis (menghilangkan koefisien 1, tidak menampilkan `^1` dan `^0`). `add_polynomials` menggunakan while loop merge yang tepat.
- **Hasil Testing Terminal:** **PASSED** ✅

### 3. Tugas 3: Aplikasi Linked List - Music Playlist
- **Pengecekan Kode:** Semua method playlist diimplementasikan lengkap dan benar. `next_song` memeriksa apakah current tidak None sebelum berpindah. `display` mencetak total durasi.
- **Hasil Testing Terminal:** **PASSED** ✅

**✨ NILAI MODUL 3: 100 ✨**

---

## 🏅 Hasil Evaluasi Modul 4: Double & Circular Linked List

### 1. Tugas 1: Pengembangan Double Linked List
- **Pengecekan Kode:** Logika DLL (reverse, find_min/max, swap_nodes, is_palindrome, to_list) semuanya benar. Namun terdapat baris `from prakpemstruk.kode3_1_... import Node` yang merujuk modul tidak terpasang, sehingga file gagal dijalankan langsung (`ModuleNotFoundError`). Setelah import dihapus, semua test lolos.
- **Hasil Testing Terminal:** **FAILED** ❌ (ModuleNotFoundError - import tidak valid, namun logika benar)

### 2. Tugas 2: Aplikasi DLL - Text Editor Undo/Redo
- **Pengecekan Kode:** `type_text` menghapus redo history dengan while loop sebelum membuat node baru. `undo/redo` benar. `show_history` tidak diimplementasikan (pass), namun tidak mempengaruhi hasil test assert.
- **Hasil Testing Terminal:** **PASSED** ✅

### 3. Tugas 3: Aplikasi CLL - Round Robin Scheduler
- **Pengecekan Kode:** `remove_process` hanya menangani kasus single-node (langsung set head=None); untuk kasus multi-node jika yang dihapus bukan head, tidak ada logika penghapusan. `execute_one_cycle` tidak mengembalikan `result` (tidak ada `return result`). `run()` mencetak "All processes completed!" di dalam loop setiap iterasi. Akibatnya scheduler tidak berfungsi dengan benar dan masuk infinite loop.
- **Hasil Testing Terminal:** **FAILED** ❌ (infinite loop akibat remove_process tidak lengkap)

**✨ NILAI MODUL 4: 80 ✨**

---
### **🏆 NILAI RATA-RATA SEMENTARA (Modul 1-4): 95.00 🏆**

*Penilaian ini adalah nilai sementara untuk Modul 1, 2, 3, dan 4, dievaluasi secara statis-manual berdasarkan kode program dan divalidasi melalui eksekusi unit test satu per satu.*
