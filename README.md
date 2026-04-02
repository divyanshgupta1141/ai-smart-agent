# 🤖 Smart AI Agent (LLM-Based Decision System)

## 🚀 Overview
This project is an AI-powered agent that uses a Large Language Model (LLM) to dynamically decide actions and route tasks to appropriate tools.

Unlike traditional rule-based systems, this agent interprets user input and intelligently chooses between:
- Mathematical computation
- Stock data retrieval
- General conversational responses

---

## 🧠 Architecture

User Input  
→ LLM Decision Layer (JSON output)  
→ Tool Execution OR LLM Response  
→ Final Output  

---

## ⚙️ Features
- LLM-based decision making (no hardcoded rules)
- Tool integration (calculator, stock lookup)
- Clean separation of decision and execution layers
- Error handling with fallback logic
- Efficient API usage (no redundant calls)
- Debug mode for development

---

## 🛠️ Tech Stack
- Python
- OpenRouter API
- Llama 3.3 70B Instruct
- JSON-based action routing

---

## ▶️ Installation

git clone https://github.com/Divyanshgupta1141/ai-smart-agent.git
cd ai-smart-agent
pip install -r requirements.txt

---

## 🔑 Setup

Create a `.env` file:

OPENROUTER_API_KEY=your_api_key_here

---

## ▶️ Run

python3 main.py

---

## 💡 Example Queries

- What is 25 * 12?
- Tell me Reliance stock price
- Explain Artificial Intelligence

---

## 🧠 Key Learnings
- Designing LLM-based decision systems
- Building reliable AI agents without tool-calling dependency
- Handling structured outputs (JSON) from LLMs
- Separating reasoning (AI) from execution (code)

---

## ⚡ Design Insight

This project avoids relying on native tool-calling APIs and instead implements a manual decision layer using LLM-generated JSON.  
This ensures higher reliability across different models and environments.

---

## 🚀 Future Improvements
- Integration with real-time APIs (stock, weather, news)
- Multi-step reasoning agents
- Memory and conversation context
- Web-based UI (Streamlit or React)

---

## 👨‍💻 Author
Divyansh Gupta