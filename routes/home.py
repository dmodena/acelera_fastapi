import fastapi

router = fastapi.APIRouter()


@router.get('/')
def index():
    return fastapi.responses.RedirectResponse(url='/home')


@router.get('/home')
def home():
    return {'message': 'Hello!'}
