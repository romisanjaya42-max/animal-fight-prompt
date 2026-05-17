import streamlit as st
import random
from datetime import datetime


# ==================== KONFIGURASI MUDAH DIUBAH ====================
ACCESS_KEY = "SOFYAN2026"
DURASI_JAM = 24

st.set_page_config(page_title="🐾 Animal Fight Prompt Generator", page_icon="🐾", layout="wide")

# ==================== CUSTOM CSS (LEBIH KEREN) ====================
st.markdown("""
<style>
    .main-title {
        font-size: 3.2rem;
        font-weight: 900;
        text-align: center;
        background: linear-gradient(90deg, #FF6B35, #F7931E, #FF6B35);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 0.3rem;
    }
    .subtitle {
        text-align: center;
        font-size: 1.25rem;
        color: #444;
        margin-bottom: 2rem;
    }
    .stButton>button {
        background: linear-gradient(90deg, #FF6B35, #F7931E);
        color: white;
        font-weight: bold;
        border: none;
        padding: 0.9rem 2.5rem;
        border-radius: 50px;
        font-size: 1.15rem;
        transition: all 0.3s ease;
    }
    .stButton>button:hover {
        transform: translateY(-3px);
        box-shadow: 0 15px 25px rgba(255, 107, 53, 0.4);
    }
    .section-header {
        font-size: 1.4rem;
        font-weight: 700;
        color: #FF6B35;
        margin-bottom: 0.8rem;
    }
    .prompt-box {
        background: #f8f9fa;
        border-left: 8px solid #FF6B35;
        padding: 1.8rem;
        border-radius: 12px;
        font-family: 'Courier New', monospace;
        font-size: 0.95rem;
        line-height: 1.7;
        box-shadow: 0 4px 15px rgba(0,0,0,0.08);
    }
    .success-box {
        background: linear-gradient(90deg, #d4edda, #c3e6cb);
        padding: 1rem;
        border-radius: 10px;
        border-left: 6px solid #28a745;
    }
</style>
""", unsafe_allow_html=True)

# ==================== DATA ====================
ANIMALS_WORLD = [
    "Singa", "Harimau Sumatra", "Gajah Afrika", "Komodo", "Orca", "Hiu Putih Besar",
    "Beruang Grizzly", "Beruang Kutub", "Anaconda Hijau", "Elang Botak", "Serigala Abu-abu",
    "Kuda Nil", "Badak Putih", "Macan Tutul", "Buaya Nil", "Ular Kobra Raja", "Gorila Gunung",
    "Simpanse", "Zebra", "Jerapah", "Bison Amerika", "Moose", "Penguin Kaisar", "Paus Biru",
    "Hiu Martil", "Ikan Pari Manta", "Elang Harpy", "Harimau Siberia", "Singa Gunung",
    "Wolverine", "Tasmanian Devil", "Kanguru Merah", "Koala", "Panda Raksasa", "Cheetah",
    "Leopard Salju", "Hyena", "Baboon", "Mandril", "Okapi", "Tapir", "Sloth", "Armadillo",
    "Capybara", "Piranha", "Electric Eel", "Alligator Amerika", "Python Burma",
    "T-Rex", "Velociraptor", "Spinosaurus", "Triceratops", "Mammoth", "Saber-Tooth Tiger",
    "Giant Squid", "Megalodon", "Saltwater Crocodile", "Honey Badger", "Cassowary",
    "Ostrich", "Emu", "Red Kangaroo", "Platypus", "Echidna", "Blue Whale", "Hammerhead Shark"
]

FANTASY_CREATURES = [
    "Naga Api", "Phoenix", "Griffin", "Unicorn", "Werewolf", "Minotaur",
    "Hydra", "Pegasus", "Dragon Turtle", "Chimera", "Basilisk", "Wyvern",
    "Kraken", "Leviathan", "Cerberus", "Sphinx", "Manticore", "Roc",
    "Thunderbird", "Fenrir", "Jörmungandr", "Bahamut"
]

