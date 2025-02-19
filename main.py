from fastapi import FastAPI, Form, File, UploadFile, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import google.generativeai as genai
from PIL import Image
import io

app = FastAPI()

# Set up CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins for testing
    allow_credentials=True,
    allow_methods=["POST"],
    allow_headers=["*"],
)

# Set up Gemini API key
API_KEY = "your-api-key"  # Replace with your actual API key
genai.configure(api_key=API_KEY)

@app.post("/analyze/")
async def analyze_text_or_image(
    prompt: str = Form(None),  # Optional prompt
    image: UploadFile = File(None)  # Optional image upload
):
    try:
        # Ensure at least one of the inputs (prompt or image) is provided
        if not prompt and not image:
            raise HTTPException(status_code=400, detail="Either a prompt or an image must be provided.")

        # Initialize the Gemini model
        model = genai.GenerativeModel("gemini-1.5-flash")

        # Handle image if provided
        if image:
            try:
                # Read the uploaded image
                image_bytes = await image.read()
                img = Image.open(io.BytesIO(image_bytes))
                img.load()  # Ensure the image is fully loaded
                # If prompt is provided, combine prompt and image for analysis
                response = model.generate_content([img, prompt])
                return {
                    "gemini_analysis": response.text if response else "No response from Gemini.",
                    "image_name": image.filename,
                    "image_size": f"{image.file._file.tell()} bytes",  # Include the image size in the response
                }

            except Exception as e:
                raise HTTPException(status_code=500, detail=f"Error processing image: {str(e)}")

        # Handle prompt if provided (even if no image is uploaded)
        if prompt and not image:
            response = model.generate_content(prompt)
            return {
                "gemini_analysis": response.text if response else "No response from Gemini.",
                "prompt_length": len(prompt),  # Include the length of the prompt in the response
            }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
