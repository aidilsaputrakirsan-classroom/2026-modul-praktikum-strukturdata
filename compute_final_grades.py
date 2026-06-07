"""
Compute final grades for Kelas A & B Struktur Data.

Komposisi bobot:
- Praktikum: 30%  (rata-rata M1-M12 dari README evaluasi)
- Kuis:      10%
- UTS:       25%
- UAS:       25%  (belum ada - kolom placeholder)
- Kehadiran: 10%  (HADIR=1, IZIN=0.5, TANPA KETERANGAN=0, null=skip)

Konversi huruf (batas bawah inklusif):
- A:  >= 86
- AB: 76 <= x < 86
- B:  66 <= x < 76
- BC: 56 <= x < 66
- C:  51 <= x < 56
- D:  41 <= x < 51
- E:  < 41

Catatan:
- Daftar mahasiswa diambil dari file Excel (presensi), sehingga setiap NIM
  yang terdaftar tetap masuk laporan meskipun tidak ada data evaluasi.
- Sel kosong di tabel menggunakan tanda '-'.
- Kolom Huruf hanya menampilkan huruf (tanpa badge skor).
"""

import openpyxl
from pathlib import Path

EXCEL_PATH = Path('PRESENSI PRAKTIKUM STRUKTUR DATA.xlsx')

BOBOT = {
    'praktikum': 0.30,
    'kuis': 0.10,
    'uts': 0.25,
    'uas': 0.25,
    'hadir': 0.10,
}


def letter_grade(score):
    if score is None:
        return '-'
    if score >= 86:
        return 'A'
    if score >= 76:
        return 'AB'
    if score >= 66:
        return 'B'
    if score >= 56:
        return 'BC'
    if score >= 51:
        return 'C'
    if score >= 41:
        return 'D'
    return 'E'


def safe_num(v):
    if v is None or v == '' or (isinstance(v, str) and v.strip() == ''):
        return None
    try:
        return float(str(v).strip())
    except (ValueError, TypeError):
        return None


def compute_attendance(row_values, week_active):
    """Hitung kehadiran. `week_active` adalah list bool sepanjang row_values
    yang menandai minggu mana yang sudah berjalan (ada minimal 1 HADIR di kelas).

    - HADIR -> 1.0
    - IZIN / SAKIT -> 0.5
    - TANPA KETERANGAN / ALPA / sel kosong di minggu yang SUDAH berjalan -> 0
    - sel kosong di minggu yang BELUM berjalan -> skip
    """
    weight_sum = 0.0
    max_sum = 0.0
    for i, v in enumerate(row_values):
        is_empty = v is None or (isinstance(v, str) and v.strip() == '')
        if is_empty:
            if i < len(week_active) and week_active[i]:
                max_sum += 1.0  # minggu sudah berjalan, sel kosong = alpa
            continue
        s = str(v).strip().upper()
        if s == 'HADIR':
            weight_sum += 1.0
            max_sum += 1.0
        elif s in ('IZIN', 'SAKIT'):
            weight_sum += 0.5
            max_sum += 1.0
        else:  # TANPA KETERANGAN, ALPA, atau lainnya
            max_sum += 1.0
    if max_sum == 0:
        return None
    return (weight_sum / max_sum) * 100.0


def detect_active_weeks(sheet, n_cols):
    """Return list bool: True jika minggu (kolom ke-i) sudah berjalan.
    Minggu dianggap sudah berjalan jika ada >= 1 entry HADIR/IZIN di kolom tsb.
    """
    active = [False] * n_cols
    for row in sheet.iter_rows(min_row=3, values_only=True):
        cells = row[2:2 + n_cols]
        for i, v in enumerate(cells):
            if v is None or (isinstance(v, str) and v.strip() == ''):
                continue
            s = str(v).strip().upper()
            if s in ('HADIR', 'IZIN', 'SAKIT', 'TANPA KETERANGAN', 'ALPA'):
                active[i] = True
    return active


