# Laporan Evaluasi Terperinci - Praktikum Struktur Data

---

## Data Mahasiswa
- **Nama:** Rifat Sutha Abdillah
- **NIM:** 10251107
- **Kelas:** Struktur Data A
- **GitHub Username:** `strukturdata-a-RifatSuthaAbdillah`

---

## Hasil Evaluasi Modul 1: Pengantar Struktur Data

### 1. Tugas 1: Pengembangan ADT Counter
- **Pengecekan Kode:**
  - Operasi instansiasi `add` dan pengali `multiply` berfungsi wajar. Fungsi limit minimal 0 pada operasi kurang disikapi sangat berhati-hati melalui pengecekan `if self._value > 0`.
- **Hasil Testing Codelab:** **PASSED** ✅ (100%)

### 2. Tugas 2: Pengembangan ADT Stack - Aplikasi Reverse String
- **Pengecekan Kode:**
  - Metode pencetakan stack memanfaatkan mekanisme instan Python List dan balikan string diraih konsisten melalui struktur `while` loop yang merakit huruf baru berdasarkan metode pop satu persatu.
- **Hasil Testing Codelab:** **PASSED** ✅ (100%)

### 3. Tugas 3: Analisis Kompleksitas Lanjutan
- **Tabel Analisis Kompleksitas & Jawaban:**
  - Kalimat dan analoginya terjelaskan gamblang, bahkan menambahkan notasi logaritmik seperti "\$O(\log n)$". Eksperimen logika pergerakan untuk basis data pengguna KTP sebagai *bottleneck* skenario `O(n²)` dirumuskan realistis.
- **Hasil Testing Codelab:** **PASSED** ✅ (100%)

**NILAI MODUL 1: 100**

---

## Hasil Evaluasi Modul 2: Array

### 1. Tugas 1: Pengembangan MyArray
- **Pengecekan Kode:**
  - Fitur mutasi data *reverse* memamerkan implementasi perulangan bagi setengah array (`for i in range(n // 2):`) yang ditukar-silang untuk mengamankan redundansi pembacaan ulang, ini efisiensi algoritma kelas wahid. Pengecekan max dan min tersaring errornya dengan apik melalui iterasi natural `for val in self._elements`. 
- **Hasil Testing Codelab:** **PASSED** ✅ (100%)

### 2. Tugas 2: Aplikasi Array - Statistik Data
- **Pengecekan Kode:**
  - Performa *search* terbesar ke dua diamankan menggunakan penempatan nilai minus terekstrim (`float('-inf')`), dan penyortiran ganda diracik tepat guna mencegah error index yang bergeser. Pengecekan nilai *duplikat* terdistribusi rapi untuk verifikasi double loop.
- **Hasil Testing Codelab:** **PASSED** ✅ (100%)

### 3. Tugas 3: Aplikasi Matrix - Operasi Dasar
- **Pengecekan Kode:**
  - Semua operasi (termasuk perkalian skalar, rotasi matrix `transpose_matrix`, diagonal, dan uji simetris `is_symmetric`) dibina apik dengan alokasi iterasi baris yang berstruktur solid.
- **Hasil Testing Codelab:** **PASSED** ✅ (100%)

**NILAI MODUL 2: 100**

---

## Hasil Evaluasi Modul 3: Single Linked List

### 1. Tugas 1: Implementasi Single Linked List
- **Pengecekan Kode:**
  - **File Tugas 1 (Pengembangan LinkedList dengan reverse/find_min/find_max/remove_value/to_list) tidak ditemukan** dalam folder `Praktikum & Tugas 3`. Folder hanya berisi `Tugas3.1` (Music Playlist), `Tugas3.2` (Polynomial), dan `Tugas3.3` (Music Playlist duplikat). Tidak ada file yang mengimplementasikan class `LinkedList` dengan method-method baru yang diminta.
- **Hasil Testing:** **TIDAK ADA SUBMISSION** ❌ (0%)

### 2. Tugas 2: Aplikasi Polinomial
- **Pengecekan Kode:**
  - `add_term()` menangani penyisipan terurut dengan benar. Format display menggunakan tanda `+`/`-` secara elegan sesuai koefisien positif/negatif. `add_polynomials()` menggunakan pendekatan copy-and-add yang sederhana dan benar. Output: `3x^2 + 2x^1 + 5x^0`.
- **Hasil Testing:** **PASSED** ✅ (100%)

### 3. Tugas 3: Aplikasi Music Playlist
- **Pengecekan Kode:**
  - Terdapat **duplikasi**: file `Tugas3.1` dan `Tugas3.3` keduanya berisi implementasi Music Playlist yang hampir identik. Implementasi sendiri sudah benar — semua operasi (`add_song`, `remove_song`, `play`, `next_song`, `search_by_artist`) berjalan dengan baik. `remove_song` mereset `current` ke `None` jika lagu yang dihapus sedang diputar.
- **Hasil Testing:** **PASSED** ✅ (100%)

**NILAI MODUL 3: 70**

---

## Hasil Evaluasi Modul 4: Double Linked List & Circular Linked List

### 1. Tugas 1: Implementasi Double Linked List
- **Pengecekan Kode:**
  - `reverse()` menukar pointer prev/next per node secara in-place dan memperbarui `tail` di awal. `swap_nodes()` menemukan kedua node dalam satu pass dengan flag idx. `is_palindrome()` menggunakan dua pointer (left dari head, right dari tail). Semua method terdokumentasi dan benar.
- **Hasil Testing:** **PASSED** ✅ (100%)

### 2. Tugas 2: Aplikasi Text Editor Undo/Redo
- **Pengecekan Kode:**
  - `type_text()` menyambungkan node baru ke current tanpa memotong cabang redo secara eksplisit (`self.current.next = None` tidak dipanggil sebelum penambahan node baru). Namun karena `self.current.next = new_node` segera menimpa referensi lama, tes branching tetap lulus. Ini merupakan minor issue: redo history lama tidak dibersihkan secara eksplisit sehingga ada potensi memory leak.
- **Hasil Testing:** **PASSED** ✅ (100%)

### 3. Tugas 3: Aplikasi Round Robin Scheduler
- **Pengecekan Kode:**
  - `add_process()` membangun circular list dengan benar. `remove_process()` menangani kasus single-node (`head == head.next`) dan multi-node dengan mencari `prev`. Eksekusi Round Robin berjalan sesuai: A → B → C → A → B(selesai) → C(selesai) → A(selesai) dalam 12 unit waktu. Statistik lengkap disertakan.
- **Hasil Testing:** **PASSED** ✅ (100%)

**NILAI MODUL 4: 100**

---
### **NILAI RATA-RATA SEMENTARA: 92.50 🌟**

*Penilaian ini adalah nilai sementara untuk Modul 1 hingga Modul 4, dievaluasi secara statis berdasarkan instruksi/flowchart dan divalidasi melalui unit test execution.*
