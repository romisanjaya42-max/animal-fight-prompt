import streamlit as st
import random
from datetime import datetime

# ==================== PAGE CONFIG ====================
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
        font-weight: bold;
        text-align: center;
        background: linear-gradient(90deg, #FF6B35, #F7931E, #FF6B35);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 0.5rem;
    }
    .subtitle {
        text-align: center;
        font-size: 1.3rem;
        color: #555;
        margin-bottom: 2rem;
    }
    .stButton>button {
        background: linear-gradient(90deg, #FF6B35, #F7931E);
        color: white;
        font-weight: bold;
        border: none;
        padding: 0.8rem 2rem;
        border-radius: 50px;
        font-size: 1.1rem;
    }
    .stButton>button:hover {
        transform: scale(1.05);
        box-shadow: 0 10px 20px rgba(255, 107, 53, 0.3);
    }
    .prompt-box {
        background-color: #f8f9fa;
        border-left: 6px solid #FF6B35;
        padding: 1.5rem;
        border-radius: 10px;
        font-family: monospace;
        font-size: 0.95rem;
        line-height: 1.6;
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
    "Capybara", "Piranha", "Electric Eel", "Alligator Amerika", "Python Burma"
]

HABITATS = [
    "Savana Afrika yang panas", "Hutan Hujan Amazon yang lebat", "Gunung Himalaya yang dingin",
    "Laut Dalam Pasifik yang gelap", "Gurun Sahara yang terik", "Hutan Boreal Kanada",
    "Sungai Amazon yang deras", "Padang Rumput Serengeti", "Kutub Utara yang beku",
    "Hutan Tropis Indonesia", "Gunung Berapi Aktif", "Lembah Sungai Nil"
]

VIDEO_STYLES = [
    "Cinematic Epic Trailer (seperti film Hollywood)",
    "National Geographic Documentary (realistis & dramatis)",
    "Slow-Motion Action (detail gerakan maksimal)",
    "Fast-Paced Intense (seperti game AAA)",
    "Dark Fantasy Battle (atmosfer misterius & epik)",
    "Hyper-Realistic 8K (seperti rekaman alam liar)"
]

CAMERA_MOVES = [
    "Wide establishing shot → dramatic zoom in",
    "Slow orbiting 360° around the fighters",
    "Intense handheld shaky cam during attack",
    "Drone pull-back revealing the full battlefield",
    "Extreme close-up on claws & fangs + slow-mo",
    "Dynamic tracking shot following the chase"
]

# ==================== HEADER ====================
st.markdown('<h1 class="main-title">🐾 ANIMAL FIGHT PROMPT GENERATOR</h1>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">Versi Web Streamlit • Image + Video + Analysis • Pertarungan Hewan Dunia</p>', unsafe_allow_html=True)

# ==================== SIDEBAR ====================
with st.sidebar:
    st.header("⚙️ Pengaturan Cepat")
    
    st.subheader("🎲 Random Battle")
    if st.button("🔥 Pilih 2 Hewan Acak", use_container_width=True):
        random_pair = random.sample(ANIMALS_WORLD, 2)
        st.session_state.random_hewan1 = random_pair[0]
        st.session_state.random_hewan2 = random_pair[1]
        st.rerun()
    
    st.divider()
    
    st.subheader("📋 Daftar Hewan Populer")
    if st.checkbox("Tampilkan semua hewan"):
        st.write(", ".join(ANIMALS_WORLD))

# ==================== MAIN INPUT ====================
col1, col2 = st.columns(2)

with col1:
    st.subheader("🦁 Hewan 1 (Penyerang)")
    hewan1 = st.selectbox("Pilih Hewan 1", ANIMALS_WORLD, index=0, key="hewan1")
    custom1 = st.text_input("Atau ketik nama hewan custom", placeholder="Contoh: Megalodon", key="custom1")
    if custom1.strip():
        hewan1 = custom1.strip().title()

with col2:
    st.subheader("🐅 Hewan 2 (Bertahan)")
    hewan2 = st.selectbox("Pilih Hewan 2", ANIMALS_WORLD, index=1, key="hewan2")
    custom2 = st.text_input("Atau ketik nama hewan custom", placeholder="Contoh: T-Rex", key="custom2")
    if custom2.strip():
        hewan2 = custom2.strip().title()

habitat = st.selectbox("🌍 Pilih Habitat Pertarungan", HABITATS, index=0)

st.subheader("🎯 Jenis Prompt")
prompt_type = st.radio(
    "Pilih jenis prompt",
    ["🖼️ Image Prompt (untuk Midjourney / Flux / Grok Imagine)",
     "🎥 Video Prompt (untuk Kling AI / Runway / Luma / Pika)",
     "📖 Battle Analysis Prompt (untuk ChatGPT / Claude)",
     "🔥 All-in-One (Image + Video + Analysis)"],
    horizontal=True
)

if "Video" in prompt_type:
    st.subheader("🎬 Pengaturan Video Lanjutan")
    colv1, colv2 = st.columns(2)
    with colv1:
        duration = st.slider("Durasi Video (detik)", 5, 15, 10, step=1)
        video_style = st.selectbox("Gaya Video", VIDEO_STYLES)
    with colv2:
        camera_move = st.selectbox("Pergerakan Kamera", CAMERA_MOVES)
        add_sound = st.checkbox("Sertakan deskripsi suara & musik", value=True)

st.divider()
if st.button("🚀 GENERATE PROMPT SEKARANG", use_container_width=True, type="primary"):
    now = datetime.now().strftime("%Y-%m-%d %H:%M")
    
    if "Image Prompt" in prompt_type:
        prompt = f"""Masterpiece hyper-realistic cinematic battle between a powerful {hewan1} and a ferocious {hewan2} fighting to the death in the middle of the {habitat}. 

{hewan1} roaring with bared fangs and extended claws, {hewan2} charging with deadly speed and power. Intense action, flying dust and debris, broken trees, dramatic lighting, sweat and blood details, ultra detailed fur/scales/muscles, National Geographic quality, 8K resolution, photorealistic, epic composition, dynamic angle, best quality, intricate details --ar 16:9 --stylize 250 --v 6

Negative prompt: blurry, cartoon, low quality, deformed animals, extra limbs, text, watermark, ugly, overexposed"""

    elif "Video Prompt" in prompt_type:
        sound_part = ""
        if add_sound:
            sound_part = " Sound design: deep roars and growls echoing, heavy breathing, bones cracking, intense orchestral trailer music with rising tension and powerful drums. Final impact sound when one animal wins."

        prompt = f"""Create a {duration}-second ultra cinematic {video_style} video of an epic deadly battle between a massive {hewan1} and a powerful {hewan2} in the {habitat}.

Scene sequence:
1. Opening wide shot: both animals circling each other aggressively, dust rising, intense eye contact.
2. {camera_move} as they charge and clash violently.
3. Slow-motion close-up of fangs sinking, claws tearing flesh, powerful muscles flexing.
4. Dynamic action: {hewan1} leaping for a killing blow while {hewan2} counters with full force.
5. Climax: massive impact, flying debris, one animal gaining the upper hand.
6. Dramatic final shot: winner standing over the defeated, roaring in victory as sun/mist/light breaks through.

Hyper-realistic 8K, National Geographic wildlife cinematography, intense dramatic lighting, particles in air, sweat and blood details, emotional animal expressions, masterpiece quality.{sound_part}

--ar 16:9 --motion high --duration {duration}"""

    elif "Battle Analysis" in prompt_type:
        prompt = f"""Buat analisis pertarungan yang sangat detail dan dramatis antara {hewan1} melawan {hewan2} di habitat {habitat}.

Struktur analisis:
1. Perbandingan ukuran, berat, kekuatan gigitan, kecepatan, dan senjata alami masing-masing.
2. Keunggulan dan kelemahan setiap hewan di habitat tersebut.
3. Strategi bertarung yang mungkin digunakan (serangan pertama, bertahan, jebakan, dll).
4. Simulasi langkah demi langkah pertarungan (minimal 4-5 fase krusial).
5. Kesimpulan siapa yang paling mungkin menang beserta alasan ilmiah + faktor keberuntungan.
6. Tambahkan narasi epik seperti film dokumenter hewan liar.

Gunakan bahasa Indonesia yang menarik, hidup, dan mudah dibaca."""

    else:  # All-in-One
        prompt = f"""=== ALL-IN-ONE PROMPT PACK ===

🖼️ IMAGE PROMPT:
Hyper-realistic epic battle between {hewan1} and {hewan2} in {habitat}. Dramatic lighting, intense action, 8K, National Geographic style --ar 16:9

🎥 VIDEO PROMPT ({duration}s):
{hewan1} vs {hewan2} in {habitat}. {camera_move}. {video_style}. Slow-motion clashes, dust explosions, powerful roars. Cinematic masterpiece, 8K.

📖 ANALYSIS PROMPT:
Analisis lengkap pertarungan {hewan1} vs {hewan2} di {habitat} dengan perbandingan kekuatan, strategi, dan prediksi pemenang secara ilmiah + dramatis.

Negative: blurry, cartoon, low quality, deformed"""

    st.success("✅ Prompt berhasil dibuat!")
    st.subheader(f"📋 {hewan1} vs {hewan2}")
    st.code(prompt, language="markdown")
    
    st.download_button(
        label="⬇️ Download Prompt sebagai .txt",
        data=prompt,
        file_name=f"animal_fight_{hewan1.lower()}_vs_{hewan2.lower()}.txt",
        mime="text/plain",
        use_container_width=True
    )
    
    if "Video" in prompt_type:
        st.info("💡 Tips: Paste prompt ini ke Kling AI / Runway / Luma untuk hasil terbaik!")

st.caption("Animal Fight Prompt Generator v2.0 • Streamlit Edition • 2026")