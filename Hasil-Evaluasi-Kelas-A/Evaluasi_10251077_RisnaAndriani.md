# Laporan Evaluasi Terperinci - Praktikum Struktur Data

---

## Data Mahasiswa
- **Nama:** Risna Andriani
- **NIM:** 10251077
- **Kelas:** Struktur Data A
- **GitHub Username:** `strukturdata-a-RisnaAndriani-10251077`

---

## Hasil Evaluasi Modul 1: Pengantar Struktur Data

### 1. Tugas 1: Pengembangan ADT Counter
- **Pengecekan Kode:**
  - Fungsi penambahan `add` dapat tereksekusi dengan baik. Pembatasan variabel negatif pada metode iterasi pengurangan `subtract()` dirangkai mantap dengan kondisi percabangan bersarang `if n > 0` dan `if self._value >= n`.
  - **Catatan Evaluator:** Ditemukan *Syntax Error* berupa kelebihan *whitespaces* dan simbol sama dengan (`assert counter.get_value() =    = 2`) pada saat test script dijalankan. Kesalahan telah diperbaiki secara manual oleh evaluator saat proses validasi agar kode bisa di *compile*.
- **Hasil Testing Codelab:** **PASSED** ✅ (96% - *Minor Deductions for Syntax Error*)

### 2. Tugas 2: Pengembangan ADT Stack - Aplikasi Reverse String
- **Pengecekan Kode:**
  - Metode `print_stack` sangat komprehensif mengandalkan inisialisasi list, namun terdapat kesalahan indentasi (*IndentationError*) pada blok pengembalian `return result` yang menghalangi simulasi kompilasi. Fungsi tersebut memuat 5 spasi dan bukan 4. Diperbaiki oleh evaluator saat proses pemeriksaan.
- **Hasil Testing Codelab:** **PASSED** ✅ (96% - *Minor Deductions for Indentation Error*)

### 3. Tugas 3: Analisis Kompleksitas Lanjutan
- **Tabel Analisis Kompleksitas & Jawaban:**
  - Menjabarkan efisiensi algoritma iteratif vs rekursif menggunakan rumusan $O(\log n)$ dan argumen yang sangat rasional (misalnya, membandingkan total loop iteratif berdasar Big-O ke total loop *recursive halving*).
  - Ditemukan minor *Syntax Error* berupa tanda kutip panjang multi-baris yang kurang satu tanda `"""` pada block docstring `fungsi_c()`. Telah diperbaiki manual.
- **Hasil Testing Codelab:** **PASSED** ✅ (96% - *Minor Deductions for Syntax Error*)

**NILAI MODUL 1: 96** *(Deduksi poin akibat beberapa Syntax Errors kecil yang menyebabkan kode gagal di compile saat awal pengujian)*

---

## Hasil Evaluasi Modul 2: Array

### 1. Tugas 1: Pengembangan MyArray
- **Pengecekan Kode:**
  - Logika pembalikan `reverse` dirakit stabil memakai konsep *two-pointer swapping* `while left < right` dipadu mutasi serentak variabel lokal. Pencarian nilai agregat max & min dirancang handal.
- **Hasil Testing Codelab:** **PASSED** ✅ (100%)

### 2. Tugas 2: Aplikasi Array - Statistik Data
- **Pengecekan Kode:**
  - Komparasi *second_largest* dieksekusi gesit dengan melandasi komparasinya menggunakan inisialisasi integer float tiada batas `float('-inf')` sehingga komparasi nilai bergeser dengan akurat. Filter elemen duplikat diisolasi murni menggunakan array lokal pencarian `-1`. Penulisan bersih tanpa *syntax error*.
- **Hasil Testing Codelab:** **PASSED** ✅ (100%)

### 3. Tugas 3: Aplikasi Matrix - Operasi Dasar
- **Pengecekan Kode:**
  - Matriks dirakit konsisten. Pembalikan rotasi *transpose* memanfaatkan *nested loop* baris-kolom array 2D secara sempurna `[matrix[j][i] for j in range(rows)]`. Perkalian dan pemeriksaan diagonal disusun tepat fungsi.
- **Hasil Testing Codelab:** **PASSED** ✅ (100%)

**NILAI MODUL 2: 100**

---
### **NILAI RATA-RATA SEMENTARA: 98.00 🌟**

*Penilaian ini adalah nilai sementara untuk Modul 1 dan Modul 2, dievaluasi secara statis berdasarkan instruksi/flowchart dan divalidasi melalui unit test execution.*
