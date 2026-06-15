import streamlit as st

# --------------------------------------------------
# PAGE CONFIG
# --------------------------------------------------
st.set_page_config(
    page_title="MiniStore",
    page_icon="🛍️",
    layout="wide"
)

# --------------------------------------------------
# PRODUCT DATA
# --------------------------------------------------
PRODUCTS = [
    {
        "name": "Wireless Bluetooth Headphones",
        "price": 79.99,
        "description": "Premium over-ear headphones with noise cancellation and 30-hour battery life.",
        "category": "Electronics"
    },
    {
        "name": "Smart Fitness Watch",
        "price": 129.99,
        "description": "Track heart rate, sleep, workouts, and daily activity.",
        "category": "Electronics"
    },
    {
        "name": "Leather Backpack",
        "price": 59.99,
        "description": "Durable backpack for work, travel and daily use.",
        "category": "Fashion"
    },
    {
        "name": "Running Shoes",
        "price": 89.99,
        "description": "Comfortable lightweight running shoes.",
        "category": "Fashion"
    },
    {
        "name": "Coffee Maker",
        "price": 49.99,
        "description": "Programmable coffee maker for home use.",
        "category": "Home & Kitchen"
    },
    {
        "name": "Portable Laptop Stand",
        "price": 34.99,
        "description": "Adjustable aluminum ergonomic laptop stand.",
        "category": "Office"
    }
]

# Make products available to chatbot page
st.session_state["products"] = PRODUCTS

# --------------------------------------------------
# CSS
# --------------------------------------------------
st.markdown("""
<style>

.hero-section {
    background: linear-gradient(135deg,#2563eb,#7c3aed);
    padding:40px;
    border-radius:15px;
    text-align:center;
    color:white;
    margin-bottom:30px;
}

.hero-title{
    font-size:42px;
    font-weight:bold;
}

.hero-subtitle{
    font-size:18px;
}

.product-card{
    background:white;
    padding:20px;
    border-radius:15px;
    box-shadow:0px 4px 12px rgba(0,0,0,0.08);
    margin-bottom:20px;
}

.product-name{
    font-size:20px;
    font-weight:bold;
}

.product-price{
    color:green;
    font-size:24px;
    font-weight:bold;
}

.product-category{
    display:inline-block;
    background:#e0e7ff;
    padding:5px 12px;
    border-radius:20px;
    font-size:12px;
    margin-bottom:10px;
}

/* Floating Support Button */

.support-button{
    position:fixed;
    bottom:25px;
    right:25px;
    background:#2563eb;
    color:white;
    padding:15px 22px;
    border-radius:50px;
    text-decoration:none;
    font-weight:bold;
    z-index:999;
    box-shadow:0px 4px 15px rgba(0,0,0,0.3);
}

.support-button:hover{
    background:#1d4ed8;
}

</style>
""", unsafe_allow_html=True)

# --------------------------------------------------
# SIDEBAR
# --------------------------------------------------
st.sidebar.title("🛒 MiniStore")

categories = ["All"] + sorted(
    list(set(p["category"] for p in PRODUCTS))
)

selected_category = st.sidebar.selectbox(
    "Categories",
    categories
)

if "cart" not in st.session_state:
    st.session_state.cart = []

st.sidebar.markdown("---")
st.sidebar.subheader("Cart Summary")

st.sidebar.metric(
    "Items",
    len(st.session_state.cart)
)

cart_total = sum(
    item["price"]
    for item in st.session_state.cart
)

st.sidebar.metric(
    "Total",
    f"${cart_total:.2f}"
)

# --------------------------------------------------
# HERO SECTION
# --------------------------------------------------
st.markdown("""
<div class="hero-section">
    <div class="hero-title">
        🛍️ MiniStore
    </div>
    <div class="hero-subtitle">
        Shop smarter with our curated collection
    </div>
</div>
""", unsafe_allow_html=True)

# --------------------------------------------------
# WELCOME
# --------------------------------------------------
st.header("Welcome to MiniStore")

st.write("""
Explore electronics, fashion, office accessories,
and home essentials all in one place.
""")

# --------------------------------------------------
# FILTER PRODUCTS
# --------------------------------------------------
if selected_category == "All":
    filtered_products = PRODUCTS
else:
    filtered_products = [
        p for p in PRODUCTS
        if p["category"] == selected_category
    ]

# --------------------------------------------------
# FEATURED PRODUCTS
# --------------------------------------------------
st.subheader("Featured Products")

cols = st.columns(3)

for i, product in enumerate(filtered_products):

    with cols[i % 3]:

        st.markdown(f"""
        <div class="product-card">
            <div class="product-category">
                {product["category"]}
            </div>

            <div class="product-name">
                {product["name"]}
            </div>

            <p>{product["description"]}</p>

            <div class="product-price">
                ${product["price"]}
            </div>
        </div>
        """, unsafe_allow_html=True)

        if st.button(
            "Add to Cart",
            key=f"cart_{i}"
        ):
            st.session_state.cart.append(product)
            st.success("Added to cart")

# --------------------------------------------------
# FLOATING SUPPORT BUTTON
# --------------------------------------------------
st.markdown("""
<a class="support-button"
href="/Support_Chatbot"
target="_self">
💬 Support
</a>
""", unsafe_allow_html=True)