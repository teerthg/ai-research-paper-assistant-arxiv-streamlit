import chromadb


def get_chroma_client():
    """
    Create a persistent ChromaDB client.
    Data will be stored locally in the chroma_db folder.
    """
    client = chromadb.PersistentClient(path="chroma_db")
    return client


def get_or_create_collection(client, collection_name="arxiv_papers"):
    """
    Get an existing ChromaDB collection or create a new one.
    """
    collection = client.get_or_create_collection(name=collection_name)
    return collection


def add_papers_to_chroma(collection, df, embeddings):
    """
    Add paper metadata and embeddings to ChromaDB.
    """

    ids = []
    documents = []
    metadatas = []
    embedding_list = []

    for index, row in df.iterrows():
        paper_id = f"paper_{index}"

        ids.append(paper_id)
        documents.append(row["summary"])

        metadatas.append(
            {
                "title": row["title"],
                "authors": row["authors"],
                "published": row["published"],
                "pdf_url": row["pdf_url"],
                "arxiv_url": row["arxiv_url"],
            }
        )

        embedding_list.append(embeddings[index].tolist())

    collection.add(
        ids=ids,
        documents=documents,
        metadatas=metadatas,
        embeddings=embedding_list
    )


def search_chroma(collection, query_embedding, top_k=5):
    """
    Search ChromaDB using a query embedding.
    """

    results = collection.query(
        query_embeddings=query_embedding.tolist(),
        n_results=top_k
    )

    return results