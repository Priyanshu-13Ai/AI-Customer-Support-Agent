from pydantic import BaseModel
from typing import Optional, List

class Order(BaseModel):
    """Represents a customer order with shipping and payment details."""
    id: str
    customer_name: str
    product_id: str
    status: str
    quantity: int
    total_amount: float
    order_date: str
    estimated_delivery: str
    shipping_address: str
    payment_method: str
    tracking_id: Optional[str] = None

class Product(BaseModel):
    """Represents a product in the store catalog."""
    id: str
    name: str
    brand: str
    category: str
    price: float
    original_price: float  # MRP before discount
    description: str
    color: str
    size_available: List[str]
    rating: float
    reviews_count: int
    in_stock: bool

# ──────────────────────────────────────────────
# Mock Orders Database
# ──────────────────────────────────────────────
MOCK_ORDERS = {
    "ORD-1001": Order(
        id="ORD-1001", customer_name="Rahul Sharma", product_id="P101",
        status="Delivered", quantity=1, total_amount=4499.0,
        order_date="2026-06-15", estimated_delivery="2026-06-20",
        shipping_address="Flat 302, Sunshine Apartments, Andheri West, Mumbai 400058",
        payment_method="UPI (PhonePe)", tracking_id="DTDC-88432917"
    ),
    "ORD-1002": Order(
        id="ORD-1002", customer_name="Priya Patel", product_id="P205",
        status="Shipped", quantity=1, total_amount=3999.0,
        order_date="2026-06-22", estimated_delivery="2026-06-29",
        shipping_address="12, MG Road, Koramangala, Bangalore 560034",
        payment_method="Credit Card (HDFC)", tracking_id="BLUEDART-77291034"
    ),
    "ORD-1003": Order(
        id="ORD-1003", customer_name="Amit Verma", product_id="P302",
        status="Processing", quantity=2, total_amount=1998.0,
        order_date="2026-06-27", estimated_delivery="2026-07-03",
        shipping_address="45, Sector 18, Noida, UP 201301",
        payment_method="Cash on Delivery", tracking_id=None
    ),
    "ORD-1004": Order(
        id="ORD-1004", customer_name="Sneha Kulkarni", product_id="P104",
        status="Out for Delivery", quantity=1, total_amount=2999.0,
        order_date="2026-06-25", estimated_delivery="2026-06-28",
        shipping_address="78, FC Road, Shivajinagar, Pune 411005",
        payment_method="Debit Card (SBI)", tracking_id="DELHIVERY-55938201"
    ),
    "ORD-1005": Order(
        id="ORD-1005", customer_name="Vikram Singh", product_id="P401",
        status="Cancelled", quantity=1, total_amount=0.0,
        order_date="2026-06-20", estimated_delivery="N/A",
        shipping_address="23, Civil Lines, Jaipur 302006",
        payment_method="UPI (GPay)", tracking_id=None
    ),
    "ORD-1006": Order(
        id="ORD-1006", customer_name="Neha Gupta", product_id="P502",
        status="Return Initiated", quantity=1, total_amount=1299.0,
        order_date="2026-06-10", estimated_delivery="2026-06-14",
        shipping_address="90, Park Street, Kolkata 700016",
        payment_method="Net Banking (ICICI)", tracking_id="ECOM-33019287"
    ),
}

