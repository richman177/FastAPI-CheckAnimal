from fastapi import APIRouter, HTTPException, UploadFile, File
from predict import get_prediction

router = APIRouter(prefix='/api', tags=['Test2'])


@router.post('/predict')
async def predict(file: UploadFile = File(...)):

    try:
        image_bytes = await file.read()

        if not image_bytes:
            raise HTTPException(status_code=400, detail='Файл кошулган жок')

        result = await get_prediction(image_bytes)
        return result

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
