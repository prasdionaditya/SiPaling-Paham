import gradio as gr
from utils.llm_handler import LLMHandler
from utils.text_processor import TextProcessor
import time

# Inisialisasi handler
llm = LLMHandler()
processor = TextProcessor()

# Fungsi untuk format markdown ke HTML yang lebih readable
def format_markdown_to_html(text):
    """Convert markdown-style text to HTML for better rendering"""
    if not text:
        return ""
    
    # Replace **bold** with <strong>
    import re
    text = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', text)
    
    # Replace *italic* with <em>
    text = re.sub(r'\*(.+?)\*', r'<em>\1</em>', text)
    
    # Replace ### headers
    text = re.sub(r'###\s*(.+?)(\n|$)', r'<h3>\1</h3>\2', text)
    text = re.sub(r'##\s*(.+?)(\n|$)', r'<h2>\1</h2>\2', text)
    text = re.sub(r'#\s*(.+?)(\n|$)', r'<h1>\1</h1>\2', text)
    
    # Replace bullet points
    text = re.sub(r'^\s*[-•]\s*(.+?)$', r'<li>\1</li>', text, flags=re.MULTILINE)
    
    # Wrap lists in <ul>
    text = re.sub(r'(<li>.*?</li>\s*)+', r'<ul>\g<0></ul>', text, flags=re.DOTALL)
    
    # Replace newlines with <br> for paragraphs
    text = text.replace('\n\n', '</p><p>')
    
    return f'<div class="formatted-content"><p>{text}</p></div>'

# Fungsi untuk analisis materi dengan progress
def analisis_materi_fn(file, text_input, jenis_analisis, gaya_bahasa, progress=gr.Progress()):
    progress(0, desc="Memproses input...")
    
    # Ekstrak teks dari file atau gunakan input teks
    if file is not None:
        progress(0.2, desc="Membaca file...")
        materi = processor.process_file(file)
    elif text_input:
        materi = text_input
    else:
        return "<p style='color: #ff6b6b;'>⚠️ Silakan upload file atau masukkan teks materi</p>", ""
    
    # Validasi teks
    is_valid, msg = processor.validate_text(materi)
    if not is_valid:
        return f"<p style='color: #ff6b6b;'>⚠️ {msg}</p>", ""
    
    # Proses analisis
    progress(0.5, desc="Menganalisis materi dengan AI...")
    hasil = llm.analisis_materi(materi, jenis_analisis, gaya_bahasa)
    
    progress(1.0, desc="Selesai!")
    
    # Format hasil
    hasil_formatted = format_markdown_to_html(hasil)
    
    # Info tambahan
    word_count = len(materi.split())
    char_count = len(materi)
    info = f"📊 {word_count} kata • {char_count} karakter • {jenis_analisis.replace('_', ' ').title()} • {gaya_bahasa.title()}"
    
    return hasil_formatted, info

# Fungsi untuk perbandingan materi
def bandingkan_materi_fn(file1, text1, file2, text2, gaya_bahasa, progress=gr.Progress()):
    progress(0, desc="Memproses materi pertama...")
    
    # Ekstrak materi 1
    if file1 is not None:
        materi1 = processor.process_file(file1)
    elif text1:
        materi1 = text1
    else:
        return "<p style='color: #ff6b6b;'>⚠️ Silakan masukkan materi pertama</p>", ""
    
    progress(0.3, desc="Memproses materi kedua...")
    
    # Ekstrak materi 2
    if file2 is not None:
        materi2 = processor.process_file(file2)
    elif text2:
        materi2 = text2
    else:
        return "<p style='color: #ff6b6b;'>⚠️ Silakan masukkan materi kedua</p>", ""
    
    progress(0.6, desc="Membandingkan materi...")
    
    # Bandingkan
    hasil = llm.bandingkan_materi(materi1, materi2, gaya_bahasa)
    hasil_formatted = format_markdown_to_html(hasil)
    
    progress(1.0, desc="Selesai!")
    
    # Info
    info = f"📊 Materi 1: {len(materi1.split())} kata • Materi 2: {len(materi2.split())} kata"
    
    return hasil_formatted, info

