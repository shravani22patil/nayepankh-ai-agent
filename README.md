# 🌱 PankhAssist: Smart NGO Volunteer & Inquiry AI Agent

[![Python](https://img.shields.io/badge/Python-3.9%2B-blue.svg)](https://www.python.org/)
[![Framework](https://img.shields.io/badge/GenAI_SDK-Google_Gemini-orange.svg)](https://ai.google.dev/)
[![UI](https://img.shields.io/badge/UI-Streamlit-FF4B4B.svg)](https://streamlit.io/)
[![License](https://img.shields.io/badge/Status-Production__Ready-green.svg)]()

> **Live Demo:** [Click Here to View the Live Agent](https://your-app-name.streamlit.app) *(Replace with your actual Streamlit link)*

---

## 📋 Project Overview

Non-Profit Organizations (NGOs) like **NayePankh Foundation** operate at the intersection of high public engagement and lean operational teams. They frequently handle a massive influx of repetitive inquiries from potential student volunteers, donors, and partners. Delayed response times can result in lost advocacy and dropped engagement.

**PankhAssist** is an intelligent, single-agent conversational workflow designed to act as an automated digital helpdesk. It natively manages context, answers institutional questions based on system-level core values, maintains chat persistence, and dynamically triggers database registration hooks when volunteer intent is recognized.

### Key Objectives Achieved:
*   **Minimized Operational Overhead:** Automates the top-of-funnel volunteer screening and Q&A process.
*   **Deterministic Execution via Tool Use:** Uses function calling rather than unreliable regex parsing to capture structured user information.
*   **Accessible Engineering:** Built cleanly to demonstrate that high-impact AI tools can be lightweight, maintainable, and cost-efficient.

---

## 🏗️ System Architecture & Data Flow

The architecture focuses on a single-agent state machine that evaluates natural language intent against programmatic tool parameters before executing functions.

[ User Input Text ]
│
▼
[ Streamlit Session State ] <─── (Appends conversation memory context)
│
▼
[ Gemini 2.5 Flash Model ] 🪐 <── (Guided by explicit System Instructions)
│
┌────┴────────────────────────┐
▼                             ▼
[Intent: Casual/NGO Q&A]    [Intent: Explicit Volunteer Registration]
│                             │
▼                             ▼
Generates Contextual Text   Extracts: {name, email, interest_area}
│
▼
[ register_volunteer() Function ] ⚙️
│
▼
Simulates Database/CRM Entry via Mock API

---

## ✨ Features Breakdown

### 1. Persistent Context Management (Memory)
Unlike standard stateless LLM completions, the agent leverages Streamlit's `session_state` to dynamically append the entire conversational array (`user` and `model` turns) into the payload. This allows the model to remember a user’s name or chosen interest area even if specified three sentences prior.

### 2. Intelligent Tool Calling (Function Calling)
Rather than relying on the model to merely say *"I have written down your details,"* this agent implements **Function Calling**. The model intelligently realizes when it has gathered sufficient arguments (`name`, `email`, `interest_area`) and safely drops out of "text generation mode" to execute a programmatic backend task.

### 3. Graceful Server Exception Handling
To ensure enterprise-grade stability, the generation engine is wrapped in proactive `try-except` blocks. If Google's free-tier servers experience localized demand spikes (e.g., HTTP 503 errors), the app catches the exception gracefully, rendering an elegant user-facing message instead of breaking the UI with a raw Python stack trace.

---

## 🛠️ Tech Stack & Dependencies

*   **Language:** Python 3.9+
*   **Core AI SDK:** `google-genai` (The newest native Google GenAI implementation framework)
*   **Foundation Model:** `gemini-2.5-flash` (Optimized for low-latency token generation and accurate tool execution)
*   **Frontend UI:** `Streamlit` (Selected for fast prototyping, lightweight state management, and clear scannability)

---

## 🚀 Local Installation & Deployment

### 1. Clone the Repository
```bash
git clone [https://github.com/your-username/nayepankh-ai-volunteer-agent.git](https://github.com/your-username/nayepankh-ai-volunteer-agent.git)
cd nayepankh-ai-volunteer-agent

2. Configure Environment & Install Dependencies
It is recommended to run this within a clean virtual environment:

Bash
pip install -r requirements.txt
3. Set Up Your API Credentials
Acquire a developer API key from Google AI Studio. Set it in your local environment variables:

Windows (Command Prompt): set GEMINI_API_KEY="your_api_key_here"

Windows (PowerShell): $env:GEMINI_API_KEY="your_api_key_here"

Mac/Linux: export GEMINI_API_KEY="your_api_key_here"

4. Execute the Application
Bash
streamlit run app.py

### 🔮 Future Scalability Roadmap
If scaled into an enterprise-level organizational utility, the architecture is designed to support the following enhancements:

Retrieval-Augmented Generation (RAG): Connecting the agent to a Vector Database (like ChromaDB or Pinecone) containing complete NGO training manuals, compliance documents, and localized guidelines to expand the agent's knowledge baseline dynamically.

Multi-Agent Orchestration: Upgrading the workflow to a multi-agent cooperative framework (e.g., using CrewAI or LangGraph) where specialized agents are spun up explicitly for Donor Management, Social Media Content Drafting, and Public Grievance Redressal.

True Webhook Integration: Replacing the simulated mock function with live HTTP requests targeting a CRM platform (like HubSpot, Salesforce, or Google Sheets API).

### 👤 Developer Profile & Contact
Role: AI Agent Developer Intern

Focus Domains: Generative AI Workflows, Retrieval-Augmented Generation (RAG), Agentic Automation Systems.

GitHub: @your-profile

LinkedIn: Your Name

Developed with care to support the mission of youth empowerment and social development at NayePankh Foundation.
