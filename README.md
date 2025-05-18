# InsightMail – AI-Powered Customer Feedback Analyzer

InsightMail is a real-time, AI-powered feedback analytics dashboard. It ingests customer reviews, performs sentiment and topic analysis using Hugging Face NLP models, and visualizes insights in an interactive Streamlit dashboard.

---

## Live Demo

 [View the live app on Streamlit](https://insightmail-feedback-analyzer-zwk4srrfq5wzarcvfe2vlw.streamlit.app/)

---

##  Features

-  **Sentiment Analysis** using Hugging Face Transformers (no API key needed)
-  **Topic Classification** with NLP rules
-  **Interactive Streamlit Dashboard**
-  Real-time KPIs: total reviews, % negative, average rating
-  Trend charts for sentiment over time
-  Topic breakdown and word count distribution
-  Fully local, free, open-source solution

---

##  Dataset

- Source: [Amazon Fine Food Reviews Dataset on Kaggle](https://www.kaggle.com/datasets/snap/amazon-fine-food-reviews)
- Used columns:
  - `Text` → Cleaned into `clean_text`
  - `Score` → Used as optional reference rating
  - `Time` → Converted to datetime for time-series analysis

---

##  Sentiment & Topic Analysis

###  Sentiment
- Model: Hugging Face `distilbert-base-uncased-finetuned-sst-2-english`
- Labels: `positive`, `negative`

###  Topic Classification
- Rule-based keywords for:
  - `delivery`, `pricing`, `product quality`, `customer service`, `other`

---

##  Dashboard Preview

| Section | Description |
|---------|-------------|
|  Filters | Sidebar with sentiment + topic selection |
|  KPIs | Total reviews, average rating, % negative |
|  Sentiment Trends | Line chart by day and sentiment |
|  Topic Distribution | Bar chart of topic frequency |
|  Word Count | Histogram of word counts per review |

---

## Tech Stack

| Layer           | Tool                              |
|-----------------|-----------------------------------|
| Data Cleaning   | Python, Pandas, Regex             |
| Sentiment Model | Hugging Face Transformers         |
| Topic Logic     | Rule-based classification         |
| Dashboard       | Streamlit                         |
| Deployment      | Streamlit Cloud + GitHub          |

---

## How to Run Locally

```bash
# 1. Clone the repo
git clone https://github.com/yourusername/insightmail-feedback-analyzer.git
cd insightmail-feedback-analyzer

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run the app
streamlit run app.py
