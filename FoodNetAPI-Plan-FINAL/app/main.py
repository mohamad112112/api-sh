
from fastapi import FastAPI, UploadFile, File
from fastapi.responses import JSONResponse
from .model import predict_image
from .data_loader import load_food_data
from .utils import save_upload_file
from .nutrition_plan import generate_plan

app = FastAPI(title="FoodNet Pro API", description="By mohamad mansour", version="1.2")

food_data = load_food_data()

@app.get("/")
async def root():
    return {"message": "Welcome to FoodNet Pro 🍽️ - by mohamad mansour"}

@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    img_path = save_upload_file(file)
    result = predict_image(img_path, food_data)
    if result:
        return result
    return JSONResponse(status_code=404, content={"error": "الصنف غير معروف"})

@app.post("/plan")
async def plan(
    height_cm: float,
    weight_kg: float,
    target_weight: float,
    activity_level: str = "medium",
    gender: str = "male",
    age: int = 25
):
    return generate_plan(height_cm, weight_kg, target_weight, activity_level, gender, age)
