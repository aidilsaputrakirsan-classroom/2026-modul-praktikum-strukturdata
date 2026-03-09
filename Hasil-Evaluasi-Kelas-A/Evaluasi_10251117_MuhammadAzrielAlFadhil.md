# Laporan Evaluasi Terperinci - Praktikum Struktur Data

---

## Data Mahasiswa
- **Nama:** Muhammad Azriel Al Fadhil
- **NIM:** 10251117
- **Kelas:** Struktur Data A
- **GitHub Username:** `strukturdata-a-azrilalfadhil-svg`

---

## Hasil Evaluasi Modul 1: Pengantar Struktur Data

### 1. Tugas 1: Pengembangan ADT Counter
- **Pengecekan Kode:**
  - Fungsi penambahan dan pemotongan aritmatika divalidasi dengan hati-hati. Operasi instansiasi `add` dan `multiply` berfungsi konsisten mematuhi *constraint* bilangan genap dan minimal. Pengecekan limit pengurang `subtract()` minimal 0 dibangun sangat cermat.
- **Hasil Testing Codelab:** **PASSED** ✅ (100%)

### 2. Tugas 2: Pengembangan ADT Stack - Aplikasi Reverse String
- **Pengecekan Kode:**
  - Metode instan `clear` dan string representasi `print_stack` dieksekusi sempurna mengandalkan *built-in methods* Python. Perjalanan iterasi *reverse_string* memanfaatkan pola *push-pop* LIFO secara tepat.
- **Hasil Testing Codelab:** **PASSED** ✅ (100%)

### 3. Tugas 3: Analisis Kompleksitas Lanjutan
- **Tabel Analisis Kompleksitas & Jawaban:**
  - Argumen Big-O terdefinisikan elegan. Jawaban teoritis yang menjabarkan mengapa $O(\log n)$ sangat unggul pada skala ekstrim dijelaskan mendalam secara kualitatif. Mahasiswa juga memberikan penjabaran $O(n²)$ terkait sistem rekomendasi film dengan triliunan operasi rasional.
- **Hasil Testing Codelab:** **PASSED** ✅ (100%)

**NILAI MODUL 1: 100**

---

## Hasil Evaluasi Modul 2: Array

### 1. Tugas 1: Pengembangan MyArray
- **Pengecekan Kode:**
  - Penyisipan indeks awal `insert_front` menggunakan method `insert_at(0, element)` menopang fungsionalitas rotasi data efisien. *reverse* swap diselesaikan dengan efisien membagi pertukaran elemen awal dan elemen n - 1.
- **Hasil Testing Codelab:** **PASSED** ✅ (100%)

### 2. Tugas 2: Aplikasi Array - Statistik Data
- **Pengecekan Kode:**
  - Pada penelusuran angka kedua ekstrem `find_second_largest`, mahasiswa memagari evaluasi indeks inisialisasi boolean Python yang dirangkai mandiri `-inf`, sehingga terhindar dari bias data terkompresi. Filter `remove_duplicates()` digabung mantap.
- **Hasil Testing Codelab:** **PASSED** ✅ (100%)

### 3. Tugas 3: Aplikasi Matrix - Operasi Dasar
- **Pengecekan Kode:**
  - Logika permutasi 2-dimensi dieksekusi handal, rotasi *transpose*, perkalian skalar, rotasi invers *is_symmetric*, dan *get_diagonal* dipasang lincah sesuai blok ukurannya dengan menggunakan pola iterasi berlapis *(nested loops)* yang tertumpuk presisi.
- **Hasil Testing Codelab:** **PASSED** ✅ (100%)

**NILAI MODUL 2: 100**

---
### **NILAI RATA-RATA SEMENTARA: 100.00 🌟**

*Penilaian ini adalah nilai sementara untuk Modul 1 dan Modul 2, dievaluasi secara statis berdasarkan instruksi/flowchart dan divalidasi melalui unit test execution.*
