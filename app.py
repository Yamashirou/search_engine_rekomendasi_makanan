import streamlit as st
import pandas as pd
import json
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# =========================
# CONFIG
# =========================
st.set_page_config(
    page_title="Kuliner Search Engine",
    layout="wide"
)

st.title("🍽️ Search Engine Rekomendasi Kuliner")
st.caption("Ranking berbasis TF-IDF + Cosine Similarity | Review bintang 5 Google Maps")

# =========================
# LOAD DATA
# =========================
df_ui = pd.read_csv("output/kuliner_merged.csv")
df_model = pd.read_csv("output/kuliner_preprocessed.csv")

# VALIDASI KUNCI JOIN
key_cols = {"restaurant", "area"}
if not key_cols.issubset(df_ui.columns) or not key_cols.issubset(df_model.columns):
    st.error("Kolom join (restaurant, area) tidak ditemukan.")
    st.stop()

# =========================
# PREPROCESS QUERY
# =========================
def preprocess_query(text):
    return text.lower()

# =========================
# TF-IDF (MODEL ONLY)
# =========================
vectorizer = TfidfVectorizer(
    ngram_range=(1, 2),
    min_df=2,
    max_df=0.9
)

tfidf_matrix = vectorizer.fit_transform(df_model["clean_review"])

# =========================
# SIDEBAR FILTER
# =========================
st.sidebar.header("🔍 Filter")

areas = ["Semua"] + sorted(df_ui["area"].unique().tolist())
selected_area = st.sidebar.selectbox("Pilih Area", areas)

show_n = st.sidebar.radio(
    "Jumlah review ditampilkan",
    [5, 10],
    horizontal=True
)

# =========================
# SEARCH INPUT
# =========================
query = st.text_input(
    "Cari makanan / rasa / suasana:",
    placeholder="contoh: nasi goreng pedas gurih"
)

# =========================
# SEARCH LOGIC
# =========================
if query:
    query_clean = preprocess_query(query)
    query_vec = vectorizer.transform([query_clean])

    similarity = cosine_similarity(query_vec, tfidf_matrix)[0]
    df_model["score"] = similarity

    # Ranking
    df_ranked = df_model.sort_values("score", ascending=False)
    df_ranked = df_ranked[df_ranked["score"] > 0]

    # Filter area
    if selected_area != "Semua":
        df_ranked = df_ranked[df_ranked["area"] == selected_area]

    if df_ranked.empty:
        st.warning("Tidak ditemukan hasil yang relevan.")
    else:
        st.subheader("🔎 Hasil Pencarian")

        # JOIN ke UI
        results = pd.merge(
            df_ranked,
            df_ui,
            on=["restaurant", "area"],
            how="left"
        )

        for _, row in results.head(10).iterrows():
            st.markdown(
                f"""
                ### 🍴 {row['restaurant']}
                📍 **{row['area']}**  
                🔥 *Cosine similarity:* `{row['score']:.3f}`
                """
            )

            # =========================
            # REVIEW MENTAH (BINTANG 5)
            # =========================
            if pd.notna(row.get("sample_reviews")):
                reviews = json.loads(row["sample_reviews"])

                with st.expander("⭐ Lihat review bintang 5"):
                    for r in reviews[:show_n]:
                        st.markdown(
                            f"""
                            **👤 {r.get('reviewer', 'Anonim')}**  
                            ⭐⭐⭐⭐⭐  
                            {r.get('text', '')}
                            ---
                            """
                        )
            else:
                st.caption("Tidak ada review tersedia.")

            st.divider()
