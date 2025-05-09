
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv("labeled_reviews_free.csv", parse_dates=["timestamp"])

# Sidebar filters
st.sidebar.header("🔍 Filter Feedback")
sentiments = st.sidebar.multiselect("Sentiment", df["sentiment"].unique(), default=df["sentiment"].unique())
topics = st.sidebar.multiselect("Topic", df["topic"].unique(), default=df["topic"].unique())

# Filtered data
filtered = df[(df["sentiment"].isin(sentiments)) & (df["topic"].isin(topics))]

# KPIs
st.title("📬 InsightMail – AI-Powered Feedback Dashboard")
col1, col2, col3 = st.columns(3)
col1.metric("Total Reviews", len(filtered))
col2.metric("Avg Rating", f"{filtered['rating'].mean():.2f}")
col3.metric("Negative %", f"{(filtered['sentiment'] == 'negative').mean() * 100:.1f}%")

# Charts
st.markdown("### 📈 Sentiment Over Time")

# Ensure 'date' column exists in both the original df and the filtered DataFrame
df['date'] = df['timestamp'].dt.date   # Add date column to original df
filtered['date'] = filtered['timestamp'].dt.date  # Add date column to filtered DataFrame

# Now group by date and sentiment
sentiment_over_time = filtered.groupby(['date', 'sentiment']).size().unstack(fill_value=0)

# Visualize the result with Streamlit's line chart
st.line_chart(sentiment_over_time)

st.markdown("### 🧠 Topic Distribution")
topic_count = filtered["topic"].value_counts()
st.bar_chart(topic_count)

st.markdown("### 🗣️ Word Count Distribution")
st.histogram = plt.hist(filtered["clean_text"].str.split().apply(len), bins=20)
st.pyplot(plt.gcf())
