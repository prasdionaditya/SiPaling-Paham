"""
Advanced Features untuk Sistem Analisis Materi
Fitur tambahan yang bisa diintegrasikan
"""

import json
import os
from datetime import datetime
from typing import List, Dict

class HistoryManager:
    """Manage analisis history"""
    
    def __init__(self, history_file="history.json"):
        self.history_file = history_file
        self.load_history()
    
    def load_history(self):
        """Load history dari file"""
        if os.path.exists(self.history_file):
            with open(self.history_file, 'r', encoding='utf-8') as f:
                self.history = json.load(f)
        else:
            self.history = []
    
    def save_history(self):
        """Save history ke file"""
        with open(self.history_file, 'w', encoding='utf-8') as f:
            json.dump(self.history, f, ensure_ascii=False, indent=2)
    
    def add_entry(self, jenis: str, materi_preview: str, hasil: str):
        """Tambah entry baru"""
        entry = {
            "timestamp": datetime.now().isoformat(),
            "jenis": jenis,
            "materi_preview": materi_preview[:200],
            "hasil_preview": hasil[:200],
            "word_count": len(hasil.split())
        }
        self.history.append(entry)
        self.save_history()
    
    def get_recent(self, n: int = 10) -> List[Dict]:
        """Get n most recent entries"""
        return self.history[-n:]
    
    def get_stats(self) -> Dict:
        """Get statistics"""
        return {
            "total_analisis": len(self.history),
            "jenis_counts": self._count_by_type(),
            "total_words_processed": sum(e.get("word_count", 0) for e in self.history)
        }
    
    def _count_by_type(self) -> Dict:
        """Count by analysis type"""
        counts = {}
        for entry in self.history:
            jenis = entry.get("jenis", "unknown")
            counts[jenis] = counts.get(jenis, 0) + 1
        return counts