def parse_excel():
    """Return: {kelas: {nim: {nama_excel, kuis, uts, attendance}}} for ALL NIMs in Excel."""
    wb = openpyxl.load_workbook(EXCEL_PATH, data_only=True)
    data = {'A': {}, 'B': {}}

    for kelas, sheet in [('A', 'Kuis dan UTS KELAS A'), ('B', 'Kuis dan UTS KELAS B')]:
        ws = wb[sheet]
        for row in ws.iter_rows(min_row=2, values_only=True):
            nim = row[0]
            if not nim:
                continue
            try:
                nim = int(nim)
            except (ValueError, TypeError):
                continue
            data[kelas][nim] = {
                'nama_excel': row[1],
                'kuis': safe_num(row[2]),
                'uts': safe_num(row[3]),
                'attendance': None,
            }

    for kelas, sheet in [('A', 'KELAS A'), ('B', 'KELAS B')]:
        ws = wb[sheet]
        n_cols = ws.max_column - 2  # kolom A=NIM, B=Nama, C+ = minggu
        active_weeks = detect_active_weeks(ws, n_cols)
        for row in ws.iter_rows(min_row=3, values_only=True):
            nim = row[0]
            if not nim:
                continue
            try:
                nim = int(nim)
            except (ValueError, TypeError):
                continue
            att = compute_attendance(row[2:2 + n_cols], active_weeks)
            if nim not in data[kelas]:
                data[kelas][nim] = {
                    'nama_excel': row[1],
                    'kuis': None,
                    'uts': None,
                    'attendance': att,
                }
            else:
                data[kelas][nim]['attendance'] = att

    return data


# Praktikum scores per NIM (dari README evaluasi). NIM yang tidak ada di sini
# berarti tidak ada data evaluasi praktikum (akan ditampilkan '-').
PRAKTIKUM_A = {  # rata-rata M1-7, 9-14 (13 modul); update M14 Sorting Lanjutan
    10231081: 91.00,  # M14=83 (T1 blok analisis tidak diisi)
    10251002: 94.92,
    10251005: 61.08,  # M14=0 (tidak ada Modul 14)
    10251008: 67.31,  # M14=0 (hanya praktikum)
    10251011: 78.46,  # M14=33 (hanya T2)
    10251014: 89.54,
    10251017: 83.77,
    10251020: 99.23,
    10251023: 73.85,
    10251026: 85.23,
    10251029: 89.85,
    10251032: 84.54,
    10251035: 97.23,
    10251038: 95.69,
    10251044: 75.69,  # M14=0 (tidak ada Modul 14)
    10251047: 85.00,  # M14=0 (hanya praktikum)
    10251050: 79.54,  # M14=0 (tidak ada Modul 14)
    10251053: 73.08,  # M14=33 (T1 RecursionError, T2 AssertionError)
    10251056: 99.23,
    10251059: 84.62,  # M14=0 (tidak ada Modul 14)
    10251062: 87.23,  # M14=0 (tidak ada Modul 14)
    10251065: 82.08,  # M14=0 (tidak ada Modul 14)
    10251068: 86.92,
    10251071: 88.46,  # M14=0 (tidak ada Modul 14)
    10251074: 74.38,  # M14=0 (tidak ada Modul 14)
    10251086: 89.77,  # Hidayah pakai NIM 10251086 di Excel (terdaftar GitHub Classroom: 10251075); M14=100
    10251077: 81.77,  # M14=0 (hanya praktikum)
    10251080: 84.62,
    10251083: 97.46,
    10251089: 85.92,  # M14=0 (tidak ada Modul 14)
    10251092: 83.31,
    10251095: 96.15,
    10251104: 88.23,  # M14=0 (file tugas kosong)
    10251107: 75.92,  # M14=0 (hanya praktikum)
    10251110: 93.00,
    10251114: 75.69,
    10251117: 87.38,  # M14=83 (T1 blok analisis tidak diisi)
}

PRAKTIKUM_B = {  # rata-rata M1-7, 9-14 (13 modul); update M14 Sorting Lanjutan
    10231001: 97.46,
    10231038: 90.46,
    10251006: 87.46,
    10251009: 38.46,  # M14=0
    10251012: 69.23,
    10251015: 74.38,
    10251018: 88.23,
    10251021: 44.62,
    10251024: 84.62,  # M14=0
    10251027: 82.08,  # M14=0 (placeholder kosong)
    10251084: 69.54,  # M14=0 (hanya praktikum)
    10251033: 70.54,
    10251036: 55.92,  # M14=0
    10251039: 30.77,  # M14=0
    10251042: 35.93,  # M14=0
    10251048: 89.77,
    10251051: 15.39,  # M14=0
    10251054: 65.93,  # M14=0
    10251057: 79.54,
    10251060: 94.92,
    10251063: 89.77,
    10251066: 78.23,
    10251069: 51.54,  # M14=0
    10251072: 92.38,
    10251075: 20.54,  # M14=67 (T1 duplikat konten T2)
    10251078: 92.08,
    10251081: 32.31,  # M14=0
    10251087: 55.15,  # M14=0
    10251090: 88.46,  # M14=0 (konten Modul 15, bukan sorting)
    10251093: 33.39,  # M14=0
    10251099: 82.08,  # M14=0
    10251102: 15.39,  # M14=0
    10251105: 81.08,
    10251108: 62.84,  # M14=0 (hanya praktikum)
    10251112: 60.31,
    10251115: 85.92,
}

