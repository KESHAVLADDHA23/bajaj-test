from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

class RequestData(BaseModel):
    data: List[str]


@app.get("/")
def read_root():
    return {"message": "Backend is running!"}



@app.get("/bfhl")
def get_code():
    return {"operation_code": 1}

@app.post("/bfhl")
def process_data(request: RequestData):
    if not request.data:
        raise HTTPException(status_code=400, detail="Invalid JSON: 'data' field is required.")

    user_id = "keshav_laddha_23012004"
    college_email_id = "keshav@xyz.com"
    college_roll_no = "CU123456"

    numbers = []
    alphabets = []

    for item in request.data:
        if item.isdigit():
            numbers.append(item)
        elif item.isalpha() and len(item) == 1:
            alphabets.append(item)

    highest_alphabet = ""
    for char in alphabets:
        if highest_alphabet == "" or char.upper() > highest_alphabet.upper():
            highest_alphabet = char

    return {
        "is_success": True,
        "user_id": user_id,
        "email": college_email_id,
        "roll_number": college_roll_no,
        "numbers": numbers,
        "alphabets": alphabets,
        "highest_alphabet": [highest_alphabet] if highest_alphabet else []
    }
