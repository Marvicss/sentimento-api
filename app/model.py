import pickle
import numpy as np
from tensorflow.keras.models import load_model

# Carrega os artefatos
modelo = load_model("app/modelo_salvo/modelo.h5")

with open("app/modelo_salvo/vectorizer.pkl", "rb") as f:
    vectorizer = pickle.load(f)

with open("app/modelo_salvo/encoder.pkl", "rb") as f:
    encoder = pickle.load(f)

def prever_sentimento(frase: str) -> str:
    texto_vec = vectorizer.transform([frase])
    pred = modelo.predict(texto_vec.toarray())
    classe = encoder.inverse_transform([np.argmax(pred)])
    return classe[0]
