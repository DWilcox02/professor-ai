from haystack.document_stores import InMemoryDocumentStore
from haystack.utils import convert_files_to_docs

# Initialize the document store
document_store = InMemoryDocumentStore(use_bm25=True)

# Delete existing documents in the document store
document_store.delete_documents()

# Convert and load documents (PDF, text files, etc.) into Haystack
DOCS_PATH = "./data/knowledge-docs/"
docs = convert_files_to_docs(dir_path=DOCS_PATH)

# Write the converted documents into the document store
document_store.write_documents(docs)