# Username (GitHub) per NIM
USERNAME_A = {
    10231081: "NorEndGate", 10251002: "10251002", 10251005: "rifatadlyjuliandra",
    10251008: "nadyaazzahra", 10251011: "Asuci-Maharani", 10251014: "Zacky10251014",
    10251017: "devigustiani", 10251020: "Dhevrant", 10251023: "AryaCahyaNugraha22",
    10251026: "Salsabilaayees", 10251029: "SilvesterJevon", 10251032: "FiryalFarah",
    10251035: "10251035-Putri", 10251038: "10251038", 10251044: "Asrul-6",
    10251047: "syahira10251047", 10251050: "Zennin2511", 10251053: "N3CH0",
    10251056: "SyahrinaAliyyuTunggadewi", 10251059: "10251059-coder",
    10251062: "AnandaEurico", 10251065: "Bryan1065", 10251068: "Fajri-ITK",
    10251071: "MuhRasyaAlKhalifi", 10251074: "MuhammadRizqiAkbar33",
    10251086: "MuhammadRizqiHidayah", 10251077: "RisnaAndriani-10251077",
    10251080: "Julian-Zaky-Saputra", 10251083: "MossesRestuN", 10251089: "10251089-Ryan",
    10251092: "snowyy26", 10251095: "NurHayyu-10251095", 10251104: "Chelsea-10251104",
    10251107: "RifatSuthaAbdillah", 10251110: "10251110", 10251114: "Andre10251114",
    10251117: "azrilalfadhil-svg",
}

USERNAME_B = {
    10231001: "AchmadLyraa", 10231038: "firnifziah", 10251006: "Ridz010",
    10251009: "Taufiqerikhrl", 10251012: "fransiskusezekiel", 10251015: "enjelinhartini",
    10251018: "Faiz-codepy", 10251021: "alejandroaprillio", 10251024: "anawithcode",
    10251027: "kurniala", 10251084: "Vedomzz", 10251033: "MlhamNF",
    10251036: "MarineTaranda", 10251039: "strukturdata-b-10251039", 10251042: "heldaa127",
    10251048: "10251048-boop", 10251051: "AhdyarRamadhan", 10251054: "Rizi-54",
    10251057: "fasya25", 10251060: "Nastai1n-bit", 10251063: "liandizgo-design",
    10251066: "noelrandi7", 10251069: "Binngian", 10251072: "reihan-agil-wijaya",
    10251075: "KatonHillal", 10251078: "naafiannisa", 10251081: "10251081-blip",
    10251087: "nabilfdl", 10251090: "nurasyifaahmad", 10251093: "10251093",
    10251099: "Raihanp-dya", 10251102: "devansgt", 10251105: "10251105-haikal",
    10251108: "10251108-create", 10251112: "galeryc-afk", 10251115: "JonatanBagusKristiawan",
}


def compute_nilai_sementara(prak, kuis, uts, hadir):
    """Nilai sementara (tanpa UAS), dinormalisasi ke skala 100.
    Return None jika SEMUA komponen kosong.
    """
    if prak is None and kuis is None and uts is None and hadir is None:
        return None
    p = prak or 0
    k = kuis or 0
    u = uts or 0
    h = hadir or 0
    total = (p * BOBOT['praktikum'] + k * BOBOT['kuis']
             + u * BOBOT['uts'] + h * BOBOT['hadir'])
    bobot_terisi = (BOBOT['praktikum'] + BOBOT['kuis']
                    + BOBOT['uts'] + BOBOT['hadir'])
    return total / bobot_terisi


def fmt(v, dec=0):
    """Format ke integer (dibulatkan) by default. Pakai dec > 0 untuk desimal."""
    if v is None:
        return '-'
    if dec == 0:
        return str(int(round(v)))
    return f"{v:.{dec}f}"


# Override attendance untuk mahasiswa nonaktif (sesuai data resmi presensi).
# Script auto-detect "minggu sudah berjalan" bisa keliru untuk mhs yang hanya
# hadir 1-2 kali; override di sini memastikan nilainya 0 sesuai input dosen.
ATTENDANCE_OVERRIDE = {
    'A': {
        10251041: 0.0,  # Gusti Aulia
        10251098: 0.0,  # Panji Dwi
        10251101: 0.0,  # Fawwaz
    },
    'B': {},
}


