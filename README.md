# 🧠 YOLOv8 Object Detection App (Streamlit)

This project uses **YOLOv8** with **Streamlit** to create interactive video-based object detection apps.

It includes two separate interfaces:
- 🎯 `Person_detection.py` → Detects **only persons** from a video
- 🌐 `YOLO_Project.py` → Detects **all objects** supported by YOLOv8

Also included:
- 🧠 `yolov8n.pt` → Pretrained YOLOv8 nano model (lightweight and fast)

---

## 📂 Folder Structure

YOLO-Project/
├── Person_detection.py # Streamlit app for detecting only people
├── YOLO_Project.py # Streamlit app for general object detection
├── yolov8n.pt # YOLOv8n model weights
└── README.md # You're here :)

## 🔧 Requirements

- Python 3.8 or above
- `ultralytics`
- `opencv-python`
- `streamlit`

### 📦 Installation
```bash
pip install streamlit opencv-python ultralytics

🚀 How to Run the Apps
**👤 Person-Only Detection**
streamlit run Person_detection.py
**🌐 General Object Detection (all YOLO classes)**
streamlit run YOLO_Project.py


.

🧠 About the Model
1.yolov8n.pt is the nano version of YOLOv8:
2.Fastest and most lightweight
3.Good for real-time or low-resource environments
4.Automatically loaded inside each script using the ultralytics library

📌 Features
1.🖼️ Upload and process any video file
2.🧍 Person-only detection option
3.📦 General multi-object detection using YOLOv8
4.⚡ Real-time frame-by-frame processing and display
5.💡 Simple Streamlit interface (no code editing needed)

💡 Customization Tips
12You can switch to another YOLO model (e.g., yolov8s.pt, yolov8m.pt) by replacing the .pt file path
2.To modify confidence thresholds or supported classes, adjust the YOLO model configuration inside the scripts

📜 License
This project is licensed under the MIT License.
YOLOv8 is provided by Ultralytics, under their respective license.
