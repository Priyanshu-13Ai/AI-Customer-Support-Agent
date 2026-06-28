# Architecture & Design Decisions

## Overview

This project implements an AI-powered Customer Support Agent using the **ReAct (Reason + Act)** pattern. Instead of relying on hardcoded business logic, the agent analyzes the user's request, determines which tool(s) should be used, executes them, and generates a natural language response.

The implementation combines:

* LangChain (LLM integration, tools, prompts)
* LangGraph (`create_react_agent`) for reasoning and tool orchestration
* Groq Llama-4 Scout as the language model
* Streamlit as the user interface

---

# Overall Architecture

```text
                User
                  │
                  ▼
        Streamlit Interface
             (app.py)
                  │
                  ▼
         LangGraph ReAct Agent
            (agent.py)
                  │
                  ▼
        Groq Llama-4 Scout LLM
                  │
                  ▼
     Chooses Appropriate Tool(s)
      ┌──────────┼──────────┐
      ▼          ▼          ▼
 get_order   get_product  search_products
      │          │          │
      └──────────┼──────────┘
                  ▼
         Tool Results Combined
                  ▼
      Customer-Friendly Response
```

---

# Why This Architecture?

The project follows a modular architecture where every file has a single responsibility.

### app.py

Responsible for:

* Streamlit interface
* User interaction
* Chat history
* Displaying responses

---

### agent.py

Responsible for:

* Initializing the Groq LLM
* Creating the LangGraph ReAct Agent
* Registering available tools
* Executing reasoning
* Returning the final response

---

### tools.py

Contains all business logic.

Available tools:

* get_order()
* get_product()
* search_products()

Each tool performs only one specific task, making the system easy to extend and test.

---

### models.py

Acts as the application's data layer.

Contains:

* Pydantic Models
* Mock Orders
* Mock Products

---

### prompts.py

Defines the system instructions that guide the LLM.

The prompt controls:

* Tool selection
* Tool chaining
* Response style
* Hallucination prevention

---

### utils.py

Contains reusable helper utilities.

Currently:

* Centralized logging

---

# Why LangChain?

LangChain provides:

* LLM integrations
* Tool abstraction (`@tool`)
* Prompt management
* Message handling

It simplifies communication between the language model and the application's tools.

---

# Why LangGraph?

Although LangChain provides tools and prompts, LangGraph provides a structured way to build AI agents.

This project uses:

* `create_react_agent()`

Advantages include:

* Native ReAct implementation
* Automatic tool execution
* Multi-step reasoning
* Better scalability for future workflows

---

# Why Groq?

The project uses **Groq** with the **Llama-4 Scout** model because it offers:

* Very low latency
* Fast inference
* Strong tool-calling capabilities
* High-quality conversational responses

This makes it suitable for real-time customer support applications.

---

# Why ReAct?

The ReAct (Reason + Act) pattern allows the model to think before acting.

Instead of generating an answer immediately, it reasons about:

* Which information is required
* Which tool should be used
* Whether additional tools are needed
* How to combine the results

This significantly reduces hallucinations.

---

# Tool Chaining

Some customer questions require multiple tools.

Example:

### User

> Is there a cheaper alternative to the shoes I ordered in ORD-1001?

The reasoning process becomes:

```text
Step 1
Call get_order()

↓

Retrieve Product ID

↓

Call get_product()

↓

Understand category and price

↓

Call search_products()

↓

Compare products

↓

Recommend cheaper alternative

↓

Generate final response
```

The agent performs this reasoning automatically.

---

# Hallucination Prevention

To minimize incorrect responses, the project follows several safeguards.

### 1. Strict System Prompt

The prompt explicitly instructs the LLM to:

* Never invent orders
* Never invent products
* Always use tools
* Never answer without tool results

---

### 2. Tool-Based Retrieval

All order and product information comes from deterministic tools.

The language model never directly generates factual order or product data.

---

### 3. Controlled Mock Database

The application only accesses predefined mock datasets.

This guarantees predictable behavior during testing.

---

# Logging

Logging has been implemented throughout the project.

Every important action is logged, including:

* Agent execution
* Tool invocation
* Errors
* Final response generation

Example:

```text
INFO Agent started for question...

INFO Tool called: get_order ORD-1002

INFO Final response generated
```

Logging simplifies debugging and helps understand the agent's reasoning flow.

---

# Error Handling

The application gracefully handles common failures.

Examples include:

* Missing API key
* Invalid Order ID
* Invalid Product ID
* Empty search results
* Tool execution failures

Instead of crashing, the agent returns meaningful messages.

---

# Design Trade-offs

Current implementation uses an in-memory mock database.

Advantages:

* Easy to test
* Fast execution
* No external dependencies

Limitations:

* Data is not persistent
* No authentication
* No real order tracking
* Limited scalability

This trade-off keeps the project simple while demonstrating AI agent reasoning.

---

# Future Improvements

Possible production enhancements include:

* PostgreSQL/MySQL integration
* Authentication and user accounts
* LangGraph Checkpointer for persistent memory
* Real shipping and tracking APIs
* Semantic product search using embeddings
* Vector database integration
* Streaming responses
* Multi-language support
* Cloud deployment
* Admin dashboard

---

# Conclusion

The project demonstrates a modular AI agent architecture where the LLM performs reasoning while specialized tools provide reliable data.

By combining LangChain, LangGraph, Groq, and Streamlit, the application showcases:

* Intelligent tool selection
* Multi-step reasoning
* Tool chaining
* Prompt engineering
* Structured logging
* Clean software architecture

The design is intentionally modular, making it easy to replace the mock database with real backend services in the future while preserving the overall agent workflow.
