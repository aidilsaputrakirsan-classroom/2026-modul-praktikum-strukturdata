# Hasil Remedial UAS Praktikum Struktur Data (Kelas A)

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
| 10231081 | **Rendy Rifandi Kurnia** | A | 25 | 25 | 30 | 20 | 100 | 65 | 36 | **65** | Lengkap — semua PASSED |
| 10251008 | **Nadya Az-Zahra** | A | 25 | 25 | 30 | 20 | 100 | 65 | 43 | **65** | Lengkap — semua PASSED |
| 10251017 | **Devi Gustiani** | A | 25 | 25 | 30 | 20 | 100 | 65 | 48 | **65** | Lengkap — semua PASSED |
| 10251029 | **Silvester Jevon Amabel** | A | 25 | 25 | 30 | 20 | 100 | 65 | 40 | **65** | Lengkap — semua PASSED |
| 10251044 | **Muh. Asrul Syam** | A | - | - | - | - | - | - | 56 | **56** | Belum submit remedial |
| 10251053 | **Noel Natalian Somba** | A | 25 | 25 | 30 | 20 | 100 | 65 | 34 | **65** | Lengkap — semua PASSED |
| 10251062 | **Ananda Eurico Rhiva Rifqia Salim** | A | - | - | - | - | - | - | 55 | **55** | Belum submit remedial |
| 10251071 | **Muhammad Rasya Al Khalifi** | A | 25 | 25 | 30 | -15 | 65 | 65 | 55 | **65** | Tanpa README → -15 |
| 10251080 | **Julian Zaky Saputra** | A | 25 | 25 | 30 | 20 | 100 | 65 | 59 | **65** | Lengkap — semua PASSED |
| 10251092 | **Razi Abdullah** | A | 25 | 25 | 30 | 20 | 100 | 65 | 29 | **65** | 3 soal PASSED (commit 18 Jun, sblm deadline). Awal kelewat: typo folder "Remdial-UAS" |
| 10251110 | **Farel Noviansyah** | A | 25 | 25 | 30 | 20 | 100 | 65 | 38 | **65** | Lengkap — semua PASSED |
| 10251002 | **Dina Gracella Apnel Lengkong** | B | 25 | 25 | 30 | 20 | 100 | 65 | 51 | **65** | Lengkap — semua PASSED |
| 10251011 | **A. Suci Maharani P** | B | 25 | 25 | 30 | 20 | 100 | 65 | 54 | **65** | Lengkap — semua PASSED |
| 10251020 | **Dhevrant Zhelynov Malelo** | B | 0 | 25 | 15 | 20 | 60 | 60 | 41 | **60** | S1 TypeError (search None); S3 suspect-copy 0.91 vs Akbar → -50% |
| 10251032 | **Firyal Farah Khulaidah** | B | 25 | 25 | 30 | 20 | 100 | 65 | 41 | **65** | Lengkap — semua PASSED |
| 10251035 | **Putri Nabila Safitri** | B | 25 | 25 | 15 | 20 | 85 | 65 | 56 | **65** | S3 suspect-copy 0.95 vs Akbar → -50% |
| 10251047 | **Nurul Syahira Az'zahra** | B | 25 | 0 | 30 | 20 | 75 | 65 | 51 | **65** | S2 IndentationError |
| 10251056 | **Syahrina Aliyyu Tunggadewi** | B | 25 | 25 | 30 | 20 | 100 | 65 | 43 | **65** | Lengkap — semua PASSED |
| 10251065 | **Bryan Abil Al-Fikri** | B | - | - | - | - | - | - | 35 | **35** | Belum submit remedial |
| 10251074 | **Muhammad Rizqi Akbar** | B | 25 | 25 | 15 | 20 | 85 | 65 | 54 | **65** | S3 suspect-copy 0.95 vs Putri / 0.91 vs Dhevrant → -50% |
| 10251104 | **Chelsea Angelika Velayati** | B | 25 | 25 | 30 | 20 | 100 | 65 | 45 | **65** | Lengkap — semua PASSED |
| 10251114 | **Andre Adi Ruhaya** | B | 25 | 25 | 30 | 20 | 85 | 65 | 60 | **65** | Salah set: mengerjakan Set A padahal ditugaskan Set B → -15% |
| 10251005 | **Rifat Adlyjuliandra** | C | 25 | 25 | 15 | -15 | 50 | 50 | 41 | **50** | S3 pakai sorted() (bukan sort manual) → -50%; README minim tanpa Big-O → -15 |
| 10251014 | **Zacky Ahmad Ardian** | C | 25 | 25 | 30 | 20 | 100 | 65 | 54 | **65** | Lengkap — semua PASSED |
| 10251023 | **Arya Cahya Nugraha** | C | - | - | - | - | - | - | 45 | **45** | Belum submit remedial |
| 10251038 | **Ayudya Aisyah Mutiaradinna** | C | 0 | 25 | 30 | 20 | 75 | 65 | 48 | **65** | S1 IndentationError |
| 10251050 | **Muhammad Zennin Feriatta Dzakwan** | C | 25 | 25 | 30 | 20 | 100 | 65 | 44 | **65** | Lengkap — semua PASSED |
| 10251059 | **Taufiiqul Akmal** | C | 25 | 25 | 30 | 20 | 100 | 65 | 43 | **65** | Lengkap — semua PASSED |
| 10251068 | **Muhammad Fajri Ikhsan** | C | 25 | 25 | 30 | 20 | 100 | 65 | 27 | **65** | Lengkap — semua PASSED |
| 10251077 | **Risna Andriani** | C | 25 | 25 | 15 | 20 | 85 | 65 | 62 | **65** | S3 suspect-copy 0.91 vs Dewi Husna → -50% |
| 10251089 | **Muhammad Ryan Eka Putra** | C | 25 | 25 | 30 | 20 | 100 | 65 | 55 | **65** | Lengkap — semua PASSED |
| 10251107 | **Rifat Sutha Abdillah** | C | 25 | 25 | 30 | 20 | 100 | 65 | 38 | **65** | Lengkap — semua PASSED |
| 10251117 | **Muhammad Azriel Al Fadhil** | C | 25 | 25 | 30 | 20 | 100 | 65 | 52 | **65** | Lengkap — semua PASSED |

---

## Ringkasan

| Kategori | Jumlah |
|----------|------:|
| Submit & nilai naik | 29 |
| Submit tapi UAS asli >= remedial (asli dipakai) | 0 |
| Belum submit (UAS asli tetap) | 4 |
| **Total terdaftar** | **33** |
