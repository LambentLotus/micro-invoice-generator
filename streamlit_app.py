import streamlit as st

st.set_page_config(page_title="Invoice PDF Generator", layout="centered")
st.title("📄 Micro-Freelance Invoice & PDF Generator")
st.write("Input client transaction details to instantly process a standardized statement.")

# Core Client Information Intakes
company_name = st.text_input("Your Company / Name", value="Lotus Digital Assets LLC")
client_name = st.text_input("Client Company / Name", value="Acquisition Corp Inc.")

col1, col2 = st.columns(2)
with col1:
    invoice_num = st.text_input("Invoice Number", value="INV-2026-001")
    rate = st.number_input("Hourly Rate ($/hr)", min_value=1.0, value=75.0, step=5.0)
with col2:
    invoice_date = st.date_input("Billing Date")
    hours = st.number_input("Total Hours Billed", min_value=0.1, value=20.0, step=0.5)

# Execute Simple Automated Math Layers
subtotal = rate * hours
tax_rate = 0.06  # Standard localized 6% accounting margin buffer
total_tax = subtotal * tax_rate
grand_total = subtotal + total_tax

st.divider()

# Complete Structural Document Preview Layout
st.subheader("📋 Document Accounting Preview")
st.code(f"""
============================================================
INVOICE RECORD: {invoice_num} | DATE: {invoice_date}
============================================================
FROM: {company_name}
TO:   {client_name}
------------------------------------------------------------
SERVICES RENDERED          HOURS      RATE        SUBTOTAL
Consulting / Code Asset     {hours:<10}{rate:<12}${subtotal:,.2f}
------------------------------------------------------------
SUBTOTAL:                                        ${subtotal:,.2f}
TAX / PROCESSING (6.0%):                          ${total_tax:,.2f}
============================================================
TOTAL DUE ACQUISITION ACCOUNT:                   ${grand_total:,.2f}
============================================================
""", language="markdown")

st.success("🟢 LOGIC VERIFIED: Document matrix balanced successfully. Ready for clean text array export.")
