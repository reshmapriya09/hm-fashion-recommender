
import streamlit as st

st.set_page_config(
    page_title="H&M Fashion Recommendation System",
    page_icon="🧥",
    layout="centered"
)

st.title("🧥 H&M Personalized Fashion Recommendation System")

st.markdown("""
## 👩‍💻 Developed By
### R.Reshmapriya

## 🎓 Capstone Project

### Personalized Fashion Recommendation Using Neural Collaborative Filtering (NCF)

This project recommends fashion products to users based on their purchase history and preferences using an AI-powered recommendation engine.

### 🔧 Technologies Used
- Python
- TensorFlow
- Neural Collaborative Filtering (NCF)
- Pandas
- NumPy
- Gradio
- Streamlit

### 📊 Dataset
H&M Fashion Recommendation Dataset

### 🎯 Project Objective
To provide personalized fashion recommendations by learning user-item interactions and predicting products that users are likely to purchase.
""")

st.subheader("📈 Model Evaluation Results")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Precision@10", "8.20%")

with col2:
   st.metric("Recall@10", "24.87%")

with col3:
    st.metric("NDCG@10", "17.90%")

st.markdown("""
### 📌 Model Performance Interpretation

**Precision@10 = 0.0820 (8.20%)**
- Out of the top 10 recommended items, 8.20% were relevant.

**Recall@10 = 0.2487 (24.87%)**
- The model successfully retrieved 24.87% of relevant items for users.

**NDCG@10 = 0.1790 (17.90%)**
- Measures the ranking quality of recommendations by giving higher importance to relevant items appearing near the top of the recommendation list.
""")

st.subheader("🏗️ Project Architecture")

st.markdown("""
1. User Purchase History Collection
2. Data Preprocessing & Encoding
3. Neural Collaborative Filtering (NCF) Model Training
4. User-Item Interaction Learning
5. Personalized Recommendation Generation
6. Top-N Product Recommendation Output
""")

st.subheader("🚀 Deployment Status")

st.success("Application Successfully Deployed")

st.subheader("🛍️ Live Fashion Recommendation Demo")

st.link_button(
    "Open Recommendation System",
    "https://0e1ab3ce76c75a9169.gradio.live"
)

st.info(
    "The recommendation engine was developed using Neural Collaborative Filtering (NCF) "
    "and trained on the H&M Fashion Recommendation Dataset."
)

st.markdown("---")
st.markdown(
    "<center><b>© 2026 R.Reshmapriya | H&M Personalized Fashion Recommendation System</b></center>",
    unsafe_allow_html=True
)

