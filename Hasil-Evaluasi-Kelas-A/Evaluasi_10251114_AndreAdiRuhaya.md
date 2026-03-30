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

## Hasil Evaluasi Modul 3: Single Linked List

### 1. Tugas 1: Implementasi Single Linked List
- **Pengecekan Kode:**
  - `reverse()`, `find_min()`, `find_max()`, `remove_value()`, dan `to_list()` diimplementasikan dengan benar. Semua assert test berhasil dilalui dengan baik.
- **Hasil Testing:** **PASSED** ✅ (100%)

### 2. Tugas 2: Aplikasi Polinomial
- **Pengecekan Kode:**
  - `add_polynomials()` menggunakan copy-and-add, namun `add_term()` tidak menggabungkan koefisien saat pangkat sudah ada dalam hasil intermediate. Output menampilkan `3x^2 + 2x^2 + 6x + 8` alih-alih `5x^2 + 6x + 8` — bug minor display pada penggabungan koefisien. Test `evaluate(1)` tetap lulus secara numerik.
- **Hasil Testing:** **PASSED** ✅ (90%) — Test numerik lulus namun representasi polinomial hasil penjumlahan tidak dimerge dengan benar.

### 3. Tugas 3: Aplikasi Music Playlist
- **Pengecekan Kode:**
  - Semua operasi playlist (`add_song`, `remove_song`, `play`, `next_song`, `current_song`, `total_duration`, `song_count`, `search_by_artist`) berjalan dengan benar secara fungsional. Tidak menggunakan assert-based test (hanya print demo), namun output menampilkan hasil yang sesuai ekspektasi.
- **Hasil Testing:** **PASSED** ✅ (90%) — Fungsional benar namun tidak menggunakan assert statements untuk validasi otomatis.

**NILAI MODUL 3: 90**

---

## Hasil Evaluasi Modul 4: Double Linked List & Circular Linked List

### 1. Tugas 1: Implementasi Double Linked List
- **Pengecekan Kode:**
  - Semua method DLL (`reverse`, `find_min`, `find_max`, `swap_nodes`, `is_palindrome`, `to_list`) benar. `reverse()` menggunakan teknik tukar pointer yang tepat. Semua assert test lulus.
- **Hasil Testing:** **PASSED** ✅ (100%)

### 2. Tugas 2: Aplikasi Text Editor Undo/Redo
- **Pengecekan Kode:**
  - Semua operasi text editor berjalan dengan benar. `type_text()`, `append_text()`, `undo()`, `redo()`, dan branching semuanya lulus. `show_history()` menampilkan history dengan marker `^current`.
- **Hasil Testing:** **PASSED** ✅ (100%)

### 3. Tugas 3: Aplikasi Round Robin Scheduler
- **Pengecekan Kode:**
  - Terdapat **bug kritis pada `remove_process`**: setelah proses selesai (remaining=0), node tidak benar-benar dihapus dari circular list sehingga proses yang sudah "selesai" tetap ada di antrian. Ini menyebabkan **infinite loop** — program terus mencetak `"Time 12-12: Process B/C/A completed"` tanpa batas waktu. Eksekusi dihentikan paksa oleh timeout 10 detik.
- **Hasil Testing:** **FAILED** ❌ — Infinite loop akibat bug pada remove_process: proses yang sudah selesai tidak dihapus dari circular list dengan benar. TIMEOUT.

**NILAI MODUL 4: 70**

---
### **NILAI RATA-RATA SEMENTARA: 89.00 🌟**

*Penilaian ini adalah nilai sementara untuk Modul 1 hingga Modul 4, dievaluasi secara statis berdasarkan instruksi/flowchart dan divalidasi melalui unit test execution.*
