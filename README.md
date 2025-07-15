# 🎬 Movie Recommender System

This is a content-based movie recommender system built using a dataset of **5,000 movies**. It suggests **top 5 similar movies** based on your input using **cosine similarity** between movie feature vectors.

---

## 🚀 Features

- ✅ Based on content similarity (genres, keywords, cast, crew, etc.)
- 📊 Uses cosine similarity to compute related movies
- ⚡ Fast and accurate movie recommendations
- 📦 Precomputed similarity scores stored in `similarity.zip`
- 🧠 Built with **Pandas**, **scikit-learn**, **Streamlit**, and **FastAPI**

---

## 🧪 How It Works

1. The dataset is cleaned and vectorized.
2. Cosine similarity is calculated between movie vectors.
3. When a user selects a movie, the top 5 closest (most similar) movies are returned.

---

## 🛠 Tech Stack

- **Python**
- **Pandas**, **NumPy**, **scikit-learn**
- **Streamlit** (for frontend)
- **FastAPI** (for backend API)
- **Docker** (for containerization)

---

## 📁 Dataset

- Contains **5,000+ movies**
- Includes title, genres, overview, cast, crew, and more
- Processed and saved in `.zip` format to reduce size for GitHub

---
## ⚙️ Setup Instructions

1. Open your terminal and run these commands:

   ```bash
   git clone https://github.com/kunwar418/movie-recommender-system.git
   cd movie-recommender-system
   pip install -r requirements.txt
   unzip similarity.zip
   streamlit run streamlit_app.py
   uvicorn main:app --reload
   ```

### 🚀 Next Steps:
To finalize and push the change:

```bash
git add README.md
git commit -m "Fix README bash code block"
git push origin main
```