import streamlit as st

# ---------------------------
# PAGE CONFIGURATION
# ---------------------------
st.set_page_config(
    page_title="MiniStore",
    page_icon="🛍️",
    layout="wide"
)

# ---------------------------
# CUSTOM CSS
# ---------------------------
st.markdown("""
<style>

.main {
    background-color: #f6f8fc;
}

.hero {
    padding: 35px;
    border-radius: 20px;
    background: linear-gradient(90deg,#1e3c72,#2a5298);
    color: white;
    text-align: center;
    margin-bottom: 25px;
}

.hero h1{
    font-size: 50px;
}

.product-card{
    background-color:white;
    padding:20px;
    border-radius:18px;
    box-shadow:0 4px 12px rgba(0,0,0,0.08);
    margin-bottom:20px;
    min-height:340px;
}

.product-card:hover{
    transform: translateY(-5px);
    transition:0.3s;
}

.price{
    font-size:26px;
    color:#1f77ff;
    font-weight:bold;
}

.category{
    background:#eef3ff;
    color:#3366ff;
    padding:6px 10px;
    border-radius:12px;
    display:inline-block;
}

.sidebar-title{
    color:#2a5298;
}

footer{
    text-align:center;
    color:gray;
}

</style>
""", unsafe_allow_html=True)

# ---------------------------
# SAMPLE PRODUCT DATA
# ---------------------------
products = [
    {
        "name": "Wireless Headphones",
        "price": 2999,
        "category": "Electronics",
        "description": "Noise-cancelling headphones with premium sound."
    },

    {
        "name": "Smart Watch",
        "price": 4999,
        "category": "Electronics",
        "description": "Track health, fitness, and notifications."
    },

    {
        "name": "Running Shoes",
        "price": 3499,
        "category": "Fashion",
        "description": "Comfortable sports shoes for daily use."
    },

    {
        "name": "Minimal Desk Lamp",
        "price": 1799,
        "category": "Home",
        "description": "Modern LED lamp with adjustable brightness."
    },

    {
        "name": "Backpack Pro",
        "price": 2199,
        "category": "Accessories",
        "description": "Water-resistant backpack for students."
    },

    {
        "name": "Portable Speaker",
        "price": 2599,
        "category": "Electronics",
        "description": "Compact Bluetooth speaker with deep bass."
    }
]

# ---------------------------
# SESSION STATE FOR CART
# ---------------------------
if "cart" not in st.session_state:
    st.session_state.cart = []

# ---------------------------
# SIDEBAR
# ---------------------------
st.sidebar.title("🛒 MiniStore")

categories = ["All"] + sorted(
    list(set([p["category"] for p in products]))
)

selected_category = st.sidebar.radio(
    "Browse Categories",
    categories
)

st.sidebar.markdown("---")

# CART SUMMARY
st.sidebar.subheader("Shopping Cart")

cart_count = len(st.session_state.cart)
cart_total = sum(item["price"] for item in st.session_state.cart)

st.sidebar.metric("Items", cart_count)
st.sidebar.metric("Total", f"₹{cart_total}")

if st.sidebar.button("Clear Cart"):
    st.session_state.cart = []
    st.rerun()

# ---------------------------
# HERO SECTION
# ---------------------------
st.markdown("""
<div class='hero'>
<h1>🛍️ MiniStore</h1>
<h3>Your Everyday Shopping Destination</h3>
<p>Discover quality products at amazing prices.</p>
</div>
""", unsafe_allow_html=True)

# ---------------------------
# WELCOME SECTION
# ---------------------------
st.header("Welcome to MiniStore")

st.write("""
Explore our featured collection.
Shop electronics, fashion, accessories, and more.
""")

# ---------------------------
# FILTER PRODUCTS
# ---------------------------
if selected_category == "All":
    filtered = products
else:
    filtered = [
        p for p in products
        if p["category"] == selected_category
    ]

# ---------------------------
# FEATURED PRODUCTS
# ---------------------------
st.subheader("⭐ Featured Products")

cols = st.columns(3)

for i, product in enumerate(filtered):

    with cols[i % 3]:

        st.markdown(f"""
        <div class="product-card">

        <h3>{product["name"]}</h3>

        <div class="category">
        {product["category"]}
        </div>

        <br><br>

        <p>{product["description"]}</p>

        <div class="price">
        ₹{product["price"]}
        </div>

        </div>
        """, unsafe_allow_html=True)

        if st.button(
            f"Add to Cart",
            key=product["name"]
        ):
            st.session_state.cart.append(product)
            st.success(
                f'{product["name"]} added!'
            )
            st.rerun()

# ---------------------------
# CART DETAILS
# ---------------------------
if st.session_state.cart:

    st.markdown("---")
    st.subheader("🧾 Cart Items")

    for item in st.session_state.cart:
        st.write(
            f"• {item['name']} — ₹{item['price']}"
        )

# ---------------------------
# FOOTER
# ---------------------------
st.markdown("""
<footer>
<hr>
MiniStore Demo • Built with Streamlit
</footer>
""", unsafe_allow_html=True)