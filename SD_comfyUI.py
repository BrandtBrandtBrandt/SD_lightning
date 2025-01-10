import requests
from dotenv import load_dotenv
import os
import base64
import random

# Load environment variables from .env file
load_dotenv()

# API key from environment variable
BASETEN_API_KEY = os.getenv("SD_LIGHTNING_API")
if not BASETEN_API_KEY:
    raise ValueError("API_KEY not found. Please ensure it's set in the .env file.")

# Replace the empty string with your model id below
model_id = "5qe60523"

values = {
  "positive_prompt": "A forrest seen from above, with a lake in the center, 4k",
  "negative_prompt": "blurry, text, low quality",
  "controlnet_image": "https://drive.google.com/uc?export=download&id=1P1OmivWs7KyU8yUAbrZ8oM9TxEj3DpxB",
  "seed": random.randint(1, 1000000)
}

#Call model endpoint
res = requests.post(
    f"https://model-{model_id}.api.baseten.co/production/predict",
    headers={"Authorization": f"Api-Key {BASETEN_API_KEY}"},
    json={"workflow_values": values},
)

res = res.json()
preamble = "data:image/png;base64,"
output = base64.b64decode(res["result"][1]["data"].replace(preamble, ""))

# Save image to file
img_file = open("comfyui.png", 'wb')
img_file.write(output)
img_file.close()
os.system("open comfyui.png")