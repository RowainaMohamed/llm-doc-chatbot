from langchain.document_loaders import PyPDFLoader
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import Chroma
from langchain.chains import RetrievalQA
from langchain.llms import HuggingFacePipeline
from transformers import pipeline

def build_qa_chain(pdf_path):
    loader = PyPDFLoader(pdf_path)
    pages = loader.load_and_split()

    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    db = Chroma.from_documents(pages, embedding=embeddings)

    gen_pipeline = pipeline("text-generation", model="distilgpt2", max_new_tokens=100)
    llm = HuggingFacePipeline(pipeline=gen_pipeline)

    retriever = db.as_retriever()
    qa = RetrievalQA.from_chain_type(llm=llm, retriever=retriever)
    return qa
