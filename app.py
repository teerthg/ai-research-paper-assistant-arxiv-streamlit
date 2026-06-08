import streamlit as st
from src.arxiv_search import search_arxiv, save_papers_to_csv
from src.semantic_search import (
    load_embedding_model,
    create_paper_embeddings,
    semantic_search
)


st.set_page_config(
    page_title="Research Paper Assistant",
    layout="wide"
)


@st.cache_resource
def get_model():
    """
    Load the embedding model once and cache it.
    """
    return load_embedding_model()


st.title("AI Research Paper Assistant")

st.write(
    "Search academic papers from arXiv and use semantic search to find papers "
    "based on meaning, not only exact keywords."
)

query = st.text_input(
    "Enter your research topic:",
    "transformer time series forecasting"
)

max_results = st.slider(
    "Number of papers to search:",
    min_value=5,
    max_value=20,
    value=10
)

semantic_question = st.text_input(
    "Ask a semantic search question:",
    "Which papers discuss attention mechanisms for long-horizon forecasting?"
)

top_k = st.slider(
    "Number of semantic results:",
    min_value=3,
    max_value=10,
    value=5
)


if st.button("Search Papers"):

    with st.spinner("Searching papers from arXiv..."):
        df = search_arxiv(query, max_results=max_results)

    if df.empty:
        st.warning("No papers found. Try a different search topic.")

    else:
        st.success(f"Found {len(df)} papers from arXiv.")

        save_papers_to_csv(df)

        st.subheader("Keyword Search Results")

        for index, row in df.iterrows():
            st.markdown(f"## {index + 1}. {row['title']}")
            st.write(f"**Authors:** {row['authors']}")
            st.write(f"**Published:** {row['published']}")
            st.write(row["summary"])
            st.markdown(f"[PDF Link]({row['pdf_url']})")
            st.write("---")

        keyword_csv = df.to_csv(index=False)

        st.download_button(
            label="Download Keyword Results as CSV",
            data=keyword_csv,
            file_name="arxiv_papers.csv",
            mime="text/csv"
        )

        st.subheader("Semantic Search Results")

        with st.spinner("Creating embeddings and ranking papers by meaning..."):
            model = get_model()
            paper_embeddings = create_paper_embeddings(df, model)

            semantic_results = semantic_search(
                semantic_question,
                df,
                paper_embeddings,
                model,
                top_k=top_k
            )

        st.success("Semantic search completed.")

        for index, row in semantic_results.iterrows():
            score = round(row["similarity_score"], 3)

            st.markdown(f"## {row['title']}")
            st.write(f"**Similarity Score:** {score}")
            st.write(f"**Authors:** {row['authors']}")
            st.write(f"**Published:** {row['published']}")
            st.write(row["summary"])
            st.markdown(f"[PDF Link]({row['pdf_url']})")
            st.write("---")

        semantic_csv = semantic_results.to_csv(index=False)

        st.download_button(
            label="Download Semantic Results as CSV",
            data=semantic_csv,
            file_name="semantic_search_results.csv",
            mime="text/csv"
        )
