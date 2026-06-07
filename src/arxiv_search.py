import arxiv
import pandas as pd
from pathlib import Path


def search_arxiv(query, max_results=10):
    """
    Search research papers from arXiv based on a user query.
    """

    client = arxiv.Client()

    search_query = '(("time series" AND forecasting AND transformer) OR ("time series" AND forecasting AND attention) OR ("deep learning" AND "time series")) AND (cat:cs.LG OR cat:stat.ML OR cat:cs.AI)'


    search = arxiv.Search(

        query=search_query,
        max_results=max_results,
        sort_by=arxiv.SortCriterion.Relevance
)

    papers = []

    for result in client.results(search):
        paper = {
            "title": result.title,
            "authors": ", ".join(author.name for author in result.authors),
            "published": result.published.strftime("%Y-%m-%d"),
            "summary": result.summary.replace("\n", " "),
            "pdf_url": result.pdf_url,
            "arxiv_url": result.entry_id,
            "query": query
        }

        papers.append(paper)

    return pd.DataFrame(papers)


def save_papers_to_csv(df, filename="data/arxiv_papers.csv"):
    """
    Save searched papers into a CSV file.
    """

    Path("data").mkdir(exist_ok=True)
    df.to_csv(filename, index=False)
    print(f"Saved {len(df)} papers to {filename}")


if __name__ == "__main__":
    query = "transformer time series forecasting"

    df = search_arxiv(query, max_results=10)

    print(df[["title", "published", "pdf_url"]])

    save_papers_to_csv(df)

