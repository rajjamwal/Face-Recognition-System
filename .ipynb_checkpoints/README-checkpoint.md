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
![Description of image](images/demo.png)


## Project Structure
face_recognition/
│
├── images/                # images of interface
│   └── demo.png
├── database/              # Stores face images / embeddings
├── static/                # Static files for Flask (CSS, JS, images)
├── templates/             # HTML templates for Flask
│
├── main.py                # Main script to run face recognition & attendance
├── utils.py               # Helper functions
├── embeddings.pkl         # Pickled face embeddings database
├── attendance_log.txt     # Text log of attendance
│
├── notebooks/
│   ├── face.ipynb         # Jupyter notebook for initial face recognition tests
│   ├── Flask.ipynb        # Notebook experimenting with Flask routes
│   └── html.ipynb         # Notebook for HTML rendering experiments
│
└── README.md              # This file

 
---
-> Your database contains indentity names as folder name and stores 5-6 images of the person in jpg/jpeg format inside the folder
-> The algorithm will compare the image embeddings in database with your current embeddings. 
-> Face is recognised with person's name on screen when minimum distance below threshold is found. =
-> Attendance is marked.

##  How to Run

-> Clone the repository
     ```bash
     -git clone https://github.com/rajjamwal/face_recognition.git
     -cd face_recognition

-> Install necessary dependencies
-> run using script "python main.py" in terminal

Navigate to http://127.0.0.1:5000 in your browser