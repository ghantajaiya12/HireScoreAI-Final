# HireScore AI 💼🤖

An AI-powered Resume Analyzer built with Python, Streamlit, and HuggingFace models.

## 🌟 Features
- Upload your resume and paste job description
- Get a match score + skills comparison
- AI-powered resume improvement suggestions
- Fully mobile-friendly and deployed on Streamlit Cloud

## 🚀 Live App
👉 [Launch HireScore AI]([https://your-app-name.streamlit.app](https://hirescoreai-final-9w674n3gfeajhaj5eanv3m.streamlit.app/#hire-score-ai))

## 🧠 Tech Stack
- Python
- Streamlit
- Transformers (`distilgpt2`, switchable to Falcon/Mistral)
- HuggingFace Pipelines

## 📦 Setup Locally
```bash
git clone https://github.com/ghantajaiya12/HireScoreAI-Final.git
cd HireScoreAI-Final
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
streamlit run app.py
