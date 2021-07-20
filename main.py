import fastapi
import uvicorn


app = fastapi.FastAPI()


@app.get('/api/calculate')
def calculate(a, b):
    value = a + b
    return {'value': value}


if __name__ == '__main__':
    uvicorn.run(app)
