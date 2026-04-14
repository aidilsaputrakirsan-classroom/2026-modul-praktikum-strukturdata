# SOAL LATIHAN UJIAN TENGAH SEMESTER
# STRUKTUR DATA — PAKET LATIHAN

---

**Program Studi:** Sistem Informasi  
**Institut:** Teknologi Kalimantan  
**Cakupan:** Modul 1–7  
**Sifat:** Open Book — Boleh membuka catatan dan modul  
**Estimasi Waktu:** 120 menit

---

## ALUR PENGERJAAN

| Tahap | Kegiatan | Keterangan |
|-------|----------|------------|
| **1. Individu** | Kerjakan semua soal secara mandiri | Boleh buka modul/catatan |
| **2. Kelompok** | Diskusikan jawaban dengan anggota grup | Cari satu jawaban terbaik per soal |
| **3. Presentasi** | Tiap grup presentasikan jawaban mereka | Dosen akan memandu klarifikasi |

> **Catatan:** Tidak ada jawaban yang langsung dinyatakan salah di tahap individu. Fokuslah pada **penalaran dan alasan** di balik jawabanmu, karena itulah yang akan didiskusikan di tahap kelompok.

---

# BAGIAN I: PILIHAN GANDA (40 poin — 2 poin per soal)

**Petunjuk:** Pilih satu jawaban yang paling tepat. Tuliskan juga **alasan singkat** pilihanmu di bawah setiap soal!

---

**1.** Perhatikan pernyataan berikut:
- (i) ADT mendefinisikan *apa* yang bisa dilakukan terhadap data
- (ii) Struktur data konkret mendefinisikan *bagaimana* operasi diimplementasikan
- (iii) Stack adalah ADT, sedangkan Stack berbasis array adalah struktur data konkret

Pernyataan yang BENAR adalah...
- A. Hanya (i)
- B. (i) dan (ii) saja
- C. (i), (ii), dan (iii) semua benar
- D. Hanya (iii)

*Alasan:* _______________________________________________

---

**2.** Sebuah fungsi memiliki kompleksitas `T(n) = 5n² + 3n + 100`. Dalam notasi Big-O, fungsi ini dinyatakan sebagai...
- A. O(n)
- B. O(5n²)
- C. O(n² + n)
- D. O(n²)

*Alasan:* _______________________________________________

---

**3.** Perhatikan kode berikut:
```python
def hitung(n):
    result = 0
    for i in range(n):
        result += i
    for j in range(n):
        for k in range(n):
            result += j * k
    return result
```
Kompleksitas waktu Big-O fungsi di atas adalah...
- A. O(n + n²)
- B. O(n²)
- C. O(n³)
- D. O(2n²)

*Alasan:* _______________________________________________

---

**4.** Sebuah array `nilai = [70, 85, 90, 60, 75]` memiliki 5 elemen. Berapa nilai dari `nilai[3]`?
- A. 90
- B. 60
- C. 75
- D. 85

*Alasan:* _______________________________________________

---

**5.** Manakah operasi pada array yang kompleksitasnya BUKAN O(1)?
- A. Mengakses elemen di index ke-4
- B. Mengubah nilai elemen di index ke-2
- C. Menghapus elemen di posisi pertama (index 0)
- D. Memeriksa panjang array yang sudah tersimpan

*Alasan:* _______________________________________________

---

**6.** Jika array 2D `matriks` berukuran 5×6, elemen di baris ke-2 kolom ke-5 dapat diakses dengan...
- A. `matriks[2][5]`
- B. `matriks[1][4]`
- C. `matriks[2][4]`
- D. `matriks[1][5]`

*Alasan:* _______________________________________________

---

**7.** Diberikan Single Linked List: `HEAD → [A] → [B] → [C] → [D] → NULL`.  
Setelah operasi hapus node B, hasilnya adalah...
- A. `HEAD → [A] → [C] → [D] → NULL`
- B. `HEAD → [B] → [C] → [D] → NULL`
- C. `HEAD → [A] → [B] → [D] → NULL`
- D. `HEAD → [A] → [C] → NULL`

*Alasan:* _______________________________________________

---

**8.** Alasan utama mengapa mencari (search) elemen di Single Linked List membutuhkan O(n) adalah...
- A. Linked list tidak mendukung operasi pencarian sama sekali
- B. Setiap pencarian harus dimulai dari HEAD dan diperiksa satu per satu
- C. Pointer next tidak menyimpan informasi nilai node berikutnya
- D. Linked list tidak menyimpan data secara berurutan berdasarkan nilai

*Alasan:* _______________________________________________

---

