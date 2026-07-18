import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langgraph.prebuilt import create_react_agent
from langchain_core.messages import SystemMessage

from tools import get_order, get_product, search_products
from prompts import SYSTEM_PROMPT
from utils import setup_logger

load_dotenv()
logger = setup_logger("agent_core")

def build_agent():
    """Builds and returns the LangGraph ReAct agent."""
    tools = [get_order, get_product, search_products]
    
    # Initialize the LLM (Groq - fast inference)
    api_key = os.getenv("GROQ_API_KEY")
    if not api_key:
        logger.warning("GROQ_API_KEY not found in environment.")
        
    llm = ChatGroq(
        model="llama-3.3-70b-versatile", 
        temperature=0,
        groq_api_key=api_key
    )
    
    agent = create_react_agent(llm, tools, prompt=SystemMessage(content=SYSTEM_PROMPT))
    return agent

# Global instance for app to use
try:
    AGENT = build_agent()
except Exception as e:
    logger.error(f"Failed to build agent executor: {e}")
    AGENT = None

def run_agent(question: str, chat_history: list | None = None) -> str:
    """Main entrypoint for the agent as required by the assignment.

    Args:
        question: The latest user message.
        chat_history: Prior turns as a list of dicts like
            {"role": "user"/"assistant", "content": "..."}, e.g. the same
            list Streamlit keeps in st.session_state.messages (excluding the
            current question). This is what gives the agent memory of
            earlier turns so follow-ups like "1002" can be resolved in
            context instead of being treated as a brand-new conversation.
    """
    logger.info(f"Agent started for question: '{question}'")

    global AGENT
    # Reload environment in case the user just added the key
    load_dotenv(override=True)

    if not AGENT:
        try:
            AGENT = build_agent()
        except Exception as e:
            logger.error(f"Failed to build agent executor during run: {e}")

    if not AGENT:
        return "System configuration error: LLM could not be initialized. Please check API keys."

    # Build the full message list: prior turns + the new question.
    # LangGraph/LangChain accept (role, content) tuples directly.
    # Cap history to the most recent turns to keep latency/cost bounded on
    # long conversations, while still giving the agent enough context to
    # resolve short follow-ups like "1002".
    MAX_HISTORY_TURNS = 12
    trimmed_history = (chat_history or [])[-MAX_HISTORY_TURNS:]

    messages = []
    for turn in trimmed_history:
        role = turn.get("role")
        content = turn.get("content", "")
        if role == "assistant":
            messages.append(("assistant", content))
        else:
            messages.append(("user", content))
    messages.append(("user", question))

    try:
        response = AGENT.invoke({"messages": messages})
        logger.info("Final response generated")
        # The output messages contain the conversation, the last is the AI response
        return response["messages"][-1].content
    except Exception as e:
        logger.error(f"Error generating response: {e}")
        return "I'm sorry, I encountered an issue processing your request."