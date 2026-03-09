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
### **NILAI RATA-RATA SEMENTARA: 98.00 🌟**

*Penilaian ini adalah nilai sementara untuk Modul 1 dan Modul 2, dievaluasi secara statis berdasarkan instruksi/flowchart dan divalidasi melalui unit test execution.*
