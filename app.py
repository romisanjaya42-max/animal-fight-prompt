import streamlit as st
import random
from datetime import datetime

# ==================== DAFTAR USER (EDIT DI SINI) ====================
USERS = {
    "romites2":     {"durasi_jam": 8760,   "start_time": None},   # Admin (1 Tahun)
    "boy1":       {"durasi_jam": 1,  "start_time": None},   # 1 jam
    "user02":       {"durasi_jam": 24,  "start_time": None},   # 24 jam
    "user03":       {"durasi_jam": 48,  "start_time": None},   # 2 hari
    "user04":       {"durasi_jam": 72,  "start_time": None},   # 3 hari
    "user05":       {"durasi_jam": 168, "start_time": None},   # 7 hari
    "user06":       {"durasi_jam": 24,  "start_time": None},
    "user07":       {"durasi_jam": 24,  "start_time": None},
    "user08":       {"durasi_jam": 48,  "start_time": None},
    "user09":       {"durasi_jam": 72,  "start_time": None},
    "user10":       {"durasi_jam": 168, "start_time": None},
    "user11":       {"durasi_jam": 24,  "start_time": None},
    "user12":       {"durasi_jam": 48,  "start_time": None},
    "user13":       {"durasi_jam": 72,  "start_time": None},
    "user14":       {"durasi_jam": 24,  "start_time": None},
    "user15":       {"durasi_jam": 168, "start_time": None},
    "user16":       {"durasi_jam": 24,  "start_time": None},
    "user17":       {"durasi_jam": 48,  "start_time": None},
    "user18":       {"durasi_jam": 72,  "start_time": None},
    "user19":       {"durasi_jam": 24,  "start_time": None},
    "user20":       {"durasi_jam": 168, "start_time": None},
}

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

# ==================== MULTI-USER ACCESS CONTROL ====================
if "current_user" not in st.session_state:
    st.session_state.current_user = None
    st.session_state.access_time = None

if st.session_state.current_user is None:
    st.title("🔐 Animal Fight Prompt Generator")
    key_input = st.text_input("Access Key", type="password")
    
    if st.button("Masuk"):
        if key_input in USERS:
            st.session_state.current_user = key_input
            if USERS[key_input]["start_time"] is None:
                USERS[key_input]["start_time"] = datetime.now()
            st.session_state.access_time = USERS[key_input]["start_time"]
            st.rerun()
        else:
            st.error("❌ Access Key salah!")
            st.info("📌 Jika tidak memiliki akses, hubungi admin di Telegram: https://t.me/Furaney")
    st.stop()

# ==================== CEK DURASI USER ====================
current_key = st.session_state.current_user
user_data = USERS[current_key]
durasi = user_data["durasi_jam"]
start_time = user_data["start_time"]

if start_time:
    sisa_detik = (durasi * 3600) - (datetime.now() - start_time).total_seconds()
    if sisa_detik <= 0:
        st.error(f"⏰ Akses {current_key} telah kadaluarsa ({durasi} jam).")
        st.info("📌 Hubungi admin untuk perpanjangan.")
        st.stop()
    else:
        jam = int(sisa_detik // 3600)
        menit = int((sisa_detik % 3600) // 60)
        st.sidebar.success(f"👤 User: {current_key}")
        st.sidebar.success(f"⏳ Sisa waktu: {jam} jam {menit} menit")

# ==================== MAIN APP ====================
st.markdown('<h1 class="main-title">🐾 ANIMAL FIGHT PROMPT GENERATOR</h1>', unsafe_allow_html=True)
st.markdown('<p class="by-sofyan">By SOFYAN • https://facebook.com/yankees.romi</p>', unsafe_allow_html=True)

with st.sidebar:
    if st.button("🔄 Reset Durasi User Ini", use_container_width=True):
        USERS[current_key]["start_time"] = datetime.now()
        st.success("✅ Durasi berhasil di-reset!")
        st.rerun()
    
    if st.button("🔄 Logout"):
        st.session_state.current_user = None
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

visual_style = st.selectbox("🎨 Pilih Gaya Visual", 
    ["Cinematic Epic", "Hyper Realistic", "Dark Fantasy", 
     "National Geographic Documentary", "Slow Motion Action", "Dramatic Lighting"], 
    key="visual_style")

prompt_type = st.radio("📝 Jenis Prompt", 
    ["🖼️ Image", "🎥 Video", "🎨 Leonardo AI", "📖 Analysis", "🔥 All-in-One"], 
    horizontal=True, key="prompt_type")

if "Video" in prompt_type or "Leonardo" in prompt_type or "All-in-One" in prompt_type:
    durasi_video = st.slider("Durasi Video (detik)", 5, 20, 12, key="durasi")

if st.button("🚀 GENERATE", use_container_width=True, type="primary", key="generate_btn"):
    base = f"Masterpiece epic battle between {attacker} and {defender} in the {habitat}, {visual_style} style."

    if "Image" in prompt_type:
        prompt = f"{base} Hyper-realistic 8K, cinematic lighting, intense action --ar 16:9 --stylize 250"
    elif "Video" in prompt_type:
        prompt = f"{base} {durasi_video}-second cinematic video, slow-motion, dramatic camera movement."
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
{durasi_video}-second ultra cinematic video. Start with wide establishing shot, slow orbiting camera, intense slow-motion clash, dramatic music swell, dust & particles. Hyper-realistic 8K. --ar 16:9 --motion high

🎨 LEONARDO AI PROMPT:
{base}
Highly detailed digital art, epic fantasy style, dramatic volumetric lighting, ultra realistic, 8K --ar 16:9 --stylize {durasi_video}

📖 BATTLE ANALYSIS (ChatGPT / Claude):
Buat analisis lengkap pertarungan {attacker} vs {defender} di {habitat}. Jelaskan kekuatan, strategi, dan prediksi pemenang dengan gaya epik."""

    st.session_state.final_prompt = prompt
    st.session_state.final_title = f"{attacker} vs {defender}"

if "final_prompt" in st.session_state:
    st.success(f"✅ {st.session_state.final_title}")
    st.code(st.session_state.final_prompt, language="markdown")
    
    st.info("💡 Klik ikon 📋 di pojok kanan atas kode untuk menyalin prompt")
    
    if st.button("🎨 Buka Leonardo AI", key="leonardo_btn"):
        st.markdown("[Buka Leonardo AI](https://leonardo.ai)")

st.caption("By SOFYAN • Multi-User System • v5.0 • 2026")
