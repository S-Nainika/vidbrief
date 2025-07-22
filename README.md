
# 🎥 Multilingual YouTube Video Summarizer (Gemini Pro + Streamlit)

This is a simple web app built with **Streamlit** that takes a YouTube video URL and summarizes its transcript into a short paragraph (max 100 words). It supports **English**, **Hindi**, and **Telugu** summaries and generates audio using **gTTS (Google Text-to-Speech)**.  
<br><br>
🚀 Powered by Google’s **Gemini Pro 2.5** model for accurate and contextual summaries.  
<br><br>

---

## 🔧 Features

- 🔍 Fetches transcripts from YouTube videos  
- 🧠 Uses **Gemini Pro** to summarize the content  
- 🌐 Supports multilingual summaries:
  - English
  - Hindi
  - Telugu  
- 🔊 Converts summary to audio using **gTTS**  
- 🎧 Listen to the summary directly in the browser  
<br><br>

---

## 🛠️ Tech Stack

- `Streamlit` – for web interface  
- `youtube-transcript-api` – to fetch video transcripts  
- `Google Generative AI SDK (Gemini Pro)` – for summarization  
- `gTTS` – text-to-speech audio generation  
- `dotenv` – to manage API keys securely  
<br><br>

---

## 🧪 Setup Instructions

1. **Clone the repository:**

```bash
git clone https://github.com/your-username/youtube-summarizer.git
cd youtube-summarizer
```

<br>

2. **Create a virtual environment (optional but recommended):**

```bash
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
```

<br>

3. **Install dependencies:**

```bash
pip install -r requirements.txt
```

<br>

4. **Add your Gemini API key:**

Create a `.env` file in the root directory and add:

```
GEMINI_API_KEY=your_gemini_api_key_here
```

<br><br>

---

## ▶️ Run the App

```bash
streamlit run app.py
```

Replace `app.py` with the filename you saved the code as.  
<br><br>

---

## 📸 Screenshot

> _Add a screenshot of the app interface here if available._  
<br><br>

---

## ❗ Notes

- Works only for videos that have an auto-generated or uploaded transcript.  
- gTTS requires an internet connection to generate audio.  
<br><br>

---

## 📄 License

This project is open-source and available under the [MIT License](LICENSE).  
<br><br>
