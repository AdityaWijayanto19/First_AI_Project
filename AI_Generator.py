import os

import streamlit as st
from dotenv import load_dotenv
import google.generativeai as genai

# =========================
# 🔧 KONFIGURASI HALAMAN
# =========================
st.set_page_config(
    page_title="AI Content Generator Pro",
    page_icon="✍️",
    layout="wide",
    initial_sidebar_state="expanded",
)

# =========================
# 🎨 CUSTOM CSS (Chat-like)
# =========================
CHAT_CSS = """
<style>
    .app-title {
        font-size: 28px;
        font-weight: 700;
        margin-bottom: 4px;
    }
    .app-subtitle {
        font-size: 14px;
        color: #666666;
        margin-bottom: 16px;
    }
    .chat-container {
        max-width: 900px;
        margin: 0 auto;
    }
    .chat-bubble-ai {
        background-color: #000000;
        border-radius: 12px;
        padding: 16px 18px;
        margin-bottom: 16px;
        border: 1px solid #e0e0e0;
    }
    .chat-bubble-user {
        background-color: #e8f3ff;
        border-radius: 12px;
        padding: 10px 12px;
        margin-bottom: 8px;
        border: 1px solid #cbdaf5;
        font-size: 13px;
        color: #333333;
        display: inline-block;
    }
    .user-label {
        font-size: 12px;
        font-weight: 600;
        color: #555555;
        margin-bottom: 4px;
    }
    .ai-label {
        font-size: 12px;
        font-weight: 600;
        color: #10a37f;
        margin-bottom: 6px;
    }
    .input-area {
        position: sticky;
        bottom: 0;
        background-color: white;
        padding-top: 12px;
        padding-bottom: 8px;
        border-top: 1px solid #e0e0e0;
    }
    .small-helper {
        font-size: 12px;
        color: #888888;
        margin-top: 4px;
    }
</style>
"""
st.markdown(CHAT_CSS, unsafe_allow_html=True)


# =========================
# 🤖 INISIALISASI GOOGLE AI
# =========================
@st.cache_resource
def init_google_ai():
    """Menginisialisasi Model Gemini dari Google AI SDK."""
    try:
        load_dotenv()
        api_key = os.getenv("GOOGLE_API_KEY")

        if not api_key:
            st.warning(
                "⚠️ GOOGLE_API_KEY tidak ditemukan. "
                "Pastikan variabel lingkungan sudah diatur!"
            )

        genai.configure(api_key=api_key)
        model = genai.GenerativeModel("gemini-2.5-flash")
        return model

    except Exception as e:
        st.error(f"⚠️ Terjadi kesalahan saat inisialisasi Google AI: {e}")
        st.stop()


# =========================
# ✍️ FUNGSI GENERATE KONTEN
# =========================
def generate_content(topic: str, model) -> str | None:
    """
    Generate konten menggunakan Google Gemini AI.

    :param topic: Topik konten yang ingin dibuat.
    :param model: Instance model Gemini.
    :return: Teks konten dalam format Markdown, atau None jika gagal.
    """
    try:
        prompt = f"""
Kamu adalah asisten penulis konten blog yang SANGAT fokus pada topik
dan tidak pernah keluar konteks.

TUGAS UTAMA:
- Buat satu konten blog yang relevan HANYA tentang topik berikut:
  "{topic}"

ATURAN KETAT:
1. Dilarang membahas topik lain yang tidak berkaitan langsung dengan topik di atas.
2. Jangan memberikan definisi atau penjelasan umum yang terlalu jauh dari topik.
3. Setiap paragraf harus jelas koneksinya dengan topik tersebut.
4. Jangan berimajinasi berlebihan, tetap logis dan realistis.
5. Jika topik terlalu umum, sempitkan sendiri dengan cara yang masih relevan.
6. Jangan menyebut bahwa kamu adalah model AI atau menjelaskan cara kerja AI.

FORMAT KONTEN (WAJIB MENGGUNAKAN MARKDOWN):
# Judul utama yang spesifik dan menarik (bukan clickbait berlebihan)

Pendahuluan singkat (2–3 kalimat) yang:
- Menjelaskan apa yang akan dibahas
- Menyebut topik secara eksplisit

## Poin Utama 1
- Jelaskan dengan fokus pada topik
- Beri contoh atau penjelasan konkret yang relevan

## Poin Utama 2
- Tetap terhubung dengan topik
- Boleh memakai bullet list jika perlu

## Poin Utama 3
- Tambahkan insight yang masih dalam konteks
- Jangan mengulang isi dari poin sebelumnya secara kosong

Kesimpulan:
- Ringkas ulang inti pembahasan
- Jangan membuka topik baru

Call to Action:
- Buat ajakan yang masih BERKAITAN langsung dengan topik
- Contoh: mengajak pembaca mencoba, menerapkan, atau mempelajari lebih lanjut hal yang sama.

GAYA BAHASA:
- Gunakan bahasa Indonesia yang baik, natural, dan mudah dipahami.
- Hindari kalimat terlalu panjang.
- Hindari istilah teknis yang tidak perlu; jika harus dipakai, jelaskan dengan singkat.
        """

        response = model.generate_content(prompt)
        return response.text

    except Exception as e:
        st.error(f"⚠️ Terjadi kesalahan saat generate konten: {e}")
        return None



