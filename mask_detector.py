import cv2
import numpy as np
from tensorflow.keras.models import load_model

model = load_model("models/mask_model.h5")

def detect_mask(face):

    face = cv2.resize(face,(224,224))
    face = face/255.0
    face = np.reshape(face,(1,224,224,3))

    pred = model.predict(face)

    if pred[0][0] > pred[0][1]:
        return "Mask"
    else:
        return "No Mask"