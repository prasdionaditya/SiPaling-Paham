# 🚀 Quick Start Guide

## ⚡ Setup dalam 5 Menit

### 1️⃣ Install Python
```bash
# Cek versi Python
python --version  # Harus 3.9+
```

### 2️⃣ Setup Project
```bash
# Clone/download project
cd analisis-materi-kuliah

# Create virtual environment
python -m venv venv

# Activate (Windows)
venv\Scripts\activate

# Activate (Linux/Mac)
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### 3️⃣ Get API Key
1. Buka: https://platform.openai.com/api-keys
2. Login/Register
3. Click "Create new secret key"
4. Copy key (format: `sk-proj-...`)

### 4️⃣ Configure
Buat file `.env`:
```env
OPENAI_API_KEY=sk-proj-paste-your-key-here
```

### 5️⃣ Test
```bash
python check_api.py
```

✅ Jika muncul "API key valid!" → Success!

### 6️⃣ Run
```bash
python app.py
```

🎉 Buka browser: `http://localhost:7860`

---

## 📝 Cheat Sheet

### Keyboard Shortcuts
- `Ctrl + Enter` → Submit (dalam chat)
- `Ctrl + C` → Stop server
- `Tab` → Switch antar fields

### Format File Support
✅ PDF (.pdf)
✅ Word (.docx)
✅ Text (.txt)
❌ Images, PowerPoint, Excel

### Ukuran Rekomendasi
- **Minimum**: 50 karakter
- **Optimal**: 200-2000 kata
- **Maximum**: 5000 kata (split jika lebih)

### Model Comparison Quick

| Model | Speed | Cost/1k | Quality | Pilih Jika |
|-------|-------|---------|---------|-----------|
| gpt-4o-mini | 🚀🚀🚀 | $0.0001 | ⭐⭐⭐⭐ | Default, balanced |
| gpt-4o | 🚀🚀 | $0.0050 | ⭐⭐⭐⭐⭐ | Butuh quality max |
| gpt-3.5-turbo | 🚀🚀🚀 | $0.0001 | ⭐⭐⭐ | Super budget |

---

## 🎯 Common Tasks

### Task 1: Ringkas Materi
```
1. Tab "Analisis Materi"
2. Upload/paste materi
3. Pilih "Ringkasan"
4. Click "Mulai Analisis"
⏱️ ~10-20 detik
```

### Task 2: Buat Soal Ujian
```
1. Tab "Generator Soal"
2. Upload materi
3. Slider: 5 soal
4. Radio: Menengah
5. Click "Generate"
⏱️ ~15-30 detik
```

### Task 3: Tanya AI
```
1. Tab "Chat AI"
2. Ketik: "Jelaskan [konsep] dengan analogi"
3. Enter/Click kirim
⏱️ ~5-10 detik
```

### Task 4: Bandingkan 2 Materi
```
1. Tab "Bandingkan Materi"
2. Input materi 1 & 2
3. Click "Bandingkan"
⏱️ ~20-40 detik
```

---

## 🔥 Pro Tips

### Tip 1: Maksimalkan Ringkasan
❌ **Jangan:** Upload 1 paragraf
✅ **Do:** Minimum 200 kata untuk hasil optimal

### Tip 2: Specific Questions
❌ **Jangan:** "Jelaskan ini"
✅ **Do:** "Jelaskan konsep inheritance dalam OOP dengan analogi rumah tangga"

### Tip 3: Multi-Step Analysis
1. Ringkasan dulu → overview
2. Poin penting → fokus study
3. Penjelasan sederhana → pemahaman
4. Q&A → test knowledge

### Tip 4: Save Everything
- Export hasil ke TXT
- Buat folder per mata kuliah
- Naming: `[MataKuliah]_[Topik]_[Tanggal].txt`

### Tip 5: Batch Mode
Untuk banyak file:
1. Analisis satu per satu
2. Export masing-masing
3. Gabungkan di Word/Notion

---

## ⚠️ Quick Troubleshooting

### Problem: API Error 401
```bash
# Check .env file
cat .env  # Linux/Mac
type .env  # Windows

# Should see:
OPENAI_API_KEY=sk-proj-xxxxx
```

### Problem: ModuleNotFoundError
```bash
# Re-install
pip install -r requirements.txt --force-reinstall
```

### Problem: Port Already in Use
```bash
# Change port in app.py (line last)
server_port=7861  # atau port lain
```

### Problem: Slow Response
- Tunggu 30 detik
- Check internet
- Try smaller file
- Restart app

---

## 📱 Mobile Usage

