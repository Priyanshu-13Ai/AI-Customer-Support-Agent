import pytest
from agent import run_agent

# Skip tests if no API key is provided to avoid failing CI
import os
pytestmark = pytest.mark.skipif(not os.getenv("GROQ_API_KEY"), reason="Requires GROQ_API_KEY")

def test_valid_order():
    response = run_agent("Where is order ORD-1002?")
    assert "ORD-1002" in response
    assert "Shipped" in response or "shipped" in response.lower()

def test_invalid_order():
    response = run_agent("Track my order ORD-9999.")
    assert "not exist" in response.lower() or "not find" in response.lower() or "couldn't find" in response.lower()

def test_valid_product():
    response = run_agent("Tell me about product P101.")
    assert "Pegasus" in response or "Nike" in response
    assert "4499" in response

def test_invalid_product():
    response = run_agent("Give me details of product P999.")
    assert "not exist" in response.lower() or "not find" in response.lower() or "couldn't find" in response.lower()

def test_search_empty():
    response = run_agent("Show me some spaceships.")
    assert "no matching products" in response.lower() or "not find any" in response.lower() or "no products" in response.lower()

def test_cheaper_alternative():
    response = run_agent("Is there a cheaper alternative to the shoes I ordered in ORD-1001?")
    # ORD-1001 contains P101 (Nike Air Zoom Pegasus 40 - ₹4499)
    # Cheaper running-shoe alternatives in the catalog: P102 (₹2799), P105 (₹1499)
    assert "P102" in response or "P105" in response or "Puma" in response or "Campus" in response

def test_greetings():
    response = run_agent("Hello there!")
    assert "hello" in response.lower() or "hi " in response.lower() or "how can i help" in response.lower()

def test_unrelated_questions():
    response = run_agent("What is the capital of France?")
    # It should politefully decline
    assert "store" in response.lower() or "order" in response.lower() or "product" in response.lower() or "cannot" in response.lower() or "can't answer" in response.lower()

def test_conversation_memory_followup_order_id():
    """Regression test for the core bug: the agent must resolve a short
    follow-up (just an order number) using the order ID mentioned earlier
    in the conversation, instead of asking the customer to repeat it."""
    history = [
        {"role": "user", "content": "where is my order"},
        {"role": "assistant", "content": "Could you share your order ID?"},
    ]
    response = run_agent("1002", chat_history=history)
    assert "1002" in response
    assert "shipped" in response.lower()

def test_conversation_memory_what_did_i_order():
    """Regression test: 'what did I order' must chain get_order -> get_product
    and describe the actual product, not just dump raw order fields."""
    history = [
        {"role": "user", "content": "what did i order"},
        {"role": "assistant", "content": "Could you share your order ID?"},
    ]
    response = run_agent("1002", chat_history=history)
    # Should mention the actual product (boAt Airdopes), not just order status
    assert "boAt" in response or "Airdopes" in response or "earbuds" in response.lower()