import streamlit as st
import pandas as pd
import time
from modules.collector import collect_metrics
from modules.analyzer import detect_anomalies, identify_bottlenecks
from modules.forecaster import forecast_cpu
from modules.recommender import recommend_optimizations
import altair as alt

st.set_page_config(page_title="AI Process Analyzer", page_icon="🧠", layout="wide")

st.title("🧠 AI-Powered OS Process Performance Analyzer")
st.caption("Real-time monitoring • AI insights • Forecasting")

# Initialize session state
if "history" not in st.session_state:
    st.session_state.history = pd.DataFrame()

refresh_rate = st.sidebar.slider("⏱ Refresh interval (seconds)", 1, 10, 3)
run = st.sidebar.checkbox("▶️ Start Monitoring", value=False)

placeholder = st.empty()

while run:
    df = collect_metrics()
    st.session_state.history = pd.concat([st.session_state.history, df]).tail(500)

    anomalies = detect_anomalies(df)
    high_cpu, high_mem = identify_bottlenecks(df)
    forecast_df = forecast_cpu(st.session_state.history)
    recs = recommend_optimizations(high_cpu, high_mem)

    with placeholder.container():
        col1, col2 = st.columns(2)

        with col1:
            st.subheader("📊 CPU Usage Over Time")
            cpu_chart = alt.Chart(st.session_state.history).mark_line(color="orange").encode(
                x="timestamp:T", y="cpu_percent:Q"
            )
            st.altair_chart(cpu_chart, use_container_width=True)

        with col2:
            st.subheader("📈 CPU Forecast (Next 5s)")
            if forecast_df is not None:
                forecast_chart = alt.Chart(forecast_df).mark_line(color="green").encode(
                    x="timestamp:T", y="predicted_cpu:Q"
                )
                st.altair_chart(forecast_chart, use_container_width=True)
            else:
                st.info("Not enough data yet to forecast.")

        st.divider()
        st.subheader("⚙️ Bottleneck Processes")
        st.dataframe(pd.concat([high_cpu, high_mem]).drop_duplicates(subset='pid').head(10))

        st.subheader("💡 AI Recommendations")
        for r in recs:
            st.write("-", r)

        st.subheader("🚨 Detected Anomalies")
        if not anomalies.empty:
            st.dataframe(anomalies)
        else:
            st.success("No anomalies detected.")

    time.sleep(refresh_rate)
