from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
from requests import post, get
import operator
import time
app = FastAPI()
class Resp(BaseModel):
    valor1: int
    valor2: int
    operacao: str
    
    def Operacao(self):
        
        resposta : int
        if self.operacao == "+":
            resposta = self.valor1 + self.valor2
            return {"resultado" : resposta}
        elif self.operacao == "-":
            resposta = self.valor1 - self.valor2
            return {"resultado" : resposta}
        elif self.operacao == "*":
            resposta = self.valor1 * self.valor2
            return {"resultado" : resposta}
        elif self.operacao == "/":
            resposta = self.valor1 / self.valor2
            return {"resultado" : resposta}
        else:
            return "Operador errado"

        
    # apt: Optional[str] = None
    

@app.post('/novarota')
async def novarota(resp: Resp):
    
    return resp.Operacao()





@app.get('/')
async def root():
    
    return {
        'resultado': 'resposta'
        }




