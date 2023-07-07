from dataclasses import dataclass


@dataclass
class Document:
    url: str
    content: str
