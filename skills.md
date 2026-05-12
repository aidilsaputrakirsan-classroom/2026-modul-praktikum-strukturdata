---
description: Alur Evaluasi Manual Praktikum Struktur Data (Agent Skill/Workflow)
---
# Alur Evaluasi Manual Praktikum Struktur Data

File instruksi ini memandu AI Assistant untuk mengevaluasi repositori mahasiswa kelas Struktur Data secara **manual satu-per-satu**. Pendekatan ini menjamin integritas evaluasi melalui validasi test dan code review individual.

> ⚠️ **DILARANG** menggunakan skrip Python otomatis `generate` kasar untuk evaluasi massal. Setiap mahasiswa harus dievaluasi secara komparatif dengan ketelitian tinggi.

---

## 1. Persiapan Laporan

- Buat direktori `Hasil-Evaluasi-Kelas-X/` (X = A, B, dst).
- Di dalamnya:
  - Satu `README.md` berisi tabel rekapitulasi nilai + catatan khusus.
  - Satu file `Evaluasi_NIM_NamaLengkap_username.md` per mahasiswa.

---

## 2. Pemahaman Soal

- Baca `01-modul.md`, `02-modul.md`, dst. di root project untuk memahami soal tugas setiap modul.
- Identifikasi apa yang seharusnya diimplementasikan mahasiswa (method, output, validasi test case).

---

## 3. Penyusuran Direktori Mahasiswa

- Clone repositori global: `gh classroom clone student-repos` (atau `git pull` jika sudah ada).
- Folder mahasiswa biasanya berada di `strukturdata-{a|b}-submissions/strukturdata-{a|b}-{username}/`.
- Saring folder `.git` dan repositori non-relevan.
- Struktur internal mahasiswa **bervariasi** — bisa `minggu 1/`, `Minggu1/`, `Modul-01/`, `tugas/week-1/`, dll. Jangan asumsikan satu pola.

---

## 4. Verifikasi Isi Folder

- `list_dir` setiap folder mahasiswa per minggu.
- Cek apakah file tugas (`Tugas1_*.py`, `Tugas2_*.py`, `Tugas3_*.py`) ada di lokasi yang diharapkan **atau** folder alternatif (`Tugas/`, `Tugas 2/`, dst.).
- Jika ekstensi `.py` hilang (mis. `tugas1_NIM` tanpa `.py`), tetap test dengan Python interpreter — namun **kenakan penalti -15 per tugas** (lihat bagian 7).

---

## 5. Testing Execution

**Perintah standar:**
```bash
PYTHONIOENCODING=utf-8 python "path/ke/file.py" 2>&1
```

- Selalu set `PYTHONIOENCODING=utf-8` — Windows console default cp1252 sering error untuk emoji/unicode dalam test output.
- Tambahkan `2>&1` untuk capture stderr (error message dari interpreter).

**Kasus khusus — Windows path invalid:**
File/folder dengan karakter invalid di Windows (mis. titik di akhir: `Shafwat Azzah H. L.`) tidak dapat di-checkout. Gunakan:
```bash
git show origin/main:"path/ke/file.py" | python
```

---

## 6. Validasi Hasil — Tidak Cukup Hanya "PASSED"

Wajib cek **3 hal**:

1. **Test case lulus** — semua `✓ Test ... PASSED` dan tidak ada `AssertionError`/exception.
2. **Konten file sesuai tugas** — banyak mahasiswa submit file salah:
   - File praktikum dikumpulkan sebagai tugas (mis. `ArrayStack.py` bukan Browser History).
   - Kode modul lain dicopy ke folder modul ini (mis. M5 Browser History dicopy ke folder M6 sebagai T3 Bank Queue).
   - File template kosong/placeholder (1–2 baris).
3. **Output masuk akal** — bukan cuma PASSED, validasi nilai numerik:
   - Avg waiting time bank queue **harus positif** (negatif = logika salah).
   - Total execution time Round Robin scheduler harus sesuai (mis. 12 detik).
   - Right-associativity `^`: `A^B^C` harus jadi `A B C ^ ^` (bukan `A B ^ C ^`).

---

## 7. Konvensi Penilaian

### Skor per Tugas
| Kondisi | Nilai |
|---|---|
| Test lulus + konten benar | 100 |
| File tidak ada / tidak dikumpul | 0 |
| Test gagal / error fatal | 0 |
| Konten salah (file praktikum, modul lain, placeholder) | 0 |
| Test lulus tapi terlambat | max 50 |
| Test lulus tapi tanpa ekstensi `.py` | -15 (jadi 85) |
| Bug minor (mis. 1 method gagal dari N method) | proportional |

### Skor per Modul
Rata-rata 3 tugas: `(T1 + T2 + T3) / 3`

Contoh: `(100 + 100 + 0) / 3 = 67`

### Skor Rata-Rata
Rata-rata semua modul yang sudah dievaluasi: `(M1 + M2 + ... + Mn) / n`