# =========================
# 🖥️ SIDEBAR
# =========================
def sidebar_layout():
    with st.sidebar:
        st.header("⚙️ Panel Kontrol")
        st.markdown("Atur preferensi dan lihat info aplikasi di sini.")
        st.markdown("---")

        st.subheader("Model LLM")
        st.selectbox(
            "Saat ini:",
            ["Gemini 2.5 Flash (Aktif)", "Gemini 2.5 Pro (Coming soon)"],
            index=0,
            disabled=True,
        )

        st.markdown("---")
        st.caption(
            "💡 Aplikasi ini dirancang sebagai generator konten blog "
            "dengan pengalaman mirip chat untuk workflow yang lebih natural."
        )


# =========================
# 💬 LAYOUT MIRIP CHATGPT
# =========================
def main_layout():
    # Inisialisasi model
    model = init_google_ai()

    # Inisialisasi riwayat percakapan di session_state
    if "messages" not in st.session_state:
        # Setiap item: {"role": "user"/"ai", "topic": "...", "content": "..."}
        st.session_state.messages = []

    st.markdown('<div class="chat-container">', unsafe_allow_html=True)

    # Header / Title
    st.markdown(
        '<div class="app-title">✍️ AI Content Generator Pro</div>',
        unsafe_allow_html=True,
    )
    st.markdown(
        '<div class="app-subtitle">'
        "Masukkan topik yang ingin kamu tulis. "
        "AI akan menghasilkan konten blog lengkap untukmu, dengan gaya seperti obrolan."
        "</div>",
        unsafe_allow_html=True,
    )

    # Tampilkan riwayat "chat" (mirip ChatGPT)
    for msg in st.session_state.messages:
        if msg["role"] == "user":
            # Bubble user kecil di atas
            st.markdown(
                f"""
                <div class="user-label">Kamu</div>
                <div class="chat-bubble-user">
                    {msg["topic"]}
                </div>
                """,
                unsafe_allow_html=True,
            )
        elif msg["role"] == "ai":
            # Bubble AI berisi konten markdown
            st.markdown(
                '<div class="ai-label">AI Content Generator</div>',
                unsafe_allow_html=True,
            )
            with st.container():
                st.markdown(
                    f'<div class="chat-bubble-ai">{msg["content"]}</div>',
                    unsafe_allow_html=True,
                )

    st.markdown("</div>", unsafe_allow_html=True)

    # ===== Area Input di Bawah (mirip ChatGPT) =====
    st.markdown('<div class="chat-container input-area">', unsafe_allow_html=True)

    with st.form("chat_input_form", clear_on_submit=True):
        topic_input = st.text_area(
            "Tuliskan topik konten yang kamu inginkan:",
            placeholder="Contoh: Dampak Internet of Things dalam dunia pendidikan...",
            height=80,
        )
        col_btn1, col_btn2 = st.columns([1, 4])
        with col_btn1:
            submit = st.form_submit_button("Generate")
        with col_btn2:
            st.markdown(
                '<div class="small-helper">'
                "Tekan Enter dua kali untuk baris baru, atau klik Generate untuk mengirim."
                "</div>",
                unsafe_allow_html=True,
            )

    st.markdown("</div>", unsafe_allow_html=True)

    # Logika ketika tombol Generate diklik
    if submit:
        if not topic_input.strip():
            st.warning("⚠️ Mohon masukkan topik terlebih dahulu.")
        else:
            # Simpan pesan user
            st.session_state.messages.append(
                {
                    "role": "user",
                    "topic": topic_input.strip(),
                    "content": "",
                }
            )

            with st.spinner("⏳ Sedang membuat konten dengan Gemini..."):
                hasil_konten = generate_content(topic_input.strip(), model)

            if hasil_konten:
                st.session_state.messages.append(
                    {
                        "role": "ai",
                        "topic": "",
                        "content": hasil_konten,
                    }
                )
                st.toast("✅ Konten berhasil dibuat!", icon="🎉")
                st.rerun()


# =========================
# 🚀 MAIN EXECUTION
# =========================
def run():
    sidebar_layout()
    main_layout()


if __name__ == "__main__":
    run()
