import streamlit as st

from services.get_models_list import get_ollama_models_list
from services.get_title import get_chat_title
from services.chat_utilities import get_answer
from db.conversations import (
    create_new_conversation,
    add_message,
    get_conversation,
    get_all_conversations,
)

# ---------------- Page Config ----------------
st.set_page_config(
    page_title="Local MoGPT",
    page_icon="🤖",
    layout="centered",
)

# ---------------- Custom CSS ----------------
st.markdown(
    """
    <style>
    /* App background */
    .stApp {
        background: linear-gradient(135deg, #0f172a, #020617);
        color: #e5e7eb;
    }

    /* Titles */
    h1, h2, h3 {
        font-weight: 700;
        letter-spacing: -0.02em;
    }

    /* Sidebar */
    section[data-testid="stSidebar"] {
        background: #020617;
        border-right: 1px solid #1e293b;
    }

    /* Buttons */
    .stButton>button {
        background: #1e293b;
        color: #e5e7eb;
        border-radius: 10px;
        padding: 0.5rem 1rem;
        border: 1px solid #334155;
        transition: all 0.2s ease;
    }
    .stButton>button:hover {
        background: #334155;
        transform: translateY(-1px);
    }

    /* Selectbox */
    div[data-baseweb="select"] {
        background-color: #020617;
        border-radius: 10px;
    }

    /* Chat bubbles */
    .stChatMessage {
        padding: 0.75rem 1rem;
        border-radius: 14px;
        margin-bottom: 0.5rem;
        max-width: 90%;
    }

    /* User bubble */
    .stChatMessage[data-testid="user"] {
        background: linear-gradient(135deg, #2563eb, #1d4ed8);
        margin-left: auto;
        color: white;
    }

    /* Assistant bubble */
    .stChatMessage[data-testid="assistant"] {
        background: #020617;
        border: 1px solid #1e293b;
        color: #e5e7eb;
    }

    /* Chat input */
    textarea {
        background: #020617 !important;
        color: #e5e7eb !important;
        border-radius: 12px !important;
        border: 1px solid #334155 !important;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# ---------------- Header ----------------
st.markdown(
    """
    <h1 style="text-align:center;">🤖 Local ChatGPT</h1>
    <p style="text-align:center; color:#94a3b8;">
        Fast • Private • Powered by Ollama
    </p>
    """,
    unsafe_allow_html=True,
)

# ---------------- Models ----------------
if "OLLAMA_MODELS" not in st.session_state:
    st.session_state.OLLAMA_MODELS = get_ollama_models_list()

selected_model = st.selectbox(
    "🧠 Active Model",
    st.session_state.OLLAMA_MODELS,
)

# ---------------- Session State ----------------
st.session_state.setdefault("conversation_id", None)
st.session_state.setdefault("conversation_title", None)
st.session_state.setdefault("chat_history", [])

# ---------------- Sidebar ----------------
with st.sidebar:
    st.markdown("## 💬 Conversations")

    if st.button("➕ New Chat", use_container_width=True):
        st.session_state.conversation_id = None
        st.session_state.conversation_title = None
        st.session_state.chat_history = []

    st.markdown("---")

    conversations = get_all_conversations()

    for cid, title in conversations.items():
        is_current = cid == st.session_state.conversation_id
        label = f"🟢 **{title}**" if is_current else f"⚪ {title}"

        if st.button(label, key=f"conv_{cid}", use_container_width=True):
            doc = get_conversation(cid) or {}
            st.session_state.conversation_id = cid
            st.session_state.conversation_title = doc.get("title", "Untitled")
            st.session_state.chat_history = [
                {"role": m["role"], "content": m["content"]}
                for m in doc.get("messages", [])
            ]

# ---------------- Chat History ----------------
for msg in st.session_state.chat_history:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# ---------------- Chat Input ----------------
user_query = st.chat_input("Type your message and press Enter…")

if user_query:
    # Show + store user message
    st.chat_message("user").markdown(user_query)
    st.session_state.chat_history.append(
        {"role": "user", "content": user_query}
    )

    # Persist user message
    if st.session_state.conversation_id is None:
        try:
            title = get_chat_title(selected_model, user_query) or "New Chat"
        except Exception:
            title = "New Chat"

        conv_id = create_new_conversation(
            title=title,
            role="user",
            content=user_query,
        )
        st.session_state.conversation_id = conv_id
        st.session_state.conversation_title = title
    else:
        add_message(
            st.session_state.conversation_id,
            "user",
            user_query,
        )

    # Get assistant response
    try:
        assistant_text = get_answer(
            selected_model,
            st.session_state.chat_history,
        )
    except Exception as e:
        assistant_text = f"[Error getting response: {e}]"

    # Show + store assistant message
    with st.chat_message("assistant"):
        st.markdown(assistant_text)

    st.session_state.chat_history.append(
        {"role": "assistant", "content": assistant_text}
    )

    # Persist assistant message
    if st.session_state.conversation_id:
        add_message(
            st.session_state.conversation_id,
            "assistant",
            assistant_text,
        )
