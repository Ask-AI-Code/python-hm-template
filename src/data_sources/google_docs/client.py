from typing import List

from src.data_sources.google_docs.dataclasses import Document

__all__ = ["GoogleDocsClient"]

FAKE_KEY = "fake-google-docs-key"


class GoogleDocsClient:
    def __init__(self, credentials: str):
        self.credentials = credentials

    def get_docs(self) -> List[Document]:
        """
        Get the customer documents
        :return: documents
        """
        if not self.credentials or self.credentials != FAKE_KEY:
            raise ValueError("Wrong credentials provided")

        return [
            Document(
                url="https://docs.google.com/document/d/1/edit",
                content="Hello World - 1",
            ),
            Document(
                url="https://docs.google.com/document/d/2/edit",
                content="Hello World - 2",
            ),
        ]
