from fastapi import FastAPI, UploadFile, File, Form
from llm_chain import build_qa_chain
import tempfile, os

app = FastAPI()

@app.post("/ask")
async def ask_question(file: UploadFile = File(...), question: str = Form(...)):
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as temp:
        content = await file.read()
        temp.write(content)
        temp.flush()
        qa_chain = build_qa_chain(temp.name)
        answer = qa_chain.run(question)
        os.unlink(temp.name)
        return {"answer": answer}
