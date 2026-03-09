# Laporan Evaluasi Terperinci - Praktikum Struktur Data

---

## Data Mahasiswa
- **Nama:** Rendy
- **NIM:** 10231081
- **Kelas:** Struktur Data A
- **GitHub Username:** `strukturdata-a-NorEndGate`

---

## Hasil Evaluasi Modul 1: Pengantar Struktur Data

### 1. Tugas 1: Pengembangan ADT Counter
- **Pengecekan Kode:**
  - `add(n)`: Diimplementasikan dengan pengkondisian nilai minimum (harus positif).
  - `subtract(n)`: Pengecekan *boundary* berhasil dieksekusi agar selisihnya tidak menyebabkan defisit mutlak di bawah `0`.
  - `multiply(n)`: Dikerjakan dengan baik. Terdapat pengecekan jika nilai minus/negatif.
  - `__str__()`: Pembuatan representasi format string terimplementasi.
- **Hasil Testing Codelab:** **PASSED** ✅ (100%)

### 2. Tugas 2: Pengembangan ADT Stack - Aplikasi Reverse String
- **Pengecekan Kode:**
  - Fitur `print_stack` menampilkan elemen LIFO dari array stack (`self._items`).
  - Fitur `clear` menghapus list *items* seluruh instansiasi Object.
  - Implementasi reverse_string berjalan tepat memanfaatkan sifat LIFO stack buatan mahasiswa.
- **Hasil Testing Codelab:** **PASSED** ✅ (100%)

### 3. Tugas 3: Analisis Kompleksitas Lanjutan
- **Tabel Analisis Kompleksitas & Jawaban:**
  - Prediksi operasi Big-O akurat (A-F). Mahasiswa mengerti korelasi waktu terhadap tipe eksekusi *iterative* versus rekurens. Secara inisiatif menyesuaikan variabel unit test `n` lebih kecil saat algoritma bersifat log(n³). Jawaban dan penjabaran narasi juga sangat baik dan komprehensif.
- **Hasil Testing Codelab:** **PASSED** ✅ (100%)

**NILAI MODUL 1: 100**

---

## Hasil Evaluasi Modul 2: Array

### 1. Tugas 1: Pengembangan MyArray
- **Pengecekan Kode:**
  - Metode penambahan maupun pengurangan node awal `insert_front` / `delete_front` berjalan valid melalui manipulasi index array internal Python. Pengecekan minimaks dan pemutaran arah array diimplementasikan sesuai *flowchart*.
- **Hasil Testing Codelab:** **PASSED** ✅ (100%)

### 2. Tugas 2: Aplikasi Array - Statistik Data
- **Pengecekan Kode:**
  - Berhasil menyusun pengolahan analitik dari angka *floating point* / *integer*. Fungsi aggregasi seperti sum, filter unit ganda (*remove duplicates*), perankingan rata-rata tereksekusi tanpa hambatan.
- **Hasil Testing Codelab:** **PASSED** ✅ (100%)

### 3. Tugas 3: Aplikasi Matrix - Operasi Dasar
- **Pengecekan Kode:**
  - Mahasiswa memahami *multi-dimensional arrays*. Mahasiswa mengimplementasikan fungsi ekstra untuk komparasi validasi dan representasi matriks *printing* (tugas yang melebihi standar baseline). *Output* komparasi dan kalkulasi skalar sangat stabil.
- **Hasil Testing Codelab:** **PASSED** ✅ (100%)

**NILAI MODUL 2: 100**

---
### **NILAI RATA-RATA SEMENTARA: 100 🌟**

*Penilaian ini adalah nilai sementara untuk Modul 1 dan Modul 2, dievaluasi secara statis berdasarkan instruksi/flowchart dan divalidasi melalui unit test execution.*
