# 🧠 YOLOv8 Object Detection Project

This project uses **YOLOv8 (You Only Look Once)** models to perform object detection on video files. It contains two scripts:

- 🎯 `Person_detection.py` → Detects only **persons** from a video  
- 🌐 `YOLO_Project.py` → Detects **all objects** supported by YOLOv8  
- 🧠 `yolov8n.pt` → Pretrained YOLOv8 nano model

---

## 📂 Folder Structure

YOLO-Project/
├── Person_detection.py # Detects only people from videos
├── YOLO_Project.py # General object detection for all YOLOv8 classes
├── yolov8n.pt # Pretrained YOLOv8n model (tiny version)
└── README.md # Project documentation

## ⚙️ Requirements

- Python 3.8+
- OpenCV (`cv2`)
- Ultralytics YOLOv8

### 🛠️ Installation

1. Create a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # or venv\Scripts\activate on Windows

**Install dependencies:**
   pip install ultralytics opencv-python

**🚀 How to Run**
👤 Person Detection Only
python Person_detection.py (in command prompt)

**🌐 Full YOLOv8 Object Detection**
python YOLO_Project.py