# Fungsi untuk membuat latihan soal
def buat_soal_fn(file, text_input, jumlah_soal, tingkat, gaya_bahasa, progress=gr.Progress()):
    progress(0, desc="Memproses materi...")
    
    # Ekstrak teks
    if file is not None:
        materi = processor.process_file(file)
    elif text_input:
        materi = text_input
    else:
        return "<p style='color: #ff6b6b;'>⚠️ Silakan upload file atau masukkan teks materi</p>", ""
    
    # Validasi
    is_valid, msg = processor.validate_text(materi)
    if not is_valid:
        return f"<p style='color: #ff6b6b;'>⚠️ {msg}</p>", ""
    
    progress(0.4, desc=f"Membuat {jumlah_soal} soal tingkat {tingkat}...")
    
    # Buat soal
    hasil = llm.buat_latihan_soal(materi, jumlah_soal, tingkat, gaya_bahasa)
    hasil_formatted = format_markdown_to_html(hasil)
    
    progress(1.0, desc="Selesai!")
    
    info = f"✅ {jumlah_soal} soal • {tingkat} • {gaya_bahasa.title()}"
    
    return hasil_formatted, info

# Fungsi chat interaktif - FIXED
def chat_fn(message, history, gaya_bahasa):
    if not message.strip():
        return history, ""
    
    # Validasi pesan terlalu pendek atau tidak jelas
    if len(message.strip()) < 3:
        new_history = history + [[message, "Maaf, pertanyaan Anda terlalu pendek. Bisa tolong diperjelas? Contoh: 'Jelaskan apa itu algoritma sorting'"]]
        return new_history, ""
    
    # Buat system prompt sesuai gaya bahasa
    system_prompts = {
        "formal": "Anda adalah asisten AI akademis yang membantu mahasiswa memahami materi kuliah. Gunakan bahasa formal dan profesional. Jawab dalam Bahasa Indonesia dengan jelas dan terstruktur.",
        "santai": "Anda adalah tutor friendly yang membantu mahasiswa belajar. Gunakan bahasa santai tapi tetap informatif. Jawab dalam Bahasa Indonesia dengan gaya ngobrol yang asik.",
        "sederhana": "Anda adalah kakak tingkat yang suka menjelaskan dengan bahasa super simple. Gunakan analogi, contoh sehari-hari, dan hindari istilah ribet. Jawab dalam Bahasa Indonesia yang mudah dimengerti."
    }
    
    system_prompt = system_prompts.get(gaya_bahasa, system_prompts["formal"])
    
    # Convert history to API format
    api_messages = [{"role": "system", "content": system_prompt}]
    for human, assistant in history:
        if human:
            api_messages.append({"role": "user", "content": human})
        if assistant:
            api_messages.append({"role": "assistant", "content": assistant})
    
    # Add current message
    api_messages.append({"role": "user", "content": message})
    
    # Get response from LLM
    try:
        response = llm.client.chat.completions.create(
            model=llm.model,
            messages=api_messages,
            temperature=0.7,
            max_tokens=1500
        )
        
        assistant_message = response.choices[0].message.content
        new_history = history + [[message, assistant_message]]
        
    except Exception as e:
        assistant_message = f"Maaf, terjadi error: {str(e)}"
        new_history = history + [[message, assistant_message]]
    
    return new_history, ""

# Fungsi export hasil
def export_hasil(text, filename="hasil_analisis"):
    if not text:
        return None
    
    # Remove HTML tags for export
    import re
    clean_text = re.sub('<.*?>', '', text)
    clean_text = clean_text.replace('&nbsp;', ' ')
    
    timestamp = time.strftime("%Y%m%d_%H%M%S")
    filepath = f"{filename}_{timestamp}.txt"
    
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(clean_text)
    
    return filepath