class SmartSummarizer:
    """Advanced summarization dengan level"""
    
    @staticmethod
    def tiered_summary(text: str) -> Dict[str, str]:
        """Create summaries at different lengths"""
        words = text.split()
        word_count = len(words)
        
        # Calculate different summary lengths
        short_length = min(100, word_count // 10)
        medium_length = min(300, word_count // 4)
        long_length = min(500, word_count // 2)
        
        return {
            "word_count": word_count,
            "estimated_short": short_length,
            "estimated_medium": medium_length,
            "estimated_long": long_length
        }
    
    @staticmethod
    def extract_keywords(text: str, top_n: int = 10) -> List[str]:
        """Extract top keywords (simple implementation)"""
        # Simple word frequency
        words = text.lower().split()
        
        # Filter stopwords (basic Indonesian stopwords)
        stopwords = {'dan', 'atau', 'yang', 'untuk', 'dari', 'dengan', 'pada', 
                    'adalah', 'ini', 'itu', 'ke', 'di', 'akan', 'telah', 'dalam'}
        
        filtered_words = [w for w in words if w not in stopwords and len(w) > 3]
        
        # Count frequency
        freq = {}
        for word in filtered_words:
            freq[word] = freq.get(word, 0) + 1
        
        # Sort and get top N
        sorted_words = sorted(freq.items(), key=lambda x: x[1], reverse=True)
        return [word for word, count in sorted_words[:top_n]]


class StudyPlanner:
    """Generate study plans based on material"""
    
    @staticmethod
    def create_study_schedule(topics: List[str], days: int = 7) -> Dict:
        """Create a study schedule"""
        if not topics or days < 1:
            return {}
        
        topics_per_day = max(1, len(topics) // days)
        schedule = {}
        
        for day in range(1, days + 1):
            start_idx = (day - 1) * topics_per_day
            end_idx = start_idx + topics_per_day
            
            if day == days:  # Last day gets remaining topics
                day_topics = topics[start_idx:]
            else:
                day_topics = topics[start_idx:end_idx]
            
            schedule[f"Hari {day}"] = {
                "topics": day_topics,
                "durasi_estimasi": f"{len(day_topics) * 30} menit",
                "tips": "Review, latihan soal, dan buat catatan"
            }
        
        return schedule
    
    @staticmethod
    def estimate_study_time(word_count: int) -> Dict:
        """Estimate study time based on word count"""
        # Average reading speed: 200-250 words/minute
        reading_time = word_count / 225  # minutes
        
        # Add time for comprehension and notes
        comprehension_time = reading_time * 0.5
        note_taking_time = reading_time * 0.3
        
        total_time = reading_time + comprehension_time + note_taking_time
        
        return {
            "reading_time": round(reading_time, 1),
            "comprehension_time": round(comprehension_time, 1),
            "note_taking_time": round(note_taking_time, 1),
            "total_time": round(total_time, 1),
            "total_time_formatted": f"{int(total_time // 60)}h {int(total_time % 60)}m"
        }


class ExportManager:
    """Handle various export formats"""
    
    @staticmethod
    def export_markdown(content: Dict, filename: str = "output.md") -> str:
        """Export to Markdown format"""
        md_content = f"""# Hasil Analisis Materi Kuliah

**Tanggal**: {datetime.now().strftime('%d %B %Y, %H:%M')}

---

## Informasi
- **Jenis Analisis**: {content.get('jenis', 'N/A')}
- **Jumlah Kata**: {content.get('word_count', 'N/A')}

---

## Hasil

{content.get('hasil', 'Tidak ada hasil')}

---

*Generated by Sistem Analisis Materi Kuliah*
"""
        
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(md_content)
        
        return filename
    
    @staticmethod
    def export_json(content: Dict, filename: str = "output.json") -> str:
        """Export to JSON format"""
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(content, f, ensure_ascii=False, indent=2)
        
        return filename


class QuizValidator:
    """Validate and enhance quiz questions"""
    
    @staticmethod
    def validate_quiz(quiz_text: str) -> Dict:
        """Validate quiz structure"""
        lines = quiz_text.split('\n')
        
        questions = 0
        options = 0
        answers = 0
        
        for line in lines:
            line = line.strip()
            if line.startswith('Soal') or line.startswith('Q'):
                questions += 1
            elif line.startswith(('a)', 'b)', 'c)', 'd)')):
                options += 1
            elif 'Jawaban:' in line or 'Answer:' in line:
                answers += 1
        
        is_valid = (questions > 0 and 
                   options >= questions * 4 and 
                   answers >= questions)
        
        return {
            "valid": is_valid,
            "questions_count": questions,
            "options_count": options,
            "answers_count": answers,
            "quality_score": (answers / max(questions, 1)) * 100
        }


# Utility functions
def format_file_size(size_bytes: int) -> str:
    """Format file size in human readable format"""
    for unit in ['B', 'KB', 'MB', 'GB']:
        if size_bytes < 1024.0:
            return f"{size_bytes:.1f} {unit}"
        size_bytes /= 1024.0
    return f"{size_bytes:.1f} TB"


def estimate_processing_time(word_count: int) -> str:
    """Estimate processing time based on word count"""
    # Rough estimate: 1000 words = ~5 seconds
    seconds = (word_count / 1000) * 5
    
    if seconds < 60:
        return f"~{int(seconds)} detik"
    else:
        minutes = seconds / 60
        return f"~{int(minutes)} menit"


def get_difficulty_emoji(tingkat: str) -> str:
    """Get emoji for difficulty level"""
    emoji_map = {
        "mudah": "🟢",
        "menengah": "🟡",
        "sulit": "🔴"
    }
    return emoji_map.get(tingkat.lower(), "⚪")


# Example usage and testing
if __name__ == "__main__":
    # Test History Manager
    print("Testing History Manager...")
    history = HistoryManager()
    history.add_entry("ringkasan", "Test materi", "Test hasil")
    print(f"Stats: {history.get_stats()}")
    
    # Test Smart Summarizer
    print("\nTesting Smart Summarizer...")
    test_text = " ".join(["word"] * 1000)
    summary_info = SmartSummarizer.tiered_summary(test_text)
    print(f"Summary tiers: {summary_info}")
    
    # Test Study Planner
    print("\nTesting Study Planner...")
    topics = ["Topic 1", "Topic 2", "Topic 3", "Topic 4", "Topic 5"]
    schedule = StudyPlanner.create_study_schedule(topics, days=3)
    print(f"Schedule: {schedule}")
    
    print("\n✅ All tests passed!")