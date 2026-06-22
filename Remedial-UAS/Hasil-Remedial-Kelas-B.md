# Hasil Remedial UAS Praktikum Struktur Data (Kelas B)

> **Materi:** Modul 9-15 (Tree/BST, Graph, Searching, Sorting).
> **Cap nilai remedial:** 65. **Formula:** `UAS_final = MAX(UAS_asli, MIN(UAS_remedial, 65))`.
> **Deadline:** Jumat, 19 Juni 2026 14.00 WITA (sudah lewat — dinilai 22 Jun).

---

## Rubrik & Penalti

| Komponen | Bobot |
|----------|------:|
| Soal 1 (BST) | 25 |
| Soal 2 (Graph BFS/DFS) | 25 |
| Soal 3 (Sorting manual + Binary Search) | 30 |
| README (identitas + Big-O + teori) | 20 |

**Penalti diterapkan:**
- Error fatal (Syntax/Indent/Runtime) / konten salah / tanpa test: soal terkait **0**.
- Soal 3 pakai `sorted()`/`list.sort()` bawaan: **-50%** Soal 3.
- README minim/tanpa Big-O atau tidak ada: **-15**.
- **Suspect copy** (similarity implementasi **> 0.90**): soal terkait **-50%** (kebijakan: dikurangi, tidak 0).
- Salah set (kerjakan set lain dari yang ditugaskan): **-15%**.

---

## Rekapitulasi Hasil Per Mahasiswa

