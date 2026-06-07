import streamlit as st
from src.arxiv_search import search_arxiv, save_papers_to_csv


st.set_page_config(
    page_title="Research Paper Assistant",
    page_icon="📚",
    layout="wide"
)

st.title("Research Paper Assistant")

st.write(
    "Search academic papers from arXiv by entering a research topic. "
    "The app retrieves paper titles, authors, abstracts, dates, and PDF links."
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

if st.button("Research Papers"):

    with st.spinner("Searching papers from arXiv..."):
        df = search_arxiv(query, max_results=max_results)

    if df.empty:
        st.warning("No papers found. Try a different search topic.")

    else:
        st.success(f"Found {len(df)} papers.")

        save_papers_to_csv(df)

        st.subheader("Search Results")

        for index, row in df.iterrows():
            st.markdown(f"## {index + 1}. {row['title']}")
            st.write(f"**Authors:** {row['authors']}")
            st.write(f"**Published:** {row['published']}")
            st.write(row["summary"])
            st.markdown(f"[PDF Link]({row['pdf_url']})")
            st.write("---")

        csv = df.to_csv(index=False)

        st.download_button(
            label="Download Results as CSV",
            data=csv,
            file_name="arxiv_papers.csv",
            mime="text/csv"
        )
        