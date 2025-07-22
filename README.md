
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
- `dotenv` – to load API keys securely  
<br><br>

---

## 🧪 Setup Instructions

1. **Clone the repository:**

```bash
git clone https://github.com/S-Nainika/vidbrief.git
cd vidbrief
```

<br>                                                                                                                                                            

2. **Install dependencies:**

```bash
pip install -r requirements.txt
```

<br>

3. **Add your Gemini API key:**

Create a `.env` file in the root directory and add:

```
GEMINI_API_KEY=your_gemini_api_key_here
```
Get free gemini key from google

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

<img width="914" height="676" alt="image" src="https://github.com/user-attachments/assets/ac90d0ee-0f75-42ce-8330-8608e08f781e" />

<br><br>

---

## ❗ Notes

- only works for english subtitled vedios  
- gTTS requires an internet connection to generate audio.  
<br><br>

---

## 📄 License

This project is open-source and available under the [MIT License](LICENSE).  
<br><br>
