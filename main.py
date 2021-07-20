import fastapi
import uvicorn


app = fastapi.FastAPI()


@app.get('/api/calculate')
def calculate():
    return 2+2


uvicorn.run(app)
