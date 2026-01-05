import os
from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables
load_dotenv()

print("=" * 60)
print("CEK KONFIGURASI OPENAI API KEY")
print("=" * 60)

# Cek apakah .env file ada
if os.path.exists('.env'):
    print("✅ File .env ditemukan")
else:
    print("❌ File .env TIDAK ditemukan!")
    print("   Buat file .env di root project")
    exit()

# Cek API key
api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    print("❌ OPENAI_API_KEY tidak ditemukan di .env")
    print("\nCara memperbaiki:")
    print("1. Buka file .env")
    print("2. Tambahkan baris: OPENAI_API_KEY=sk-proj-your-key-here")
    print("3. Simpan file")
    print("\nDapatkan API key di: https://platform.openai.com/api-keys")
    exit()

print(f"✅ API Key ditemukan: {api_key[:20]}...{api_key[-4:]}")

# Test koneksi ke API
print("\n" + "=" * 60)
print("TEST KONEKSI KE OPENAI API")
print("=" * 60)

try:
    client = OpenAI(api_key=api_key)
    
    print("⏳ Mengirim test request...")
    
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "Anda adalah asisten yang helpful."},
            {"role": "user", "content": "Halo, respond dengan 'API key valid!' dalam Bahasa Indonesia"}
        ],
        max_tokens=50
    )
    
    response_text = response.choices[0].message.content
    
    print("✅ KONEKSI BERHASIL!")
    print(f"Response dari OpenAI: {response_text}")
    print(f"Model yang digunakan: {response.model}")
    print(f"Tokens used: {response.usage.total_tokens}")
    print("\n🎉 API key Anda valid dan siap digunakan!")
    
    # Info tambahan
    print("\n" + "=" * 60)
    print("INFORMASI MODEL YANG TERSEDIA")
    print("=" * 60)
    print("Model yang bisa digunakan:")
    print("1. gpt-4o-mini       - Murah, cepat, bagus untuk sebagian besar task")
    print("2. gpt-4o            - Paling pintar, lebih mahal")
    print("3. gpt-3.5-turbo     - Lebih murah, cukup bagus")
    print("\nModel saat ini: gpt-4o-mini (sudah optimal)")
    
except Exception as e:
    print(f"❌ KONEKSI GAGAL!")
    print(f"Error: {str(e)}")
    print("\nKemungkinan masalah:")
    print("1. API key tidak valid")
    print("2. API key belum diaktifkan")
    print("3. Tidak ada credit di akun OpenAI")
    print("4. Tidak ada koneksi internet")
    print("\nSolusi:")
    print("- Periksa kembali API key di https://platform.openai.com/api-keys")
    print("- Pastikan ada credit di https://platform.openai.com/account/billing")
    print("- Generate API key baru jika perlu")
    print("- Pastikan ada koneksi internet")

print("\n" + "=" * 60)