HABITATS = [
    "Savana Afrika yang panas", "Hutan Hujan Amazon yang lebat", "Gunung Himalaya yang dingin",
    "Laut Dalam Pasifik yang gelap", "Gurun Sahara yang terik", "Hutan Boreal Kanada",
    "Sungai Amazon yang deras", "Padang Rumput Serengeti", "Kutub Utara yang beku",
    "Hutan Tropis Indonesia", "Gunung Berapi Aktif", "Lembah Sungai Nil", "Kawah Vulkanik",
    "Hutan Bambu Cina", "Padang Es Antartika"
]

# ==================== ACCESS CONTROL ====================
if "access_granted" not in st.session_state:
    st.session_state.access_granted = False
    st.session_state.access_time = None

if not st.session_state.access_granted:
    st.title("🔐 Animal Fight Prompt Generator")
    key_input = st.text_input("Access Key", type="password")
    if st.button("Masuk"):
        if key_input == ACCESS_KEY:
            st.session_state.access_granted = True
            st.session_state.access_time = datetime.now()
            st.rerun()
        else:
            st.error("❌ Access Key salah!")
            st.info("📌 Jika tidak memiliki akses, hubungi admin di Telegram: https://t.me/Furaney")
    st.stop()

if st.session_state.access_time:
    if (datetime.now() - st.session_state.access_time).total_seconds() > DURASI_JAM * 3600:
        st.error(f"⏰ Akses kadaluarsa ({DURASI_JAM} jam)")
        st.info("📌 Jika tidak memiliki akses, hubungi admin di Telegram: https://t.me/Furaney")
        st.stop()

# ==================== MAIN APP ====================
st.markdown('<h1 class="main-title">🐾 ANIMAL FIGHT PROMPT GENERATOR</h1>', unsafe_allow_html=True)
st.markdown('<p class="by-sofyan">By SOFYAN • https://facebook.com/yankees.romi</p>', unsafe_allow_html=True)

with st.sidebar:
    st.success(f"✅ Akses aktif ({DURASI_JAM} jam)")
    if st.button("🔄 Reset Akses"):
        st.session_state.access_granted = False
        st.rerun()

# ==================== SIDEBAR ====================
with st.sidebar:
    st.header("⚙️ Pengaturan Cepat")
    
    if st.button("🔥 Pilih Pertarungan Acak", use_container_width=True):
        if random.choice([True, False]):
            hewan1 = random.choice(ANIMALS_WORLD)
            hewan2 = random.choice(ANIMALS_WORLD)
        else:
            hewan1 = random.choice(FANTASY_CREATURES)
            hewan2 = random.choice(ANIMALS_WORLD)
        st.session_state.random_hewan1 = hewan1
        st.session_state.random_hewan2 = hewan2
        st.rerun()

# ==================== MODE SELECTION ====================
st.subheader("🎯 Pilih Mode Pertarungan")

mode = st.radio(
    "",
    ["🦁 Real Animal vs Real Animal",
     "🦄 Fantasy Creature vs Real Animal",
     "🐉 Fantasy vs Fantasy"],
    horizontal=True
)

# ==================== INPUT SECTION ====================
col1, col2 = st.columns(2)
with col1:
    if "Fantasy" in mode:
        attacker = st.selectbox("Penyerang", FANTASY_CREATURES, key="attacker_fantasy")
    else:
        attacker = st.selectbox("Penyerang", ANIMALS_WORLD, key="attacker_real")
    attacker = st.text_input("Custom Penyerang", key="custom_attacker") or attacker

with col2:
    if "Fantasy vs Fantasy" in mode:
        defender = st.selectbox("Lawan", FANTASY_CREATURES, key="defender_fantasy")
    else:
        defender = st.selectbox("Lawan", ANIMALS_WORLD, key="defender_real")
    defender = st.text_input("Custom Lawan", key="custom_defender") or defender

habitat = st.selectbox("🌍 Habitat", HABITATS, key="habitat")
habitat = st.text_input("Custom Habitat", key="custom_habitat") or habitat

# Prompt Type
st.subheader("📝 Jenis Prompt")
prompt_type = st.radio(
    "",
    ["🖼️ Image Prompt (Midjourney / Flux / Grok Imagine)",
     "🎥 Video Prompt (Kling AI / Runway / Luma / Pika)",
     "📖 Battle Analysis (ChatGPT / Claude)",
     "🔥 All-in-One (Semua Sekaligus)"],
    horizontal=True
)

