import cv2
from deepface import DeepFace
import os

def recognize_face(frame):

    try:
        result = DeepFace.find(
            img_path=frame,
            db_path="dataset",
            model_name="Facenet",
            enforce_detection=False
        )

        if len(result[0]) > 0:
            identity = result[0].iloc[0]['identity']
            name = os.path.basename(os.path.dirname(identity))
            return name

    except:
        return "Unknown"

    return "Unknown"