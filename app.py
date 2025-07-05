import streamlit as st
from transformers import pipeline

# Load the sentiment-analysis model
sentiment_model = pipeline("sentiment-analysis")

# Streamlit UI
st.title("💬 AI-Based Sentiment Analyzer")
st.write("Enter a sentence or review below to see its sentiment:")

user_input = st.text_area("Your Text")

if st.button("Analyze"):
    if user_input.strip() != "":
        with st.spinner("Analyzing..."):
            result = sentiment_model(user_input)[0]
            label = result['label']
            score = result['score']

            st.success(f"**Sentiment:** {label}")
            st.write(f"**Confidence Score:** {round(score * 100, 2)}%")
    else:
        st.warning("Please enter some text to analyze.")
