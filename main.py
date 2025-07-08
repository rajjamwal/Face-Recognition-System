# main.py
from flask import Flask, request, render_template
import os
import base64
import cv2
import numpy as np
import time
from utils import recognize_face, log_attendance, generate_database_embeddings,speak

app = Flask(__name__)
os.makedirs("static", exist_ok=True)

@app.route("/", methods=["GET", "POST"])
def index():
    status = ""
    image_path = None

    if request.method == "POST":
        img_data = request.form["captured_image"]

        # Decode base64 image
        header, encoded = img_data.split(",", 1)
        image_bytes = base64.b64decode(encoded)
        nparr = np.frombuffer(image_bytes, np.uint8)
        img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

        # Save with timestamp
        timestamp = int(time.time())
        filename = f"captured_{timestamp}.jpg"
        filepath = os.path.join("static", filename)
        cv2.imwrite(filepath, img)

        # 🔍 Recognition instead of verification
        match, recognized_id, distance = recognize_face(filepath)

        if match:
            status = f"✅ Recognized: {recognized_id} (distance = {distance:.4f})"
            log_attendance(recognized_id)
            speak(f"Welcome {recognized_id}")
        else:
            status = f"❌ Face not recognized (min distance = {distance:.4f})"
            speak("Face not recognized")

        image_path = f"static/{filename}"

    return render_template("index.html", status=status, image_path=image_path)

if __name__ == "__main__":
    if not os.path.exists("embeddings.pkl"):
        generate_database_embeddings()
    app.run(debug=True)
