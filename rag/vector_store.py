from pathlib import Path

from langchain_community.vectorstores import FAISS
from langchain_core.documents import Document
from langchain_community.embeddings import HuggingFaceEmbeddings

from loader import PDFLoader
from splitter import DocumentSplitter


class VectorStoreBuilder:

    def __init__(
        self,
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    ):
        self.embedding_model = HuggingFaceEmbeddings(
            model_name=model_name
        )

        self.vector_db_path = Path(__file__).parent / "vector_db"

    def build_vector_store(self, documents: list[Document]):

        print("Creating FAISS Vector Store...")

        vector_store = FAISS.from_documents(
            documents,
            self.embedding_model
        )

        vector_store.save_local(str(self.vector_db_path))

        print(f"\nVector database saved to:\n{self.vector_db_path}")

        return vector_store


if __name__ == "__main__":

    loader = PDFLoader()
    documents = loader.load_documents()

    splitter = DocumentSplitter()
    chunks = splitter.split_documents(documents)

    builder = VectorStoreBuilder()

    builder.build_vector_store(chunks)

    print("\nDone.")