# CSS Custom untuk styling yang support light/dark mode
custom_css = """
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');

* {
    font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif !important;
}

/* Color scheme dengan CSS variables untuk light/dark mode */
:root {
    --primary-color: #6366f1;
    --primary-dark: #4f46e5;
    --primary-light: #818cf8;
}

/* Dark mode colors */
@media (prefers-color-scheme: dark) {
    :root {
        --bg-primary: #0f172a;
        --bg-secondary: #1e293b;
        --bg-tertiary: #334155;
        --text-primary: #f1f5f9;
        --text-secondary: #cbd5e1;
        --border-color: #334155;
        --hover-bg: #475569;
    }
}

/* Light mode colors */
@media (prefers-color-scheme: light) {
    :root {
        --bg-primary: #ffffff;
        --bg-secondary: #f8fafc;
        --bg-tertiary: #f1f5f9;
        --text-primary: #0f172a;
        --text-secondary: #475569;
        --border-color: #e2e8f0;
        --hover-bg: #e2e8f0;
    }
}

/* Manual dark mode class (fallback) */
.dark {
    --bg-primary: #0f172a;
    --bg-secondary: #1e293b;
    --bg-tertiary: #334155;
    --text-primary: #f1f5f9;
    --text-secondary: #cbd5e1;
    --border-color: #334155;
    --hover-bg: #475569;
}

/* Manual light mode class (fallback) */
.light {
    --bg-primary: #ffffff;
    --bg-secondary: #f8fafc;
    --bg-tertiary: #f1f5f9;
    --text-primary: #0f172a;
    --text-secondary: #475569;
    --border-color: #e2e8f0;
    --hover-bg: #e2e8f0;
}

/* Main container */
.gradio-container {
    max-width: 1400px !important;
    margin: auto !important;
    background: var(--bg-primary) !important;
}

body {
    background: var(--bg-primary) !important;
    color: var(--text-primary) !important;
}

/* Header minimalis */
.main-header {
    background: linear-gradient(135deg, var(--primary-color), var(--primary-dark));
    padding: 2rem 1.5rem;
    border-radius: 16px;
    margin-bottom: 2rem;
    text-align: center;
}

.main-header h1 {
    margin: 0;
    font-size: 2.25rem;
    font-weight: 700;
    color: white;
    letter-spacing: -0.025em;
}

.main-header .tagline {
    margin: 0.5rem 0 0 0;
    font-size: 1rem;
    color: rgba(255, 255, 255, 0.9);
    font-weight: 400;
}

/* Tabs minimalis */
.tab-nav {
    background: var(--bg-secondary) !important;
    border-radius: 12px;
    padding: 0.5rem;
    margin-bottom: 1.5rem;
    border: 1px solid var(--border-color) !important;
}

.tab-nav button {
    font-size: 14px !important;
    font-weight: 500 !important;
    padding: 10px 20px !important;
    border-radius: 8px !important;
    transition: all 0.2s ease !important;
    background: transparent !important;
    color: var(--text-secondary) !important;
    border: none !important;
}

.tab-nav button:hover {
    background: var(--hover-bg) !important;
    color: var(--text-primary) !important;
}

.tab-nav button.selected {
    background: var(--primary-color) !important;
    color: white !important;
    box-shadow: 0 1px 3px rgba(99, 102, 241, 0.3);
}

/* Input fields responsive to mode */
textarea, input, .input-component {
    background: var(--bg-secondary) !important;
    border: 1px solid var(--border-color) !important;
    border-radius: 10px !important;
    color: var(--text-primary) !important;
    transition: all 0.2s ease !important;
}

textarea::placeholder, input::placeholder {
    color: var(--text-secondary) !important;
    opacity: 0.6;
}

textarea:focus, input:focus {
    border-color: var(--primary-color) !important;
    box-shadow: 0 0 0 3px rgba(99, 102, 241, 0.1) !important;
    outline: none !important;
}

/* Buttons minimalis */
button {
    border-radius: 10px !important;
    font-weight: 500 !important;
    transition: all 0.2s ease !important;
}

.primary-btn, button[variant="primary"] {
    background: var(--primary-color) !important;
    color: white !important;
    border: none !important;
    padding: 12px 24px !important;
}

.primary-btn:hover, button[variant="primary"]:hover {
    background: var(--primary-dark) !important;
    transform: translateY(-1px);
    box-shadow: 0 4px 12px rgba(99, 102, 241, 0.4) !important;
}

button[variant="secondary"] {
    background: var(--bg-tertiary) !important;
    color: var(--text-primary) !important;
    border: 1px solid var(--border-color) !important;
}

button[variant="secondary"]:hover {
    background: var(--hover-bg) !important;
}

/* Output box dengan proper formatting */
.output-box {
    background: var(--bg-secondary) !important;
    border: 1px solid var(--border-color) !important;
    border-radius: 12px !important;
    padding: 1.5rem !important;
    color: var(--text-primary) !important;
    line-height: 1.8 !important;
    min-height: 200px;
}

/* Formatted content styling */
.formatted-content {
    color: var(--text-primary);
    line-height: 1.8;
}

.formatted-content h1, 
.formatted-content h2, 
.formatted-content h3 {
    color: var(--text-primary);
    margin: 1.5rem 0 1rem 0;
    font-weight: 600;
}

.formatted-content h1 { font-size: 1.75rem; }
.formatted-content h2 { font-size: 1.5rem; }
.formatted-content h3 { font-size: 1.25rem; }

.formatted-content strong {
    color: var(--primary-color);
    font-weight: 600;
}

.formatted-content em {
    color: var(--text-secondary);
    font-style: italic;
}

.formatted-content ul {
    margin: 1rem 0;
    padding-left: 1.5rem;
}

.formatted-content li {
    margin: 0.5rem 0;
    color: var(--text-primary);
}

.formatted-content p {
    margin: 1rem 0;
    color: var(--text-primary);
}

/* Labels and info text */
label, .label {
    color: var(--text-primary) !important;
    font-weight: 500 !important;
    margin-bottom: 0.5rem !important;
}

.info, .gr-form {
    color: var(--text-secondary) !important;
}

/* File upload area */
.file-upload {
    background: var(--bg-secondary) !important;
    border: 2px dashed var(--border-color) !important;
    border-radius: 12px !important;
    color: var(--text-secondary) !important;
}

.file-upload:hover {
    border-color: var(--primary-color) !important;
    background: var(--bg-tertiary) !important;
}

/* Radio and checkbox */
.gr-radio, .gr-checkbox {
    background: var(--bg-secondary) !important;
    border: 1px solid var(--border-color) !important;
    border-radius: 10px !important;
    padding: 1rem !important;
}

.gr-radio label, .gr-checkbox label {
    color: var(--text-primary) !important;
}

/* Slider */
.gr-slider {
    background: var(--bg-secondary) !important;
}

.gr-slider input[type="range"] {
    background: var(--bg-tertiary) !important;
}

/* Chatbot styling */
.chatbot {
    background: var(--bg-secondary) !important;
    border: 1px solid var(--border-color) !important;
    border-radius: 12px !important;
}

.message {
    padding: 1rem !important;
    margin: 0.5rem !important;
    border-radius: 10px !important;
}

.message.user {
    background: var(--primary-color) !important;
    color: white !important;
    margin-left: auto !important;
}

.message.bot {
    background: var(--bg-tertiary) !important;
    color: var(--text-primary) !important;
}

/* Accordion */
.accordion {
    background: var(--bg-secondary) !important;
    border: 1px solid var(--border-color) !important;
    border-radius: 10px !important;
}

/* Info badges */
.info-badge {
    background: var(--bg-tertiary);
    color: var(--text-secondary);
    padding: 0.5rem 1rem;
    border-radius: 8px;
    display: inline-block;
    font-size: 0.875rem;
    font-weight: 500;
    margin: 0.5rem 0;
    border: 1px solid var(--border-color);
}

/* Markdown content */
.markdown, .gr-markdown {
    color: var(--text-primary) !important;
}

.markdown p, .gr-markdown p {
    color: var(--text-primary) !important;
}

.markdown strong, .gr-markdown strong {
    color: var(--primary-color) !important;
}

/* Column and Row backgrounds */
.gr-box, .gr-panel {
    background: transparent !important;
}

/* Progress bar */
.progress-bar {
    background: var(--primary-color) !important;
}

/* Scrollbar adaptive */
::-webkit-scrollbar {
    width: 10px;
    height: 10px;
}

::-webkit-scrollbar-track {
    background: var(--bg-secondary);
}

::-webkit-scrollbar-thumb {
    background: var(--bg-tertiary);
    border-radius: 5px;
}

::-webkit-scrollbar-thumb:hover {
    background: var(--border-color);
}

/* Remove unwanted backgrounds */
.gr-form, .gr-input, .gr-box, .form {
    background: transparent !important;
}

.container, .wrap {
    background: transparent !important;
}

/* Ensure all text is readable */
p, span, div, li {
    color: var(--text-primary) !important;
}

/* Interactive quiz styling */
.quiz-feedback {
    padding: 1rem;
    border-radius: 8px;
    margin: 1rem 0;
    border-left: 4px solid;
}

.quiz-feedback.correct {
    background: rgba(16, 185, 129, 0.1);
    border-color: #10b981;
    color: #10b981;
}

.quiz-feedback.incorrect {
    background: rgba(239, 68, 68, 0.1);
    border-color: #ef4444;
    color: #ef4444;
}
"""

