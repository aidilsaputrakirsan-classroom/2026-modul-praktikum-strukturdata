# Laporan Evaluasi Terperinci - Praktikum Struktur Data

---

## Data Mahasiswa
- **Nama:** Syahrina Aliyyu Tunggadewi
- **NIM:** 10251056
- **Kelas:** Struktur Data A
- **GitHub Username:** `strukturdata-a-SyahrinaAliyyuTunggadewi`

---

## Hasil Evaluasi Modul 1: Pengantar Struktur Data

### 1. Tugas 1: Pengembangan ADT Counter
- **Pengecekan Kode:**
  - Metode penambahan `add` dikodekan dengan baik tanpa redundansi iterasi. Kontrol untuk error aritmatika minimal nol telah divalidasi tepat melalui baris `else: self._value = 0` sehingga kalkulasi `subtract()` sepenuhnya mulus.
- **Hasil Testing Codelab:** **PASSED** ✅ (100%)

### 2. Tugas 2: Pengembangan ADT Stack - Aplikasi Reverse String
- **Pengecekan Kode:**
  - `print_stack()` mengandalkan *built-in list behavior* sementara fungsi balik `reverse_string` mengaplikan format Stack sesuai kriteria, *push*-*pop* karakter dilalui mulus menggunakan tipe list array sederhana.
- **Hasil Testing Codelab:** **PASSED** ✅ (100%)

### 3. Tugas 3: Analisis Kompleksitas Lanjutan
- **Tabel Analisis Kompleksitas & Jawaban:**
  - Argumen Big-O dirumuskan jelas, mahasiswa juga membandingkan waktu kompleksitas dalam skala real, misal bahwa `1 juta operasi bagi O(n)` tersebut sudah cukup mudah bagi komputer modern namun untuk jumlah miliaran disarankan "optimasi paralel". Sangat kritis dan mantap!  
- **Hasil Testing Codelab:** **PASSED** ✅ (100%)

**NILAI MODUL 1: 100**

---

## Hasil Evaluasi Modul 2: Array

### 1. Tugas 1: Pengembangan MyArray
- **Pengecekan Kode:**
  - Operasi struktur `insert_front` dieksekusi dengan metode built-in namun masih terisolir dengan baik. Fungsi max & min dideklarasikan cermat menggunakan pengisian sementara indeks ke-0 dan diteruskan dengan pemotongan pembacaan `for el in self._elements[1:]`. Pertukaran pemutaran dinamis (reverse swap) tersusun efisien menggunakan rasio tengah `.size() // 2`.
- **Hasil Testing Codelab:** **PASSED** ✅ (100%)

### 2. Tugas 2: Aplikasi Array - Statistik Data
- **Pengecekan Kode:**
  - Pada pembentukan pencarian angka terbesar kedua, implementasi `None` digunakan dengan elegan sebagai flag sementara ganda. Fungsi range dideklarasikan matang. Metode eliminasi terduplikasi `remove_duplicates()` membandingkan nilai sebelum dimasukkan (O(n²)) dengan fungsionalitas mulus.
- **Hasil Testing Codelab:** **PASSED** ✅ (100%)

### 3. Tugas 3: Aplikasi Matrix - Operasi Dasar
- **Pengecekan Kode:**
  - Metode permutasi matrix dimodelkan secara komprehensif. Syarat pengecekan operasi diagonal pun disertakan tanpa kendala. Nested loop kalkulasi matematika `add_matrices` dikendalikan sangat tanggap pada setiap koordinat *row-column*.
- **Hasil Testing Codelab:** **PASSED** ✅ (100%)

**NILAI MODUL 2: 100**

---

## Hasil Evaluasi Modul 3: Single Linked List

### 1. Tugas 1: Implementasi Single Linked List
- **Pengecekan Kode:**
  - Semua method wajib (reverse, find_min, find_max, remove_value, to_list) diimplementasikan dengan benar. Algoritma reverse menggunakan tiga pointer (prev, current, next_node) yang efisien O(n). find_min/find_max menggunakan traversal linear dengan tracking nilai min/max. remove_value menangani kasus head maupun tengah/akhir dengan tepat.
- **Hasil Testing:** **PASSED** ✅ (100%)

### 2. Tugas 2: Aplikasi Polinomial
- **Pengecekan Kode:**
  - Kelas Polynomial menggunakan linked list terurut dari pangkat tertinggi ke terendah. Method add_term menangani penggabungan koefisien pada pangkat yang sama. evaluate dan degree diimplementasikan dengan benar. add_polynomials membangun polynomial baru dari dua polynomial input.
- **Hasil Testing:** **PASSED** ✅ (100%)

### 3. Tugas 3: Aplikasi Music Playlist
- **Pengecekan Kode:**
  - Kelas Playlist dengan SongNode lengkap. Method add_song, remove_song, play, next_song, current_song, total_duration, song_count, display, dan search_by_artist diimplementasikan dengan benar dan berfungsi baik. search_by_artist menggunakan case-insensitive comparison.
- **Hasil Testing:** **PASSED** ✅ (100%)

**NILAI MODUL 3: 100**

---

## Hasil Evaluasi Modul 4: Double Linked List & Circular Linked List

### 1. Tugas 1: Implementasi Double Linked List
- **Pengecekan Kode:**
  - Implementasi DLL lengkap dengan head dan tail. Method reverse, find_min, find_max, swap_nodes diimplementasikan dengan benar. Namun terdapat bug kritis pada method is_palindrome: baris `left = left.next` dan `right = right.prev` berada di luar while loop (indentasi salah), menyebabkan pointer tidak pernah diperbarui dan program masuk infinite loop saat method dipanggil.
- **Hasil Testing:** **FAILED** ❌ - is_palindrome menyebabkan infinite loop (timeout), program terhenti paksa setelah 10 detik.

### 2. Tugas 2: Aplikasi Text Editor Undo/Redo
- **Pengecekan Kode:**
  - Implementasi TextEditor menggunakan DLL dengan StateNode. Method type_text, append_text, undo, redo, get_text, can_undo, can_redo, dan show_history semuanya berfungsi dengan benar. Branching (menghapus history redo saat mengetik setelah undo) ditangani dengan tepat.
- **Hasil Testing:** **PASSED** ✅ (100%)

### 3. Tugas 3: Aplikasi Round Robin Scheduler
- **Pengecekan Kode:**
  - Implementasi RoundRobinScheduler menggunakan Circular Linked List. add_process, remove_process, execute_one_cycle, run, display_queue, dan get_statistics diimplementasikan dengan benar. Eksekusi rotasi proses berjalan sesuai algoritma Round Robin.
- **Hasil Testing:** **PASSED** ✅ (100%)

**NILAI MODUL 4: 90**

---
### **NILAI RATA-RATA SEMENTARA: 97.50 🌟**

*Penilaian ini adalah nilai sementara untuk Modul 1 hingga Modul 4, dievaluasi secara statis berdasarkan instruksi/flowchart dan divalidasi melalui unit test execution.*
