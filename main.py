from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import subprocess


app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://localhost:3001"],
    allow_credentials=True,
    allow_methods=["POST"],
    allow_headers=["*"],
)
# Create the second FastAPI instance
app2 = FastAPI()

# Configure CORS for the second instance
app2.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://localhost:3001"],
    allow_credentials=True,
    allow_methods=["POST"],
    allow_headers=["*"],
)


class Message(BaseModel):
    user: str
    text: str


messages = []

@app.post("/send-and-receive-message/")
async def send_and_receive_message(message: Message):
    messages.append(message)

    elements = message.text.split(',')

    if len(elements) != 7:
        return {"message": "Received text does not contain 7 elements separated by a comma"}

    gender, bmi, b_sugar, b_pressure, b_cholestrol, activity_level, food_preferences = map(
        str.strip, elements)

    # Run the Python script and capture its output
    try:
        result = subprocess.check_output(
            ['python', 'FoodReco.py', gender, bmi, b_sugar, b_pressure,
                b_cholestrol, activity_level, food_preferences],
            text=True, stderr=subprocess.STDOUT
        )

        # Return the result to React
        return {"message": result}
    except subprocess.CalledProcessError as e:
        return {"message": f"Script failed with error: {e.returncode}\n{e.output}"}



class Message(BaseModel):
    user: dict


