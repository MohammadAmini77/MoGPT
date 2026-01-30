
# 🤖 MoGPT — Local ChatGPT Powered by Ollama

MoGPT is a **local, private ChatGPT-like interface** built on top of **Ollama**, allowing you to run and chat with large language models entirely on your own machine.  
Fast, lightweight, and privacy-friendly — no data leaves your system.

![MoGPT Screenshot](https://github.com/user-attachments/assets/d879a7cf-a24d-427f-a6df-0e2a75748b3e)


---

## ✨ Features

- 🔒 **Fully Local & Private** — No cloud, no data sharing  
- ⚡ **Fast Inference** using Ollama
- 🧠 **Multiple Model Support**
  - `gemma2:2b`
  - `gemma3:12b`
  - `qwen3:4b`
- 💬 **Chat-style UI** similar to ChatGPT
- 🔁 **Switch models on the fly**
- 🖥️ **Clean & modern web interface**
- 🧩 Easy to extend and customize

---

## 🛠️ Tech Stack

- **Backend**: Ollama
- **Frontend**: Web UI (Streamlit-style interface)
- **Models**: Gemma, Qwen (via Ollama)
- **Runtime**: Localhost (`http://localhost:8501`)

---

## 🚀 Getting Started

### 1️⃣ Install Ollama
Make sure Ollama is installed and running:

```bash

https://ollama.com/download


ollama --version
```


### 2️⃣ Pull Models
```bash
ollama pull gemma2:2b
ollama pull gemma3:12b
ollama pull qwen3:4b

```

### 3️⃣ Clone the Repository

```bash
git clone https://github.com/MohammadAmini77/MoGPT.git
cd MoGPT
```


### 4️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 5️⃣ Run MoGPT
```bash
streamlit run app.py

```


http://localhost:8501

```

