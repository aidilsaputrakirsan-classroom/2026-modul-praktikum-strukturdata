---
description: Alur Evaluasi Manual Praktikum Struktur Data (Agent Skill/Workflow)
---
# Alur Evaluasi Manual Praktikum Struktur Data

Dokumen ini adalah standarisasi panduan (skill/workflow) untuk agent dalam melakukan evaluasi, code review, dan pengujian kode tugas praktikum mahasiswa secara manual. Panduan ini dirancang agar dapat direplikasi untuk memeriksa **Kelas B** dan kelas-kelas lainnya.

## 1. Persiapan Evaluasi
- Pastikan repositori mahasiswa sudah berhasil di-clone (misal menggunakan `gh classroom clone student-repos`).
- Siapkan direktori laporan hasil evaluasi yang terpisah per kelas (misal: `Hasil-Evaluasi-Kelas-A`, `Hasil-Evaluasi-Kelas-B`).
- Di dalam direktori tersebut, buat satu file rekapitulasi utama bernama `README.md`.
- Lakukan evaluasi secara berurutan, direpresentasikan dalam _checklist_ tugas (berdasarkan NIM terkecil hingga terbesar jika memungkinkan).

## 2. Proses Pemeriksaan (Per Mahasiswa)
Untuk setiap mahasiswa, agent harus mereplikasi langkah berikut:
1. **Pencarian File Pendukung:** Temukan direktori tugas Modul 1 dan Modul 2 (atau modul lainnya) milik mahasiswa bersangkutan.
   *Catatan: perhatikan variansi nama folder dan file. Mahasiswa seringkali menamai file tanpa ekstensi `.py` atau menggunakan kapitalisasi yang berbeda.*
2. **Review Kode Statis (Code Review):**
   - Buka dan baca source code mahasiswa menggunakan `view_file`.
   - Lakukan inspeksi penerapan struktur data (Stack, Array, dsb) secara logis sesuai modul/flowchart.
   - Deteksi adanya _bug_ sintaksis, kesalahan indentasi, atau inefisiensi pointer sebelum skrip dieksekusi.
3. **Pengujian Kode (Unit Testing):**
   - Jalankan script Python satu per satu secara independen menggunakan terminal (`run_command`).
   - Amati *output* dari blok `__main__` (*test case*).
   - Pastikan apakah testing memperoleh `PASSED` secara utuh atau terdapat kegagalan seperti `AssertionError` / `Traceback`.
4. **Penilaian dan Pencatatan Logika:**
   - Berikan nilai **100** jika semua test *PASSED* dan struktur program berjalan sangat baik.
   - Jika terdapat *error* kompilasi atau *bug* logic, berikan penalti rasional (misal menjadi 80 atau 90) dan jabarkan analisis kerusakannya secara spesifik.

## 3. Pembuatan Laporan
1. **Laporan Individu:**
   - Tulis *Markdown file* baru khusus untuk mahasiswa tersebut (format: `Evaluasi_[NIM]_[NamaTanpaSpasi].md`) tersimpan di dalam direktori `Hasil-Evaluasi-Kelas-X`.
   - Masukkan informasi mahasiswa, hasil review kode fungsional per tugas, hasil uji unit, dan nilai parsial modul.
   - Hitung dan berikan blok **NILAI RATA-RATA SEMENTARA** pada akhir dokumen.
2. **Update Laporan Keseluruhan:**
   - Tambahkan baris _table row_ baru di dalam file `README.md`.
   - Cantumkan: Nomor urut, Nama Lengkap, NIM, Nilai per Modul, Rata-rata, dan _relative link_ yang mengarah secara tepat ke Laporan Individu mahasiswa tersebut.

## 4. Pelaporan ke User
- Setelah memproses _batch/queue_ sejumlah mahasiswa, segera hentikan proses untuk konfirmasi dengan merekap capaian evaluasi menggunakan `notify_user` ke Pengguna agar memberikan wewenang lebih lanjut.
