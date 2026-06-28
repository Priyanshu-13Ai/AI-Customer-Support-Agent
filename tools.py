from langchain.tools import tool
from models import MOCK_ORDERS, MOCK_PRODUCTS
from utils import setup_logger

logger = setup_logger("agent_tools")

@tool
def get_order(order_id: str) -> str:
    """Fetches full details of a customer order given its order_id (e.g. ORD-1001).
    Returns order status, product ordered, shipping details, tracking info, and payment method.
    Use this whenever a customer asks about their order, delivery status, or tracking.
    """
    logger.info(f"Tool called: get_order {order_id}")
    # Normalize: accept "1002" or "ORD-1002"
    order_id = order_id.strip().upper()
    if not order_id.startswith("ORD-"):
        order_id = f"ORD-{order_id}"
    
    order = MOCK_ORDERS.get(order_id)
    if order:
        tracking_info = f"Tracking ID: {order.tracking_id}" if order.tracking_id else "Tracking ID not yet assigned"
        return (
            f"Order {order.id}:\n"
            f"  Customer: {order.customer_name}\n"
            f"  Product ID: {order.product_id}\n"
            f"  Quantity: {order.quantity}\n"
            f"  Total: ₹{order.total_amount}\n"
            f"  Status: {order.status}\n"
            f"  Order Date: {order.order_date}\n"
            f"  Estimated Delivery: {order.estimated_delivery}\n"
            f"  Shipping To: {order.shipping_address}\n"
            f"  Payment: {order.payment_method}\n"
            f"  {tracking_info}"
        )
    return f"No order found with ID {order_id}. Please double-check the order ID and try again."

@tool
def get_product(product_id: str) -> str:
    """Fetches full details of a product given its product_id (e.g. P101).
    Returns name, brand, price, MRP, description, color, sizes, rating, and stock status.
    Use this to give customers detailed product information.
    """
    logger.info(f"Tool called: get_product {product_id}")
    product_id = product_id.strip().upper()
    if not product_id.startswith("P"):
        product_id = f"P{product_id}"
        
    product = MOCK_PRODUCTS.get(product_id)
    if product:
        discount = round((1 - product.price / product.original_price) * 100)
        stock = "In Stock ✅" if product.in_stock else "Out of Stock ❌"
        return (
            f"Product {product.id}: {product.name}\n"
            f"  Brand: {product.brand}\n"
            f"  Category: {product.category}\n"
            f"  Price: ₹{product.price} (MRP ₹{product.original_price}, {discount}% off)\n"
            f"  Description: {product.description}\n"
            f"  Color: {product.color}\n"
            f"  Sizes: {', '.join(product.size_available)}\n"
            f"  Rating: {product.rating}/5 ({product.reviews_count} reviews)\n"
            f"  Availability: {stock}"
        )
    return f"No product found with ID {product_id}. Please check the product ID."

@tool
def search_products(query: str) -> str:
    """Searches the product catalog using a text query.
    Supports searching by name, brand, category, color, description keywords, and price ranges.
    Examples: 'running shoes', 'black sneakers under 3000', 'earbuds', 'Nike', 'backpack'.
    Use this to find products, recommend alternatives, or browse the catalog.
    """
    logger.info(f"Tool called: search_products {query}")
    query_lower = query.lower()
    
    # Extract price constraints from query
    max_price = None
    min_price = None
    import re
    # Match patterns like "under 3000", "below 5000", "upto 2000"
    under_match = re.search(r'(?:under|below|upto|up to|less than|within|max)\s*₹?\s*(\d+)', query_lower)
    if under_match:
        max_price = float(under_match.group(1))
    # Match patterns like "above 1000", "over 2000", "min 500"  
    above_match = re.search(r'(?:above|over|more than|min|minimum|starting)\s*₹?\s*(\d+)', query_lower)
    if above_match:
        min_price = float(above_match.group(1))
    # Match "range X to Y" or "between X and Y"
    range_match = re.search(r'(?:range|between)\s*₹?\s*(\d+)\s*(?:to|and|-)\s*₹?\s*(\d+)', query_lower)
    if range_match:
        min_price = float(range_match.group(1))
        max_price = float(range_match.group(2))

    # Remove price phrases from query for text matching
    text_query = re.sub(r'(?:under|below|upto|up to|less than|within|max|above|over|more than|min|minimum|starting|range|between)\s*₹?\s*\d+\s*(?:to|and|-)?\s*₹?\s*\d*', '', query_lower).strip()
    # Clean leftover words
    text_query = re.sub(r'\s+', ' ', text_query).strip()
    
    # Split query into keywords for flexible matching
    keywords = [kw for kw in text_query.split() if len(kw) > 1] if text_query else []

    results = []
    for p in MOCK_PRODUCTS.values():
        # Price filter
        if max_price and p.price > max_price:
            continue
        if min_price and p.price < min_price:
            continue
            
        # Text matching: check if ANY keyword matches any searchable field
        if keywords:
            searchable = f"{p.name} {p.brand} {p.category} {p.color} {p.description}".lower()
            if not any(kw in searchable for kw in keywords):
                continue
        elif not max_price and not min_price:
            # No keywords and no price filter means empty query
            continue
                
        results.append(p)
    
    if not results:
        return f"No matching products found for '{query}'. Try different keywords or a broader search."
        
    results.sort(key=lambda p: p.price)
    lines = []
    for p in results:
        discount = round((1 - p.price / p.original_price) * 100)
        lines.append(f"- {p.id}: {p.name} ({p.brand}) — ₹{p.price} (MRP ₹{p.original_price}, {discount}% off) | {p.rating}⭐ ({p.reviews_count} reviews) | Color: {p.color}")
    return f"Found {len(results)} product(s):\n" + "\n".join(lines)
