from typing import Optional

import fastapi
import uvicorn


app = fastapi.FastAPI()


@app.get('/api/calculate')
def calculate(a: int, b: int, c: Optional[int] = None):
    value = (a + b)

    if c == 0:
        return fastapi.responses.JSONResponse(
            content={'error': 'ERROR: c cannot be zero'}, status_code=400)
    elif c is not None:
        value /= c

    return {'value': value}


if __name__ == '__main__':
    uvicorn.run(app)