# Kuis override (untuk mhs yang data Kuis-nya kosong/salah di Excel)
KUIS_OVERRIDE = {
    'A': {},
    'B': {
        10251115: 60,  # Jonatan Bagus Kristiawan (Excel kosong, diinput susulan)
    },
}


# UTS Final setelah remedial. Formula:
# UTS_final = MAX(UTS_asli, MIN(UTS_remedial, 65))
# Hanya berisi mhs yang skornya naik karena remedial. Yang lain pakai UTS asli dari Excel.
UTS_FINAL_OVERRIDE = {
    'A': {
        10251002: 65,  # Dina (asli 30, remedial cap 65)
        10251005: 65,  # Rifat A (asli 46)
        10251017: 65,  # Devi (asli 45)
        10251023: 65,  # Arya (asli 35)
        10251029: 65,  # Jevon (asli 56)
        10251032: 65,  # Firyal (asli 43)
        10251044: 65,  # Asrul (asli 56)
        10251047: 65,  # Syahira (asli 65) - sama
        10251053: 65,  # Noel (asli 50)
        10251056: 65,  # Syahrina (asli 47)
        10251059: 65,  # Taufiiqul (asli 43)
        10251068: 65,  # Fajri (asli 37)
        10251074: 65,  # Akbar (asli 54)
        10251092: 65,  # Razi (asli 35)
        10251104: 65,  # Chelsea (asli 45)
        10251110: 65,  # Farel (asli 37)
        # Yang remedial tapi UTS asli > remedial: Suci (62 vs 45), Ayudya (53 vs 50), Zennin (55 vs 0)
        # → tidak di-override, tetap pakai UTS asli
    },
    'B': {
        10251012: 65,  # Fransiskus (asli 51)
        10251027: 65,  # Kurnia (asli 55)
        10251039: 65,  # Khoiry (asli 52)
        10251048: 65,  # Dewi (asli 61)
        10251054: 65,  # Rizky (asli 49)
        10251066: 65,  # Noel R (asli 52)
        10251075: 65,  # Katon (asli 32)
        10251102: 65,  # Devan (asli 28)
        10251105: 65,  # Haikal (asli 26)
        10251108: 65,  # Kevin (asli 26)
        10251112: 65,  # Cindy (asli 62)
        # Yang remedial tapi UTS asli > remedial: Firni (51 vs 45), Enjelin (44 vs 35),
        # Marine (57 vs 0), Shafwat (59 vs 55), Albin (39 vs 10) → tetap pakai UTS asli
    },
}


# Sort order: pakai urutan README evaluasi dulu, lalu mahasiswa "extra" dari
# Excel (yang tidak ada di evaluasi) di-append di akhir.
ORDER_A = [
    10231081, 10251002, 10251005, 10251008, 10251011, 10251014, 10251017,
    10251020, 10251023, 10251026, 10251029, 10251032, 10251035, 10251038,
    10251044, 10251047, 10251050, 10251053, 10251056, 10251059, 10251062,
    10251065, 10251068, 10251071, 10251074, 10251086, 10251077, 10251080,
    10251083, 10251089, 10251092, 10251095, 10251104, 10251107, 10251110,
    10251114, 10251117,
]

ORDER_B = [
    10231001, 10231038, 10251006, 10251009, 10251012, 10251015, 10251018,
    10251021, 10251024, 10251027, 10251084, 10251033, 10251036, 10251039,
    10251042, 10251048, 10251051, 10251054, 10251057, 10251060, 10251063,
    10251066, 10251069, 10251072, 10251075, 10251078, 10251081, 10251087,
    10251090, 10251093, 10251099, 10251102, 10251105, 10251108, 10251112,
    10251115,
]


def find_evaluation_file(kelas, nim, username):
    folder = Path(f'Hasil-Evaluasi-Kelas-{kelas}')
    if not folder.exists():
        return None
    matches = list(folder.glob(f"Evaluasi_{nim}_*.md"))
    if matches:
        return matches[0].name
    if username:
        matches = list(folder.glob(f"Evaluasi_*_{username}.md"))
        if matches:
            return matches[0].name
    return None


def build_row_order(kelas, excel_data, order_list):
    """Return list NIM diurutkan ASCENDING berdasarkan NIM (semua mahasiswa,
    termasuk yang ada di Excel maupun di order_list)."""
    all_nims = set(excel_data.keys()) | set(order_list)
    return sorted(all_nims)


