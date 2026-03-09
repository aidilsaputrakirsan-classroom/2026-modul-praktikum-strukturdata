# Laporan Evaluasi Terperinci - Praktikum Struktur Data

---

## Data Mahasiswa
- **Nama:** Andre Adi Ruhaya
- **NIM:** 10251114
- **Kelas:** Struktur Data A
- **GitHub Username:** `strukturdata-a-Andre10251114`

---

## Hasil Evaluasi Modul 1: Pengantar Struktur Data

### 1. Tugas 1: Pengembangan ADT Counter
- **Pengecekan Kode:**
  - Fungsi beroperasi stabil secara menyeluruh. Struktur kondisional disempurnakan dengan penanganan batas nol yang efisien: `if self._value < 0: self._value = 0`.
- **Hasil Testing Codelab:** **PASSED** ✅ (100%)

### 2. Tugas 2: Pengembangan ADT Stack - Aplikasi Reverse String
- **Pengecekan Kode:**
  - Metode `pop` dan `peek` terlindungi dengan *safety check* `if not self.is_empty():` yang menghindarkan program dari `IndexError`. Logika eksekusi berjalan stabil pada kalkulasi LIFO *string*.
- **Hasil Testing Codelab:** **PASSED** ✅ (100%)

### 3. Tugas 3: Analisis Kompleksitas Lanjutan
- **Tabel Analisis Kompleksitas & Jawaban:**
  - Tabel kompleksitas ditulis sesuai. Jawaban atas pertanyaan-pertanyaan spesifik tentang efisiensi pencarian maksimum dan kelemahan O(n²) diuraikan dengan argumentasi nyata terhadapat sistem pengguna jaringan.
- **Hasil Testing Codelab:** **PASSED** ✅ (100%)

**NILAI MODUL 1: 100**

---

## Hasil Evaluasi Modul 2: Array

### 1. Tugas 1: Pengembangan MyArray
- **Pengecekan Kode:**
  - Fitur `insert_front` dan `delete_front` memakai metode `insert(0, ...)` dan `pop(0)` bawaan array *list* dengan benar. Sayangnya baris komentar *TODO* tidak dihilangkan, namun tidak memengaruhi jalannya fungsi fundamental.
- **Hasil Testing Codelab:** **PASSED** ✅ (100%)

### 2. Tugas 2: Aplikasi Array - Statistik Data
- **Pengecekan Kode:**
  - Kode program *error* (ModuleNotFoundError) di awal lantaran nama *file* pustaka import di-set menjadi _"tugas1_10251114_Andre"_ padahal penamaan aktualnya _"Tugas1_10251114_Andre_Adi_Ruhaya"_. Setelah disunting, kode statistik tereksekusi mulus tanpa hambatan.
- **Hasil Testing Codelab:** **PASSED** ✅ (90%) - Pengurangan 10 poin atas *error* penamaan modul.

### 3. Tugas 3: Aplikasi Matrix - Operasi Dasar
- **Pengecekan Kode:**
  - Validasi asimetris dirangkai lugas menggunakan klausa pengujian `ValueError` dimensi di metode penjumlahan. Matrix berjalan sempurna.
- **Hasil Testing Codelab:** **PASSED** ✅ (100%)

**NILAI MODUL 2: 96**

---
### **NILAI RATA-RATA SEMENTARA: 98.00 🌟**

*Penilaian ini adalah nilai sementara untuk Modul 1 dan Modul 2, dievaluasi secara statis berdasarkan instruksi/flowchart dan divalidasi melalui unit test execution.*
