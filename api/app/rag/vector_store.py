from langchain_qdrant import QdrantVectorStore, RetrievalMode, FastEmbedSparse
from app.core.config import Settings, get_qdrant_client, get_embeddings

def get_vector_store(settings: Settings) -> QdrantVectorStore:
    client = get_qdrant_client(settings)   #qdrant client
    if not client.collection_exists(settings.collection_name):
        raise RuntimeError(f"collection {settings.collection_name} not found.")

    return QdrantVectorStore(
        client=client,
        collection_name=settings.collection_name,   #collection
        embedding=get_embeddings(settings),    #embed
        retrieval_mode=RetrievalMode.HYBRID,
        sparse_embedding=FastEmbedSparse(moel_name="Qdrant/bm25"),
        vector_name="dense",
        sparse_vector_name="sparse"
    )
