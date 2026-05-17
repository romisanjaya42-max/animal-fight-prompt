import streamlit as st
import random
from datetime import datetime, timedelta

# ==================== KONFIGURASI SUPER MUDAH DIUBAH (EDIT DI SINI SAJA) ====================
ACCESS_KEY = "SOFYAN2026"          # ← GANTI KEY DI SINI (bagikan ke user)
DURASI_JAM = 1                     # ← GANTI DURASI AKSES (dalam jam)

st.set_page_config(
    page_title="🐾 Animal Fight Prompt Generator",
    page_icon="🐾",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ==================== CUSTOM CSS ====================
st.markdown("""
<style>
    .main-title {
        font-size: 3rem;
        font-weight: 900;
        text-align: center;
        background: linear-gradient(90deg, #FF6B35, #F7931E);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }
    .subtitle {
        text-align: center;
        font-size: 1.1rem;
        color: #555;
    }
    .by-sofyan {
        text-align: center;
        font-size: 1rem;
        color: #FF6B35;
        font-weight: bold;
        margin-bottom: 1.5rem;
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

# ==================== ACCESS CONTROL (KEY + MASA AKTIF) ====================
if "access_granted" not in st.session_state:
    st.session_state.access_granted = False
    st.session_state.access_time = None

if not st.session_state.access_granted:
    st.title("🔐 Animal Fight Prompt Generator")
    st.subheader("Masukkan Access Key untuk Melanjutkan")
    
    key_input = st.text_input("Access Key", type="password", placeholder="Masukkan key yang diberikan")
    
    if st.button("Masuk"):
        if key_input == ACCESS_KEY:
            st.session_state.access_granted = True
            st.session_state.access_time = datetime.now()
            st.rerun()
        else:
            st.error("❌ Access Key salah! Hubungi admin untuk key baru.")
    
    st.stop()

# Cek masa aktif
if st.session_state.access_time:
    waktu_berlalu = datetime.now() - st.session_state.access_time
    if waktu_berlalu.total_seconds() > DURASI_JAM * 3600:
        st.error(f"⏰ Akses telah kadaluarsa ({DURASI_JAM} jam). Hubungi admin untuk key baru.")
        st.stop()

# ==================== MAIN APP ====================
st.markdown('<h1 class="main-title">🐾 ANIMAL FIGHT PROMPT GENERATOR</h1>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">Versi Web Streamlit • Image + Video + Analysis + Leonardo AI</p>', unsafe_allow_html=True)
st.markdown('<p class="by-sofyan">By SOFYAN • https://facebook.com/yankees.romi</p>', unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.header("⚙️ Pengaturan")
    st.success(f"✅ Akses aktif ({DURASI_JAM} jam)")
    st.caption(f"Key saat ini: {ACCESS_KEY}")
    
    if st.button("🔄 Reset Akses (Admin)"):
        st.session_state.access_granted = False
        st.rerun()

# Mode
st.subheader("🎯 Mode Pertarungan")
mode = st.radio("", ["🦁 Real vs Real", "🦄 Fantasy vs Real", "🐉 Fantasy vs Fantasy"], horizontal=True)

# Input Hewan + Custom
col1, col2 = st.columns(2)
with col1:
    st.markdown("### Penyerang")
    if "Fantasy" in mode:
        attacker = st.selectbox("Fantasy Creature", FANTASY_CREATURES)
    else:
        attacker = st.selectbox("Hewan", ANIMALS_WORLD)
    custom_attacker = st.text_input("Atau ketik nama custom", placeholder="Contoh: Megalodon Putih")
    if custom_attacker.strip():
        attacker = custom_attacker.strip()

with col2:
    st.markdown("### Lawan")
    if "Fantasy vs Fantasy" in mode:
        defender = st.selectbox("Fantasy Creature", FANTASY_CREATURES)
    else:
        defender = st.selectbox("Hewan", ANIMALS_WORLD)
    custom_defender = st.text_input("Atau ketik nama custom", placeholder="Contoh: Naga Hitam", key="def")
    if custom_defender.strip():
        defender = custom_defender.strip()

# Habitat + Custom
habitat = st.selectbox("🌍 Habitat Pertarungan", HABITATS)
custom_habitat = st.text_input("Atau ketik habitat custom", placeholder="Contoh: Hutan Kalimantan")
if custom_habitat.strip():
    habitat = custom_habitat.strip()

# Prompt Type
st.subheader("📝 Jenis Prompt")
prompt_type = st.radio(
    "",
    ["🖼️ Image Prompt (Midjourney/Flux/Grok)",
     "🎥 Video Prompt (Kling/Runway/Luma/Pika)",
     "🎨 Leonardo AI Prompt",
     "📖 Battle Analysis",
     "🔥 All-in-One"],
    horizontal=True
)

# Video Duration
if "Video" in prompt_type or "Leonardo" in prompt_type:
    video_duration = st.slider("Durasi Video / Style Strength (detik)", 5, 20, 12, step=1)

# Generate Button
if st.button("🚀 GENERATE PROMPT SEKARANG", use_container_width=True, type="primary"):
    base = f"Masterpiece epic battle between {attacker} and {defender} in the {habitat}."

    if "Image Prompt" in prompt_type:
        prompt = f"{base} Hyper-realistic 8K, cinematic lighting, intense action, dramatic atmosphere --ar 16:9 --stylize 250"
    elif "Video Prompt" in prompt_type:
        prompt = f"{base} {video_duration}-second ultra cinematic video with slow-motion, dramatic camera movement, National Geographic style."
    elif "Leonardo AI" in prompt_type:
        prompt = f"{base} Highly detailed digital art, epic fantasy style, dramatic lighting, ultra realistic, best quality, 8K --ar 16:9 --stylize {video_duration}"
    elif "Battle Analysis" in prompt_type:
        prompt = f"Buat analisis lengkap dan dramatis pertarungan {attacker} vs {defender} di {habitat}. Jelaskan kekuatan, strategi, kelemahan, dan prediksi pemenang dengan gaya epik."
    else:  # All-in-One
        prompt = f"""=== ALL-IN-ONE PROMPT PACK ===
🖼️ IMAGE: {base} 8K realistic --ar 16:9
🎥 VIDEO: {video_duration}s cinematic fight
🎨 LEONARDO: Epic digital art version
📖 ANALYSIS: Detail kekuatan & strategi {attacker} vs {defender}"""

    st.session_state.prompt = prompt
    st.session_state.title = f"{attacker} vs {defender}"

# Show Result
if "prompt" in st.session_state:
    st.success(f"✅ Prompt untuk: {st.session_state.title}")
    st.code(st.session_state.prompt, language="markdown")
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("📋 Copy Prompt"):
            st.toast("✅ Prompt berhasil di-copy!")
    with col2:
        if st.button("🎬 Buka Kling AI"):
            st.markdown("[Buka Kling AI](https://kling.ai)")

st.caption("By SOFYAN • https://facebook.com/yankees.romi • v3.1 • 2026")
