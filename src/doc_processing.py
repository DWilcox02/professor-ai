from device_management import device
from haystack.document_stores import InMemoryDocumentStore
from haystack.utils import convert_files_to_docs
from haystack.nodes import EmbeddingRetriever

# Initialize the document store
document_store = InMemoryDocumentStore(use_bm25=True, embedding_dim=384)

# Delete existing documents in the document store
document_store.delete_documents()

# Convert and load documents (PDF, text files, etc.) into Haystack
DOCS_PATH = "./data/knowledge-docs/"
docs = convert_files_to_docs(dir_path=DOCS_PATH)

# Embed the documents
retriever = EmbeddingRetriever(
    document_store=document_store, embedding_model="sentence-transformers/all-MiniLM-L6-v2", use_gpu=device
)

# Write the converted documents into the document store
document_store.write_documents(docs)
document_store.update_embeddings(retriever)
