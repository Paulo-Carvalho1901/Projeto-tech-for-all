from fastapi import FastAPI


app = FastAPI(
    title='API Papi concessionaria',
    description='API REST para cadastro, consulta, atualização, e exclusão',
    version='1.0.0'
)

@app.get('/', tags=['root'])
def read_root():
    return {'msg': 'API concessionaria - Visite/docs para documentação'}

# uvicorn app.main:app --reload