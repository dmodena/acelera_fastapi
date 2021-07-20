import fastapi
import uvicorn


app = fastapi.FastAPI()


@app.get('/api/calculate')
def calculate():
    return 2+2


if __name__ == '__main__':
    uvicorn.run(app)
