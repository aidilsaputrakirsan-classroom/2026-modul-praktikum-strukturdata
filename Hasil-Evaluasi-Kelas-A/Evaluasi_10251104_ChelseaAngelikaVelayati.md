# Laporan Evaluasi Terperinci - Praktikum Struktur Data

---

## Data Mahasiswa
- **Nama:** Chelsea Angelika Velayati
- **NIM:** 10251104
- **Kelas:** Struktur Data A
- **GitHub Username:** `strukturdata-a-Chelsea-10251104`

---

## Hasil Evaluasi Modul 1: Pengantar Struktur Data

### 1. Tugas 1: Pengembangan ADT Counter
- **Pengecekan Kode:**
  - Metode `subtract()` berhasil dimodifikasi sesuai spesifikasi dengan membatasi agar tidak berada di bawah nol melalui metode kondisional bersarang (`if/else`). 
- **Hasil Testing Codelab:** **PASSED** ✅ (100%)

### 2. Tugas 2: Pengembangan ADT Stack - Aplikasi Reverse String
- **Pengecekan Kode:**
  - Fungsi iterasi string didalam metode pembalikan (*reverse_string*) diterapkan dengan struktur yang baik. Seluruh karakter berhasil ditambahkan denga `stack.push(char)` dan ditarik kembali secara LIFO dengan `result += stack.pop()`.
- **Hasil Testing Codelab:** **PASSED** ✅ (100%)

### 3. Tugas 3: Analisis Kompleksitas Lanjutan
- **Tabel Analisis Kompleksitas & Jawaban:**
  - Argumentasi yang diberikan cukup lengkap dan tepat sasaran. Penjelasan alasan dibalik efisiensi algoritma dihubungkan dengan prinsip operasi *Recursive Halving* serta perbandingan linear `O(n)`.
- **Hasil Testing Codelab:** **PASSED** ✅ (100%)

**NILAI MODUL 1: 100**

---

## Hasil Evaluasi Modul 2: Array

### 1. Tugas 1: Pengembangan MyArray
- **Pengecekan Kode:**
  - Logika modifikasi pointer kiri (*left*) dan kanan (*right*) dalam metode *reverse* diketik berbarengan dalam satu baris (*multiple assignment*) layaknya bahasa komputasi level lanjutan secara optimal `self._elements[left], self._elements[right] = self._elements[right], self._elements[left]`. Ini menghindari penggunaan variabel penampung sementara (`temp`).
- **Hasil Testing Codelab:** **PASSED** ✅ (100%)

### 2. Tugas 2: Aplikasi Array - Statistik Data
- **Pengecekan Kode:**
  - Penerapan `while` loop untuk seluruh fungsi membedakan kode mahasiswa ini dari yang lain yang mayoritas dominan menggunakan `for` iterasi ganda, sebuah nilai plus disisi variasi eksekusi tanpa mengubah kompleksitas aslinya `O(n)`.
- **Hasil Testing Codelab:** **PASSED** ✅ (100%)

### 3. Tugas 3: Aplikasi Matrix - Operasi Dasar
- **Pengecekan Kode:**
  - Konsep dimensi matriks berhasil direpresentasikan dalam algoritma iterasi *nested for-loop*.
- **Hasil Testing Codelab:** **PASSED** ✅ (100%)

**NILAI MODUL 2: 100**

---
### **NILAI RATA-RATA SEMENTARA: 100.00 🌟**

*Penilaian ini adalah nilai sementara untuk Modul 1 dan Modul 2, dievaluasi secara statis berdasarkan instruksi/flowchart dan divalidasi melalui unit test execution.*
