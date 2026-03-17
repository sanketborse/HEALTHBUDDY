import os
from dotenv import load_dotenv
import streamlit as st
from groq import Groq

# ---------- LOAD ENV ----------
load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

if not GROQ_API_KEY:
    raise ValueError("GROQ_API_KEY not found in .env file")

client = Groq(api_key=GROQ_API_KEY)

# ---------- SYSTEM PROMPT ----------
SYSTEM_PROMPT = """

You are HealthBuddy — a friendly AI health assistant.

GOAL:
- Help users understand common health symptoms and wellness issues.
- Speak in a warm, conversational tone similar to chatting with a healthcare guide.
- Be short, practical, and supportive.

LANGUAGE RULE:
- Detect the language of the user's message.
- Reply in the same language style:
  - English → English
  - Hindi → Hindi
  - Marathi → Marathi
  - Hinglish → Hinglish
  - Mixed language → respond in the same mix

STYLE:
- Keep responses simple and human-like.
- Use short paragraphs.
- First acknowledge the user's concern.
- Then give 2–4 practical wellness suggestions (diet, routine, lifestyle).
- Ask follow-up questions only when needed.

SAFETY:
- Do not claim to be a licensed doctor.
- Do not prescribe strong medicines or diagnose diseases with certainty.
- Encourage consulting healthcare professionals for serious symptoms.

SCOPE:
- Topics allowed:
  - digestion
  - acidity
  - stress
  - sleep
  - lifestyle
  - exercise
  - diet
  - basic wellness advice

OUT OF SCOPE:
- If the user asks unrelated questions, politely say the assistant only helps with health topics.
"""





# ---------- HELPERS ----------
def call_groq(history):
    """
    history: list of dicts: {"role": "user"/"assistant", "content": "text"}
    returns: assistant reply text
    """
    messages = [{"role": "system", "content": SYSTEM_PROMPT}]
    for m in history:
        # Only allow user/assistant roles
        if m["role"] in ("user", "assistant"):
            messages.append(
                {"role": m["role"], "content": m["content"]}
            )

    try:
        completion = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=messages,
            temperature=0.4,
        )
        reply = completion.choices[0].message.content
    except Exception as e:
        reply = f"Error while calling Groq: {e}"

    return reply


# ---------- STREAMLIT UI ----------
st.set_page_config(page_title="healthbuddy", page_icon="🩺")

# --- CUSTOM CSS FOR CENTERED TITLE ---
# Replaces st.title() and st.subheader() with a centered HTML block
st.markdown(
    """
    <style>
    .title-container {
        text-align: center;
        padding-bottom: 25px;
    }
    .title-container h1 {
        font-size: 2rem;
        font-weight: 600;
        margin-bottom: 0px;
        color: white;
    }
    .title-container h3 {
        font-size: 0.9rem;
        font-weight: 300;
        margin-top: -10px;
        color: #b0b0b0;
    }
    </style>
    
    <div class="title-container">
        <h1>🩺 HealthBuddy</h1>
        <h3>Your AI Health Companion</h3>
    </div>
    """,
    unsafe_allow_html=True
)

# Initialize chat history
if "history" not in st.session_state:
    st.session_state.history = []

# Show previous messages
for msg in st.session_state.history:
    with st.chat_message("user" if msg["role"] == "user" else "assistant"):
        st.markdown(msg["content"])

# ---------- CHAT INPUT ----------
user_input = st.chat_input("Ask your health question...")

if user_input:
    # 1. Add User Message
    st.session_state.history.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    # 2. Get AI Response
    with st.spinner("HealthBuddy is thinking..."):
        reply = call_groq(st.session_state.history)

    # 3. Add Assistant Message
    st.session_state.history.append({"role": "assistant", "content": reply})
    with st.chat_message("assistant"):
        st.markdown(reply)













