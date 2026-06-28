# 🤖 AI Customer Support Agent

A production-quality AI-powered Customer Support Agent built using **LangGraph**, **LangChain**, **Groq Llama-4 Scout**, and **Streamlit**.

The agent answers customer queries about orders and products by intelligently selecting the appropriate tool, performing multi-step reasoning (tool chaining), and generating natural, customer-friendly responses.

---

# 🚀 Features

* Intelligent tool selection using LangGraph ReAct Agent
* Multi-step reasoning (Tool Chaining)
* Customer-friendly conversational responses
* Order tracking
* Product information retrieval
* Product search & recommendations
* Cheaper alternative recommendations
* Robust error handling
* Logging for debugging and monitoring
* Streamlit-based chat interface
* Unit tests using Pytest

---

# 📌 Project Workflow

Streamlit
     │
     ▼
agent.py
     │
     ▼
ChatGroq (LangChain Integration)
     │
     ▼
LangGraph create_react_agent()
     │
     ▼
LangChain Tools
(get_order, get_product, search_products)
     │
     ▼
Response

# 🧠 How the Agent Thinks

Instead of hardcoding logic, the AI agent reasons step-by-step.

Example:

### User

```
Is there a cheaper alternative to the shoes I ordered in ORD-1001?
```

### Agent Reasoning

```
Step 1
↓

Call get_order()

↓

Find Product ID

↓

Call get_product()

↓

Identify Category

↓

Call search_products()

↓

Compare Prices

↓

Recommend cheaper product

↓

Generate natural language response
```

This demonstrates **tool chaining**, one of the primary objectives of the assignment.

---

# 📂 Project Structure

```
AI-Customer-Support-Agent/

│── app.py
│── agent.py
│── tools.py
│── models.py
│── prompts.py
│── utils.py
│── requirements.txt
│── README.md
│── DESIGN.md
│── test_agent.py
│── .env.example
│── .gitignore
```

---

# 📄 File Responsibilities

### app.py

* Streamlit chat interface
* Handles user interaction
* Maintains chat session
* Displays responses

---

### agent.py

Responsible for:

* Initializing Groq LLM
* Building LangGraph ReAct Agent
* Registering available tools
* Executing reasoning
* Returning final response

---

### tools.py

Contains all business tools.

Current tools:

* get_order()
* get_product()
* search_products()

Each tool is decorated using LangChain's `@tool`.

---

### models.py

Contains:

* Pydantic Models
* Mock Orders Database
* Mock Products Database

Acts as the application's data layer.

---

### prompts.py

Defines the system prompt.

It instructs the LLM to:

* Never hallucinate
* Always use tools
* Perform tool chaining
* Generate customer-friendly responses

---

### utils.py

Contains reusable utilities.

Currently provides:

* Centralized logging

---

### test_agent.py

Contains unit tests validating:

* Order lookup
* Product lookup
* Invalid IDs
* Greetings
* Search
* Cheaper alternatives

---

# ⚙️ Technologies Used

* Python 3.9+
* LangChain
* LangGraph
* Groq API
* Llama-4 Scout
* Streamlit
* Pydantic
* Python-dotenv
* Pytest

---

# 📦 Installation

Clone the repository

```bash
git clone <repository-url>
```

Move into the project

```bash
cd AI-Customer-Support-Agent
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

# 🔑 Environment Variables

Create a `.env` file.

```
GROQ_API_KEY=your_groq_api_key_here
```

> **Note:** The `.env` file is intentionally excluded from GitHub using `.gitignore` for security.

---

# ▶️ Running the Application

Start the Streamlit application

```bash
streamlit run app.py
```

The application will open automatically in your browser.

---

# 🧪 Running Tests

```bash
pytest test_agent.py -v
```

---

# 💬 Example Queries

```
Where is my order ORD-1002?

Track my order ORD-1001.

Tell me about product P101.

Show black running shoes.

Show wireless earbuds under 3000.

Is there a cheaper alternative to the shoes I ordered in ORD-1001?

Hello

What did I order in ORD-1003?
```

---

# 📸 Example Conversation

**User**

```
Where is order ORD-1002?
```

↓

**Agent**

```
Order Status : Shipped

Estimated Delivery :
29 June

Tracking ID :
BLUEDART-77291034
```

---

**User**

```
Tell me about product P205
```

↓

**Agent**

```
Product:
boAt Airdopes 141

Category:
Wireless Earbuds

Price:
₹1299

Rating:
4.1⭐
```

---

# 📈 Future Improvements

* Database Integration (PostgreSQL / MySQL)
* Authentication
* Conversation Memory using LangGraph Checkpointer
* Real Shipping API Integration
* Vector Database for Product Search
* Semantic Search using Embeddings
* Streaming Responses
* Multi-language Support
* Admin Dashboard
* Deployment on Cloud

---

# 📚 Learning Outcomes

This project demonstrates practical understanding of:

* AI Agents
* LangGraph
* LangChain Tools
* ReAct Pattern
* Tool Chaining
* Prompt Engineering
* Structured Logging
* LLM Integration
* Streamlit
* Software Design Principles

---

# 👨‍💻 Author

Developed as part of an AI Agent assignment to demonstrate intelligent tool selection, reasoning, tool chaining, and customer-focused conversational AI.
