from pathlib import Path
from typing import List

from langchain_community.document_loaders import PyPDFLoader
from langchain_core.documents import Document


class PDFLoader:
    """
    Loads all PDF documents from the specified folder.
    """

    def __init__(self, documents_path: str = "rag/data/documents"):
        self.documents_path = Path(documents_path)

    def load_documents(self) -> List[Document]:
        """
        Load all PDF files from the documents folder.

        Returns:
            List[Document]: Loaded LangChain documents.
        """

        documents = []

        if not self.documents_path.exists():
            raise FileNotFoundError(
                f"Documents folder not found: {self.documents_path}"
            )

        pdf_files = sorted(self.documents_path.glob("*.pdf"))

        if not pdf_files:
            raise FileNotFoundError(
                f"No PDF files found in {self.documents_path}"
            )

        for pdf in pdf_files:
            print(f"Loading: {pdf.name}")

            loader = PyPDFLoader(str(pdf))
            docs = loader.load()

            # Store source filename as metadata
            for doc in docs:
                doc.metadata["source"] = pdf.name

            documents.extend(docs)

        print(f"\nLoaded {len(pdf_files)} PDF files")
        print(f"Total Pages Loaded: {len(documents)}")

        return documents


if __name__ == "__main__":
    loader = PDFLoader()
    docs = loader.load_documents()

    print("\nFirst Document Preview")
    print("-" * 60)
    print(docs[0].page_content[:500])