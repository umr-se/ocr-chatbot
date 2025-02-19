# OCR Chatbot

OCR Chatbot is a web-based application that extracts text from images using the Flash model and provides responses to user prompts. The backend is developed in FastAPI, integrating the Gemini API key for enhanced capabilities. The extracted text is saved as an Excel file using the `openpyxl` library. The frontend is built using HTML and CSS, while Flask handles request-related logic.

## Features
- Extract text from images using the Flash OCR model.
- Generate Excel files for extracted text using `openpyxl`.
- AI-powered response generation using the Gemini API.
- Web-based interface with HTML & CSS.
- Flask handles request routing and API calls.

## Tech Stack
### Backend
- **FastAPI** – Handles API endpoints.
- **Gemini API** – AI response generation.
- **Flash Model** – OCR for text extraction.
- **openpyxl** – Excel file generation.
- **Flask** – Manages request-related logic.

### Frontend
- **HTML & CSS** – User interface for uploading images and receiving responses.

## Installation & Setup
### Prerequisites
Ensure you have Python installed on your system. You also need `pip` for package management.

### Clone the Repository
```sh
git clone https://github.com/umr-se/ocr_chatbot.git
cd ocr_chatbot
```

### Install Dependencies
```sh
pip install -r requirements.txt
```

### Set Up Environment Variables
Create a `.env` file and add your Gemini API key:
```sh
GEMINI_API_KEY=your_api_key_here
```

### Run the Backend (FastAPI)
```sh
uvicorn app:app --reload
```

### Run the Frontend (Flask)
```sh
cd frontend
python app.py
```

## Usage
1. Upload an image via the web interface.
2. The Flash model extracts text from the image.
3. The extracted text is saved as an Excel file.
4. The Flash model generates responses for any input prompts.
5. Download the generated Excel file from the interface.

## Contributing
Feel free to contribute by creating a pull request or reporting issues.

![image](https://github.com/user-attachments/assets/4b0f36be-8e51-4b14-bdc0-e1e062b1a94a)
![image](https://github.com/user-attachments/assets/3050ebc7-afc3-4933-8c06-621462878bd0)



