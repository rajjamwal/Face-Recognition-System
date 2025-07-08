import os
import pickle
import numpy as np
from deepface import DeepFace
import pyttsx3

def generate_database_embeddings():
    database = {}

    print("[INFO] Generating embeddings for database...")
    for person in os.listdir("database"):
        person_path = os.path.join("database", person)
        if os.path.isdir(person_path):
            embeddings = []
            for image_name in os.listdir(person_path):
                image_path = os.path.join(person_path, image_name)
                try:
                    embedding = DeepFace.represent(
                        img_path=image_path,
                        model_name="Facenet",
                        enforce_detection=True
                    )[0]["embedding"]
                    embedding = np.array(embedding) / np.linalg.norm(embedding)
                    embeddings.append(embedding)
                    print(f"[INFO] Saved embedding for: {image_path}")
                except Exception as e:
                    print(f"[WARN] Could not process {image_path}: {e}")
            if embeddings:
                database[person] = embeddings

    with open("embeddings.pkl", "wb") as f:
        pickle.dump(database, f)
    print("[INFO] Database embeddings saved to embeddings.pkl")


def recognize_face(input_img_path, threshold=0.7):
    with open("embeddings.pkl", "rb") as f:
        database = pickle.load(f)

    try:
        input_embedding = DeepFace.represent(
            img_path=input_img_path,
            model_name="Facenet",
            enforce_detection=False
        )[0]["embedding"]
        input_embedding = np.array(input_embedding) / np.linalg.norm(input_embedding)

        print(f"[DEBUG] Input embedding norm: {np.linalg.norm(input_embedding):.4f}")
        print(f"[DEBUG] First 5 values: {input_embedding[:5]}")

        min_dist = float("inf")
        recognized_id = None

        for person_id, embeddings in database.items():
            for idx, emb in enumerate(embeddings):
                dist = np.linalg.norm(input_embedding - emb)
                print(f"[DEBUG] Distance to {person_id} - sample {idx+1}: {dist:.4f}")
                if dist < min_dist:
                    min_dist = dist
                    recognized_id = person_id

        print(f"[RESULT] Closest match: {recognized_id} (distance = {min_dist:.4f})")

        if min_dist < threshold:
            return True, recognized_id, min_dist
        else:
            return False, None, min_dist

    except Exception as e:
        print("[ERROR] Recognition failed:", e)
        return False, None, None

engine= pyttsx3.init()
def speak(text): 
         try:
             engine.say(text)
             engine.runAndWait()
         except Exception as e:
             print(f"[ERROR] speaking failed: {e}")


def log_attendance(student_id):
    with open("attendance_log.txt", "a") as f:
        f.write(f"{student_id}\n")
    print(f"[INFO] Logged attendance for {student_id}")
