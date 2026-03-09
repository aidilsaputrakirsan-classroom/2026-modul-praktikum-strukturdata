---
description: Alur Evaluasi Manual Praktikum Struktur Data (Agent Skill/Workflow)
---
# Alur Evaluasi Manual Praktikum Struktur Data (Skill)

File instruksi dan kapabilitas ini memandu saya, AI Assistant, untuk mengevaluasi repositori mahasiswa dari kelas Struktur Data secara otomatis semi-manual. Metode ini menjamin integritas evaluasi dan tidak menggunakan skrip Python otomasisasi `generate` kasar (sebagaimana instruksi eksplisit pengguna), melainkan melibatkan proses komparatif test dan validasi satu per satu dengan ketelitian tinggi oleh saya.

## Langkah Evaluasi untuk Kelas-Kelas Berikutnya (Contoh: Kelas B)

1. **Persiapan Laporan**  
   - Buat direktori `Hasil-Evaluasi-Kelas-X` yang di dalamnya terpadu satu file inti `Laporan_Evaluasi.md` berisi tabel ringkasan nilai dengan List/Link menuju Laporan Individu tiap mahasiswa secara terpisah.

2. **Membaca Instruksi Dasar dan Modul**  
   - Buka `01-modul.md` atau `02-modul.md` untuk memahami soal Tugas Terstruktur yang diselesaikan mahasiswa.
   
3. **Penyusuran Top-Level Direktori**  
   - Identifikasi semua folder mahasiswa di dalam sebuah _clone_ repositori global (biasanya via `gh classroom clone student-repos`).
   - Saring folder-folder relevan (hindari file `.git` dan repositori acak di dalamnya).
   
4. **Verifikasi Isi Folder Mahasiswa Secara Manual (Via Tool AI)**  
   - `list_dir` pada setiap folder mahasiswa. Perhatikan peletakan file tugas masing-masing mahasiswa yang memiliki struktur berbeda (ada di `Minggu1`, `Minggu 1`, `Modul1`, dsb).
   - Apabila ekstensi file hilang (misal hanya `tugas1_NIM`), lakukan perintah *rename/move* (`mv`) pada terminal di sisi pengguna untuk menyematkan `.py`.
   
5. **Menjalankan _Testing Execution_ (Manual Checking)**  
   - Lakukan pemanggilan bash terminal: `python "path_absolut_direktori_mahasiswa_A/Minggu 1/tugasX.py"`.
   - Konfirmasi keluaran Terminal atas seluruh test case yang ada dalam script. Evaluasi dan baca seluruh kode program yang ditulis (`view_file`).

6. **Pencatatan Individual dan Tabulasi Rata-Rata**  
   - Untuk setiap mahasiswa yang dievaluasi, buat file markdown bernama `Evaluasi_NIM_NamaLengkap.md`. 
   - Di dalamnya, tulislah hasil *code review* dengan ringkas dan terperinci untuk Tugas masing-masing (seperti "Penggunaan *list swap/if-else statement* yang brilian", dll) dan cantumkan nilai per modul.
   - Hitung nilai rata-rata sementara dan bubuhkan di profil Laporan.
   - Tambahkan *hyperlink* rujukan di daftar nama ke dalam `Laporan_Evaluasi.md`.

*Pendekatan ini berpegang teguh pada integritas analisis manual AI dan mencegah skor buatan otomatis yang tidak bisa diverifikasi silang dengan logika algoritma orisinil tiap mahasiswa.*
