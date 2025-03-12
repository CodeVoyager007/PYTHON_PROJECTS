import streamlit as st

st.set_page_config(page_title="Unit Converter", page_icon="⚡", layout="centered")

st.markdown("""
    <style>
        body { background-color: black; color: white; }
        .stButton button { 
            background: linear-gradient(90deg, #ff0000, #ff7300);
            color: white;
            border-radius: 8px;
            font-size: 18px;
            font-weight: bold;
            padding: 8px 20px;
            transition: 0.3s ease;
        }
        .stButton button:hover { 
            transform: scale(1.05);
            background: linear-gradient(90deg, #ff7300, #ff0000);
        }
        .result-box {
            background-color: #222;
            padding: 15px;
            border-radius: 8px;
            font-size: 20px;
            font-weight: bold;
            text-align: center;
            border: 2px solid #ff0000;
        }
        .copy-btn {
            background: linear-gradient(90deg, #00c3ff, #0072ff);
            color: white;
            border-radius: 8px;
            font-size: 16px;
            font-weight: bold;
            padding: 5px 15px;
            margin-top: 10px;
            cursor: pointer;
        }
        .copy-btn:hover { transform: scale(1.1); }
    </style>
""", unsafe_allow_html=True)

CATEGORIES = {
    "Length": {"Meter": 1, "Kilometer": 0.001, "Centimeter": 100, "Millimeter": 1000},
    "Weight": {"Gram": 1, "Kilogram": 0.001, "Pound": 0.00220462},
    "Temperature": {"Celsius": 1, "Fahrenheit": 33.8, "Kelvin": 274.15}
}

st.title("⚡ Advanced Unit Converter")

category = st.selectbox("Select Category", list(CATEGORIES.keys()), index=0)
from_unit = st.selectbox("Convert From", ["Choose an option"] + list(CATEGORIES[category].keys()), index=0)
to_unit = st.selectbox("Convert To", ["Choose an option"] + list(CATEGORIES[category].keys()), index=0)
value = st.number_input("Enter Value", min_value=0.0, format="%.2f")

if "result_text" not in st.session_state:
    st.session_state.result_text = ""

# Convert button
if st.button("Convert 🔥"):
    if from_unit == "Choose an option" or to_unit == "Choose an option":
        st.warning("⚠ Please select valid units for conversion!")
    else:
        result = (value / CATEGORIES[category][from_unit]) * CATEGORIES[category][to_unit]
        st.session_state.result_text = f"{value} {from_unit} = {result:.4f} {to_unit}"

if st.session_state.result_text:
    st.markdown(f'<div class="result-box">{st.session_state.result_text}</div>', unsafe_allow_html=True)

    #copy button
    st.code(st.session_state.result_text, language="plaintext") 
    st.button("📋 Copy Result", on_click=lambda: st.session_state.update({"clipboard": st.session_state.result_text}))
