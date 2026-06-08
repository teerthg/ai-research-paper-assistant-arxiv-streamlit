# AI Research Paper Assistant using arXiv API and Streamlit

## Overview

This is a simple research paper assistant built with Python, Streamlit, and the arXiv API.

The main idea of this project is to make it easier to search academic papers from arXiv. The user can enter a research topic, and the app returns relevant papers with their title, authors, publication date, abstract, and PDF link.

In the current version, I focused mainly on papers related to transformer-based time series forecasting.

## Why I built this

As a statistics and data science student, I often need to search for research papers while preparing for projects, thesis ideas, or technical discussions. Searching manually can take time, and sometimes the results are not very focused.

The project now includes both keyword-based arXiv search and semantic search using sentence-transformer embeddings.
## Features

- Search research papers from arXiv
- Display paper title, authors, publication date, abstract, and PDF link
- Focus results on AI, machine learning, and statistics-related papers
- Save the results into a CSV file
- Download the search results from the app
- Simple Streamlit interface
- Semantic search using sentence embeddings
- Rank papers by similarity score
- Ask natural language research questions
- Download semantic search results as CSV

## Tech Stack

- Python
- Streamlit
- Pandas
- arXiv API
- Sentence Transformers
- Scikit-learn
- Cosine Similarity

## Folder Structure

```text
agentic-ai-research-assistant/
│
├── data/
│   └── arxiv_papers.csv
│
├── src/
│   ├── arxiv_search.py
│   └── semantic_search.py
│
├── app.py
├── requirements.txt
├── README.md
└── .gitignore
  
