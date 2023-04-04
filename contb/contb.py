from fastapi import FastAPI

app = FastAPI()

@app.get('/b')
def b():
    print("contb b()")