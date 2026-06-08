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
```

## How to Run

Clone the repository:

```bash
git clone https://github.com/teerthg/ai-research-paper-assistant-arxiv-streamlit.git
```

Go to the project folder:

```bash
cd ai-research-paper-assistant-arxiv-streamlit
```

Create a virtual environment:

```bash
python -m venv venv
```

Install the required packages:

```bash
pip install -r requirements.txt
```

Run the Streamlit app:

```bash
streamlit run app.py
```

On Windows, this command can also be used:

```bash
.\venv\Scripts\python.exe -m streamlit run app.py
```

## Example Search

Research topic:

```text
transformer time series forecasting
```

Semantic question:

```text
Which papers discuss attention mechanisms for long-horizon forecasting?
```

## Output

For each paper, the app shows:

- Title
- Authors
- Published date
- Abstract
- PDF link
- Similarity score for semantic search results

The user can download both keyword search results and semantic search results as CSV files.

## Current Limitations

- The current version mainly focuses on transformer-based time series forecasting.
- The app uses abstracts rather than full paper PDFs.
- Semantic search ranks papers by abstract similarity, but it does not yet generate full answers.
- The app does not yet include citation analysis or paper summarization.

## Future Work

- Add ChromaDB for persistent vector storage
- Add RAG-based question answering
- Add automatic paper summarization
- Use Semantic Scholar API for citation information
- Add filters for year, author, and paper category
- Build an agentic workflow using LangGraph

## Status

Version 2 completed.

The app can search arXiv papers, display results, save them as CSV, and perform semantic search using sentence-transformer embeddings and cosine similarity.
