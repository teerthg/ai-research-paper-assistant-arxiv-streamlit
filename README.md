# AI Research Paper Assistant using arXiv API and Streamlit

## Overview

This is a research paper assistant built with Python, Streamlit, and the arXiv API.

The main idea of this project is to make it easier to search academic papers from arXiv. The user can enter a research topic, and the app returns relevant papers with their title, authors, publication date, abstract, and PDF link.

The project now includes both keyword-based arXiv search and semantic search using sentence-transformer embeddings. In the current version, I focused mainly on papers related to transformer-based time series forecasting.

## Why I built this

As a statistics and data science student, I often need to search for research papers while preparing for projects, thesis ideas, or technical discussions. Searching manually can take time, and sometimes the results are not very focused.

This project is a first step toward building a more advanced AI research assistant that can later include paper summarization, RAG-based question answering, and agentic workflows.

## Features

- Search research papers from arXiv
- Display paper title, authors, publication date, abstract, and PDF link
- Focus results on AI, machine learning, and statistics-related papers
- Save keyword search results into a CSV file
- Download keyword search results from the app
- Ask natural language research questions
- Semantic search using sentence-transformer embeddings
- Rank papers by similarity score
- Download semantic search results as CSV
- Simple Streamlit interface

## Version 1: Keyword Search

In Version 1, I built a basic Streamlit app that connects to the arXiv API and retrieves papers based on a research topic.

The app collects paper metadata such as:

- Title
- Authors
- Publication date
- Abstract
- PDF link

## Version 2: Semantic Search

In Version 2, I added semantic search using sentence-transformer embeddings.

Instead of only relying on exact keyword matching, the app converts paper abstracts and the user's semantic question into numerical embeddings. It then calculates cosine similarity between the question embedding and paper abstract embeddings to rank the most relevant papers.

Example semantic question:

```text
Which papers discuss attention mechanisms for long-horizon forecasting?
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
  
