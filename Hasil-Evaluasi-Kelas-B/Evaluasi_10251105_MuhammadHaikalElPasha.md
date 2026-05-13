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

## 🥉 Hasil Evaluasi Modul 3: Single Linked List

### 1. Tugas 1: Pengembangan LinkedList
- **Pengecekan Kode:** Semua method baru (`reverse`, `find_min`, `find_max`, `remove_value`, `to_list`) diimplementasikan dengan benar. Struktur kode rapi dan mengikuti pola yang sama dengan modul praktikum.
- **Hasil Testing Terminal:** **PASSED** ✅ (100%)

### 2. Tugas 2: Aplikasi Linked List - Polynomial
- **Pengecekan Kode:** Implementasi `Polynomial` dengan semua method yang diperlukan berjalan benar. `add_term` menyimpan term terurut dari pangkat tertinggi ke terendah dan menggabungkan koefisien jika pangkat sama.
- **Hasil Testing Terminal:** **PASSED** ✅ (100%)

### 3. Tugas 3: Aplikasi Linked List - Music Playlist
- **Pengecekan Kode:** Class `Playlist` diimplementasikan lengkap dengan semua method yang diminta. Format display menggunakan `format_duration` untuk konversi detik ke mm:ss.
- **Hasil Testing Terminal:** **PASSED** ✅ (100%)

**✨ NILAI MODUL 3: 100 ✨**

---

## 🏅 Hasil Evaluasi Modul 4: Double & Circular Linked List

### 1. Tugas 1: Pengembangan Double Linked List
- **Pengecekan Kode:** Semua method baru (`reverse`, `find_min`, `find_max`, `swap_nodes`, `is_palindrome`, `to_list`) diimplementasikan dengan benar. Implementasi identik dengan referensi dan lulus semua test case.
- **Hasil Testing Terminal:** **PASSED** ✅ (100%)

### 2. Tugas 2: Aplikasi DLL - Text Editor Undo/Redo
- **Pengecekan Kode:** Class `TextEditor` diimplementasikan dengan benar termasuk fitur branching (menghapus redo history saat mengetik teks baru setelah undo). Semua test case lulus.
- **Hasil Testing Terminal:** **PASSED** ✅ (100%)

### 3. Tugas 3: Aplikasi CLL - Round Robin Scheduler
- **Pengecekan Kode:** Class `RoundRobinScheduler` diimplementasikan dengan benar. Output timeline eksekusi sesuai ekspektasi. Statistik total waktu juga benar (12 unit).
- **Hasil Testing Terminal:** **PASSED** ✅ (100%)

**✨ NILAI MODUL 4: 100 ✨**

---

## 🥇 Hasil Evaluasi Modul 5: Stack

### 1. Tugas 1: Pengembangan Stack
- **Pengecekan Kode:** Stack dengan `get_min/max`, `to_list`, `copy`, `reverse`, `clear` diimplementasikan benar.
- **Hasil Testing Terminal:** **PASSED** ✅ (100%)

### 2. Tugas 2: Konversi dan Evaluasi Ekspresi
- **Pengecekan Kode:** Infix to postfix dengan right-associativity `^` benar. Full calculation lulus semua.
- **Hasil Testing Terminal:** **PASSED** ✅ (100%)

### 3. Tugas 3: Aplikasi Stack - Browser History
- **Pengecekan Kode:** BrowserHistory dengan 2 stack, visit/back/forward benar.
- **Hasil Testing Terminal:** **PASSED** ✅ (100%)

**✨ NILAI MODUL 5: 100 ✨**

---

## 🥈 Hasil Evaluasi Modul 6: Queue

- **Pengecekan Kode:** Repositori diperiksa, **tidak ada file tugas untuk Modul 6** — hanya terdapat file praktikum (`Prak6.1/2/3.py`) dan placeholder `test`. ⚠️
- **Hasil Testing Terminal:** **FAILED** ❌ (0%)

**✨ NILAI MODUL 6: 0 ✨**

---
## 🔢 Hasil Evaluasi Modul 7: Review & Studi Kasus (Persiapan UTS)

### Semua Tugas
- **Pengecekan Kode:** Folder `Minggu 7/` hanya berisi `Prak7.1.py` (PRAKTIKUM Browser Tabs) dan `Prak7.2.py` (PRAKTIKUM Task Scheduler) — bukan TUGAS 7.2 Sistem Perpustakaan. Tidak ada PDF jawaban teori.
- **Hasil:** **TIDAK DIKUMPULKAN** ❌ (0%)

**✨ NILAI MODUL 7: 0 ✨**

---

## 🔢 Hasil Evaluasi Modul 9: Tree & Binary Tree

### 1. Tugas 1: BinaryTree Class
- **Hasil Testing Terminal:** **PASSED** ✅ (100%)

### 2. Tugas 2: Expression Tree
- **Hasil Testing Terminal:** **PASSED** ✅ (100%)

### 3. Tugas 3: Analisis Kompleksitas Tree
- **Pengecekan Kode:** `height()` rekursif tanpa `sys.setrecursionlimit` → `RecursionError` pada skewed tree.
- **Hasil Testing Terminal:** **FAILED** ❌ (0%)

**✨ NILAI MODUL 9: 67 ✨**

---
## Hasil Evaluasi Modul 10: Binary Search Tree (BST)

### 1. Tugas 1: Pengembangan BST Class
- **Pengecekan Kode:** Semua test lulus.
- **Hasil Testing Terminal:** **PASSED** ✅ (100%)

### 2. Tugas 2: Sistem Phonebook dengan BST
- **Pengecekan Kode:** Semua test lulus.
- **Hasil Testing Terminal:** **PASSED** ✅ (100%)

### 3. Tugas 3: Analisis Performa BST
- **Pengecekan Kode:** Sorted BST height n-1 benar. Analisis lengkap n=50000.
- **Hasil Testing Terminal:** **PASSED** ✅ (100%)

**NILAI MODUL 10: 100**

---
### **NILAI RATA-RATA (Modul 1-7, 9, 10): 72.67**

| Modul | Nilai |
|-------|-------|
| Modul 1 | 100 |
| Modul 2 | 87 |
| Modul 3 | 100 |
| Modul 4 | 100 |
| Modul 5 | 100 |
| Modul 6 | 0 |
| Modul 7 | 0 |
| Modul 9 | 67 |
| Modul 10 | 100 |
| **Rata-rata** | **72.67** |

*Penilaian dievaluasi secara statis-manual berdasarkan kode program dan divalidasi melalui eksekusi unit test satu per satu.*
