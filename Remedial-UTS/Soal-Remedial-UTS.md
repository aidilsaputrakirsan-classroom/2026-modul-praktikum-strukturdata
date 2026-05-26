# SOAL REMEDIAL UJIAN TENGAH SEMESTER
# STRUKTUR DATA

---

**Program Studi:** Sistem Informasi - Institut Teknologi Kalimantan
**Cakupan:** Modul 1 – Modul 7
**Sifat:** Take-Home, Individu
**Estimasi Waktu Pengerjaan:** ~5–7 jam total

---

## INFORMASI PENTING

| Item | Keterangan |
|------|------------|
| **Deadline** | _diisi dosen_ (saran: 1 minggu sejak diumumkan) |
| **Format submission** | Folder `Remedial-UTS/` di repo GitHub Classroom masing-masing |
| **Cap nilai maksimal** | **65** (lihat formula di bawah) |
| **Plagiat / AI** | Dilarang. Tools allowed: dokumentasi Python, modul kuliah, catatan pribadi. **DILARANG:** copy dari teman, copy dari ChatGPT/AI tanpa modifikasi & pemahaman, copy dari GitHub orang lain |

**Formula nilai akhir UTS:**
```
UTS_final = MAX(UTS_asli, MIN(UTS_remedial, 65))
```

Artinya: kalau nilai remedial > UTS awal, dipakai nilai remedial (max 65). Kalau remedial < UTS awal, dipakai UTS awal.

---

## ALUR PENGERJAAN

1. **Cek set kamu** di file `Daftar-Mahasiswa-Remedial.md` (Set A / B / C).
2. **Kerjakan 3 soal** di set kamu, masing-masing di file `.py` terpisah.
3. **Tulis README** berisi identitas, refleksi, jawaban teori, dan analisis kompleksitas.
4. **Push ke repo Classroom** kamu dalam folder `Remedial-UTS/`.
5. **Jangan push sekaligus di akhir** — commit bertahap supaya history kerjamu terlihat (anti-plagiat check via `git log`).

---

## STRUKTUR FOLDER YANG HARUS DI-SUBMIT

```
Remedial-UTS/
├── README.md                            ← identitas + jawaban teori + analisis
├── Soal1_<Topik>_<NIM>.py
├── Soal2_<Topik>_<NIM>.py
└── Soal3_<Topik>_<NIM>.py
```

Contoh untuk mhs Set A, NIM 10251002:
```
Remedial-UTS/
├── README.md
├── Soal1_Inventory_10251002.py
├── Soal2_StokHistory_10251002.py
└── Soal3_TokoIntegrasi_10251002.py
```

---

## RUBRIK PENILAIAN (Total 100, dicap maks 65)

| Komponen | Bobot | Penjelasan |
|----------|------:|------------|
| Soal 1 (Array/ADT) | 25 | Implementasi + test PASSED + Big-O benar |
| Soal 2 (Linked List) | 25 | Implementasi + test PASSED + tracing benar |
| Soal 3 (Stack/Queue integrasi) | 30 | Implementasi + integrasi 2+ struktur + test PASSED |
| README teori & refleksi | 20 | Jawaban benar, analisis akurat, refleksi jelas |

**Penalti otomatis:**
- File `.py` tidak bisa di-execute (Syntax/Runtime error fatal): -50% per soal
- File salah konten (mis. submit Praktikum copy modul): 0 untuk soal tsb
- 1 commit besar di akhir tanpa history bertahap: investigasi plagiat, -20% nilai total
- README kosong / tanpa analisis Big-O: -15

---

## TEMPLATE README.md (WAJIB DIIKUTI)

