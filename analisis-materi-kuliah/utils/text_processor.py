import PyPDF2
import docx
import io

class TextProcessor:
    @staticmethod
    def extract_from_pdf(file_obj):
        """
        Ekstrak teks dari file PDF
        """
        try:
            pdf_reader = PyPDF2.PdfReader(file_obj)
            text = ""
            for page in pdf_reader.pages:
                text += page.extract_text() + "\n"
            return text.strip()
        except Exception as e:
            return f"Error membaca PDF: {str(e)}"
    
    @staticmethod
    def extract_from_docx(file_obj):
        """
        Ekstrak teks dari file DOCX
        """
        try:
            doc = docx.Document(file_obj)
            text = ""
            for paragraph in doc.paragraphs:
                text += paragraph.text + "\n"
            return text.strip()
        except Exception as e:
            return f"Error membaca DOCX: {str(e)}"
    
    @staticmethod
    def extract_from_txt(file_obj):
        """
        Ekstrak teks dari file TXT
        """
        try:
            content = file_obj.read()
            if isinstance(content, bytes):
                return content.decode('utf-8')
            return content
        except Exception as e:
            return f"Error membaca TXT: {str(e)}"
    
    @staticmethod
    def process_file(file):
        """
        Proses file berdasarkan ekstensinya
        """
        if file is None:
            return ""
        
        file_name = file.name
        
        if file_name.endswith('.pdf'):
            return TextProcessor.extract_from_pdf(file)
        elif file_name.endswith('.docx'):
            return TextProcessor.extract_from_docx(file)
        elif file_name.endswith('.txt'):
            return TextProcessor.extract_from_txt(file)
        else:
            return "Format file tidak didukung. Gunakan PDF, DOCX, atau TXT."
    
    @staticmethod
    def validate_text(text, min_length=50):
        """
        Validasi teks input
        """
        if not text or len(text.strip()) < min_length:
            return False, f"Teks terlalu pendek. Minimal {min_length} karakter."
        return True, "Teks valid"
    
    @staticmethod
    def chunk_text(text, max_chunk_size=10000):
        """
        Memecah teks panjang menjadi chunks
        Berguna untuk materi yang sangat panjang
        """
        words = text.split()
        chunks = []
        current_chunk = []
        current_length = 0
        
        for word in words:
            current_length += len(word) + 1
            if current_length > max_chunk_size:
                chunks.append(" ".join(current_chunk))
                current_chunk = [word]
                current_length = len(word)
            else:
                current_chunk.append(word)
        
        if current_chunk:
            chunks.append(" ".join(current_chunk))
        
        return chunks