import streamlit as st
import cv2
from ultralytics import YOLO
import tempfile
import os

# Load YOLOv8 model
model = YOLO('yolov8n.pt')  # make sure this file is in your working directory

st.title('Human Detection with YOLOv8')
st.markdown('Upload a video to detect humans using YOLOv8.')

# File uploader
upload_file = st.file_uploader('Upload a video file', type=['mp4', 'mov', 'webm'])

if upload_file is not None:
    # Save uploaded file to a temporary location
    with tempfile.NamedTemporaryFile(delete=False, suffix='.mp4') as tfile:
        tfile.write(upload_file.read())
        temp_video_path = tfile.name

    cap = cv2.VideoCapture(temp_video_path)
    stframe = st.empty()

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        # Run YOLO detection
        results = model(frame)[0]
        for box in results.boxes:
            cls = int(box.cls[0])
            if model.names[cls] == 'person':
                x1, y1, x2, y2 = map(int, box.xyxy[0])
                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
                cv2.putText(frame, "person", (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

        # Show frame in Streamlit
        stframe.image(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB), channels="RGB")

    cap.release()
    os.unlink(temp_video_path)