```markdown
# Remedial UTS - Struktur Data

## Identitas
- Nama: ___________________
- NIM: ___________________
- Kelas: A / B
- Set Remedial: A / B / C
- Tanggal Submit: ___________________

## Refleksi Singkat (3-5 kalimat)
Apa kesalahan/kelemahan saya di UTS sebelumnya, dan apa yang akan saya
perbaiki sekarang?

___________________________________________________________________
___________________________________________________________________

## Penjelasan per Soal

### Soal 1: <Judul>
Penjelasan implementasi (3-5 kalimat):
___________________________________________________________________

Analisis kompleksitas Big-O per method utama:
| Method | Best | Average | Worst | Alasan singkat |
|--------|------|---------|-------|----------------|
| ...    | ...  | ...     | ...   | ...            |

### Soal 2: <Judul>
(format sama)

### Soal 3: <Judul>
(format sama)

## Jawaban Soal Teori (semua set sama, WAJIB)

### Teori 1 — Perbedaan Stack vs Queue
Jelaskan perbedaan utama Stack dan Queue (cara akses + use case nyata),
masing-masing minimal 1 contoh use case di dunia nyata (selain yang sudah
ada di modul).

Jawaban:
___________________________________________________________________

### Teori 2 — Tracing Manual
Diberikan operasi pada Stack: push(5), push(8), push(2), pop(), push(11),
peek(), pop(), push(7).
Tunjukkan isi Stack setelah setiap operasi (gambar/representasi list).
Berapa nilai terakhir di top setelah semua operasi selesai?

Jawaban:
___________________________________________________________________

### Teori 3 — Perbandingan Kompleksitas
Bandingkan kompleksitas operasi `insert_at_position(i, value)` pada:
- (a) Array (Python list)
- (b) Single Linked List
- (c) Double Linked List

Sebutkan Big-O Worst Case untuk masing-masing, dan jelaskan kapan
struktur mana yang lebih efisien.

Jawaban:
___________________________________________________________________
```

---

---

# SET A — Sistem Manajemen Inventory Toko

> **Skenario:** Kamu membuat sistem inventory untuk toko kelontong "Toko Berkah".
> Sistem ini akan mengelola data barang, histori perubahan stok, dan transaksi pelanggan.

---

## SET A — Soal 1: Inventory dengan MyArray Custom

Implementasikan class `MyArray` (custom, JANGAN langsung pakai Python list bawaan) dan class `Inventory` yang menggunakannya.

### Spesifikasi `MyArray`
| Method | Deskripsi |
|--------|-----------|
| `__init__(capacity=10)` | Inisialisasi dengan kapasitas awal |
| `append(value)` | Tambah elemen di akhir |
| `get(index)` | Ambil elemen di index |
| `set(index, value)` | Set elemen di index |
| `remove_at(index)` | Hapus elemen di index, geser ke kiri |
| `size()` | Jumlah elemen aktual |
| `__iter__()` | Supaya bisa di-loop dengan `for x in arr` |

### Spesifikasi `Inventory`
| Method | Deskripsi |
|--------|-----------|
| `add_item(nama, harga, stok)` | Tambah barang |
| `remove_item(nama)` | Hapus barang berdasarkan nama |
| `find_by_name(nama)` | Cari barang, return dict atau None |
| `total_value()` | Total nilai inventory = sum(harga * stok) |
| `sort_by_stock(ascending=True)` | Urutkan inventory berdasar stok |
| `count_low_stock(threshold)` | Hitung barang dengan stok ≤ threshold |

### Test Case Wajib (taruh di bagian `if __name__ == "__main__":`)
```python
inv = Inventory()
inv.add_item("Beras 5kg", 65000, 20)
inv.add_item("Minyak 1L", 18000, 50)
inv.add_item("Gula 1kg", 14000, 5)
inv.add_item("Telur kg", 28000, 8)

assert inv.find_by_name("Beras 5kg")["stok"] == 20
assert inv.find_by_name("Tidak Ada") is None
assert inv.total_value() == (65000*20 + 18000*50 + 14000*5 + 28000*8)
assert inv.count_low_stock(threshold=10) == 2  # Gula & Telur

inv.remove_item("Minyak 1L")
assert inv.find_by_name("Minyak 1L") is None

inv.sort_by_stock(ascending=True)
# urutan stok harus naik: 5, 8, 20
print("Semua test Soal 1 PASSED")
```

---

## SET A — Soal 2: StokHistory dengan Double Linked List

Implementasikan class `Node`, `DoublyLinkedList`, dan `StokHistory` untuk mencatat perubahan stok barang dengan kemampuan **undo / redo**.

