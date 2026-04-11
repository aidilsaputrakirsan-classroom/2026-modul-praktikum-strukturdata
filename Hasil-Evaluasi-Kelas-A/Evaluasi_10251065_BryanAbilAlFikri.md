# Laporan Evaluasi Terperinci - Praktikum Struktur Data

---

## Data Mahasiswa
- **Nama:** Bryan Abil Al-Fikri
- **NIM:** 10251065
- **Kelas:** Struktur Data A
- **GitHub Username:** `strukturdata-a-Bryan1065`

---

## Hasil Evaluasi Modul 1: Pengantar Struktur Data

### 1. Tugas 1: Pengembangan ADT Counter
- **Pengecekan Kode:**
  - Fungsi penambahan, pengurangan, hingga perkalian disusun solid menggunakan operator penugasan Python standar (`+=`, `-=`, `*=`). Terlihat pemahaman akan metode `reset` bawaan yang dieksekusi benar.
- **Hasil Testing Codelab:** **PASSED** ✅ (100%)

### 2. Tugas 2: Pengembangan ADT Stack - Aplikasi Reverse String
- **Pengecekan Kode:**
  - Metode operasional *stack stack.push()* dan *stack.pop()* dibalut rapi. Untuk fungsi ekstraksi pembalikan berjalan efisien mendayagunakan skema LIFO *last in first out* secara utuh.
- **Hasil Testing Codelab:** **PASSED** ✅ (100%)

### 3. Tugas 3: Analisis Kompleksitas Lanjutan
- **Tabel Analisis Kompleksitas & Jawaban:**
  - Pemahaman terhadap *Triple Nested Loop O(n³)* dan *Recursive Halving O(log n)* dijelaskan logis dan mudah dipahami. Contoh skenario dunia nyata untuk O(n²) diilustrasikan dengan valid.
- **Hasil Testing Codelab:** **PASSED** ✅ (100%)

**NILAI MODUL 1: 100**

---

## Hasil Evaluasi Modul 2: Array

### 1. Tugas 1: Pengembangan MyArray
- **Pengecekan Kode:**
  - Implementasi pertukaran nilai bolak-balik fitur *reverse* dijalankan aman menggunakan pendekatan `while left < right` yang efisien *in-place*. 
- **Hasil Testing Codelab:** **PASSED** ✅ (100%)

### 2. Tugas 2: Aplikasi Array - Statistik Data
- **Pengecekan Kode:**
  - *find_second_largest* tidak menggunakan angka literal statis tetapi *None* sebagai referensi inisiasi. Fitur logika duplikasi *remove_duplicates* menghindari pendobelan array element-by-element sukses.
- **Hasil Testing Codelab:** **PASSED** ✅ (100%)

### 3. Tugas 3: Aplikasi Matrix - Operasi Dasar
- **Pengecekan Kode:**
  - Transposisi matrix dan modifikasi per komponen melalui komputasi iteratif yang rapi dengan `zip()` yang menunjukkan penguasaan *built-in methods* Python dengan presisi tinggi.
- **Hasil Testing Codelab:** **PASSED** ✅ (100%)

**NILAI MODUL 2: 100**

---

## Hasil Evaluasi Modul 3: Single Linked List

### 1. Tugas 1: Implementasi Single Linked List
- **Pengecekan Kode:**
  - Semua method wajib (reverse, find_min, find_max, remove_value, to_list) diimplementasikan dengan benar dan lengkap. Algoritma reverse menggunakan tiga pointer efisien O(n). find_min dan find_max menggunakan traversal linear. remove_value menangani semua kasus edge dengan tepat.
- **Hasil Testing:** **PASSED** ✅ (100%)

### 2. Tugas 2: Aplikasi Polinomial
- **Pengecekan Kode:**
  - Polynomial menggunakan linked list terurut dari pangkat tertinggi ke terendah. add_term menangani insert terurut dan penggabungan koefisien pada pangkat yang sama. evaluate menggunakan kalkulasi pangkat dengan benar. add_polynomials menghasilkan polynomial baru hasil penjumlahan yang tepat.
- **Hasil Testing:** **PASSED** ✅ (100%)

### 3. Tugas 3: Aplikasi Music Playlist
- **Pengecekan Kode:**
  - Kelas Playlist dengan SongNode diimplementasikan lengkap. Semua method (add_song, remove_song, play, next_song, current_song, total_duration, song_count, display, search_by_artist) berfungsi dengan benar. File dikumpulkan tanpa ekstensi .py namun terdeteksi sebagai Python script yang valid.
- **Hasil Testing:** **PASSED** ✅ (100%)

**NILAI MODUL 3: 100**

---

## Hasil Evaluasi Modul 4: Double Linked List & Circular Linked List

### 1. Tugas 1: Implementasi Double Linked List
- **Pengecekan Kode:**
  - DLL dengan head dan tail diimplementasikan lengkap. reverse, find_min, find_max, swap_nodes, is_palindrome semuanya benar. is_palindrome menggunakan two-pointer approach dengan terminasi loop yang tepat. File dikumpulkan tanpa ekstensi .py namun valid sebagai Python script.
- **Hasil Testing:** **PASSED** ✅ (100%)

### 2. Tugas 2: Aplikasi Text Editor Undo/Redo
- **Pengecekan Kode:**
  - TextEditor menggunakan DLL dengan StateNode. type_text menghapus future history (branching) sebelum menambah state baru. undo/redo bernavigasi mundur/maju dengan benar. show_history menampilkan seluruh chain history dengan marker current yang jelas menggunakan format kurung kotak.
- **Hasil Testing:** **PASSED** ✅ (100%)

### 3. Tugas 3: Aplikasi Round Robin Scheduler
- **Pengecekan Kode:**
  - RoundRobinScheduler menggunakan CLL. execute_one_cycle mengeksekusi quantum dan melakukan rotasi `self.head = self.head.next` dengan tepat. remove_process menangani penghapusan node dari CLL dengan benar. run menghasilkan timeline Round Robin yang akurat sesuai output yang diharapkan.
- **Hasil Testing:** **PASSED** ✅ (100%)

**NILAI MODUL 4: 100**

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

> ⏳ **Belum ada submission Modul 6** saat evaluasi dilakukan (per April 2026). Nilai akan diperbarui jika mahasiswa mengumpulkan.

**NILAI MODUL 6: -** *(belum dikumpulkan)*

---

### **NILAI RATA-RATA SEMENTARA: 100 🌟**

| Modul | Nilai |
|-------|-------|
| Modul 1 | 100 |
| Modul 2 | 100 |
| Modul 3 | 100 |
| Modul 4 | 100 |
| Modul 5 | 100 |
| Modul 6 | - |
| **Rata-rata (M1-M5)** | **100** |
