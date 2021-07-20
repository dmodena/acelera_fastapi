import fastapi
import uvicorn


app = fastapi.FastAPI()


@app.get('/api/calculate')
def calculate():
    value = 2+2
    return {'value': value}


if __name__ == '__main__':
    uvicorn.run(app)