### Spesifikasi `DoublyLinkedList`
| Method | Deskripsi |
|--------|-----------|
| `append(data)` | Tambah di akhir |
| `delete_node(node)` | Hapus node spesifik (O(1) karena DLL) |
| `to_list()` | Convert ke Python list (untuk display/test) |
| `size()` | Jumlah node |

### Spesifikasi `StokHistory`
| Method | Deskripsi |
|--------|-----------|
| `record(item, action, jumlah)` | Catat perubahan ("IN"/"OUT"). Setelah record, redo history harus terhapus |
| `undo()` | Batalkan record terakhir, pindahkan ke redo stack |
| `redo()` | Ulangi record yang baru saja di-undo |
| `show_history()` | Return list semua record aktif (urut kronologis) |
| `find_by_item(item)` | Return list record untuk barang tertentu |

### Test Case Wajib
```python
h = StokHistory()
h.record("Beras", "IN", 50)
h.record("Beras", "OUT", 10)
h.record("Gula", "IN", 20)

assert len(h.show_history()) == 3
assert h.find_by_item("Beras") == [
    {"item":"Beras","action":"IN","jumlah":50},
    {"item":"Beras","action":"OUT","jumlah":10},
]

h.undo()  # batalkan "Gula IN 20"
assert len(h.show_history()) == 2
h.redo()  # ulangi "Gula IN 20"
assert len(h.show_history()) == 3

# Setelah record baru, redo history harus hilang
h.undo()  # batalkan "Gula IN 20" lagi
h.record("Telur", "IN", 5)  # record baru, redo terhapus
h.redo()  # tidak ada efek
assert len(h.show_history()) == 3
print("Semua test Soal 2 PASSED")
```

---

## SET A — Soal 3: Integrasi Toko (Stack + Queue)

Buat class `Toko` yang menggabungkan **Stack** (untuk pending order yang menunggu konfirmasi) dan **Queue** (untuk order yang siap diproses kasir).

### Spesifikasi
| Method | Deskripsi |
|--------|-----------|
| `add_pending_order(customer, items)` | Push order ke `pending_stack` |
| `confirm_top_order()` | Pop dari `pending_stack`, enqueue ke `process_queue` |
| `process_next_order()` | Dequeue dari `process_queue`, return order yang diproses |
| `pending_count()` | Jumlah order di stack |
| `processing_count()` | Jumlah order di queue |
| `cancel_top_pending()` | Pop dari `pending_stack` tanpa proses (customer batal) |

### Test Case Wajib
```python
toko = Toko()
toko.add_pending_order("Andi", ["Beras", "Minyak"])
toko.add_pending_order("Budi", ["Gula"])
toko.add_pending_order("Citra", ["Telur"])
assert toko.pending_count() == 3

# Stack: konfirmasi top = Citra (LIFO)
o1 = toko.confirm_top_order()
assert o1["customer"] == "Citra"
assert toko.pending_count() == 2
assert toko.processing_count() == 1

toko.confirm_top_order()  # Budi
toko.confirm_top_order()  # Andi
assert toko.processing_count() == 3

# Queue: proses FIFO = Citra dulu (karena Citra yang pertama konfirmasi)
p1 = toko.process_next_order()
assert p1["customer"] == "Citra"
assert toko.processing_count() == 2

# Test cancel
toko.add_pending_order("Doni", ["Susu"])
toko.cancel_top_pending()
assert toko.pending_count() == 0
print("Semua test Soal 3 PASSED")
```

---

---

# SET B — Sistem Antrian Layanan Customer Service

> **Skenario:** Kamu membangun sistem antrian customer service untuk perusahaan
> telekomunikasi. Sistem ini menangani daftar pelanggan, riwayat chat, dan
> antrian penanganan keluhan berdasarkan prioritas.

---

## SET B — Soal 1: CustomerList dengan MyArray Custom

Implementasikan class `MyArray` (custom) dan class `CustomerList`.

### Spesifikasi `MyArray`
Sama seperti Set A — `__init__`, `append`, `get`, `set`, `remove_at`, `size`, `__iter__`.

