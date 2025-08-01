import streamlit as st
import cv2
from ultralytics import YOLO
import tempfile
import os
import random

# Load YOLOv8 model
model = YOLO('yolov8n.pt')  # Make sure this file is in your working directory

st.title('YOLOv8 Object Detection')
st.markdown('Upload a video to detect multiple objects using YOLOv8.')

# Generate color for each class name
def get_color(name):
    random.seed(hash(name) % 10000)  # Deterministic color based on class name
    return tuple(random.randint(0, 255) for _ in range(3))
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
            class_name = model.names[cls]
            x1, y1, x2, y2 = map(int, box.xyxy[0])

            color = get_color(class_name) # Get color for the class name

            # Draw bounding box and label
            cv2.rectangle(frame, (x1, y1), (x2, y2), color, 2)
            cv2.putText(frame, class_name, (x1, y1 - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.9, color, 2)

        # Show frame in Streamlit
        stframe.image(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB), channels="RGB")

    cap.release()
    os.unlink(temp_video_path)