**9.** Perbedaan yang TEPAT antara Single Linked List dan Double Linked List adalah...
- A. Double LL dapat menyimpan lebih banyak data dibanding Single LL
- B. Single LL hanya bisa dibuat dengan bahasa C, bukan Python
- C. Double LL memiliki pointer prev sehingga traversal ke belakang dimungkinkan
- D. Single LL selalu lebih cepat dari Double LL untuk semua operasi

*Alasan:* _______________________________________________

---

**10.** Pada Double Linked List dengan pointer HEAD dan TAIL, operasi manakah yang dapat dilakukan dengan O(1)?
- A. Mencari node dengan nilai tertentu
- B. Menghapus node di tengah list
- C. Menghapus node di posisi paling akhir
- D. Menghitung jumlah total node dalam list

*Alasan:* _______________________________________________

---

**11.** Circular Linked List berbeda dari Single Linked List karena...
- A. Setiap node memiliki dua pointer penghubung ke node lain
- B. Node terakhir menyimpan pointer yang kembali menunjuk ke HEAD
- C. Tidak memerlukan pointer HEAD untuk memulai traversal
- D. Dapat menyimpan tipe data yang berbeda di setiap node

*Alasan:* _______________________________________________

---

**12.** Stack dengan operasi berikut dijalankan secara berurutan pada stack kosong:
```
push(3), push(7), push(2), pop(), push(5), pop(), pop()
```
Berapa nilai yang tersisa di dalam stack setelah semua operasi selesai?
- A. [3]
- B. [3, 7]
- C. [7]
- D. Stack kosong

*Alasan:* _______________________________________________

---

**13.** Dalam algoritma pengecekan balanced parentheses menggunakan stack, karakter `]` yang ditemukan akan memicu aksi...
- A. Langsung di-push ke dalam stack
- B. Stack di-pop, lalu dicek apakah hasilnya adalah `[`
- C. Seluruh isi stack dikosongkan
- D. Program berhenti dan langsung menyimpulkan tidak balanced

*Alasan:* _______________________________________________

---

**14.** Manakah yang merupakan hasil konversi BENAR dari ekspresi infix `P * Q + R` ke postfix?
- A. `P Q R * +`
- B. `P Q * R +`
- C. `* P Q + R`
- D. `P Q + R *`

*Alasan:* _______________________________________________

---

**15.** Pada konversi infix ke postfix untuk ekspresi `A - B + C`, hasil postfix yang benar adalah...
- A. `A B - C +`
- B. `A B C - +`
- C. `A B + C -`
- D. `- A B + C`

*Alasan:* _______________________________________________

---

**16.** Queue menggunakan prinsip FIFO. Jika operasi berikut dijalankan pada queue kosong:
```
enqueue(X), enqueue(Y), enqueue(Z), dequeue(), enqueue(W), dequeue()
```
Elemen apa yang tersisa di dalam queue?
- A. [Z, W]
- B. [Y, Z, W]
- C. [W]
- D. [Z]

*Alasan:* _______________________________________________

---

**17.** Pada Linear Queue dengan kapasitas 4 (index 0–3), kondisi saat ini: `front = 2, rear = 3`. Masalah apa yang terjadi jika dilakukan `enqueue` lagi?
- A. Tidak ada masalah, enqueue berhasil di index 0
- B. Terjadi false overflow karena rear sudah di posisi terakhir meskipun index 0 dan 1 kosong
- C. Queue akan otomatis diperluas kapasitasnya
- D. Elemen paling lama secara otomatis dihapus untuk memberi ruang

*Alasan:* _______________________________________________

---

**18.** Formula yang digunakan Circular Queue untuk menghitung posisi rear baru setelah enqueue adalah...
- A. `rear = rear + 1`
- B. `rear = (rear + 1) / capacity`
- C. `rear = (rear + 1) % capacity`
- D. `rear = rear % (capacity + 1)`

*Alasan:* _______________________________________________

---

**19.** Priority Queue digunakan ketika...
- A. Semua elemen harus diproses sesuai urutan waktu masuknya
- B. Elemen dengan nilai numerik terkecil selalu dikeluarkan pertama
- C. Elemen perlu dikeluarkan berdasarkan tingkat kepentingan, bukan urutan masuk
- D. Dibutuhkan struktur data yang dapat menyimpan pasangan key-value

*Alasan:* _______________________________________________

---

**20.** Sebuah sistem operasi menggunakan struktur data untuk menjadwalkan proses secara bergiliran agar setiap proses mendapat jatah CPU yang adil. Struktur data yang paling tepat adalah...
- A. Stack
- B. Array terurut
- C. Double Linked List
- D. Circular Queue

*Alasan:* _______________________________________________

