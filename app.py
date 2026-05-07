import streamlit as st
import pandas as pd

st.set_page_config(page_title="WorkflowDominator Simulator", layout="wide")
st.title("🚀 WorkflowDominator v1.0")
st.subheader("EU AI Act Dual-Verification Bottleneck Simulator")

st.markdown("### Input your scenario")
volume = st.slider("Monthly high-risk decisions", 100, 10000, 1000, 100)
trigger = st.selectbox("Annex III Trigger", ["Employment screening", "Biometric ID in hiring", "Justice-adjacent decisions", "Other high-risk"])

if st.button("Run Simulation"):
    # Simple model based on our quantified data
    base_fte_per_500 = 1.6
    fte = round((volume / 500) * base_fte_per_500 * 1.1, 1)  # slight overhead
    annual_drag = round(fte * 92000)
    throughput_loss = min(68, int(40 + (volume / 10000) * 28))
    
    st.success(f"**Results for {volume} decisions/month**")
    col1, col2, col3 = st.columns(3)
    col1.metric("Extra FTE Required", f"{fte}")
    col2.metric("Annual Compliance Drag", f"€{annual_drag:,}")
    col3.metric("Throughput Compression", f"{throughput_loss}%")
    
    st.markdown("---")
    st.info("This matches the high-volume kill shots from the EU AI Act analysis. For full prompts + editable code, grab the $67 pack.")
    
    if volume > 2000:
        st.warning("High-volume warning: Only €100M+ ARR platforms can absorb this. Consider white-label pivot.")