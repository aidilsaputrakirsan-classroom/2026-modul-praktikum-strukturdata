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
### **NILAI RATA-RATA SEMENTARA: 100.00 🌟**

*Penilaian ini adalah nilai sementara untuk Modul 1 dan Modul 2, dievaluasi secara statis berdasarkan instruksi/flowchart dan divalidasi melalui unit test execution.*
