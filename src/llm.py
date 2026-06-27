import ollama


class LLM:

    def __init__(self):

        self.model = "llama3.2"

    def generate_answer(
        self,
        question,
        context
    ):

        prompt = f"""
Context:

{context}

Question:

{question}

Answer:
"""

        response = ollama.chat(

            model=self.model,

            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        return response["message"]["content"]