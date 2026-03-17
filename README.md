# 🩺 HealthBuddy – AI Health Assistant

HealthBuddy is a conversational AI health assistant built using **Streamlit** and **Groq LLM API**.
It allows users to ask health-related questions and receive simple, practical wellness guidance in a conversational chat interface.

The assistant supports **multiple languages** (English, Hindi, Marathi, and Hinglish) and mirrors the user’s language style automatically.

HealthBuddy focuses on **basic health awareness, lifestyle guidance, and wellness suggestions** in a friendly chat format.

---

# 🚀 Features

### 🧠 AI-Powered Health Chat

Users can ask health-related questions and receive helpful responses powered by an LLM.

### 🌍 Multilingual Support

The assistant automatically detects and replies in:

* English
* Hindi
* Marathi
* Hinglish (Hindi + English mix)

### 💬 Conversational Interface

Built with **Streamlit Chat UI**, making the interaction simple and natural.

### 🩺 Wellness-Focused Guidance

HealthBuddy provides suggestions related to:

* digestion
* sleep
* stress
* lifestyle
* diet
* general wellness

### 🔒 Environment-Based API Keys

API keys are stored securely using `.env`.

---

# 🏗️ Tech Stack

| Technology | Purpose                         |
| ---------- | ------------------------------- |
| Python     | Core programming language       |
| Streamlit  | Web interface                   |
| Groq API   | LLM inference                   |
| dotenv     | Environment variable management |

---

# 📂 Project Structure

```
healthbuddy/
│
├── app.py            # Main Streamlit application
├── .env              # Environment variables (API key)
├── requirements.txt  # Project dependencies
└── README.md         # Project documentation
```

---

# ⚙️ Installation

### 1️⃣ Clone the repository

```bash
git clone https://github.com/yourusername/healthbuddy.git
cd healthbuddy
```

---

### 2️⃣ Create a virtual environment

```bash
python -m venv venv
```

Activate it:

**Windows**

```bash
venv\Scripts\activate
```

**Mac / Linux**

```bash
source venv/bin/activate
```

---

### 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

---

### 4️⃣ Add Groq API Key

Create a `.env` file in the project root:

```
GROQ_API_KEY=your_api_key_here
```

You can get an API key from:

https://console.groq.com

---

# ▶️ Running the Application

Start the Streamlit server:

```bash
streamlit run app.py
```

The app will open in your browser:

```
http://localhost:8501
```

---

# 💬 Example Usage

User:

```
I have acidity after eating spicy food. What should I do?
```

HealthBuddy:

```
Acidity after spicy food is quite common. It usually happens when the stomach produces excess acid.

You can try:
• Eating lighter meals
• Avoiding very spicy or oily foods at night
• Drinking warm water after meals
• Not lying down immediately after eating

Does the acidity happen daily or only after certain foods?
```

---

# ⚠️ Disclaimer

HealthBuddy provides **general health and wellness information only**.

It is **not a substitute for professional medical advice, diagnosis, or treatment**.
Always consult a qualified healthcare professional for medical concerns.

---

# 🌟 Future Improvements

Planned upgrades include:

* symptom triage system
* patient profile memory
* emergency symptom detection
* medical knowledge grounding
* mobile-friendly UI
* deployment on cloud platforms

---

# 👨‍💻 Author

**Sanket Borse**

---

# ⭐ Support

If you like this project:

⭐ Star the repository
🍴 Fork the project
🚀 Contribute improvements