# Generate Button
st.divider()
if st.button("🚀 GENERATE PROMPT SEKARANG", use_container_width=True, type="primary"):
    now = datetime.now().strftime("%Y-%m-%d %H:%M")

   # Slider durasi (dengan indentasi yang benar)
if "Video" in prompt_type or "Leonardo" in prompt_type or "All-in-One" in prompt_type:
    durasi = st.slider("Durasi Video (detik)", 5, 20, 12, key="durasi")

    
    if "Fantasy" in mode:
        title = f"{attacker} vs {defender}"
    else:
        title = f"{attacker} vs {defender}"
    
    base = f"""Masterpiece epic battle between {attacker} and {defender} in the {habitat}."""

    if "Image Prompt" in prompt_type:
        prompt = f"""{base}
Hyper-realistic, cinematic lighting, intense action, flying debris, dramatic {habitat} atmosphere, ultra detailed scales/fur/feathers, National Geographic quality, 8K, photorealistic, dynamic angle --ar 16:9 --stylize 250 --v 6"""
    
    elif "Video Prompt" in prompt_type:
        prompt = f"""{base}
Create a 12-second ultra cinematic video. Start with wide shot, slow orbiting camera, intense slow-motion clash, dramatic music swell, dust and fire particles, emotional close-ups on eyes and claws. Hyper-realistic 8K, National Geographic style. --ar 16:9 --motion high"""
    
    elif "Battle Analysis" in prompt_type:
        prompt = f"""Buat analisis lengkap dan dramatis pertarungan antara {attacker} vs {defender} di {habitat}.
Jelaskan kekuatan, strategi, kelemahan, dan prediksi pemenang dengan gaya narasi epik seperti film dokumenter."""
    
    else:  # All-in-One (Versi Sempurna)
    prompt = f"""=== ALL-IN-ONE PROMPT PACK ===

🖼️ IMAGE PROMPT (Midjourney / Flux / Grok Imagine):
{base}
Hyper-realistic 8K, cinematic lighting, intense action, dramatic atmosphere, ultra detailed, National Geographic quality --ar 16:9 --stylize 250 --v 6

🎥 VIDEO PROMPT (Kling AI / Runway / Luma / Pika):
{base}
{durasi}-second ultra cinematic video. Start with wide establishing shot, slow orbiting camera, intense slow-motion clash, dramatic music swell, dust & particles, emotional close-ups. Hyper-realistic 8K, National Geographic wildlife cinematography. --ar 16:9 --motion high

🎨 LEONARDO AI PROMPT:
{base}
Highly detailed digital art, epic fantasy style, dramatic volumetric lighting, ultra realistic textures, best quality, masterpiece, 8K resolution --ar 16:9 --stylize {durasi}

📖 BATTLE ANALYSIS (ChatGPT / Claude):
Buat analisis lengkap dan dramatis pertarungan antara {attacker} vs {defender} di habitat {habitat}.
Jelaskan:
1. Perbandingan kekuatan & kelemahan
2. Strategi bertarung yang mungkin digunakan
3. Simulasi pertarungan langkah demi langkah
4. Prediksi pemenang beserta alasan ilmiah + faktor keberuntungan

Gunakan gaya narasi epik seperti film dokumenter hewan liar."""
    
    st.session_state.generated_prompt = prompt
    st.session_state.title = title

# Display result
if "generated_prompt" in st.session_state:
    st.success(f"✅ Prompt untuk: {st.session_state.title}")
    
    st.markdown(f"""
    <div class="prompt-box">
    {st.session_state.generated_prompt.replace(chr(10), '<br>')}
    </div>
    """, unsafe_allow_html=True)
    
    col_btn1, col_btn2 = st.columns(2)
    
    with col_btn1:
        if st.button("📋 Copy Prompt", use_container_width=True):
            st.toast("Prompt berhasil di-copy!")
    
    with col_btn2:
        if st.button("🎬 Buka Kling AI + Paste", use_container_width=True):
            st.markdown("[Klik di sini untuk buka Leonardo AI](https://app.leonardo.ai/)")
            st.info("Setelah leonardo AI terbuka, tekan Ctrl+V untuk paste prompt otomatis.")

st.caption("By SOFYAN • https://facebook.com/yankees.romi • v3.1 • 2026")

