import json
import os
from pydantic import BaseModel
from typing import List, Optional

os.chdir(os.path.dirname(os.path.abspath(__file__)))


class Book(BaseModel):
    title: str
    subtitle: str
    author: str
    publisher: str
    price: float
    isbn_10: Optional[str]
    isbn_13: Optional[str] = None
    subtitle: Optional[str] = None


def main() -> None:
    with open("./data.json") as file:
        data = json.load(file)
        books: List[Book] = [Book(**item) for item in data]
        print(books[0])


if __name__ == "__main__":
    main()
