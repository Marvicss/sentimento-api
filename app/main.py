from fastapi import FastAPI
from pydantic import BaseModel
from app.model import prever_sentimento
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Você pode trocar "*" por uma lista de domínios específicos ex: ["http://localhost:3000"]
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class EntradaTexto(BaseModel):
    frase: str

@app.post("/classificar")
def classificar_sentimento(entrada: EntradaTexto):
    resultado = prever_sentimento(entrada.frase)
    return {"sentimento": resultado}