### Spesifikasi `CustomerList`
| Method | Deskripsi |
|--------|-----------|
| `register(customer_id, nama, priority)` | Tambah customer (priority: 1=normal, 2=premium, 3=vip) |
| `search_by_id(customer_id)` | Return dict customer atau None |
| `sort_by_priority(descending=True)` | Urutkan customer (vip dulu kalau descending) |
| `get_top_n(n)` | Return n customer dengan priority tertinggi (list of dict) |
| `count_by_priority(priority)` | Hitung customer dengan priority tertentu |
| `avg_priority()` | Return rata-rata priority semua customer (float) |

### Test Case Wajib
```python
cl = CustomerList()
cl.register("C001", "Andi", 1)
cl.register("C002", "Budi", 3)
cl.register("C003", "Citra", 2)
cl.register("C004", "Dewi", 3)
cl.register("C005", "Eko", 1)

assert cl.search_by_id("C002")["nama"] == "Budi"
assert cl.search_by_id("X999") is None
assert cl.count_by_priority(3) == 2  # Budi, Dewi
assert abs(cl.avg_priority() - 2.0) < 0.01  # (1+3+2+3+1)/5

cl.sort_by_priority(descending=True)
top2 = cl.get_top_n(2)
assert all(c["priority"] == 3 for c in top2)
print("Semua test Soal 1 PASSED")
```

---

## SET B — Soal 2: ChatHistory dengan Single Linked List

Implementasikan `Node`, `SingleLinkedList`, dan `ChatHistory` untuk menyimpan
riwayat chat antara customer dan CS.

### Spesifikasi `SingleLinkedList`
| Method | Deskripsi |
|--------|-----------|
| `append(data)` | Tambah di akhir |
| `delete_at(index)` | Hapus node di index ke-i |
| `reverse()` | Balikkan urutan node (in-place) |
| `to_list()` | Return Python list |
| `size()` | Jumlah node |

### Spesifikasi `ChatHistory`
| Method | Deskripsi |
|--------|-----------|
| `add_message(sender, text)` | Tambah pesan baru |
| `delete_message(index)` | Hapus pesan ke-i |
| `reverse_chat()` | Balikkan urutan chat (chat terbaru jadi paling atas) |
| `find_keyword(keyword)` | Return list pesan yang mengandung keyword (case insensitive) |
| `count_by_sender(sender)` | Hitung pesan dari sender tertentu |

### Test Case Wajib
```python
ch = ChatHistory()
ch.add_message("Customer", "Halo, koneksi internet saya lambat")
ch.add_message("CS", "Halo, kami akan cek dari sini")
ch.add_message("Customer", "Iya, saya tunggu")
ch.add_message("CS", "Sudah kami restart modemnya")
ch.add_message("Customer", "Sekarang sudah cepat, terima kasih")

assert ch.count_by_sender("Customer") == 3
assert ch.count_by_sender("CS") == 2

hasil = ch.find_keyword("cepat")
assert len(hasil) == 1
assert "cepat" in hasil[0]["text"].lower()

ch.delete_message(1)  # hapus pesan CS "Halo, kami akan cek..."
assert ch.count_by_sender("CS") == 1

ch.reverse_chat()
# pesan pertama setelah reverse harus "Sekarang sudah cepat..."
print("Semua test Soal 2 PASSED")
```

---

## SET B — Soal 3: Integrasi LayananCS (Priority Queue + Stack)

Buat class `LayananCS` yang menggabungkan **Priority Queue** (untuk antrian
keluhan berdasarkan urgency) dan **Stack** (untuk undo penanganan terakhir).

### Spesifikasi
| Method | Deskripsi |
|--------|-----------|
| `submit_complaint(customer, isi, urgency)` | Tambah keluhan ke priority queue (urgency 1=low, 3=urgent) |
| `handle_next()` | Ambil keluhan urgency tertinggi (FIFO untuk urgency sama), simpan ke action stack |
| `undo_last_handle()` | Kembalikan keluhan terakhir yang ditangani ke priority queue |
| `pending_count()` | Jumlah keluhan menunggu |
| `handled_count()` | Jumlah keluhan yang sudah ditangani (di stack) |
| `peek_next()` | Lihat keluhan berikutnya tanpa mengambilnya |

