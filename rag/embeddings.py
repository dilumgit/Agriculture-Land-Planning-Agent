from sentence_transformers import SentenceTransformer


class EmbeddingModel:

    def __init__(self, model_name="all-MiniLM-L6-v2"):
        print(f"Loading embedding model: {model_name}")
        self.model = SentenceTransformer(model_name)

    def embed_documents(self, texts):
        return self.model.encode(
            texts,
            convert_to_numpy=True,
            show_progress_bar=True
        )

    def embed_query(self, text):
        return self.model.encode(text, convert_to_numpy=True)


if __name__ == "__main__":

    model = EmbeddingModel()

    sample_text = [
        "Banana cultivation requires well-drained soil.",
        "Ginger grows best in loamy soil."
    ]

    embeddings = model.embed_documents(sample_text)

    print("\nNumber of embeddings:", len(embeddings))
    print("Embedding dimension:", len(embeddings[0]))