Akses dari HP:
1. PC dan HP harus 1 WiFi
2. Cek IP PC: `ipconfig` (Windows) / `ifconfig` (Linux)
3. Buka di HP: `http://[IP-PC]:7860`
4. Example: `http://192.168.1.100:7860`

---

## 💰 Cost Calculator

### Estimasi Biaya (GPT-4o-mini)

| Aktivitas | Token | Biaya | Per Hari | Per Bulan |
|-----------|-------|-------|----------|-----------|
| 1x Analisis | ~2k | $0.001 | - | - |
| 10x Analisis | ~20k | $0.01 | - | - |
| Heavy user (50x) | ~100k | $0.05 | $0.05 | $1.50 |
| Super heavy (200x) | ~400k | $0.20 | $0.20 | $6.00 |

💡 Untuk mahasiswa normal: **~$2-5/bulan**

---

## 🎓 Best Practices

### For Exam Prep
1. Upload semua materi
2. Generate ringkasan → buat cheatsheet
3. Extract poin penting → fokus hafalan
4. Generate soal → practice test
5. Chat dengan AI → clarify concepts

### For Assignment
1. Paste requirement
2. "Penjelasan Sederhana" → understand task
3. Chat: "Bagaimana approach terbaik?"
4. Generate soal → test understanding

### For Research
1. Compare materi dari berbagai sumber
2. Identify gaps & differences
3. Chat untuk diskusi mendalam
4. Export semua untuk referensi

---

## 🔗 Quick Links

- **OpenAI Dashboard**: https://platform.openai.com
- **API Keys**: https://platform.openai.com/api-keys
- **Billing**: https://platform.openai.com/account/billing
- **Usage**: https://platform.openai.com/account/usage
- **Gradio Docs**: https://gradio.app/docs

---

## 📞 Need Help?

### Checklist Debug:
- [ ] Python 3.9+ installed?
- [ ] Virtual env activated?
- [ ] Dependencies installed?
- [ ] .env file created?
- [ ] API key valid?
- [ ] Internet connection?
- [ ] Port 7860 available?

Semua ✅? Should work! 🎉

Masih error? Run:
```bash
python check_api.py
```

Dan lihat error message-nya.

---

<div align="center">

**Happy Learning! 📚✨**

[← Back to README](README.md)

</div># 🚀 Quick Start Guide

## ⚡ Setup dalam 5 Menit

### 1️⃣ Install Python
```bash
# Cek versi Python
python --version  # Harus 3.9+
```

### 2️⃣ Setup Project
```bash
# Clone/download project
cd analisis-materi-kuliah

# Create virtual environment
python -m venv venv

# Activate (Windows)
venv\Scripts\activate

# Activate (Linux/Mac)
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### 3️⃣ Get API Key
1. Buka: https://platform.openai.com/api-keys
2. Login/Register
3. Click "Create new secret key"
4. Copy key (format: `sk-proj-...`)

### 4️⃣ Configure
Buat file `.env`:
```env
OPENAI_API_KEY=sk-proj-paste-your-key-here
```

### 5️⃣ Test
```bash
python check_api.py
```

✅ Jika muncul "API key valid!" → Success!

### 6️⃣ Run
```bash
python app.py
```

🎉 Buka browser: `http://localhost:7860`

---

## 📝 Cheat Sheet

### Keyboard Shortcuts
- `Ctrl + Enter` → Submit (dalam chat)
- `Ctrl + C` → Stop server
- `Tab` → Switch antar fields

### Format File Support
✅ PDF (.pdf)
✅ Word (.docx)
✅ Text (.txt)
❌ Images, PowerPoint, Excel

### Ukuran Rekomendasi
- **Minimum**: 50 karakter
- **Optimal**: 200-2000 kata
- **Maximum**: 5000 kata (split jika lebih)

### Model Comparison Quick

| Model | Speed | Cost/1k | Quality | Pilih Jika |
|-------|-------|---------|---------|-----------|
| gpt-4o-mini | 🚀🚀🚀 | $0.0001 | ⭐⭐⭐⭐ | Default, balanced |
| gpt-4o | 🚀🚀 | $0.0050 | ⭐⭐⭐⭐⭐ | Butuh quality max |
| gpt-3.5-turbo | 🚀🚀🚀 | $0.0001 | ⭐⭐⭐ | Super budget |

---

## 🎯 Common Tasks

### Task 1: Ringkas Materi
```
1. Tab "Analisis Materi"
2. Upload/paste materi
3. Pilih "Ringkasan"
4. Click "Mulai Analisis"
⏱️ ~10-20 detik
```

