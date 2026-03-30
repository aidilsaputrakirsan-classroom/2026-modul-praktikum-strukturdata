# Laporan Evaluasi Terperinci - Praktikum Struktur Data

---

## Data Mahasiswa
- **Nama:** Nur Hayyu Nurdin
- **NIM:** 10251095
- **Kelas:** Struktur Data A
- **GitHub Username:** `strukturdata-a-NurHayyu-10251095`

---

## Hasil Evaluasi Modul 1: Pengantar Struktur Data

### 1. Tugas 1: Pengembangan ADT Counter
- **Pengecekan Kode:**
  - Fungsi penambahan `add` dan pengali `multiply` dieksekusi bersih. Restriksi *counter* pada batasan nol telah disuntikkan secara solid dalam fungsi pengurangan `subtract()`.
- **Hasil Testing Codelab:** **PASSED** ✅ (100%)

### 2. Tugas 2: Pengembangan ADT Stack - Aplikasi Reverse String
- **Pengecekan Kode:**
  - Teknik penyusunan `stack` cukup fundamental namun efektif dalam menargetkan memori LIFO (Last-In-First-Out) saat string dijejalkan (*push*) lantas dipanggil (*pop*) tanpa bocor ke indeks di bawahnya.
- **Hasil Testing Codelab:** **PASSED** ✅ (100%)

### 3. Tugas 3: Analisis Kompleksitas Lanjutan
- **Tabel Analisis Kompleksitas & Jawaban:**
  - Argumentasi logis dan bernarasi apik. Pembahasan tentang filter spam di email dengan jumlah lebih dari 1 juta entitas melawan 1 juta filter *blacklist* sebagai analogi $O(n^2)$ yang gagal (*crash real-time*) sangat inovatif dan akurat.
- **Hasil Testing Codelab:** **PASSED** ✅ (100%)

**NILAI MODUL 1: 100**

---

## Hasil Evaluasi Modul 2: Array

### 1. Tugas 1: Pengembangan MyArray
- **Pengecekan Kode:**
  - Penyematan kendali pergerakan node ke dalam awal array `insert_front` telah dijaga restriksinya dari kemungkinan error melalui indeks minus `if 0 <= len`. Namun pembalikan array `reverse` dikesekusi apik dengan menukar batas `left` dan `right`.
- **Hasil Testing Codelab:** **PASSED** ✅ (100%)

### 2. Tugas 2: Aplikasi Array - Statistik Data
- **Pengecekan Kode:**
  - Rata-rata elemen telah dihitung memakai `while loop` yang manual dan konsisten `while i < length`. Pada penemuan nilai kedua tertinggi `find_second_largest` kode mengimplementasikan komparasi single pass yang gesit.
- **Hasil Testing Codelab:** **PASSED** ✅ (100%)

### 3. Tugas 3: Aplikasi Matrix - Operasi Dasar
- **Pengecekan Kode:**
  - Kalkulasi linear dengan pertukaran matriks `transpose` berkerja mulus menggunakan baris/kolom. Loop perulangan matriks `for i in range` dirakit terstruktur dengan aman dari error bentrok tipe list dan integer.
- **Hasil Testing Codelab:** **PASSED** ✅ (100%)

**NILAI MODUL 2: 100**

---

## Hasil Evaluasi Modul 3: Single Linked List

### 1. Tugas 1: Implementasi Single Linked List
- **Pengecekan Kode:**
  - Implementasi `reverse()` menggunakan tiga pointer (prev, current, next_node) secara in-place dengan benar. `find_min()` dan `find_max()` melakukan iterasi O(n) dengan inisialisasi dari head. `remove_value()` menangani kasus head dan tengah list. `to_list()` berjalan mulus. Seluruh method baru ditulis bersih dan terdokumentasi dengan baik.
- **Hasil Testing:** **PASSED** ✅ (100%)

### 2. Tugas 2: Aplikasi Polinomial
- **Pengecekan Kode:**
  - `add_term()` menangani penyisipan terurut (pangkat tertinggi ke terendah) dan penggabungan koefisien duplikat dengan benar. `evaluate()` menghitung nilai polinomial secara akurat. `add_polynomials()` menghasilkan polinomial hasil penjumlahan yang tepat: `5x^2 + 6x^1 + 8x^0`.
- **Hasil Testing:** **PASSED** ✅ (100%)

### 3. Tugas 3: Aplikasi Music Playlist
- **Pengecekan Kode:**
  - Semua operasi playlist (`add_song`, `remove_song`, `play`, `next_song`, `current_song`, `total_duration`, `song_count`, `search_by_artist`) diimplementasikan dengan tepat menggunakan Single Linked List. `remove_song` juga memperbarui pointer `current` jika lagu yang dihapus sedang diputar.
- **Hasil Testing:** **PASSED** ✅ (100%)

**NILAI MODUL 3: 100**

---

## Hasil Evaluasi Modul 4: Double Linked List & Circular Linked List

### 1. Tugas 1: Implementasi Double Linked List
- **Pengecekan Kode:**
  - `reverse()` menukar pointer `prev` dan `next` setiap node secara in-place lalu menukar `head` dan `tail`. `find_min()` dan `find_max()` bekerja dengan benar. `swap_nodes()` menukar data antar dua posisi. `is_palindrome()` menggunakan dua pointer dari head dan tail yang bergerak ke tengah secara efisien.
- **Hasil Testing:** **PASSED** ✅ (100%)

### 2. Tugas 2: Aplikasi Text Editor Undo/Redo
- **Pengecekan Kode:**
  - `type_text()` memotong cabang redo yang ada (`self.current.next = None`) sebelum membuat node baru, menangani branching dengan benar. `undo()` dan `redo()` berjalan sesuai ekspektasi. `show_history()` menampilkan posisi `^current` secara akurat.
- **Hasil Testing:** **PASSED** ✅ (100%)

### 3. Tugas 3: Aplikasi Round Robin Scheduler
- **Pengecekan Kode:**
  - `add_process()` membangun circular linked list dengan benar. `execute_one_cycle()` melakukan rotasi head setelah eksekusi atau menghapus proses yang selesai. Output timeline sesuai ekspektasi Round Robin dengan quantum=2: Process A → B → C → A → B(selesai) → C(selesai) → A(selesai). Total waktu eksekusi 12 unit.
- **Hasil Testing:** **PASSED** ✅ (100%)

**NILAI MODUL 4: 100**

---
### **NILAI RATA-RATA SEMENTARA: 100.00 🌟**

*Penilaian ini adalah nilai sementara untuk Modul 1 hingga Modul 4, dievaluasi secara statis berdasarkan instruksi/flowchart dan divalidasi melalui unit test execution.*
