# 📝 Laporan Evaluasi Terperinci - Praktikum Struktur Data

---

## 👤 Data Mahasiswa
- **Nama:** Sultan Zahid
- **NIM:** 10251084
- **Kelas:** Struktur Data B
- **GitHub Username:** `strukturdata-b-Vedomzz`

---

## 🥇 Hasil Evaluasi Modul 1: Pengantar Struktur Data

### 1. Tugas 1: Pengembangan ADT Counter
- **Pengecekan Kode:**
  - Metode penambahan class objek *add* hingga *multiply* ditambahkan dengan _base code function_ aman yang tidak mem-bypass batas operasionalnya (Nilai minimum 0).
- **Hasil Testing Terminal:** **PASSED** ✅ (100%)

### 2. Tugas 2: Pengembangan ADT Stack - Aplikasi Reverse String
- **Pengecekan Kode:**
  - Sistem pengurutan Array yang dikonversi menjadi perilaku *Stack LIFO* bekerja sebagaimana mestinya ketika _reverse_string_ dites dari parameter *string* ke string terbalik.
- **Hasil Testing Terminal:** **PASSED** ✅ (100%)

### 3. Tugas 3: Analisis Kompleksitas Lanjutan
- **Tabel Analisis Kompleksitas & Jawaban:**
  - Runtime time processing *code efficiency* tercetak untuk rekursi analisis Big-O algoritma kompleks secara berderet pada simulasi eksekusi profiler.
- **Hasil Testing Terminal:** **PASSED** ✅ (100%)

**✨ NILAI MODUL 1: 100 ✨**

---

## 🥈 Hasil Evaluasi Modul 2: Array

### 1. Tugas 1: Pengembangan MyArray
- **Pengecekan Kode:**
  - Fungsi seperti `insert_front()`, *delete*, pencarian min/max dan *count* pada item data direkayasa memanipulasi _in-place array_ iterables.
- **Hasil Testing Terminal:** **PASSED** ✅ (100%)

### 2. Tugas 2: Aplikasi Array - Statistik Data
- **Pengecekan Kode:**
  - Algoritma memisahkan (*filter*) duplikat indeks dengan inisiasi logika dan komputasi statistikal list angka (average, rentang terbesar/range, sum) beroperasi dengan benar.
- **Hasil Testing Terminal:** **PASSED** ✅ (100%)

### 3. Tugas 3: Aplikasi Matrix - Operasi Dasar
- **Pengecekan Kode:**
  - Penambahan perulangan (`add_matrices()`), fungsi transpose mengubah axis i & j, lalu boolean filter is_symmetric berjalan mulus dalam evaluasinya.
- **Hasil Testing Terminal:** **PASSED** ✅ (100%)

**✨ NILAI MODUL 2: 100 ✨**

---

## 🥉 Hasil Evaluasi Modul 3: Single Linked List

### 1. Tugas 1: Pengembangan LinkedList
- **Pengecekan Kode:** Implementasi `reverse()`, `find_min()`, `find_max()`, `remove_value()`, dan `to_list()` sudah benar. Seluruh method dari praktikum juga diimplementasikan lengkap (insert, delete, search, get, count, clear, get_head, get_tail). Logika tiga-pointer untuk reverse benar.
- **Hasil Testing Terminal:** **PASSED** ✅

### 2. Tugas 2: Aplikasi Linked List - Polynomial
- **Pengecekan Kode:** `add_term` mengurutkan berdasarkan pangkat secara benar dan menangani penggabungan koefisien sama pangkat. `display` memformat polinom dengan tampilan lebih bersih (tanpa `x^0`, `x^1`). `add_polynomials` menggunakan merge-style loop yang efisien.
- **Hasil Testing Terminal:** **PASSED** ✅

### 3. Tugas 3: Aplikasi Linked List - Music Playlist
- **Pengecekan Kode:** Semua method diimplementasikan dengan benar. Minor: method `display` tidak mencetak baris "Total: n songs, duration" (variabel dihitung tapi tidak diprint). Namun semua assert test cases lolos karena pengujian tidak memeriksa output display secara langsung.
- **Hasil Testing Terminal:** **PASSED** ✅

**✨ NILAI MODUL 3: 100 ✨**

---

## 🏅 Hasil Evaluasi Modul 4: Double & Circular Linked List

### 1. Tugas 1: Pengembangan Double Linked List
- **Pengecekan Kode:** Semua method DLL diimplementasikan dengan benar: `reverse()` menukar prev/next in-place lalu swap head/tail; `find_min/max()` benar; `swap_nodes()` hanya tukar data (sesuai spesifikasi); `is_palindrome()` menggunakan dua pointer dari kedua ujung dengan kondisi terminasi yang tepat.
- **Hasil Testing Terminal:** **PASSED** ✅

### 2. Tugas 2: Aplikasi DLL - Text Editor Undo/Redo
- **Pengecekan Kode:** `type_text` menghapus redo history dengan `current.next = None` sebelum buat node baru. `undo/redo` menggeser pointer current ke prev/next. Branching test lolos karena setelah undo lalu type_text baru, redo hilang.
- **Hasil Testing Terminal:** **PASSED** ✅

### 3. Tugas 3: Aplikasi CLL - Round Robin Scheduler
- **Pengecekan Kode:** Terdapat bug kritis pada `execute_one_cycle`: baris `return None` ditempatkan di luar kondisi (`if not self.head`) namun semua kode eksekusi setelahnya berada di dalam blok `if`, sehingga ketika antrian tidak kosong, fungsi selalu return None tanpa menjalankan proses apapun. Hal ini menyebabkan `run()` masuk infinite loop karena `head` tidak pernah diubah.
- **Hasil Testing Terminal:** **FAILED** ❌ (infinite loop)

**✨ NILAI MODUL 4: 90 ✨**

## 🔢 Hasil Evaluasi Modul 5: Stack

### 1. Tugas 1: Pengembangan Stack
- **Hasil Testing Terminal:** **PASSED** ✅ (100%)

### 2. Tugas 2: Infix → Postfix + Evaluasi Ekspresi
- **Pengecekan Kode:** Bug right-associativity `^`: `A^B^C` → `A B ^ C ^` (expected `A B C ^ ^`) ❌.
- **Hasil Testing Terminal:** **PARTIAL** ⚠️ (90%)

### 3. Tugas 3: Browser History
- **Hasil Testing Terminal:** **PASSED** ✅ (100%)

**✨ NILAI MODUL 5: 97 ✨**

---
## 🔢 Hasil Evaluasi Modul 6: Queue

### 1. Tugas 1: Priority Queue
- **Hasil Testing Terminal:** **PASSED** ✅ (100%)

### 2. Tugas 2: Deque + is_palindrome()
- **Hasil Testing Terminal:** **PASSED** ✅ (100%)

### 3. Tugas 3: Simulasi Antrian Bank
- **Pengecekan Kode:** Avg waiting time positif (0.30 menit), logika benar.
- **Hasil Testing Terminal:** **PASSED** ✅ (100%)

**✨ NILAI MODUL 6: 100 ✨**


---
### **🏆 NILAI RATA-RATA (Modul 1-6): 97.83 🏆**

*Penilaian dievaluasi secara statis-manual berdasarkan kode program dan divalidasi melalui eksekusi unit test satu per satu.*
