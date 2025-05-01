

# Solar Battery Monitor Dashboard using Streamlit (Elegant & Dynamic UI)
import streamlit as st
from battery_monitor import BatteryMonitor

st.set_page_config(page_title="Solar Battery Monitor", layout="wide")

# Custom CSS for elegant and aura design
st.markdown("""
    <style>
    body {
        background: linear-gradient(120deg, #232526 0%, #414345 100%);
        color: #f8f8f2;
    }
    .main {
        background: rgba(30, 32, 34, 0.95);
        border-radius: 18px;
        box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.37);
        padding: 2rem 2.5rem 2rem 2.5rem;
        margin-top: 2rem;
    }
    .stTextInput>div>div>input, .stNumberInput>div>input {
        background: #232526;
        color: #f8f8f2;
        border-radius: 8px;
        border: 1px solid #444;
    }
    .stSlider>div>div>div {
        background: #232526;
    }
    .stMarkdown h1, .stMarkdown h2, .stMarkdown h3 {
        color: #a3e635;
        font-family: 'Segoe UI', 'Roboto', sans-serif;
    }
    .stMarkdown h4 {
        color: #facc15;
    }
    .stAlert-success {
        background: linear-gradient(90deg, #a3e635 0%, #bef264 100%);
        color: #232526;
        border-radius: 10px;
    }
    .stAlert-error {
        background: linear-gradient(90deg, #f87171 0%, #fbbf24 100%);
        color: #232526;
        border-radius: 10px;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown("<div class='main'>", unsafe_allow_html=True)
st.markdown("""
# 🔋 Solar Battery Monitor Dashboard
<span style='font-size:1.2em;color:#facc15;'>Elegant, dynamic, and always up-to-date.</span>
---
""", unsafe_allow_html=True)

# System Specifications
st.header("System Specifications")
cols = st.columns(3)
battery_capacity = cols[0].number_input("Battery Capacity (kWh)", min_value=0.1, value=10.0, step=0.1, key="bat_cap")
avg_power = cols[1].number_input("Average Power Consumption (kW)", min_value=0.1, value=2.0, step=0.1, key="avg_pow")
efficiency = cols[2].number_input("Battery Efficiency (0-1)", min_value=0.5, max_value=1.0, value=0.85, step=0.01, key="eff")
monitor = BatteryMonitor(battery_capacity, avg_power, efficiency)

st.markdown("---")

# Dynamic Calculations
st.header("Live Battery Usage Insights")
cols2 = st.columns(3)

# 1. Runtime from battery percentage
battery_percent = cols2[0].number_input("Current Battery Percentage (%)", min_value=0.0, max_value=100.0, value=100.0, step=0.1, key="bat_pct")
try:
    runtime = monitor.calculate_runtime(battery_percent)
    cols2[0].markdown(f"<h4>Runtime:</h4> <span style='font-size:1.5em;color:#a3e635'>{runtime} hours</span> <br> <span style='color:#facc15'>{round(runtime/24, 2)} days</span>", unsafe_allow_html=True)
except Exception as e:
    cols2[0].error(str(e))

# 2. Required battery percentage for desired runtime
desired_hours = cols2[1].number_input("Desired Runtime (hours)", min_value=0.1, value=5.0, step=0.1, key="des_hours")
try:
    required_percent = monitor.calculate_required_percentage(desired_hours)
    cols2[1].markdown(f"<h4>Required %:</h4> <span style='font-size:1.5em;color:#a3e635'>{required_percent}%</span>", unsafe_allow_html=True)
except Exception as e:
    cols2[1].error(str(e))

# 3. Optimal power consumption for desired runtime and battery
opt_hours = cols2[2].number_input("Desired Runtime (hours, optimal)", min_value=0.1, value=5.0, step=0.1, key="opt_hours")
opt_battery_percent = cols2[2].number_input("Available Battery Percentage (%)", min_value=0.0, max_value=100.0, value=100.0, step=0.1, key="opt_bat_pct")
try:
    optimal_power = monitor.calculate_optimal_power(opt_hours, opt_battery_percent)
    cols2[2].markdown(f"<h4>Optimal Power:</h4> <span style='font-size:1.5em;color:#a3e635'>{optimal_power} kW</span>", unsafe_allow_html=True)
except Exception as e:
    cols2[2].error(str(e))

st.markdown("---")
st.caption("<span style='color:#a3e635'>Made with ❤️ for solar users. Elegant, dynamic, and always up-to-date.</span>", unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)
