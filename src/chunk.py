from langchain_text_splitters import RecursiveCharacterTextSplitter

class DocumentChunker:

    def __init__(self):

        self.splitter = RecursiveCharacterTextSplitter(
            chunk_size=500,
            chunk_overlap=100,
            separators=[
                "\n\n",
                "\n",
                ". ",
                " ",
                ""
            ]
        )

    def split_document(self, document):

        chunks = self.splitter.split_text(document)

        return chunks