# Buat interface Gradio dengan UI/UX minimalis
with gr.Blocks(title="SiPaling Paham - Asisten Belajar AI") as demo:
    
    # Header
    gr.HTML("""
        <div class="main-header">
            <h1>📚 SiPaling Paham</h1>
            <p class="tagline">Asisten Belajar AI yang Bikin Materi Kuliah Jadi Gampang Dipahami</p>
        </div>
    """)
    
    with gr.Tabs() as tabs:
        # Tab 1: Analisis Materi
        with gr.Tab("📖 Analisis Materi", id=0):
            with gr.Row():
                with gr.Column(scale=1):
                    gr.Markdown("### Input Materi")
                    
                    file_input1 = gr.File(
                        label="Upload File (PDF, DOCX, TXT)",
                        file_types=[".pdf", ".docx", ".txt"]
                    )
                    
                    gr.Markdown("**atau**")
                    
                    text_input1 = gr.Textbox(
                        label="Paste Teks Materi",
                        placeholder="Tempelkan materi kuliah di sini...",
                        lines=6
                    )
                    
                    gr.Markdown("### Pengaturan")
                    
                    jenis_analisis = gr.Radio(
                        choices=[
                            ("Ringkasan", "ringkasan"),
                            ("Poin Penting", "poin_penting"),
                            ("Penjelasan Sederhana", "penjelasan_sederhana"),
                            ("Tanya Jawab", "qna")
                        ],
                        label="Jenis Analisis",
                        value="ringkasan"
                    )
                    
                    gaya_bahasa1 = gr.Radio(
                        choices=[
                            ("Formal & Akademis", "formal"),
                            ("Santai & Friendly", "santai"),
                            ("Sederhana & Mudah", "sederhana")
                        ],
                        label="Gaya Bahasa",
                        value="santai",
                        info="Pilih gaya penjelasan yang Anda suka"
                    )
                    
                    with gr.Row():
                        btn_analisis = gr.Button("🚀 Analisis", variant="primary", size="lg")
                        btn_clear1 = gr.Button("🗑️ Clear", size="lg", variant="secondary")
                
                with gr.Column(scale=1):
                    gr.Markdown("### Hasil Analisis")
                    
                    info_analisis = gr.Markdown("", elem_classes="info-badge")
                    
                    output_analisis = gr.HTML(
                        label="",
                        elem_classes="output-box"
                    )
                    
                    btn_export1 = gr.Button("💾 Export TXT", size="sm", variant="secondary")
                    download_file1 = gr.File(label="Download", visible=False)
            
            # Event handlers
            btn_analisis.click(
                fn=analisis_materi_fn,
                inputs=[file_input1, text_input1, jenis_analisis, gaya_bahasa1],
                outputs=[output_analisis, info_analisis]
            )
            
            btn_clear1.click(
                fn=lambda: ("", "", ""),
                outputs=[text_input1, output_analisis, info_analisis]
            )
            
            btn_export1.click(
                fn=lambda x: export_hasil(x, "analisis_materi"),
                inputs=output_analisis,
                outputs=download_file1
            )
        
        # Tab 2: Perbandingan Materi
        with gr.Tab("⚖️ Bandingkan Materi", id=1):
            gr.Markdown("### Bandingkan Dua Materi")
            
            gaya_bahasa2 = gr.Radio(
                choices=[
                    ("Formal & Akademis", "formal"),
                    ("Santai & Friendly", "santai"),
                    ("Sederhana & Mudah", "sederhana")
                ],
                label="Gaya Bahasa",
                value="santai"
            )
            
            with gr.Row():
                with gr.Column():
                    gr.Markdown("#### Materi Pertama")
                    file_input2 = gr.File(label="Upload File", file_types=[".pdf", ".docx", ".txt"])
                    text_input2 = gr.Textbox(label="Atau Paste Teks", placeholder="Materi pertama...", lines=8)
                
                with gr.Column():
                    gr.Markdown("#### Materi Kedua")
                    file_input3 = gr.File(label="Upload File", file_types=[".pdf", ".docx", ".txt"])
                    text_input3 = gr.Textbox(label="Atau Paste Teks", placeholder="Materi kedua...", lines=8)
            
            with gr.Row():
                btn_bandingkan = gr.Button("⚖️ Bandingkan", variant="primary", size="lg")
                btn_clear2 = gr.Button("🗑️ Clear", size="lg", variant="secondary")
            
            info_bandingkan = gr.Markdown("", elem_classes="info-badge")
            
            output_bandingkan = gr.HTML(
                label="Hasil Perbandingan",
                elem_classes="output-box"
            )
            
            btn_export2 = gr.Button("💾 Export TXT", size="sm", variant="secondary")
            download_file2 = gr.File(label="Download", visible=False)
            
            # Event handlers
            btn_bandingkan.click(
                fn=bandingkan_materi_fn,
                inputs=[file_input2, text_input2, file_input3, text_input3, gaya_bahasa2],
                outputs=[output_bandingkan, info_bandingkan]
            )
            
            btn_clear2.click(
                fn=lambda: ("", "", "", ""),
                outputs=[text_input2, text_input3, output_bandingkan, info_bandingkan]
            )
            
            btn_export2.click(
                fn=lambda x: export_hasil(x, "perbandingan_materi"),
                inputs=output_bandingkan,
                outputs=download_file2
            )
        
        # Tab 3: Generator Latihan Soal - Interactive
        with gr.Tab("✍️ Generator Soal", id=2):
            gr.Markdown("### Generator Soal Interaktif")
            
            with gr.Row():
                with gr.Column(scale=1):
                    gr.Markdown("### Input Materi")
                    
                    file_input4 = gr.File(label="Upload File", file_types=[".pdf", ".docx", ".txt"])
                    text_input4 = gr.Textbox(label="Atau Paste Teks", placeholder="Materi untuk soal latihan...", lines=6)
                    
                    gr.Markdown("### Konfigurasi")
                    
                    jumlah_soal = gr.Slider(
                        minimum=3,
                        maximum=20,
                        value=5,
                        step=1,
                        label="Jumlah Soal"
                    )
                    
                    tingkat_soal = gr.Radio(
                        choices=[
                            ("Mudah", "mudah"),
                            ("Menengah", "menengah"),
                            ("Sulit", "sulit")
                        ],
                        label="Tingkat Kesulitan",
                        value="menengah"
                    )
                    
                    gaya_bahasa3 = gr.Radio(
                        choices=[
                            ("Formal & Akademis", "formal"),
                            ("Santai & Friendly", "santai"),
                            ("Sederhana & Mudah", "sederhana")
                        ],
                        label="Gaya Bahasa",
                        value="formal"
                    )
                    
                    mode_soal = gr.Radio(
                        choices=[
                            ("Generate Semua", "all"),
                            ("Satu per Satu (Interaktif)", "interactive")
                        ],
                        label="Mode Soal",
                        value="all",
                        info="Mode interaktif untuk latihan step-by-step"
                    )
                    
                    with gr.Row():
                        btn_soal = gr.Button("✨ Generate Soal", variant="primary", size="lg")
                        btn_clear3 = gr.Button("🗑️ Clear", size="lg", variant="secondary")
                
                with gr.Column(scale=1):
                    gr.Markdown("### Latihan Soal")
                    
                    info_soal = gr.Markdown("", elem_classes="info-badge")
                    
                    output_soal = gr.HTML(
                        label="",
                        elem_classes="output-box"
                    )
                    
                    # Interactive controls (shown only in interactive mode)
                    with gr.Row(visible=False) as interactive_controls:
                        with gr.Column(scale=2):
                            jawaban_user = gr.Radio(
                                choices=["A", "B", "C", "D"],
                                label="Pilih Jawaban Anda",
                                value=None
                            )
                        with gr.Column(scale=1):
                            btn_submit_jawaban = gr.Button("✓ Submit Jawaban", variant="primary")
                            btn_next_soal = gr.Button("→ Soal Berikutnya", variant="secondary")
                    
                    score_display = gr.Markdown("", visible=False)
                    
                    with gr.Row():
                        btn_export3 = gr.Button("💾 Export TXT", size="sm", variant="secondary")
                        download_file3 = gr.File(label="Download", visible=False)
            
            # State untuk interactive mode
            soal_state = gr.State([])
            current_index = gr.State(0)
            user_answers = gr.State([])
            
            # Toggle interactive controls visibility
            def toggle_mode(mode):
                return gr.update(visible=(mode == "interactive"))
            
            mode_soal.change(
                fn=toggle_mode,
                inputs=mode_soal,
                outputs=interactive_controls
            )
            
            # Event handlers
            btn_soal.click(
                fn=buat_soal_fn,
                inputs=[file_input4, text_input4, jumlah_soal, tingkat_soal, gaya_bahasa3],
                outputs=[output_soal, info_soal]
            )
            
            btn_clear3.click(
                fn=lambda: ("", "", ""),
                outputs=[text_input4, output_soal, info_soal]
            )
            
            btn_export3.click(
                fn=lambda x: export_hasil(x, "latihan_soal"),
                inputs=output_soal,
                outputs=download_file3
            )
        
        # Tab 4: Chat AI Assistant
        with gr.Tab("💬 Chat Assistant", id=3):
            gr.Markdown("### Tanya Jawab dengan AI")
            
            gaya_bahasa_chat = gr.Radio(
                choices=[
                    ("Formal & Akademis", "formal"),
                    ("Santai & Friendly", "santai"),
                    ("Sederhana & Mudah", "sederhana")
                ],
                label="Gaya Bahasa",
                value="santai",
                info="Atur gaya komunikasi AI"
            )
            
            chatbot = gr.Chatbot(
                label="Percakapan",
                height=450
            )
            
            with gr.Row():
                msg_input = gr.Textbox(
                    label="",
                    placeholder="Ketik pertanyaan... (contoh: Jelaskan apa itu machine learning dengan analogi)",
                    show_label=False,
                    scale=4
                )
                send_btn = gr.Button("📤 Kirim", scale=1, variant="primary")
            
            clear_chat_btn = gr.Button("🗑️ Clear Chat", variant="secondary")
            
            gr.Markdown("""
            **Contoh pertanyaan:**
            - Jelaskan konsep inheritance dalam OOP dengan analogi
            - Apa perbedaan supervised dan unsupervised learning?
            - Bagaimana cara kerja algoritma bubble sort step by step?
            - Buatkan analogi sederhana untuk konsep rekursi
            """)
            
            # Chat handlers
            send_btn.click(
                fn=chat_fn,
                inputs=[msg_input, chatbot, gaya_bahasa_chat],
                outputs=[chatbot, msg_input]
            )
            
            msg_input.submit(
                fn=chat_fn,
                inputs=[msg_input, chatbot, gaya_bahasa_chat],
                outputs=[chatbot, msg_input]
            )
            
            clear_chat_btn.click(
                fn=lambda: ([], ""),
                outputs=[chatbot, msg_input]
            )
        
        # Tab 5: Panduan
        with gr.Tab("ℹ️ Panduan", id=4):
            with gr.Row():
                with gr.Column():
                    gr.Markdown("""
                    ## Fitur Utama
                    
                    ### 📖 Analisis Materi
                    - **Ringkasan**: Overview lengkap materi
                    - **Poin Penting**: Ekstrak konsep kunci
                    - **Penjelasan Sederhana**: Untuk materi kompleks
                    - **Tanya Jawab**: Generate Q&A untuk review
                    
                    ### ⚖️ Perbandingan
                    Bandingkan 2 materi berbeda dan lihat:
                    - Persamaan dan perbedaan
                    - Kelebihan masing-masing
                    - Rekomendasi penggunaan
                    
                    ### ✍️ Generator Soal
                    - 3-20 soal pilihan ganda
                    - 3 tingkat kesulitan
                    - Lengkap dengan penjelasan
                    
                    ### 💬 Chat Assistant
                    Tanya jawab interaktif:
                    - Diskusi konsep
                    - Minta penjelasan tambahan
                    - Request analogi dan contoh
                    """)
                
                with gr.Column():
                    gr.Markdown("""
                    ## Cara Pakai
                    
                    ### Step 1: Input
                    - Upload file (PDF/DOCX/TXT), atau
                    - Copy-paste teks langsung
                    - Minimal 50 karakter
                    
                    ### Step 2: Pilih Gaya
                    - **Formal**: Bahasa akademis profesional
                    - **Santai**: Friendly tapi tetap informatif
                    - **Sederhana**: Super mudah dipahami
                    
                    ### Step 3: Proses
                    - Klik tombol process
                    - Tunggu 5-30 detik
                    - Lihat hasil
                    
                    ### Step 4: Export
                    - Export ke TXT jika perlu
                    - Simpan untuk belajar offline
                    
                    ## Tips
                    
                    ✅ **Materi terstruktur** → Hasil lebih baik
                    ✅ **Konteks lengkap** → Analisis lebih akurat
                    ✅ **Coba gaya berbeda** → Temukan yang cocok
                    ✅ **Gunakan chat** → Untuk klarifikasi
                    
                    ## Teknologi
                    
                    - AI: OpenAI GPT-4o-mini
                    - Framework: Gradio
                    - Processing: PyPDF2, python-docx
                    """)
            
            gr.Markdown("""
            ---
            <div style="text-align: center; padding: 1.5rem; background: linear-gradient(135deg, #6366f1, #4f46e5); border-radius: 12px; color: white; margin-top: 2rem;">
                <h3 style="margin: 0 0 0.5rem 0;">📚 SiPaling Paham</h3>
                <p style="margin: 0; opacity: 0.95;">Asisten Belajar AI untuk Mahasiswa Indonesia</p>
                <p style="margin: 0.5rem 0 0 0; font-size: 0.9rem; opacity: 0.85;">v2.0 • Minimalis • Dark Mode • Multi Gaya Bahasa</p>
            </div>
            """)
    
    # Footer minimalis
    gr.Markdown("""
    <div style="text-align: center; padding: 1rem; color: #94a3b8; margin-top: 2rem;">
        <p style="margin: 0;">Powered by OpenAI • Built with ❤️</p>
    </div>
    """)

# Jalankan aplikasi
if __name__ == "__main__":
    demo.launch(
        share=False,
        server_name="0.0.0.0",
        server_port=7860,
        css=custom_css
    )