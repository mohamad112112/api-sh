
def generate_plan(height_cm, weight_kg, target_weight, activity_level, gender="male", age=25):
    # حساب معدل الأيض الأساسي BMR باستخدام معادلة Mifflin-St Jeor
    gender_factor = 5 if gender == "male" else -161
    bmr = 10 * weight_kg + 6.25 * height_cm - 5 * age + gender_factor

    if activity_level == "low":
        calories = bmr * 1.2
    elif activity_level == "medium":
        calories = bmr * 1.5
    else:
        calories = bmr * 1.75

    status = "تثبيت وزن"
    if target_weight < weight_kg:
        calories -= 500
        status = "خسارة وزن"
    elif target_weight > weight_kg:
        calories += 500
        status = "زيادة وزن"

    # نموذج وجبات وتمارين
    if status == "خسارة وزن":
        meals = {
            "breakfast": "بيض مسلوق + خضار + شوفان",
            "lunch": "صدر دجاج مشوي + أرز بني + سلطة",
            "dinner": "لبن قليل الدسم + توست + تفاح",
            "snacks": ["شاي أخضر", "مكسرات خفيفة"]
        }
        workout = {"type": "جري أو تمارين كارديو", "duration_per_day": "45 دقيقة"}
    elif status == "زيادة وزن":
        meals = {
            "breakfast": "بيض + جبنة + خبز أسمر + حليب",
            "lunch": "لحم أو دجاج + بطاطا + رز",
            "dinner": "تونة + خبز + زبادي",
            "snacks": ["مكسرات", "عصير طبيعي"]
        }
        workout = {"type": "تمارين مقاومة (جيم)", "duration_per_day": "ساعة واحدة"}
    else:
        meals = {
            "breakfast": "توست + جبنة + خضار",
            "lunch": "دجاج أو سمك + رز + سلطة",
            "dinner": "لبن + خبز + خضار",
            "snacks": ["ماء", "تفاحة"]
        }
        workout = {"type": "مشي أو نشاط خفيف", "duration_per_day": "30 دقيقة"}

    return {
        "status": status,
        "calories_target": round(calories),
        "meals": meals,
        "workout": workout,
        "notes": "اشرب 2.5 لتر ماء يوميًا، وابتعد عن السكر المضاف"
    }
