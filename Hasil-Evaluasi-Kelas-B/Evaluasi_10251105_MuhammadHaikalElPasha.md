# 📝 Laporan Evaluasi Terperinci - Praktikum Struktur Data

---

## 👤 Data Mahasiswa
- **Nama:** Muhammad Haikal El Pasha
- **NIM:** 10251105
- **Kelas:** Struktur Data B
- **GitHub Username:** `strukturdata-b-10251105-haikal`

---

## 🥇 Hasil Evaluasi Modul 1: Pengantar Struktur Data

### 1. Tugas 1: Pengembangan ADT Counter
- **Pengecekan Kode:**
  - Metode `add`, `subtract`, dan `multiply` telah diimplementasikan dengan sangat baik sesuai flowchart. Operasi matematika dan kondisional negatif ditangani dengan cermat.
- **Hasil Testing Terminal:** **PASSED** ✅ (100%)

### 2. Tugas 2: Pengembangan ADT Stack - Aplikasi Reverse String
- **Pengecekan Kode:**
  - Logika LIFO menggunakan struktur `push` dan `pop` berfungsi sebagaimana instruksi, membalik karakter pada array Stack.
- **Hasil Testing Terminal:** **PASSED** ✅ (100%)

### 3. Tugas 3: Analisis Kompleksitas Lanjutan
- **Tabel Analisis Kompleksitas & Jawaban:**
  - Fungsi iteratif perulangan dan recursive berjalan, memetakan waktu milidetik secara rinci.
- **Hasil Testing Terminal:** **PASSED** ✅ (100%)

**✨ NILAI MODUL 1: 100 ✨**

---

## 🥈 Hasil Evaluasi Modul 2: Array

### 1. Tugas 1: Pengembangan MyArray
- **Pengecekan Kode:**
  - Mengimplementasikan `find_min`, `find_max`, `reverse`, dan insert/delete front dengan benar.
  - **Kekurangan:** Method `count()` hanya di-pass (`pass`) tanpa diimplementasikan algoritmanya, sehingga memicu *AssertionError* saat unit test diinisiasi.
- **Hasil Testing Terminal:** **FAILED** ❌ (85%) - Penalti karena fitur count kosong.

### 2. Tugas 2: Aplikasi Array - Statistik Data
- **Pengecekan Kode:**
  - Sebenarnya telah memulai pengkodean logika deteksi Sum, Rata-rata, max-min, dan largest second element.
  - **Kekurangan fatal:** Pada fungsi iterasi duplikat (`remove_duplicates`), kodenya dipecah dan *indentation/syntax*-nya merusak modul lain sehingga gagal saat akan memanggil `insert_end` pada level _top execution_. Test case terminal tidak bisa berjalan tuntas karena *Traceback Error* pada baris 137.
- **Hasil Testing Terminal:** **FAILED** ❌ (75%) - Penalti logika coding yang rusak.

### 3. Tugas 3: Aplikasi Matrix - Operasi Dasar
- **Pengecekan Kode:**
  - Pengoperasian *addition matrices* dan rotasi array berjalan dengan aman.
- **Hasil Testing Terminal:** **PASSED** ✅ (100%)

**✨ NILAI MODUL 2: 86.6 ✨**
*(Dibulatkan menjadi 87)*

---
### **🏆 NILAI RATA-RATA SEMENTARA: 93.50 🏆**

*Penilaian ini adalah nilai sementara untuk Modul 1 dan Modul 2, dievaluasi secara statis-manual berdasarkan kode program dan divalidasi melalui eksekusi unit test satu per satu.* 
