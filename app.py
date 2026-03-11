import streamlit as st
import cv2
from face_recognition import recognize_face
from attendance import register_attendance
from mask_detector import detect_mask
from export_excel import export_excel

st.title("AI Smart Attendance System")

run = st.checkbox("Start Camera")

camera = cv2.VideoCapture(0)

FRAME_WINDOW = st.image([])

while run:

    ret, frame = camera.read()

    name = recognize_face(frame)

    mask_status = detect_mask(frame)

    if name != "Unknown" and mask_status=="Mask":
        register_attendance(name)

    cv2.putText(frame,name,(30,50),cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),2)
    cv2.putText(frame,mask_status,(30,90),cv2.FONT_HERSHEY_SIMPLEX,1,(255,0,0),2)

    FRAME_WINDOW.image(frame)

if st.button("Export Excel Report"):
    st.success(export_excel())