### Task 2: Buat Soal Ujian
```
1. Tab "Generator Soal"
2. Upload materi
3. Slider: 5 soal
4. Radio: Menengah
5. Click "Generate"
⏱️ ~15-30 detik
```

### Task 3: Tanya AI
```
1. Tab "Chat AI"
2. Ketik: "Jelaskan [konsep] dengan analogi"
3. Enter/Click kirim
⏱️ ~5-10 detik
```

### Task 4: Bandingkan 2 Materi
```
1. Tab "Bandingkan Materi"
2. Input materi 1 & 2
3. Click "Bandingkan"
⏱️ ~20-40 detik
```

---

## 🔥 Pro Tips

### Tip 1: Maksimalkan Ringkasan
❌ **Jangan:** Upload 1 paragraf
✅ **Do:** Minimum 200 kata untuk hasil optimal

### Tip 2: Specific Questions
❌ **Jangan:** "Jelaskan ini"
✅ **Do:** "Jelaskan konsep inheritance dalam OOP dengan analogi rumah tangga"

### Tip 3: Multi-Step Analysis
1. Ringkasan dulu → overview
2. Poin penting → fokus study
3. Penjelasan sederhana → pemahaman
4. Q&A → test knowledge

### Tip 4: Save Everything
- Export hasil ke TXT
- Buat folder per mata kuliah
- Naming: `[MataKuliah]_[Topik]_[Tanggal].txt`

### Tip 5: Batch Mode
Untuk banyak file:
1. Analisis satu per satu
2. Export masing-masing
3. Gabungkan di Word/Notion

---

## ⚠️ Quick Troubleshooting

### Problem: API Error 401
```bash
# Check .env file
cat .env  # Linux/Mac
type .env  # Windows

# Should see:
OPENAI_API_KEY=sk-proj-xxxxx
```

### Problem: ModuleNotFoundError
```bash
# Re-install
pip install -r requirements.txt --force-reinstall
```

### Problem: Port Already in Use
```bash
# Change port in app.py (line last)
server_port=7861  # atau port lain
```

### Problem: Slow Response
- Tunggu 30 detik
- Check internet
- Try smaller file
- Restart app

---

## 📱 Mobile Usage

Akses dari HP:
1. PC dan HP harus 1 WiFi
2. Cek IP PC: `ipconfig` (Windows) / `ifconfig` (Linux)
3. Buka di HP: `http://[IP-PC]:7860`
4. Example: `http://192.168.1.100:7860`

---

## 💰 Cost Calculator

### Estimasi Biaya (GPT-4o-mini)

| Aktivitas | Token | Biaya | Per Hari | Per Bulan |
|-----------|-------|-------|----------|-----------|
| 1x Analisis | ~2k | $0.001 | - | - |
| 10x Analisis | ~20k | $0.01 | - | - |
| Heavy user (50x) | ~100k | $0.05 | $0.05 | $1.50 |
| Super heavy (200x) | ~400k | $0.20 | $0.20 | $6.00 |

💡 Untuk mahasiswa normal: **~$2-5/bulan**

---

## 🎓 Best Practices

### For Exam Prep
1. Upload semua materi
2. Generate ringkasan → buat cheatsheet
3. Extract poin penting → fokus hafalan
4. Generate soal → practice test
5. Chat dengan AI → clarify concepts

### For Assignment
1. Paste requirement
2. "Penjelasan Sederhana" → understand task
3. Chat: "Bagaimana approach terbaik?"
4. Generate soal → test understanding

### For Research
1. Compare materi dari berbagai sumber
2. Identify gaps & differences
3. Chat untuk diskusi mendalam
4. Export semua untuk referensi

---

## 🔗 Quick Links

- **OpenAI Dashboard**: https://platform.openai.com
- **API Keys**: https://platform.openai.com/api-keys
- **Billing**: https://platform.openai.com/account/billing
- **Usage**: https://platform.openai.com/account/usage
- **Gradio Docs**: https://gradio.app/docs

---

## 📞 Need Help?

### Checklist Debug:
- [ ] Python 3.9+ installed?
- [ ] Virtual env activated?
- [ ] Dependencies installed?
- [ ] .env file created?
- [ ] API key valid?
- [ ] Internet connection?
- [ ] Port 7860 available?

Semua ✅? Should work! 🎉

Masih error? Run:
```bash
python check_api.py
```

Dan lihat error message-nya.

---

<div align="center">

**Happy Learning! 📚✨**

[← Back to README](README.md)

</div>