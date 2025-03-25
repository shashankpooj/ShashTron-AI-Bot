# ShashTron AI 🤖

ShashTron AI is a Streamlit-based chatbot powered by **Google Gemini** (via `langchain_google_genai`). It provides interactive AI conversations, taking system role messages and user inputs to generate intelligent responses.

## 🚀 Features
- Utilizes **Google Gemini (Gemini-2.0-flash)** for AI responses.
- Supports **system role messages** for custom behavior.
- Interactive chat interface using **Streamlit** and **streamlit_chat**.
- **Session-based message storage** to maintain chat history.

## 🛠️ Installation
1. Clone the repository:
   git clone https://github.com/your-username/ShashTron-AI.git
   cd ShashTron-AI

2. Create a virtual environment (optional but recommended):
   python -m venv venv
   source venv/bin/activate  # On macOS/Linux
   venv\Scripts\activate     # On Windows
  
3. Install dependencies:
   pip install -r requirements.txt

## 📂 Environment Setup
1. Create a `.env` file in the root directory and add your Google Gemini API key:
   GOOGLE_API_KEY=your_api_key_here
   ```

## ▶️ Running ShashTron AI
Run the Streamlit app using:
streamlit run app.py
```

## 🖥️ Usage
1. Enter a **system role message** in the sidebar (optional).
2. Type a message in the **user input field**.
3. Wait for ShashTron AI's response.
4. Chat history is maintained within the session.

## 📜 Requirements
- Python 3.8+
- `streamlit`
- `streamlit_chat`
- `langchain`
- `langchain_google_genai`
- `python-dotenv`

## 🛠️ Contributing
Feel free to open an **issue** or submit a **pull request** if you find any bugs or have suggestions!

## 📜 License
This project is licensed under the MIT License.

---
Developed with ❤️ by Shashank 🚀

