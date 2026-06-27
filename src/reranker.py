from sentence_transformers import CrossEncoder


class ReRanker:

    def __init__(self):
        self.model = CrossEncoder(
            "cross-encoder/ms-marco-MiniLM-L-6-v2"
        )

        print("Re-ranking Model Loaded.\n")

    def rerank(
        self,
        query,
        documents,
        top_k=3
    ):

        pairs = []

        for document in documents:

            pairs.append(
                [query, document]
            )

        scores = self.model.predict(pairs)

        ranked = list(zip(documents, scores))

        ranked.sort(
            key=lambda x: x[1],
            reverse=True
        )

        return ranked[:top_k]