# ──────────────────────────────────────────────
# Mock Products Database
# ──────────────────────────────────────────────
MOCK_PRODUCTS = {
    # ── Shoes ──
    "P101": Product(
        id="P101", name="Nike Air Zoom Pegasus 40", brand="Nike",
        category="Running Shoes", price=4499.0, original_price=5999.0,
        description="Lightweight, responsive running shoes with Air Zoom cushioning. Breathable mesh upper for all-day comfort. Perfect for daily runs and marathon training.",
        color="Black/White", size_available=["UK 7", "UK 8", "UK 9", "UK 10", "UK 11"],
        rating=4.5, reviews_count=2340, in_stock=True
    ),
    "P102": Product(
        id="P102", name="Puma Velocity Nitro 2", brand="Puma",
        category="Running Shoes", price=2799.0, original_price=3999.0,
        description="Affordable and reliable running shoes with NITRO foam midsole. Great grip and durability for beginners and daily joggers.",
        color="Black/Red", size_available=["UK 6", "UK 7", "UK 8", "UK 9", "UK 10"],
        rating=4.2, reviews_count=1580, in_stock=True
    ),
    "P103": Product(
        id="P103", name="Adidas Ultraboost Light", brand="Adidas",
        category="Running Shoes", price=6999.0, original_price=8999.0,
        description="Premium cushioned running shoes with BOOST midsole and Continental rubber outsole. Ultra-responsive energy return for serious runners.",
        color="Cloud White", size_available=["UK 7", "UK 8", "UK 9", "UK 10"],
        rating=4.7, reviews_count=3120, in_stock=True
    ),
    "P104": Product(
        id="P104", name="Skechers D'Lux Walker", brand="Skechers",
        category="Casual Shoes", price=2999.0, original_price=3499.0,
        description="Comfortable casual sneakers with Air-Cooled Memory Foam insole. Stylish and lightweight for everyday wear.",
        color="Navy Blue", size_available=["UK 7", "UK 8", "UK 9", "UK 10", "UK 11"],
        rating=4.3, reviews_count=987, in_stock=True
    ),
    "P105": Product(
        id="P105", name="Campus Action Pro", brand="Campus",
        category="Running Shoes", price=1499.0, original_price=1999.0,
        description="Budget-friendly black running shoes. Lightweight EVA sole for cushioning. Ideal for gym workouts and casual running.",
        color="Black", size_available=["UK 6", "UK 7", "UK 8", "UK 9", "UK 10"],
        rating=3.9, reviews_count=4520, in_stock=True
    ),

    # ── Electronics ──
    "P205": Product(
        id="P205", name="boAt Airdopes 141", brand="boAt",
        category="Wireless Earbuds", price=1299.0, original_price=2990.0,
        description="True wireless earbuds with 42-hour total playback, 8mm drivers, ENx noise cancellation for calls, IPX4 water resistance, and Bluetooth 5.3.",
        color="Bold Black", size_available=["One Size"],
        rating=4.1, reviews_count=89320, in_stock=True
    ),
    "P206": Product(
        id="P206", name="Sony WF-C700N", brand="Sony",
        category="Wireless Earbuds", price=4999.0, original_price=6990.0,
        description="Active noise cancelling wireless earbuds with DSEE audio upscaler, multipoint connection, 15-hour battery, and IPX4 water resistance.",
        color="Lavender", size_available=["One Size"],
        rating=4.4, reviews_count=5620, in_stock=True
    ),
    "P207": Product(
        id="P207", name="JBL Tune 230NC", brand="JBL",
        category="Wireless Earbuds", price=3499.0, original_price=4999.0,
        description="JBL Pure Bass sound with active noise cancellation, 40-hour battery life, 4 microphones for perfect calls, and speed charge.",
        color="Black", size_available=["One Size"],
        rating=4.3, reviews_count=12450, in_stock=True
    ),
    "P208": Product(
        id="P208", name="Samsung Galaxy Watch 6", brand="Samsung",
        category="Smartwatch", price=18999.0, original_price=23999.0,
        description="Premium smartwatch with BioActive sensor, heart rate and sleep tracking, sapphire crystal glass, Wear OS, and 40-hour battery life.",
        color="Graphite", size_available=["40mm", "44mm"],
        rating=4.5, reviews_count=3450, in_stock=True
    ),

    # ── Fitness ──
    "P302": Product(
        id="P302", name="Boldfit Yoga Mat 6mm", brand="Boldfit",
        category="Yoga Mat", price=599.0, original_price=999.0,
        description="Anti-slip yoga mat with alignment lines, 6mm thickness for joint comfort, lightweight and portable with carry strap included.",
        color="Blue", size_available=["6mm"],
        rating=4.2, reviews_count=15670, in_stock=True
    ),
    "P303": Product(
        id="P303", name="Boldfit Resistance Bands Set", brand="Boldfit",
        category="Fitness Accessories", price=449.0, original_price=799.0,
        description="Set of 5 resistance bands (extra light to extra heavy). Latex-free, skin-friendly. Great for home workouts, physiotherapy, and stretching.",
        color="Multicolor", size_available=["One Size"],
        rating=4.3, reviews_count=8930, in_stock=True
    ),

    # ── Bags ──
    "P401": Product(
        id="P401", name="American Tourister Urban Groove", brand="American Tourister",
        category="Backpack", price=1899.0, original_price=2800.0,
        description="32L laptop backpack with padded laptop compartment (fits up to 15.6 inch), water-resistant fabric, multiple organizer pockets, and padded shoulder straps.",
        color="Black", size_available=["One Size"],
        rating=4.4, reviews_count=6780, in_stock=True
    ),
    "P402": Product(
        id="P402", name="Wildcraft Blaze 45L", brand="Wildcraft",
        category="Trekking Bag", price=2499.0, original_price=3499.0,
        description="45-litre trekking backpack with rain cover, chest and hip strap, hydration sleeve, and durable rip-stop fabric. Perfect for weekend treks.",
        color="Olive Green", size_available=["One Size"],
        rating=4.5, reviews_count=2340, in_stock=True
    ),

    # ── Clothing ──
    "P502": Product(
        id="P502", name="Allen Solly Polo T-Shirt", brand="Allen Solly",
        category="T-Shirt", price=899.0, original_price=1299.0,
        description="Classic cotton polo t-shirt with ribbed collar and cuffs, button placket, and embroidered logo. Regular fit for casual and semi-formal wear.",
        color="White", size_available=["S", "M", "L", "XL", "XXL"],
        rating=4.1, reviews_count=7890, in_stock=True
    ),
    "P503": Product(
        id="P503", name="Levi's 511 Slim Fit Jeans", brand="Levi's",
        category="Jeans", price=2199.0, original_price=3299.0,
        description="Iconic slim fit jeans with stretch denim, sits below waist, slim through hip and thigh. Classic 5-pocket styling. Versatile everyday wear.",
        color="Dark Indigo", size_available=["30", "32", "34", "36"],
        rating=4.6, reviews_count=11230, in_stock=True
    ),
}