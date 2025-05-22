from langchain.document_loaders import JSONLoader
from pathlib import Path

def load_documents(json_path: str):
    loader = JSONLoader(
        file_path=json_path,
        jq_schema=".[]",
        text_content=False
    )
    return loader.load()
