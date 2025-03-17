from whoosh.index import create_in
from whoosh.fields import Schema, TEXT
import os

schema = Schema(title=TEXT(stored=True), content=TEXT(stored=True))

def create_index(index_dir="indexdir"):
    if not os.path.exists(index_dir):
        os.mkdir(index_dir)

    ix = create_in(index_dir, schema)
    return ix

def add_document(ix, title, content):
    writer = ix.writer()
    writer.add_document(title=title, content=content)
    writer.commit()

# Create index and add sample document
ix = create_index()
add_document(ix, "Example Page", "This is a sample content of the page.")

# Debug: Check if data was added
with ix.searcher() as searcher:
    print("📌 Indexed Documents:", list(searcher.documents()))
