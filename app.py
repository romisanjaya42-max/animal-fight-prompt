import streamlit as st
import random
from datetime import datetime

# ==================== KONFIGURASI MUDAH DIUBAH ====================
ACCESS_KEY = "romites"
DURASI_JAM = 1

st.set_page_config(page_title="🐾 Animal Fight Prompt Generator", page_icon="🐾", layout="wide")

st.markdown("""
<style>
    .main-title {font-size: 3rem; font-weight: 900; text-align: center; 
                 background: linear-gradient(90deg, #FF6B35, #F7931E); 
                 -webkit-background-clip: text; -webkit-text-fill-color: transparent;}
    .by-sofyan {text-align: center; color: #FF6B35; font-weight: bold; margin-bottom: 1.5rem;}
</style>
""", unsafe_allow_html=True)

ANIMALS_WORLD = ["Singa", "Harimau Sumatra", "Gajah Afrika", "Komodo", "Orca", "Hiu Putih Besar",
    "Beruang Grizzly", "Beruang Kutub", "Anaconda Hijau", "Elang Botak", "Serigala Abu-abu",
    "Kuda Nil", "Badak Putih", "Macan Tutul", "Buaya Nil", "Ular Kobra Raja", "Gorila Gunung",
    "Simpanse", "Zebra", "Jerapah", "Bison Amerika", "Moose", "Penguin Kaisar", "Paus Biru",
    "Hiu Martil", "Ikan Pari Manta", "Elang Harpy", "Harimau Siberia", "Singa Gunung",
    "Wolverine", "Tasmanian Devil", "Kanguru Merah", "Koala", "Panda Raksasa", "Cheetah",
    "Leopard Salju", "Hyena", "Baboon", "Mandril", "Okapi", "Tapir", "Sloth", "Armadillo",
    "Capybara", "Piranha", "Electric Eel", "Alligator Amerika", "Python Burma",
    "T-Rex", "Velociraptor", "Spinosaurus", "Triceratops", "Mammoth", "Saber-Tooth Tiger",
    "Giant Squid", "Megalodon", "Saltwater Crocodile", "Honey Badger", "Cassowary",
    "Ostrich", "Emu", "Red Kangaroo", "Platypus", "Echidna", "Blue Whale", "Hammerhead Shark"]

FANTASY_CREATURES = ["Naga Api", "Phoenix", "Griffin", "Unicorn", "Werewolf", "Minotaur",
    "Hydra", "Pegasus", "Dragon Turtle", "Chimera", "Basilisk", "Wyvern",
    "Kraken", "Leviathan", "Cerberus", "Sphinx", "Manticore", "Roc",
    "Thunderbird", "Fenrir", "Jörmungandr", "Bahamut"]

HABITATS = ["Savana Afrika yang panas", "Hutan Hujan Amazon yang lebat", "Gunung Himalaya yang dingin",
    "Laut Dalam Pasifik yang gelap", "Gurun Sahara yang terik", "Hutan Boreal Kanada",
    "Sungai Amazon yang deras", "Padang Rumput Serengeti", "Kutub Utara yang beku",
    "Hutan Tropis Indonesia", "Gunung Berapi Aktif", "Lembah Sungai Nil", "Kawah Vulkanik",
    "Hutan Bambu Cina", "Padang Es Antartika"]

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

mode = st.radio("🎯 Mode", ["🦁 Real vs Real", "🦄 Fantasy vs Real", "🐉 Fantasy vs Fantasy"], horizontal=True, key="mode")

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

# ==================== PILIHAN GAYA VISUAL ====================
visual_style = st.selectbox("🎨 Pilih Gaya Visual", 
    ["Cinematic Epic", "Hyper Realistic", "Dark Fantasy", 
     "National Geographic Documentary", "Slow Motion Action", "Dramatic Lighting"], 
    key="visual_style")

# ==================== JENIS PROMPT (DIPINDAH KE ATAS) ====================
prompt_type = st.radio("📝 Jenis Prompt", 
    ["🖼️ Image", "🎥 Video", "🎨 Leonardo AI", "📖 Analysis", "🔥 All-in-One"], 
    horizontal=True, key="prompt_type")

# Slider durasi
if "Video" in prompt_type or "Leonardo" in prompt_type or "All-in-One" in prompt_type:
    durasi = st.slider("Durasi Video (detik)", 5, 20, 12, key="durasi")

if st.button("🚀 GENERATE", use_container_width=True, type="primary", key="generate_btn"):
    base = f"Masterpiece epic battle between {attacker} and {defender} in the {habitat}, {visual_style} style."

    if "Image" in prompt_type:
        prompt = f"{base} Hyper-realistic 8K, cinematic lighting, intense action --ar 16:9 --stylize 250"
    elif "Video" in prompt_type:
        prompt = f"{base} {durasi}-second cinematic video, slow-motion, dramatic camera movement."
    elif "Leonardo" in prompt_type:
        prompt = f"{base} Epic digital art, dramatic lighting, 8K --ar 16:9"
    elif "Analysis" in prompt_type:
        prompt = f"Analisis lengkap {attacker} vs {defender} di {habitat}. Kekuatan, strategi, prediksi pemenang."
    else:  # All-in-One
        prompt = f"""=== ALL-IN-ONE PROMPT PACK ===

🖼️ IMAGE PROMPT (Midjourney / Flux / Grok Imagine):
{base}
Hyper-realistic 8K, cinematic lighting, intense action, dramatic atmosphere --ar 16:9 --stylize 250 --v 6

🎥 VIDEO PROMPT (Kling AI / Runway / Luma / Pika):
{base}
{durasi}-second ultra cinematic video. Start with wide establishing shot, slow orbiting camera, intense slow-motion clash, dramatic music swell, dust & particles. Hyper-realistic 8K. --ar 16:9 --motion high

🎨 LEONARDO AI PROMPT:
{base}
Highly detailed digital art, epic fantasy style, dramatic volumetric lighting, ultra realistic, 8K --ar 16:9 --stylize {durasi}

📖 BATTLE ANALYSIS (ChatGPT / Claude):
Buat analisis lengkap pertarungan {attacker} vs {defender} di {habitat}. Jelaskan kekuatan, strategi, dan prediksi pemenang dengan gaya epik."""

    st.session_state.final_prompt = prompt
    st.session_state.final_title = f"{attacker} vs {defender}"

if "final_prompt" in st.session_state:
    st.success(f"✅ {st.session_state.final_title}")
    
    st.code(st.session_state.final_prompt, language="markdown")
    
    st.info("💡 **Cara menyalin:** Klik ikon 📋 di pojok kanan atas kode di atas")
    
    if st.button("🎨 Buka Leonardo AI", key="leonardo_btn"):
        st.markdown("[Buka Leonardo AI](https://leonardo.ai)")

st.caption("By SOFYAN • https://facebook.com/yankees.romi • v3.1 • 2026")