### Test Case Wajib
```python
cs = LayananCS()
cs.submit_complaint("Andi", "Internet lambat", 2)
cs.submit_complaint("Budi", "Tidak bisa nelpon", 3)
cs.submit_complaint("Citra", "Tagihan salah", 1)
cs.submit_complaint("Dewi", "Service mati total", 3)

# Urgency tertinggi (3): Budi & Dewi. FIFO untuk urgency sama: Budi dulu.
assert cs.peek_next()["customer"] == "Budi"

h1 = cs.handle_next()
assert h1["customer"] == "Budi"
assert cs.handled_count() == 1
assert cs.pending_count() == 3

h2 = cs.handle_next()
assert h2["customer"] == "Dewi"

# Undo: Dewi kembali ke queue, jadi peek_next harus Dewi lagi
cs.undo_last_handle()
assert cs.peek_next()["customer"] == "Dewi"
assert cs.handled_count() == 1
print("Semua test Soal 3 PASSED")
```

---

---

# SET C — Sistem Manajemen Tugas (Project Tracker)

> **Skenario:** Kamu membuat aplikasi project tracker untuk tim software developer.
> Sistem mengelola daftar tugas, rotasi assignee, dan penjadwalan eksekusi tugas.

---

## SET C — Soal 1: TaskList dengan MyArray Custom

Implementasikan class `MyArray` (custom) dan class `TaskList`.

### Spesifikasi `MyArray`
Sama seperti Set A & B.

### Spesifikasi `TaskList`
| Method | Deskripsi |
|--------|-----------|
| `add_task(task_id, judul, deadline_days)` | Tambah tugas (deadline_days = hari tersisa, integer) |
| `complete_task(task_id)` | Tandai tugas sebagai selesai (status="DONE") |
| `find_task(task_id)` | Return dict task atau None |
| `sort_by_deadline(ascending=True)` | Urutkan berdasar deadline_days |
| `count_overdue()` | Hitung task dengan deadline_days < 0 dan status != "DONE" |
| `get_progress()` | Return persentase task DONE (float 0-100) |

### Test Case Wajib
```python
tl = TaskList()
tl.add_task("T001", "Implement login", 3)
tl.add_task("T002", "Fix bug navbar", -2)  # overdue
tl.add_task("T003", "Write docs", 7)
tl.add_task("T004", "Code review", -1)   # overdue
tl.add_task("T005", "Deploy staging", 5)

assert tl.find_task("T002")["judul"] == "Fix bug navbar"
assert tl.count_overdue() == 2

tl.complete_task("T001")
tl.complete_task("T002")
assert tl.count_overdue() == 1  # T004 saja, T002 sudah DONE
assert abs(tl.get_progress() - 40.0) < 0.01  # 2/5 = 40%

tl.sort_by_deadline(ascending=True)
# urutan deadline_days terkecil dulu (paling overdue dulu)
print("Semua test Soal 1 PASSED")
```

---

## SET C — Soal 2: AssigneeRotator dengan Circular Linked List

Implementasikan `Node`, `CircularLinkedList`, dan `AssigneeRotator` untuk
rotasi penugasan task secara round-robin di antara anggota tim.

### Spesifikasi `CircularLinkedList`
| Method | Deskripsi |
|--------|-----------|
| `add(data)` | Tambah node baru (tail.next harus menunjuk head) |
| `remove(data)` | Hapus node dengan data tertentu (jaga circular structure) |
| `size()` | Jumlah node |
| `to_list()` | Return list (mulai dari head, satu round) |

### Spesifikasi `AssigneeRotator`
| Method | Deskripsi |
|--------|-----------|
| `add_assignee(nama)` | Tambah anggota tim |
| `remove_assignee(nama)` | Hapus anggota tim dari rotasi |
| `next_assignee()` | Return nama anggota berikutnya (rotasi) lalu maju pointer |
| `current()` | Return nama anggota saat ini (tanpa maju pointer) |
| `count()` | Jumlah anggota tim |

