from fastapi import FastAPI
from pydantic import BaseModel
from app.model import prever_sentimento

app = FastAPI()

class EntradaTexto(BaseModel):
    frase: str

@app.post("/classificar")
def classificar_sentimento(entrada: EntradaTexto):
    resultado = prever_sentimento(entrada.frase)
    return {"sentimento": resultado}
