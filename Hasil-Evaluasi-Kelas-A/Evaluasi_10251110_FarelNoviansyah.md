# Laporan Evaluasi Terperinci - Praktikum Struktur Data

---

## Data Mahasiswa
- **Nama:** Farel Noviansyah
- **NIM:** 10251110
- **Kelas:** Struktur Data A
- **GitHub Username:** `strukturdata-a-10251110`

---

## Hasil Evaluasi Modul 1: Pengantar Struktur Data

### 1. Tugas 1: Pengembangan ADT Counter
- **Pengecekan Kode:**
  - Fungsi beroperasi stabil namun ditemukan banyak penulisan *class* `Counter` berganda/berulang dengan identasi tak menentu yang menumpuk *namespace* (Bad Practice). Namun program selamat berkat deklarasi paling bawah yang menimpa defenisi rusak sebelumnya.
- **Hasil Testing Codelab:** **PASSED** ✅ (100%)

### 2. Tugas 2: Pengembangan ADT Stack - Aplikasi Reverse String
- **Pengecekan Kode:**
  - Metode LIFO pada Reverse String berjalan sangat mulus. Terdapat duplikasi blok `class Stack` namun sama seperti logika atas, modul berjalan menimpa struktur sebelumnya. 
- **Hasil Testing Codelab:** **PASSED** ✅ (100%)

### 3. Tugas 3: Analisis Kompleksitas Lanjutan
- **Tabel Analisis Kompleksitas & Jawaban:**
  - Terdapat *SyntaxError* diakibatkan string comment mutli-line (`"""`) belum tertutup dengan baik di *bottom-line*, asisten laboran harus menyunting skrip sebelum program dapat *compile*. Walau begitu, isian penalaran Big-O terjawab komprehensif.
- **Hasil Testing Codelab:** **PASSED** ✅ (90%) - Pengurangan 10 poin akibat *SyntaxError* docstring.

**NILAI MODUL 1: 96**

---

## Hasil Evaluasi Modul 2: Array

### 1. Tugas 1: Pengembangan MyArray
- **Pengecekan Kode:**
  - Modul array dibuat *clean*. Proses `reverse` menumpu pada metode manipulasi instan bawaan python `self._elements.reverse()` dibandingkan *two pointer swapping* manual. Tetap fungsional.
- **Hasil Testing Codelab:** **PASSED** ✅ (100%)

### 2. Tugas 2: Aplikasi Array - Statistik Data
- **Pengecekan Kode:**
  - `find_second_largest()` dapat mengecualikan angka duplikat dan mengambil peringkat secara presisi di list Python. Komentar terisi lengkap dan Modularitas terjaga baik.
- **Hasil Testing Codelab:** **PASSED** ✅ (100%)

### 3. Tugas 3: Aplikasi Matrix - Operasi Dasar
- **Pengecekan Kode:**
  - Fitur simetris divalidasikan singkat berlandaskan `return matrix == transposed` walau menyisipkan kata `pass` dibelakang *return statement* (Redundant). Operasi matriks *add* dan *multiply* bebas malfungsi.
- **Hasil Testing Codelab:** **PASSED** ✅ (100%)

**NILAI MODUL 2: 100**

---

## Hasil Evaluasi Modul 3: Single Linked List

### 1. Tugas 1: Implementasi Single Linked List
- **Pengecekan Kode:**
  - Implementasi `reverse()`, `find_min()`, `find_max()`, `remove_value()`, dan `to_list()` semuanya benar dan bersih. Terdokumentasi dengan baik. Semua assert test berhasil dilalui.
- **Hasil Testing:** **PASSED** ✅ (100%)

### 2. Tugas 2: Aplikasi Polinomial
- **Pengecekan Kode:**
  - `add_polynomials()` menggunakan pendekatan copy-and-add (menambahkan semua term p1 kemudian p2), namun `add_term()` tidak menggabungkan koefisien saat pangkat sudah ada dalam hasil. Akibatnya output menampilkan `3x^2 + 2x^2 + 6x + 8` alih-alih `5x^2 + 6x + 8`. Test `evaluate(1)` tetap lulus karena hasilnya sama secara numerik (3+2+6+8=19), namun representasi polinomial tidak dimerge dengan benar — ini merupakan bug minor pada fungsi `add_term` yang hanya ditrigger saat digunakan via `add_polynomials`.
- **Hasil Testing:** **PASSED** ✅ (90%) — Test lulus namun terdapat bug display: koefisien pangkat sama tidak digabung.

### 3. Tugas 3: Aplikasi Music Playlist
- **Pengecekan Kode:**
  - Semua operasi playlist berjalan benar. `add_song`, `remove_song`, `play`, `next_song`, `current_song`, `total_duration`, `song_count`, `search_by_artist` diimplementasikan dengan tepat menggunakan Single Linked List.
- **Hasil Testing:** **PASSED** ✅ (100%)

**NILAI MODUL 3: 95**

---

## Hasil Evaluasi Modul 4: Double Linked List & Circular Linked List

### 1. Tugas 1: Implementasi Double Linked List
- **Pengecekan Kode:**
  - Semua method DLL (`reverse`, `find_min`, `find_max`, `swap_nodes`, `is_palindrome`, `to_list`) diimplementasikan dengan benar. `reverse()` menukar pointer prev/next dan menukar head/tail. `is_palindrome()` menggunakan counter setengah list.
- **Hasil Testing:** **PASSED** ✅ (100%)

### 2. Tugas 2: Aplikasi Text Editor Undo/Redo
- **Pengecekan Kode:**
  - Seluruh operasi `type_text`, `append_text`, `undo`, `redo`, `branching` berjalan benar. `show_history()` menampilkan label `(current)` di akhir entry yang aktif (format berbeda namun informatif).
- **Hasil Testing:** **PASSED** ✅ (100%)

### 3. Tugas 3: Aplikasi Round Robin Scheduler
- **Pengecekan Kode:**
  - Terdapat **bug pada logika rotasi**: scheduler mengeksekusi Process A secara berturut-turut 3 kali sebelum beralih ke Process B, lalu B berturut-turut, lalu C berturut-turut — bukan pola Round Robin yang bergantian antar proses. Masalah ada pada `remove_process` atau mekanisme rotasi `head` yang tidak memindahkan proses ke belakang antrian setelah dieksekusi quantum. Proses diselesaikan secara sequential bukan circular.
- **Hasil Testing:** **FAILED** ❌ — Round Robin tidak bekerja: proses dieksekusi sequential (A selesai dulu, baru B, baru C) bukan bergantian per quantum.

**NILAI MODUL 4: 85**

---
### **NILAI RATA-RATA SEMENTARA: 94.00 🌟**

*Penilaian ini adalah nilai sementara untuk Modul 1 hingga Modul 4, dievaluasi secara statis berdasarkan instruksi/flowchart dan divalidasi melalui unit test execution.*
