# AI Research Paper Assistant using arXiv API and Streamlit

## Overview

This is a simple research paper assistant built with Python, Streamlit, and the arXiv API.

The main idea of this project is to make it easier to search academic papers from arXiv. The user can enter a research topic, and the app returns relevant papers with their title, authors, publication date, abstract, and PDF link.

In the current version, I focused mainly on papers related to transformer-based time series forecasting.

## Why I built this

As a statistics and data science student, I often need to search for research papers while preparing for projects, thesis ideas, or technical discussions. Searching manually can take time, and sometimes the results are not very focused.

This project is a first step toward building a more advanced AI research assistant that can later include semantic search, paper summarization, and RAG-based question answering.

## Features

- Search research papers from arXiv
- Display paper title, authors, publication date, abstract, and PDF link
- Focus results on AI, machine learning, and statistics-related papers
- Save the results into a CSV file
- Download the search results from the app
- Simple Streamlit interface

## Tech Stack

- Python
- Streamlit
- Pandas
- arXiv API

## Folder Structure

```text
agentic-ai-research-assistant/
│
├── data/
│   └── arxiv_papers.csv
│
├── src/
│   └── arxiv_search.py
│
├── app.py
├── requirements.txt
├── README.md
└── .gitignore

