from langchain_text_splitters import RecursiveCharacterTextSplitter

from loader import PDFLoader


class DocumentSplitter:
    def __init__(
        self,
        chunk_size: int = 1000,
        chunk_overlap: int = 200
    ):
        self.splitter = RecursiveCharacterTextSplitter(
            chunk_size=chunk_size,
            chunk_overlap=chunk_overlap,
            separators=[
                "\n\n",
                "\n",
                ". ",
                " ",
                ""
            ]
        )

    def split_documents(self, documents):
        chunks = self.splitter.split_documents(documents)
        return chunks


if __name__ == "__main__":

    loader = PDFLoader()
    documents = loader.load_documents()

    splitter = DocumentSplitter()

    chunks = splitter.split_documents(documents)

    print(f"\nTotal Chunks: {len(chunks)}")

    print("\nFirst Chunk")
    print("-" * 60)
    print(chunks[0].page_content)

    print("\nMetadata")
    print(chunks[0].metadata)