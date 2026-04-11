# Laporan Evaluasi Terperinci - Praktikum Struktur Data

---

## Data Mahasiswa
- **Nama:** snowyy26
- **NIM:** Tidak Diketahui
- **Kelas:** Struktur Data A
- **GitHub Username:** `strukturdata-a-snowyy26`

---

## Hasil Evaluasi Modul 1: Pengantar Struktur Data

- **Pengecekan Kode:**
  - Repositori GitHub ditemukan, namun terlambat.
- **Hasil Testing Codelab:** **PASSED** ✅ (50%)

**NILAI MODUL 1: 50**

---

## Hasil Evaluasi Modul 2: Array

- **Pengecekan Kode:**
  - Repositori GitHub ditemukan, namun terlambat.
- **Hasil Testing Codelab:** **PASSED** ✅ (50%)

**NILAI MODUL 2: 50**

---

## Hasil Evaluasi Modul 3: Single Linked List

### 1. Tugas 1: Implementasi Single Linked List
- **Pengecekan Kode:** `reverse()`, `find_min()`, `find_max()`, `remove_value()`, `to_list()` diimplementasikan dengan benar. Semua assert test lulus.
- **Hasil Testing:** **PASSED** ✅ (100%)

### 2. Tugas 2: Aplikasi Polinomial
- **Pengecekan Kode:** `add_polynomials()` menggunakan merge yang benar — koefisien pangkat sama digabungkan (`3x^2 + 2x^2 = 5x^2`). Output: `5x^2 + 6x^1 + 8x^0`. Semua test lulus.
- **Hasil Testing:** **PASSED** ✅ (100%)

### 3. Tugas 3: Aplikasi Music Playlist
- **Pengecekan Kode:** Semua operasi playlist (`add_song`, `remove_song`, `play`, `next_song`, `search_by_artist`, `total_duration`, `song_count`) diimplementasikan dan lulus semua test.
- **Hasil Testing:** **PASSED** ✅ (100%)

**NILAI MODUL 3: 100**

---

## Hasil Evaluasi Modul 4: Double Linked List & Circular Linked List

### 1. Tugas 1: Implementasi Double Linked List
- **Pengecekan Kode:** File berisi program "Sistem Profil dan Analisis Nilai Mahasiswa" yang menggunakan `input()` — **bukan implementasi Double Linked List**. Konten sama sekali tidak relevan dengan tugas yang diminta.
- **Hasil Testing:** **SALAH FILE** ❌ (0%)

### 2. Tugas 2: Aplikasi Text Editor Undo/Redo
- **Pengecekan Kode:** File identik dengan T1 — program profil mahasiswa yang sama, bukan Text Editor dengan DLL.
- **Hasil Testing:** **SALAH FILE** ❌ (0%)

### 3. Tugas 3: Aplikasi Round Robin Scheduler
- **Pengecekan Kode:** Round Robin benar: eksekusi bergantian `A→B→C→A→B(selesai)→C(selesai)→A(selesai)`. Rotasi head setelah tiap quantum berjalan baik.
- **Hasil Testing:** **PASSED** ✅ (100%)

**NILAI MODUL 4: 33** *(T1:0 + T2:0 + T3:100) / 3 ≈ 33*

---

## Hasil Evaluasi Modul 5: Stack

### 1. Tugas 1: Pengembangan Stack dengan Method Baru
- **Pengecekan Kode:** Semua method baru diimplementasikan dengan benar. Semua test lulus.
- **Hasil Testing:** **PASSED** ✅ (100%)

### 2. Tugas 2: Konversi dan Evaluasi Ekspresi
- **Pengecekan Kode:** `infix_to_postfix()` benar termasuk right-associativity `^`. Semua test lulus.
- **Hasil Testing:** **PASSED** ✅ (100%)

### 3. Tugas 3: Aplikasi Browser History
- **Pengecekan Kode:** `BrowserHistory` benar. Semua test lulus.
- **Hasil Testing:** **PASSED** ✅ (100%)

**NILAI MODUL 5: 100**

---

## Hasil Evaluasi Modul 6: Queue

### 1. Tugas 1: Implementasi Priority Queue
- **Pengecekan Kode:** `PriorityQueue` benar, urutan prioritas terjaga. Semua test lulus.
- **Hasil Testing:** **PASSED** ✅ (100%)

### 2. Tugas 2: Implementasi Deque + Palindrome
- **Pengecekan Kode:** `Deque` benar. Namun `is_palindrome()` tidak mengembalikan nilai apapun (return `None`) — tidak ada `return True/False`. Akibatnya semua pemanggilan `is_palindrome()` mengembalikan `None`.
- **Hasil Testing:** **FAILED** ❌ — `is_palindrome()` selalu return `None` (50%)

### 3. Tugas 3: Simulasi Antrian Bank
- **Pengecekan Kode:** 20 customers, 3 tellers, avg wait 0.30 menit — statistik benar.
- **Hasil Testing:** **PASSED** ✅ (100%)

**NILAI MODUL 6: 83** *(T1:100 + T2:50 + T3:100) / 3 ≈ 83*

---

### **NILAI RATA-RATA: 69**

| Modul | Nilai | Keterangan |
|-------|-------|------------|
| Modul 1 | 50 | Telat (Maks 50) |
| Modul 2 | 50 | Telat (Maks 50) |
| Modul 3 | 100 | |
| Modul 4 | 33 | T1/T2 salah file (profil mahasiswa, bukan DLL) |
| Modul 5 | 100 | |
| Modul 6 | 83 | |
| **Rata-rata** | **69** | |