def generate_markdown(kelas, praktikum_map, username_map, order_list, excel_data, output_path):
    full_order = build_row_order(kelas, excel_data, order_list)
    lines = []
    lines.append(f"# Nilai Final Praktikum Struktur Data (Kelas {kelas})")
    lines.append("")
    lines.append(f"> **Komposisi bobot:** Praktikum **{int(BOBOT['praktikum']*100)}%**, "
                 f"Kuis **{int(BOBOT['kuis']*100)}%**, UTS **{int(BOBOT['uts']*100)}%**, "
                 f"UAS **{int(BOBOT['uas']*100)}%**, Kehadiran **{int(BOBOT['hadir']*100)}%**.")
    lines.append("")
    lines.append("> **Kehadiran:** HADIR = 1, IZIN = 0.5, TANPA KETERANGAN = 0. Sel kosong pada "
                 "minggu yang **sudah berjalan** dianggap alpa (0); sel kosong pada minggu yang "
                 "**belum berjalan** di-skip. Skor = (sum / total minggu sudah berjalan) x 100.")
    lines.append("")
    lines.append("> **Nilai Sementara:** dihitung dari komponen yang sudah ada (Praktikum + Kuis + "
                 "UTS + Hadir), dinormalisasi ke skala 100 (asumsi UAS sebanding dengan rata-rata "
                 "komponen yang ada). Akan dihitung ulang setelah UAS terisi.")
    lines.append("")
    lines.append("> **Konversi huruf** (batas bawah inklusif): A >= 86, AB 76-86, B 66-76, "
                 "BC 56-66, C 51-56, D 41-51, E < 41.")
    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append("## Rekapitulasi Nilai")
    lines.append("")
    lines.append("| No | NIM | Nama | Praktikum (30%) | Kuis (10%) | UTS (25%) | UAS (25%) | "
                 "Hadir (10%) | Nilai Sementara | Huruf | Detail |")
    lines.append("|---:|:---|:---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|")

    overrides = ATTENDANCE_OVERRIDE.get(kelas, {})
    uts_overrides = UTS_FINAL_OVERRIDE.get(kelas, {})
    kuis_overrides = KUIS_OVERRIDE.get(kelas, {})
    for idx, nim in enumerate(full_order, start=1):
        excel = excel_data.get(nim, {})
        nama_excel = excel.get('nama_excel', '?')
        nama = nama_excel if nama_excel else f"NIM {nim}"
        prak = praktikum_map.get(nim)
        kuis = kuis_overrides.get(nim, excel.get('kuis'))
        uts = uts_overrides.get(nim, excel.get('uts'))
        hadir = overrides.get(nim, excel.get('attendance'))
        username = username_map.get(nim, '')

        nilai = compute_nilai_sementara(prak, kuis, uts, hadir)
        grade = letter_grade(nilai)

        eval_file = find_evaluation_file(kelas, nim, username)
        detail = f"[Lihat]({eval_file})" if eval_file else "-"

        lines.append(
            f"| {idx} | {nim} | **{nama}** | {fmt(prak)} | {fmt(kuis)} | {fmt(uts)} | - | "
            f"{fmt(hadir)} | **{fmt(nilai)}** | **{grade}** | {detail} |"
        )

    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append("## Formula Perhitungan Final")
    lines.append("")
    lines.append("```")
    lines.append("Nilai Final = Praktikum x 0.30 + Kuis x 0.10 + UTS x 0.25 + UAS x 0.25 + Kehadiran x 0.10")
    lines.append("```")
    lines.append("")
    lines.append("Karena **UAS belum dilaksanakan**, kolom **Nilai Sementara** dihitung dengan normalisasi:")
    lines.append("")
    lines.append("```")
    lines.append("Nilai Sementara = (Praktikum x 0.30 + Kuis x 0.10 + UTS x 0.25 + Kehadiran x 0.10) / 0.75")
    lines.append("```")
    lines.append("")
    lines.append("Setelah UAS terisi, formula final akan menggunakan rumus pertama tanpa normalisasi.")
    lines.append("")

    output_path.write_text('\n'.join(lines), encoding='utf-8')
    print(f"Written: {output_path}")


if __name__ == "__main__":
    data = parse_excel()
    generate_markdown('A', PRAKTIKUM_A, USERNAME_A, ORDER_A, data['A'],
                      Path('Hasil-Evaluasi-Kelas-A/Nilai-Final-Kelas-A.md'))
    generate_markdown('B', PRAKTIKUM_B, USERNAME_B, ORDER_B, data['B'],
                      Path('Hasil-Evaluasi-Kelas-B/Nilai-Final-Kelas-B.md'))
