import streamlit as st
from sentence_transformers import SentenceTransformer
import numpy as np


@st.cache_resource
def load_embedding_model():
    model = SentenceTransformer("all-MiniLM-L6-v2")
    return model


def create_paper_embeddings(papers_df, model):
    if papers_df is None or papers_df.empty:
        return None

    texts = []

    for _, row in papers_df.iterrows():
        title = str(row.get("title", ""))
        summary = str(row.get("summary", ""))
        text = title + " " + summary
        texts.append(text)

    embeddings = model.encode(texts, show_progress_bar=True)
    return embeddings


def semantic_search(query, papers_df, embeddings, model, top_k=5):
    if papers_df is None or papers_df.empty:
        return papers_df

    if embeddings is None:
        return papers_df

    query_embedding = model.encode([query])
    similarities = np.dot(embeddings, query_embedding.T).flatten()

    top_indices = similarities.argsort()[::-1][:top_k]

    results = papers_df.iloc[top_indices].copy()
    results["similarity_score"] = similarities[top_indices]

    return results