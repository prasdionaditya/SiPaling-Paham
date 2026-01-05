import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

class LLMHandler:
    def __init__(self):
        self.client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
        # Gunakan GPT-4 atau GPT-3.5-turbo tergantung kebutuhan
        self.model = "gpt-4o-mini"  # Lebih murah, atau gunakan "gpt-4o" untuk hasil terbaik
    
    def analisis_materi(self, teks_materi, jenis_analisis="ringkasan", gaya_bahasa="santai"):
        """
        Menganalisis materi kuliah berdasarkan jenis analisis yang dipilih
        
        Args:
            teks_materi: Teks materi kuliah yang akan dianalisis
            jenis_analisis: Jenis analisis (ringkasan, poin_penting, penjelasan_sederhana, qna)
            gaya_bahasa: Gaya bahasa (formal, santai, sederhana)
        
        Returns:
            Hasil analisis dalam bentuk teks
        """
        
        # System prompts berdasarkan gaya bahasa
        system_prompts = {
            "formal": "Anda adalah asisten AI akademis profesional. Gunakan bahasa formal, terstruktur, dan istilah akademis yang tepat. Berikan penjelasan yang presisi dan komprehensif.",
            "santai": "Anda adalah tutor friendly yang asik. Gunakan bahasa santai tapi tetap informatif, seperti kakak tingkat yang enak diajak ngobrol. Tetap jelas dan tidak mengurangi kualitas penjelasan.",
            "sederhana": "Anda adalah guru yang jago bikin materi kompleks jadi super gampang. Gunakan bahasa sehari-hari, banyak analogi dan contoh konkret. Hindari jargon ribet, atau kalau terpaksa pakai, jelaskan dengan bahasa simple."
        }
        
        system_prompt = system_prompts.get(gaya_bahasa, system_prompts["santai"])
        
        prompts = {
            "ringkasan": """Buatkan ringkasan komprehensif dari materi kuliah berikut dalam Bahasa Indonesia.
            Struktur ringkasan:
            1. Konsep Utama
            2. Poin-poin Penting
            3. Kesimpulan
            
            Materi:
            {materi}""",
            
            "poin_penting": """Ekstrak poin-poin penting dari materi kuliah berikut dalam format bullet points.
            Fokus pada:
            - Definisi kunci
            - Konsep fundamental
            - Rumus atau prinsip penting
            - Contoh aplikasi
            
            Materi:
            {materi}""",
            
            "penjelasan_sederhana": """Sederhanakan materi kuliah berikut menjadi penjelasan yang mudah dipahami.
            Gunakan:
            - Bahasa sehari-hari
            - Analogi dan contoh konkret
            - Penjelasan step-by-step untuk konsep kompleks
            - Hindari jargon tanpa penjelasan
            
            Materi:
            {materi}""",
            
            "qna": """Buatkan 10 pertanyaan dan jawaban berdasarkan materi kuliah berikut.
            Format:
            Q1: [Pertanyaan]
            A1: [Jawaban detail]
            
            Variasikan tingkat kesulitan dari dasar hingga lanjutan.
            
            Materi:
            {materi}"""
        }
        
        prompt = prompts.get(jenis_analisis, prompts["ringkasan"]).format(materi=teks_materi)
        
        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {
                        "role": "system",
                        "content": system_prompt
                    },
                    {
                        "role": "user",
                        "content": prompt
                    }
                ],
                temperature=0.7,
                max_tokens=4000
            )
            
            return response.choices[0].message.content
            
        except Exception as e:
            return f"Error dalam analisis: {str(e)}\n\nPastikan API key OpenAI Anda valid dan memiliki credit."
    
    def bandingkan_materi(self, materi1, materi2, gaya_bahasa="santai"):
        """
        Membandingkan dua materi kuliah
        """
        
        system_prompts = {
            "formal": "Anda adalah analis akademis profesional yang membandingkan materi dengan objektif dan terstruktur.",
            "santai": "Anda adalah reviewer yang asik dan insightful dalam membandingkan materi pembelajaran.",
            "sederhana": "Anda adalah pembanding yang jago jelaskan perbedaan dengan bahasa super simple dan banyak contoh."
        }
        
        system_prompt = system_prompts.get(gaya_bahasa, system_prompts["santai"])
        prompt = f"""Bandingkan dua materi kuliah berikut dalam Bahasa Indonesia:

        MATERI 1:
        {materi1}
        
        MATERI 2:
        {materi2}
        
        Berikan analisis perbandingan mencakup:
        1. Persamaan konsep
        2. Perbedaan pendekatan
        3. Kelebihan dan kekurangan masing-masing
        4. Rekomendasi penggunaan"""
        
        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {
                        "role": "system",
                        "content": system_prompt
                    },
                    {
                        "role": "user",
                        "content": prompt
                    }
                ],
                temperature=0.7,
                max_tokens=4000
            )
            
            return response.choices[0].message.content
            
        except Exception as e:
            return f"Error dalam perbandingan: {str(e)}\n\nPastikan API key OpenAI Anda valid dan memiliki credit."
    
    def buat_latihan_soal(self, teks_materi, jumlah_soal=5, tingkat="menengah", gaya_bahasa="formal"):
        """
        Membuat latihan soal berdasarkan materi
        """
        
        system_prompts = {
            "formal": "Anda adalah pembuat soal ujian profesional. Buat soal dengan bahasa formal dan akademis.",
            "santai": "Anda adalah guru yang bikin soal dengan bahasa friendly tapi tetap menantang.",
            "sederhana": "Anda adalah pembuat soal yang pakai bahasa super gampang dipahami tanpa mengurangi kualitas soal."
        }
        
        system_prompt = system_prompts.get(gaya_bahasa, system_prompts["formal"])
        prompt = f"""Buatkan {jumlah_soal} soal latihan tingkat {tingkat} berdasarkan materi berikut:

        {teks_materi}
        
        Format setiap soal:
        Soal [nomor]: [Pertanyaan]
        a) [Pilihan A]
        b) [Pilihan B]
        c) [Pilihan C]
        d) [Pilihan D]
        
        Jawaban: [Jawaban benar dengan penjelasan singkat]
        
        Pastikan soal menguji pemahaman konsep, bukan hanya hafalan.
        """
        
        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {
                        "role": "system",
                        "content": system_prompt
                    },
                    {
                        "role": "user",
                        "content": prompt
                    }
                ],
                temperature=0.8,
                max_tokens=4000
            )
            
            return response.choices[0].message.content
            
        except Exception as e:
            return f"Error dalam pembuatan soal: {str(e)}\n\nPastikan API key OpenAI Anda valid dan memiliki credit."