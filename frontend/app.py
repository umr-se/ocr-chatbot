from flask import Flask, render_template, request, jsonify, send_from_directory
import requests

app = Flask(__name__, static_url_path="/static")

# FastAPI backend URL
FASTAPI_URL = "http://127.0.0.1:8000/analyze/"  # Replace with the actual FastAPI URL

@app.route("/")
def index():
    # Serve the index.html file for the frontend
    return send_from_directory('.', "index.html")

@app.route("/analyze", methods=["POST"])
def analyze():
    try:
        # Get the prompt and uploaded file from the form
        prompt = request.form.get("prompt", "").strip()  # Text input (prompt)
        file = request.files.get("file")  # File input (optional)

        # Ensure at least the prompt is provided
        if not prompt and not file:
            return jsonify({"error": "Either a prompt or an image file must be provided."}), 400

        # Prepare data to send to FastAPI
        files = {"image": (file.filename, file.stream)} if file else None  # Send file if provided
        data = {"prompt": prompt}  # Include the prompt in data

        # Send request to FastAPI backend
        response = requests.post(FASTAPI_URL, files=files, data=data)
        response.raise_for_status()  # Raise an exception if the request fails

        # Return the JSON response from FastAPI
        return jsonify(response.json())
    except requests.exceptions.RequestException as e:
        # Catch any errors from the FastAPI backend
        return jsonify({"error": f"Failed to communicate with FastAPI: {str(e)}"}), 500
    except Exception as e:
        # Catch any other errors
        return jsonify({"error": f"Unexpected error: {str(e)}"}), 500

if __name__ == "__main__":
    app.run(debug=True, port=5000)
