import json
import os
from datetime import datetime

with open("repo_evaluation.json", "r") as f:
    data = json.load(f)

# Create directory if not exists
os.makedirs("Hasil-Evaluasi", exist_ok=True)

md_content = f"""# 📊 Laporan Evaluasi Praktikum Struktur Data
> **Tanggal Evaluasi:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
> **Total Mahasiswa Dievaluasi:** {len(data)}

---

## 🎯 Ringkasan Eksekutif

Berikut adalah hasil rekapitulasi penilaian repository GitHub Classroom mahasiswa untuk **Modul 1** dan **Modul 2**.

"""

completed_m1 = sum(1 for v in data.values() if v["Modul 1"]["Status"] == "Lengkap")
completed_m2 = sum(1 for v in data.values() if v["Modul 2"]["Status"] == "Lengkap")
empty = sum(1 for v in data.values() if v["Modul 1"]["Status"] == "Kosong" and v["Modul 2"]["Status"] == "Kosong")

md_content += f"""
### 📈 Statistik
- ✅ **Selesai Modul 1 Lengkap:** {completed_m1} mahasiswa
- ✅ **Selesai Modul 2 Lengkap:** {completed_m2} mahasiswa
- ❌ **Belum MengerjakanSama Sekali:** {empty} mahasiswa

---

## 📋 Daftar Mahasiswa & Hasil Evaluasi

| No | 👤 Nama / GitHub Username | 🟢 Modul 1 Status | 📂 File M1 | 🔵 Modul 2 Status | 📂 File M2 |
|---:|:---|:---|:---:|:---|:---:|
"""

# Sort data by name
sorted_data = sorted(data.items(), key=lambda x: x[0].lower())

def get_badge(status):
    if status == "Lengkap":
        return "🟩 **LENGKAP**"
    elif status == "Kurang":
        return "🟨 **KURANG**"
    else:
        return "🟥 **KOSONG**"

for i, (name, record) in enumerate(sorted_data, 1):
    m1 = record["Modul 1"]
    m2 = record["Modul 2"]
    
    m1_badge = get_badge(m1["Status"])
    m2_badge = get_badge(m2["Status"])
    
    md_content += f"| {i} | `{name}` | {m1_badge} | {m1['File Count']} files | {m2_badge} | {m2['File Count']} files |\n"

md_content += """

---

💡 *Catatan:*
- **Lengkap**: Minimal 3 file valid ditemukan dalam modul.
- **Kurang**: Ada file ditemukan tetapi jumlahnya di bawah standar.
- **Kosong**: Tidak ada file jawaban (.py) ditemukan.

---
*Dibuat secara otomatis oleh AI Assistant* ✨
"""

with open("Hasil-Evaluasi/Laporan_Evaluasi.md", "w", encoding="utf-8") as f:
    f.write(md_content)

print("Markdown report created at Hasil-Evaluasi/Laporan_Evaluasi.md")