### Test Case Wajib
```python
rot = AssigneeRotator()
rot.add_assignee("Alice")
rot.add_assignee("Bob")
rot.add_assignee("Charlie")
assert rot.count() == 3
assert rot.current() == "Alice"

# Rotasi round-robin
assert rot.next_assignee() == "Alice"
assert rot.next_assignee() == "Bob"
assert rot.next_assignee() == "Charlie"
assert rot.next_assignee() == "Alice"  # circular, balik ke Alice

# Hapus tengah
rot.remove_assignee("Bob")
assert rot.count() == 2
# Setelah hapus Bob, next_assignee dari Alice harus langsung Charlie
sisa = [rot.next_assignee() for _ in range(4)]
# Setiap 2 langkah harus cycle Alice -> Charlie -> Alice -> Charlie
assert sisa == ["Charlie", "Alice", "Charlie", "Alice"] \
    or sisa == ["Alice", "Charlie", "Alice", "Charlie"]
print("Semua test Soal 2 PASSED")
```

---

## SET C — Soal 3: Integrasi ProjectManager (Stack + Queue)

Buat class `ProjectManager` yang menggabungkan **Stack** (untuk undo task
yang baru saja di-complete) dan **Queue** (untuk scheduler tugas yang
menunggu di-eksekusi).

### Spesifikasi
| Method | Deskripsi |
|--------|-----------|
| `schedule_task(task_id, judul)` | Enqueue tugas ke `scheduler_queue` |
| `execute_next()` | Dequeue dari `scheduler_queue`, push ke `completed_stack`, return tugas |
| `undo_complete()` | Pop dari `completed_stack`, enqueue lagi ke depan `scheduler_queue` |
| `scheduled_count()` | Jumlah task menunggu eksekusi |
| `completed_count()` | Jumlah task selesai |
| `next_scheduled()` | Lihat task berikutnya tanpa eksekusi |

### Test Case Wajib
```python
pm = ProjectManager()
pm.schedule_task("T1", "Setup database")
pm.schedule_task("T2", "Implement login")
pm.schedule_task("T3", "Build UI")
assert pm.scheduled_count() == 3

# FIFO: eksekusi T1 dulu
assert pm.next_scheduled()["task_id"] == "T1"
done1 = pm.execute_next()
assert done1["task_id"] == "T1"
assert pm.completed_count() == 1

done2 = pm.execute_next()  # T2
assert done2["task_id"] == "T2"

# Undo: T2 kembali ke depan queue (karena terakhir di-complete)
pm.undo_complete()
assert pm.completed_count() == 1
assert pm.next_scheduled()["task_id"] == "T2"  # T2 harus di depan

# Schedule task baru, T2 tetap di depan
pm.schedule_task("T4", "Write tests")
assert pm.next_scheduled()["task_id"] == "T2"

print("Semua test Soal 3 PASSED")
```

---

---

# CATATAN PENTING UNTUK PENGUMPULAN

1. **Setiap file `.py` HARUS bisa dijalankan langsung** dengan `python Soal1_*.py` dan menampilkan "Semua test Soal X PASSED" (atau pesan error yang jelas kalau gagal).

2. **Identitas di header file `.py`** wajib:
   ```python
   """
   Remedial UTS Struktur Data - Set <X>
   Soal <N>: <Judul>

   Nama : ___________________
   NIM  : ___________________
   Kelas: ___________________
   """
   ```

3. **Commit bertahap** — minimal 3 commit per soal (initial, progress, final). Jangan satu commit besar di akhir. History `git log` akan diperiksa.

4. **README.md WAJIB diisi lengkap** sesuai template di atas. Tanpa README atau README kosong = -15 dari nilai total.

5. **Pertanyaan / klarifikasi** soal: hubungi dosen via channel yang disepakati. **JANGAN tanya jawaban ke teman**.

---

*Soal ini disusun sebagai remedial UTS Praktikum Struktur Data, Program Studi Sistem Informasi - Institut Teknologi Kalimantan.*
