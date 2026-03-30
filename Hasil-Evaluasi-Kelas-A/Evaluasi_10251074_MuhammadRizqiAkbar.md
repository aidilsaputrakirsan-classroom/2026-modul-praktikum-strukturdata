# Laporan Evaluasi Terperinci - Praktikum Struktur Data

---

## Data Mahasiswa
- **Nama:** Muhammad Rizqi Akbar
- **NIM:** 10251074
- **Kelas:** Struktur Data A
- **GitHub Username:** `strukturdata-a-MuhammadRizqiAkbar33`

---

## Hasil Evaluasi Modul 1: Pengantar Struktur Data

### 1. Tugas 1: Pengembangan ADT Counter
- **Pengecekan Kode:**
  - Metode penambahan `add()` dan pemotongan `subtract()` tersusun logis sesuai batasan. Blok verifikasi untuk pertahanan nilai nol diamankan melalui fitur `max(0, self._value - n)` yang langsung menjamin efisiensi kode tanpa *if statement* bersarang yang lebih padat. 
- **Hasil Testing Codelab:** **PASSED** ✅ (100%)

### 2. Tugas 2: Pengembangan ADT Stack - Aplikasi Reverse String
- **Pengecekan Kode:**
  - Pengembalian string terbalik (*reverse_string*) sukses dibangun dengan instalisasi `Stack()` mandiri dan mengulang per baris karakter masuk via `push` lalu keluar berturutan melalui `pop`.
- **Hasil Testing Codelab:** **PASSED** ✅ (100%)

### 3. Tugas 3: Analisis Kompleksitas Lanjutan
- **Tabel Analisis Kompleksitas & Jawaban:**
  - Kalimat dan penjabaran naratif untuk analisa matematika Big-O logis dan langsung aplikatif di keseharian, seperti simulasi absensi sekolah daring 2000 siswa sebagai padanan fungsi fatalistik `O(n²)`.
- **Hasil Testing Codelab:** **PASSED** ✅ (100%)

**NILAI MODUL 1: 100**

---

## Hasil Evaluasi Modul 2: Array

### 1. Tugas 1: Pengembangan MyArray
- **Pengecekan Kode:**
  - Celah manipulasi array berhasil diselesaikan. Metode *two-pointers* diterapkan secara kental dalam proses pembalikan letak data (`reverse()`). Pemilihan *pointer* dengan increment `+ 1` untuk `left` dan `- 1` untuk `right` selaras dengan prinsip pertukaran (*swap*) dasar.
- **Hasil Testing Codelab:** **PASSED** ✅ (100%)

### 2. Tugas 2: Aplikasi Array - Statistik Data
- **Pengecekan Kode:**
  - Penyelesaian metode `find_second_largest` dan `remove_duplicates` dioptimalkan dengan cermat. Nilai elemen ditarik dalam satu putaran melintasi array saja `O(n)` meminimalisir lag komputasional, ini adalah cara mahir mengukur statis dua *state* dari variabel.
- **Hasil Testing Codelab:** **PASSED** ✅ (100%)

### 3. Tugas 3: Aplikasi Matrix - Operasi Dasar
- **Pengecekan Kode:**
  - Penambahan operasi simetris dua dimensi `add_matrices` hingga pengecekan kembar silang `is_symmetric` diselesaikan dalam iterasi kolom/baris berstandar. Mahasiswa merapikan pembatasan index kolom `len(matrix[i])` pada metode diagonal komputasi, menunjukkan pemahaman yang matang atas referensi silang matriks tak simetris.
- **Hasil Testing Codelab:** **PASSED** ✅ (100%)

**NILAI MODUL 2: 100**


---

## Hasil Evaluasi Modul 3: Single Linked List

