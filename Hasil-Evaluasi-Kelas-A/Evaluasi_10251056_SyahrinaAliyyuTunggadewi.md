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
### **NILAI RATA-RATA SEMENTARA: 100.00 🌟**

*Penilaian ini adalah nilai sementara untuk Modul 1 dan Modul 2, dievaluasi secara statis berdasarkan instruksi/flowchart dan divalidasi melalui unit test execution.*