| NIM | Nama | Set | S1 | S2 | S3 | README | Skor Mentah | Cap 65 | UAS Asli | UAS Final | Catatan |
|---|---|:---:|:---:|:---:|:---:|:---:|---:|---:|---:|---:|---|
| 10231001 | **Achmad Bayhaqi** | A | 25 | 25 | 30 | 20 | 100 | 65 | 50 | **65** | Lengkap — semua PASSED |
| 10251006 | **Muhammad Farid Kusuma Admaja** | A | 25 | 25 | 30 | 20 | 100 | 65 | 42 | **65** | Lengkap — semua PASSED |
| 10251012 | **Fransiskus Ezekiel Rama Apriliano** | A | 25 | 25 | 30 | 20 | 100 | 65 | 56 | **65** | Lengkap — semua PASSED |
| 10251027 | **Kurnia Latifiansyah** | A | - | - | - | - | - | - | 55 | **55** | Belum submit remedial |
| 10251042 | **Heldawati Ilham** | A | 0 | 0 | 0 | 20 | 20 | 20 | 42 | **42** | S1/S2/S3 IndentationError — file tidak bisa dieksekusi |
| 10251051 | **Ahdyar Ramadhan** | A | 25 | 25 | 30 | 20 | 100 | 65 | 37 | **65** | Lengkap — semua PASSED |
| 10251060 | **Nastain Masyal Sadani** | A | 25 | 25 | 30 | 20 | 100 | 65 | 52 | **65** | Lengkap — semua PASSED |
| 10251066 | **Noel Randi Pakpahan** | A | 0 | 25 | 30 | 20 | 75 | 65 | 39 | **65** | S1 konten UTS (Inventory) & tanpa test → 0 |
| 10251081 | **Fernando Frederik Lowing** | A | - | - | - | - | - | - | 0 | **0** | Belum submit remedial |
| 10251084 | **Sultan Zahid** | A | 25 | 25 | 30 | 20 | 100 | 65 | 36 | **65** | Lengkap — semua PASSED |
| 10251096 | **Gilang Artha Wijaya** | A | - | - | - | - | - | - | 0 | **0** | Belum submit remedial |
| 10251108 | **Kevin Maulana Pratama** | A | 25 | 25 | 30 | 20 | 100 | 65 | 22 | **65** | Lengkap — semua PASSED |
| 10231038 | **Firni Fauziah Ramadhini** | B | 25 | 25 | 30 | 20 | 100 | 65 | 40 | **65** | Lengkap — semua PASSED |
| 10251015 | **Enjelin Hartini** | B | 25 | 25 | 30 | 20 | 100 | 65 | 29 | **65** | Lengkap — semua PASSED |
| 10251036 | **Marine Fajar Sprinkler Taranda** | B | 25 | 25 | 30 | 20 | 100 | 65 | 32 | **65** | Logika 3 soal PASSED. Awal kelewat: folder typo "REMIDIAL-UAS" + nama file `<...>` (path invalid Windows) + README ke-paste ke .py |
| 10251045 | **Irfan Kurniawan** | B | - | - | - | - | - | - | 20 | **20** | Belum submit remedial |
| 10251054 | **Rizky Muhammad Adha** | B | 25 | 25 | 30 | 20 | 100 | 65 | 24 | **65** | Lengkap — semua PASSED |
| 10251063 | **Muhammad Hanif Murtadho** | B | 25 | 25 | 30 | 20 | 100 | 65 | 52 | **65** | 3 soal PASSED (S1 lolos test wajib). Awal kelewat: folder typo "Remidial-UAS" |
| 10251069 | **Albin Gian Aztafaiq** | B | 25 | 25 | 30 | 20 | 100 | 65 | 12 | **65** | Lengkap — semua PASSED |
| 10251072 | **Reihan Agil Wijaya** | B | - | - | - | - | - | - | 63 | **63** | Belum submit remedial |
| 10251087 | **Muhammad Nabil Fadhilla** | B | 25 | 25 | 30 | 20 | 100 | 65 | 46 | **65** | Lengkap — semua PASSED |
| 10251102 | **Muhammad Devan Abbiyu Dzaki Laksmana** | B | 25 | 25 | 30 | 20 | 100 | 65 | 32 | **65** | Lengkap — semua PASSED |
| 10251112 | **Cindy Callista Beatrice Sigalingging** | B | 25 | 25 | 30 | 20 | 100 | 65 | 54 | **65** | Lengkap — semua PASSED |
| 10251009 | **Taufiq Erik Herliansyah** | C | 25 | 25 | 30 | 20 | 100 | 65 | 20 | **65** | 3 soal PASSED. Awal kelewat: pull lokal abort (staged deletions) |
| 10251021 | **Alejandro Aprillio Bayu Aji** | C | 25 | 25 | 30 | 20 | 100 | 65 | 42 | **65** | 3 soal PASSED (commit 19 Jun, sblm deadline). Awal kelewat: file `...` invalid path blokir checkout |
| 10251039 | **Muhammad Khoiry Rijal** | C | 25 | 25 | 30 | 20 | 100 | 65 | 37 | **65** | Lengkap — semua PASSED |
| 10251048 | **Dewi 'Husna Butsainah Nuhsabila** | C | 25 | 25 | 15 | 20 | 85 | 65 | 61 | **65** | S3 suspect-copy 0.91 vs Risna → -50% |
| 10251057 | **Shafwat Azzah Hirfazanisa Latimojong** | C | - | - | - | - | - | - | 50 | **50** | Belum submit remedial |
| 10251075 | **Katon Hillal Alwan Saputra** | C | 25 | 25 | 30 | 20 | 100 | 65 | 22 | **65** | Lengkap — semua PASSED |
| 10251078 | **Naafi' Annisa Nugrahantiningdyah** | C | 25 | 25 | 30 | 20 | 100 | 65 | 58 | **65** | Lengkap — semua PASSED |
| 10251093 | **Bagas Abdullah** | C | - | - | - | - | - | - | 12 | **12** | Belum submit remedial |
| 10251099 | **Raihan Pramudya** | C | 25 | 25 | 30 | 20 | 100 | 65 | 54 | **65** | Lengkap — semua PASSED |
| 10251105 | **Muhammad Haikal El Pasha** | C | 25 | 25 | 30 | 20 | 100 | 65 | 16 | **65** | Lengkap — semua PASSED |
| 10251115 | **Jonatan Bagus Kristiawan** | C | 25 | 25 | 30 | 20 | 100 | 65 | 38 | **65** | Lengkap — semua PASSED |

---

## Ringkasan

| Kategori | Jumlah |
|----------|------:|
| Submit & nilai naik | 26 |
| Submit tapi UAS asli >= remedial (asli dipakai) | 1 |
| Belum submit (UAS asli tetap) | 7 |
| **Total terdaftar** | **34** |

> _Update 22 Jun: +4 submission terverifikasi dari komplain (Marine 10251036, Hanif 10251063, Taufiq 10251009, Alejandro 10251021) yang awalnya kelewat karena typo folder / path invalid (file `...`/`<>`) / pull abort._