### 1. Tugas 1: Implementasi Single Linked List
- **Pengecekan Kode:**
  - Implementasi `reverse()` menggunakan pendekatan three-pointer klasik (`prev`, `current`, `next_temp`) yang efisien O(n). Metode `find_min()` dan `find_max()` ditulis dengan inisialisasi dari `head.data` dan traversal penuh. `remove_value()` menangani kasus head dan non-head dengan benar. `to_list()` mengkonversi linked list ke Python list secara rapi. Seluruh method baru terintegrasi mulus dengan method praktikum yang sudah ada.
- **Hasil Testing:** **PASSED** ✅ (100%)

### 2. Tugas 2: Aplikasi Polinomial
- **Pengecekan Kode:**
  - Kelas `Polynomial` menyimpan term terurut dari pangkat tertinggi ke terendah. `add_term()` menangani kasus duplikat pangkat dengan menambahkan koefisien dan menghapus node jika koefisien menjadi 0. `evaluate()` menghitung nilai dengan benar menggunakan `x ** exponent`. Fungsi `add_polynomials()` memanfaatkan `_get_terms_by_exponent()` untuk menjumlahkan dua polinomial dengan efisien.
- **Hasil Testing:** **PASSED** ✅ (100%)

### 3. Tugas 3: Aplikasi Music Playlist
- **Pengecekan Kode:**
  - Kelas `Playlist` mengimplementasikan semua operasi yang diperlukan. `next_song()` menambahkan fitur loop ke awal saat mencapai akhir playlist. `remove_song()` memperhatikan penanganan `self.current` saat lagu yang sedang diputar dihapus. `search_by_artist()` menggunakan perbandingan case-insensitive via `.lower()`. `format_duration()` memformat durasi ke format mm:ss dengan benar.
- **Hasil Testing:** **PASSED** ✅ (100%)

**NILAI MODUL 3: 100**

---

## Hasil Evaluasi Modul 4: Double Linked List & Circular Linked List

### 1. Tugas 1: Implementasi Double Linked List
- **Pengecekan Kode:**
  - `reverse()` menukar `prev` dan `next` setiap node secara in-place lalu menukar `head` dan `tail` — implementasi idiomatik DLL. `find_min()` dan `find_max()` melakukan traversal penuh dengan inisialisasi dari head. `swap_nodes()` hanya menukar data (bukan pointer) sesuai spesifikasi. `is_palindrome()` menggunakan dua pointer dari head dan tail yang bertemu di tengah, menangani kasus genap dan ganjil dengan tepat.
- **Hasil Testing:** **PASSED** ✅ (100%)

### 2. Tugas 2: Aplikasi Text Editor Undo/Redo
- **Pengecekan Kode:**
  - `TextEditor` menggunakan DLL sebagai riwayat editing. `type_text()` memutus redo-history dengan meng-set `current.next = None` sebelum menambahkan node baru — penanganan branching yang benar. `undo()` dan `redo()` melakukan navigasi pointer dengan tepat. `can_undo()` dan `can_redo()` mengecek pointer prev/next dengan sederhana. `show_history()` menampilkan seluruh riwayat dari head dengan marker `<- current`.
- **Hasil Testing:** **PASSED** ✅ (100%)

### 3. Tugas 3: Aplikasi Round Robin Scheduler
- **Pengecekan Kode:**
  - `RoundRobinScheduler` menggunakan Circular Linked List. `add_process()` menjaga sifat sirkular dengan benar. `remove_process()` menangani semua kasus: satu node, hapus head, dan hapus non-head. `execute_one_cycle()` mengeksekusi dengan quantum yang tepat, memperbarui `remaining_time`, dan menggeser head ke proses berikutnya. Output timeline sesuai ekspektasi: A(5)+B(3)+C(4) dengan quantum=2 menghasilkan total waktu 12.
- **Hasil Testing:** **PASSED** ✅ (100%)

**NILAI MODUL 4: 100**

---
### **NILAI RATA-RATA SEMENTARA: 100.00 🌟**

*Penilaian ini adalah nilai sementara untuk Modul 1 hingga Modul 4, dievaluasi secara statis berdasarkan instruksi/flowchart dan divalidasi melalui unit test execution.*
