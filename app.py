import streamlit as st

def check_fraud(transaction_type, amount, old_balance, new_balance):
    # Expected balance calculation based on transaction type
    if transaction_type in ["PAYMENT", "WITHDRAWAL", "TRANSFER"]:
        expected_balance = old_balance - amount
    elif transaction_type == "DEPOSIT":
        expected_balance = old_balance + amount
    else:
        return "Unknown Transaction Type"

    # Allow a small margin for float precision
    if abs(new_balance - expected_balance) > 0.01:
        return "Fraud"
    return "Not Fraud"

# Streamlit UI
st.title("🔍 Fraud Detection System")

# Input fields
transaction_type = st.selectbox("Transaction Type", ["PAYMENT", "TRANSFER", "DEPOSIT", "WITHDRAWAL"])
amount = st.number_input("Amount", min_value=0.0, format="%.2f")
old_balance = st.number_input("Old Balance", min_value=0.0, format="%.2f")
new_balance = st.number_input("New Balance", min_value=0.0, format="%.2f")

# Check fraud
if st.button("Check Fraud"):
    result = check_fraud(transaction_type, amount, old_balance, new_balance)
    if result == "Fraud":
        st.error(f"⚠️ Fraud Detected!")
    else:
        st.success(f"✅ Transaction is Not Fraudulent.")