### Notasi di README
- **`-`** = belum dievaluasi (asisten belum cek)
- **`0`** = sudah dievaluasi, tapi tidak ada submission / error fatal
- **angka lain (1–100)** = sudah dievaluasi dengan nilai tersebut

Jangan campur aduk `-` dan `0`. Setelah dievaluasi, `-` harus diganti `0` jika tidak ada submission.

### Badge Warna
| Nilai | Warna Badge |
|---|---|
| ≥ 90 | `success` (hijau) |
| ≥ 70 | `yellowgreen` |
| ≥ 50 | `orange` |
| < 50 | `red` |

Format: `![Score](https://img.shields.io/badge/Score-XX.XX-{warna})`

---

## 8. Format File `Evaluasi_NIM_NamaLengkap_username.md`

```markdown
# 📝 Laporan Evaluasi Terperinci - Praktikum Struktur Data

---

## 👤 Data Mahasiswa
- **Nama:** {Nama Lengkap}
- **NIM:** {NIM}
- **Kelas:** Struktur Data {A|B}
- **GitHub Username:** `{username}`

---

## 🥇 Hasil Evaluasi Modul 1: {Judul Modul}

### 1. Tugas 1: {Judul Tugas}
- **Pengecekan Kode:** {ringkas, 1–2 kalimat tentang implementasi}
- **Hasil Testing Terminal:** **PASSED** ✅ (100%) / **FAILED** ❌ (0%)

### 2. Tugas 2: ...
### 3. Tugas 3: ...

**✨ NILAI MODUL 1: {nilai} ✨**

---

## (ulang untuk modul lain)

---
### **🏆 NILAI RATA-RATA (Modul 1-N): {avg} 🏆**

*Penilaian dievaluasi secara statis-manual berdasarkan kode program dan divalidasi melalui eksekusi unit test satu per satu.*
```

---

## 9. Format `Hasil-Evaluasi-Kelas-X/README.md`

```markdown
# Laporan Evaluasi Praktikum Struktur Data (Kelas X) - Modul 1, 2, ..., N

| No | Nama Lengkap | NIM | GitHub Username | M1 | M2 | ... | Mn | Nilai Rata-rata | Detail Evaluasi |
|---:|:---|:---|:---|:---:|:---:|:---:|:---:|:---|
| 1 | **{Nama}** | {NIM} | `{user}` | 100 | 100 | ... | ![Score](...) | [Lihat Laporan](Evaluasi_{NIM}_{Nama}_{user}.md) |
...

## 📝 Catatan Khusus Evaluasi
1. **{Nama} ({NIM}):** {penjelasan kasus tidak normal}
...
```

**Catatan khusus** hanya untuk:
- Mahasiswa dengan kasus tidak normal (file salah konten, late submission, dual account GitHub, NIM tidak sesuai, dll.).
- **Jangan** catat mahasiswa dengan nilai penuh — tidak ada yang perlu dijelaskan.

---

## 10. NIM Verification

Jika username GitHub ambigu atau mahasiswa tidak mencantumkan nama (mis. `strukturdata-b-Vedomzz`):
- Cek header file kode (`# NIM: 10251084`) untuk konfirmasi identitas.
- Cross-check dengan daftar mahasiswa resmi jika tersedia.
- Jangan asumsikan NIM dari username — selalu verifikasi.

---

## 11. Handling Feedback Mahasiswa Pasca-Evaluasi

Jika mahasiswa komplain bahwa nilainya salah:
1. **Re-test** file yang dikomplain dengan command yang sama.
2. **Verifikasi root cause** — apakah bug di kode mahasiswa atau kesalahan evaluasi.
3. **Update jika valid**:
   - Bug di kode mahasiswa → nilai **tetap** (kesalahan dia, bukan kita).
   - File ada tapi terlewat saat evaluasi → **koreksi nilai** + update eval file + README + catatan.
   - Data salah (NIM, nama) → **koreksi** + rename file eval jika perlu.
4. **Dokumentasikan** perubahan di catatan khusus README jika kasusnya tidak normal.

---

## 12. Larangan & Best Practices

- ❌ **Jangan** pakai skrip Python otomatis untuk generate nilai massal.
- ❌ **Jangan** asumsikan struktur folder mahasiswa seragam — cek manual per mahasiswa.
- ❌ **Jangan** mark file sebagai "tidak ada submission" tanpa cek folder alternatif (mis. `Tugas/` di root mahasiswa, bukan `Minggu1/Tugas/`).
- ❌ **Jangan** terburu-buru menambahkan catatan khusus untuk semua mahasiswa — hanya yang bermasalah.
- ✅ Selalu validasi konten file, bukan cuma test PASSED.
- ✅ Selalu set `PYTHONIOENCODING=utf-8`.
- ✅ Selalu cross-check NIM dari header kode jika username ambigu.
- ✅ Selalu update `README.md` + file `Evaluasi_*.md` + catatan secara konsisten setelah perubahan nilai.

---

*Pendekatan ini berpegang teguh pada integritas analisis manual AI dan mencegah skor buatan otomatis yang tidak bisa diverifikasi silang dengan logika algoritma orisinil tiap mahasiswa.*
