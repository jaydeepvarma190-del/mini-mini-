import streamlit as st

st.set_page_config(
    page_title="Support Chatbot",
    page_icon="💬"
)

# ---------------------------
# CHAT MEMORY
# ---------------------------
if "messages" not in st.session_state:
    st.session_state.messages = []

products = st.session_state.get(
    "products",
    []
)

# ---------------------------
# RESPONSE ENGINE
# ---------------------------
def generate_reply(text):

    q = text.lower()

    # Product search
    for p in products:

        if p["name"].lower() in q:

            return (
                f"{p['name']} costs ₹{p['price']}.\n\n"
                f"{p['description']}"
            )

    # Delivery
    if (
        "delivery" in q
        or
        "shipping" in q
    ):
        return (
            "Standard delivery: 2–5 business days."
        )

    # Refund
    if "refund" in q:
        return (
            "Refunds are processed in 5–7 business days."
        )

    # Return
    if "return" in q:
        return (
            "Returns are accepted within 7 days."
        )

    # Payment
    if (
        "payment" in q
        or
        "upi" in q
        or
        "card" in q
    ):
        return (
            "Supported payments:\n"
            "• UPI\n"
            "• Credit Card\n"
            "• Debit Card\n"
            "• Wallet"
        )

    # Order
    if (
        "order" in q
        or
        "status" in q
    ):
        return (
            "Demo Order Status:\nPreparing shipment."
        )

    return (
        "I can help with:\n"
        "• Products\n"
        "• Delivery\n"
        "• Refunds\n"
        "• Returns\n"
        "• Payments\n"
        "• Order Status"
    )

# ---------------------------
# PAGE
# ---------------------------
st.title(
    "💬 MiniStore Support"
)

st.write(
    "Ask about products, delivery, refunds, orders and more."
)

# Display history
for msg in st.session_state.messages:

    with st.chat_message(
        msg["role"]
    ):
        st.write(
            msg["content"]
        )

# Input
prompt = st.chat_input(
    "Ask support..."
)

if prompt:

    st.session_state.messages.append({
        "role": "user",
        "content": prompt
    })

    with st.chat_message(
        "user"
    ):
        st.write(prompt)

    answer = generate_reply(
        prompt
    )

    st.session_state.messages.append({
        "role": "assistant",
        "content": answer
    })

    with st.chat_message(
        "assistant"
    ):
        st.write(answer)