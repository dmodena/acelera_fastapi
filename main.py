import fastapi
import uvicorn
from routes import calculator, home, library

app = fastapi.FastAPI()

app.include_router(calculator.router)
app.include_router(home.router)
app.include_router(library.router)


if __name__ == '__main__':
    uvicorn.run(app)
