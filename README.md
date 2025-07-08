# Face Recognition Attendance System

This is a simple yet functional face recognition project that logs attendance based on detected faces.  
It also includes a basic Flask web interface for face recognition.

---

## Features
✅ Detect and recognize faces from a live webcam feed  
✅ Store face embeddings in a local database  
✅ Maintain an attendance log  
✅ Simple Flask app to view logs on a browser

---

<p align="center">
  <img src="images/demo.png" alt="Demo" width="500"/>
</p>

---

## Project Structure
```bash
face_recognition/
├── images/                # images of interface
│   └── demo.png
├── database/              # folders named by person with images inside
├── static/                # static files for Flask (CSS, JS, images)
├── templates/             # HTML templates for Flask
│
├── main.py                # main script to run face recognition & attendance
├── utils.py               # helper functions
├── embeddings.pkl         # pickled face embeddings database
├── attendance_log.txt     # text log of attendance
│
├── notebooks/
│   ├── face.ipynb         # initial face recognition tests
│   ├── Flask.ipynb        # experimenting with Flask routes
│   └── html.ipynb         # HTML rendering experiments
│
└── README.md              # this file
```
## How to Run

```bash
# 1️⃣ Clone the repository
git clone https://github.com/rajjamwal/Face-Recognition-System.git
cd face_recognition

# 2️⃣ Install dependencies
pip install -r requirements.txt

# 3️⃣ Run the main face recognition script
python main.py

# 4️⃣ Open your browser at
http://127.0.0.1:5000

- Ensure your 'database/' folder contains subfolders named after each person,
  with about 5-6 images (.jpg/.jpeg) of their face inside.

- The algorithm compares embeddings from these folders
  with the live webcam feed.

- When a face is recognized (distance < threshold),
  it displays the name on screen and marks attendance
  in 'attendance_log.txt'.
