from pathlib import Path

from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings


class RAGRetriever:

    def __init__(
        self,
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    ):
        self.embedding_model = HuggingFaceEmbeddings(
            model_name=model_name
        )

        vector_db_path = Path(__file__).parent / "vector_db"

        self.vector_store = FAISS.load_local(
            str(vector_db_path),
            self.embedding_model,
            allow_dangerous_deserialization=True
        )

    def search(self, query: str, k: int = 8):
        return self.vector_store.similarity_search(query, k=k)


if __name__ == "__main__":

    retriever = RAGRetriever()

    query = "Recommend crops for 2 acres in Kurunegala with a budget of Rs. 500000"

    results = retriever.search(query)

    print("\nRetrieved Documents")
    print("=" * 60)

    for i, doc in enumerate(results, start=1):
        print(f"\nResult {i}")
        print("-" * 60)
        print(doc.page_content[:500])