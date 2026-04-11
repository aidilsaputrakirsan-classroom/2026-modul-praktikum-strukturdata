# 📝 Laporan Evaluasi Terperinci - Praktikum Struktur Data

---

## 👤 Data Mahasiswa
- **Nama:** Muhammad Farid Kusuma Admaja
- **NIM:** 10251006
- **Kelas:** Struktur Data B
- **GitHub Username:** `strukturdata-b-Ridz010`

---

## 🥇 Hasil Evaluasi Modul 1: Pengantar Struktur Data

### 1. Tugas 1: Pengembangan ADT Counter
- **Pengecekan Kode:**
  - Metode penambahan kalkulasi matematis seperti iterasi *add* atau *multiply* stabil tanpa cacat saat dijalankan. Limit pengukur minimum (`min(0)`) untuk pengurangan `subtract` bekerja mulus.
- **Hasil Testing Terminal:** **PASSED** ✅ (100%)

### 2. Tugas 2: Pengembangan ADT Stack - Aplikasi Reverse String
- **Pengecekan Kode:**
  - Pembalikan kalimat huruf LIFO bekerja menggunakan parameter iterasi `.pop` mengembalikan list karakter dengan runut yang benar.
- **Hasil Testing Terminal:** **PASSED** ✅ (100%)

### 3. Tugas 3: Analisis Kompleksitas Lanjutan
- **Tabel Analisis Kompleksitas & Jawaban:**
  - Komparator kompleksitas algoritma array pada test profiler menunjukkan waktu eksekusi presisi untuk variasi test *nested loop* hingga rekursi dinamis.
- **Hasil Testing Terminal:** **PASSED** ✅ (100%)

**✨ NILAI MODUL 1: 100 ✨**

---

## 🥈 Hasil Evaluasi Modul 2: Array

### 1. Tugas 1: Pengembangan MyArray
- **Pengecekan Kode:**
  - Fungsi seperti `insert_front()`, *delete*, hingga evaluasi `find_min` dimodifikasi _in-place_ menggunakan iterasi range yang stabil.
- **Hasil Testing Terminal:** **PASSED** ✅ (100%)

### 2. Tugas 2: Aplikasi Array - Statistik Data
- **Pengecekan Kode:**
  - Algoritma pencarian kalkulasi untuk _average_, komputasi akumulatif `sum()`, filter duplikasi logik bekerja sukses.
- **Hasil Testing Terminal:** **PASSED** ✅ (100%)

### 3. Tugas 3: Aplikasi Matrix - Operasi Dasar
- **Pengecekan Kode:**
  - Pengecekan *loop addition* dan validasi simetrik dari matrix dua dimensi memberikan true output *True/False* secara asertif.
- **Hasil Testing Terminal:** **PASSED** ✅ (100%)

**✨ NILAI MODUL 2: 100 ✨**

---

## 🥉 Hasil Evaluasi Modul 3: Single Linked List

### 1. Tugas 1: Pengembangan LinkedList
- **Pengecekan Kode:** Semua method baru (`reverse()`, `find_min()`, `find_max()`, `remove_value()`, `to_list()`) diimplementasikan benar dan efisien. Semua test case referensi lulus.
- **Hasil Testing Terminal:** **PASSED** ✅

### 2. Tugas 2: Aplikasi Linked List - Polynomial
- **Pengecekan Kode:** Implementasi `Polynomial` dengan `TermNode` dan penyisipan terurut berjalan benar. Method `evaluate()`, `degree()`, dan `add_polynomials()` menghasilkan output yang tepat.
- **Hasil Testing Terminal:** **PASSED** ✅

### 3. Tugas 3: Aplikasi Linked List - Music Playlist
- **Pengecekan Kode:** Logika semua method playlist benar, `format_duration()` diimplementasikan dengan format `mm:ss`. Namun terdapat minor bug pada method `display()`: baris separator `"========================"` dan baris `Total:` dicetak di dalam perulangan while (setelah setiap lagu), bukan setelah loop selesai. Akibatnya setiap lagu diikuti oleh baris total, menghasilkan tampilan yang tidak sesuai format. Semua assert tetap lulus.
- **Hasil Testing Terminal:** **PASSED** ✅ (assert lulus, namun format display salah - total dicetak per lagu)

**✨ NILAI MODUL 3: 90 ✨**

---

## 🏅 Hasil Evaluasi Modul 4: Double & Circular Linked List

### 1. Tugas 1: Pengembangan Double Linked List
- **Pengecekan Kode:** Implementasi `reverse()`, `find_min()`, `find_max()`, `swap_nodes()`, dan `is_palindrome()` semuanya benar dan lulus semua test case DLL termasuk skenario palindrome.
- **Hasil Testing Terminal:** **PASSED** ✅

### 2. Tugas 2: Aplikasi DLL - Text Editor Undo/Redo
- **Pengecekan Kode:** Text editor dengan DLL mengimplementasikan operasi `type_text()`, `append_text()`, `undo()`, `redo()`, dan branching history dengan benar. Semua test case lulus termasuk skenario overwrite history.
- **Hasil Testing Terminal:** **PASSED** ✅

### 3. Tugas 3: Aplikasi CLL - Round Robin Scheduler
- **Pengecekan Kode:** CLL digunakan untuk mensimulasikan Round Robin. Eksekusi proses per quantum, penghapusan proses yang selesai, serta tampilan timeline dan statistik total waktu semuanya benar.
- **Hasil Testing Terminal:** **PASSED** ✅

**✨ NILAI MODUL 4: 100 ✨**

---

## 🔢 Hasil Evaluasi Modul 5: Stack

### 1. Tugas 1: Pengembangan Stack
- **Hasil Testing Terminal:** **PASSED** ✅ (100%)

### 2. Tugas 2: Infix → Postfix + Evaluasi Ekspresi
- **Pengecekan Kode:** Bug right-associativity `^`: `A^B^C` → `A B ^ C ^` (expected `A B C ^ ^`) ❌. Operator `^` tidak diperlakukan sebagai right-associative di while loop.
- **Hasil Testing Terminal:** **PARTIAL** ⚠️ (90%)

### 3. Tugas 3: Browser History
- **Hasil Testing Terminal:** **PASSED** ✅ (100%)

**✨ NILAI MODUL 5: 97 ✨**

---

## 🔢 Hasil Evaluasi Modul 6: Queue

### 1. Tugas 1: Priority Queue
- **Hasil Testing Terminal:** **PASSED** ✅ (100%)

### 2. Tugas 2: Deque + is_palindrome()
- **Pengecekan Kode:** Deque berfungsi benar, namun `is_palindrome()` tidak memiliki `return True/False` — selalu mengembalikan `None` untuk semua input.
- **Hasil Testing Terminal:** **PARTIAL** ⚠️ (50%)

### 3. Tugas 3: Simulasi Antrian Bank
- **Pengecekan Kode:** Avg waiting time positif (0.30 menit), 20 customer dilayani semua. Logika benar.
- **Hasil Testing Terminal:** **PASSED** ✅ (100%)

**✨ NILAI MODUL 6: 83 ✨**

---
### **🏆 NILAI RATA-RATA (Modul 1-6): 91.83 🏆**

*Penilaian dievaluasi secara statis-manual berdasarkan kode program dan divalidasi melalui eksekusi unit test satu per satu.*
