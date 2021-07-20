import fastapi
import uvicorn
from routes import calculator, home

app = fastapi.FastAPI()

app.include_router(calculator.router)
app.include_router(home.router)


if __name__ == '__main__':
    uvicorn.run(app)
