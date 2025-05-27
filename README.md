
# 🎯 YOLOv8 Laptop Camera Object Detection

A real-time object detection system that uses your **laptop's webcam** powered by **YOLOv8** and **OpenCV**. This project demonstrates the power of computer vision to detect common objects from a live video stream with fast and accurate inference.

---

## 📸 Live Demo Preview

> Real-time object detection on webcam feed:

![demo](demo/demo.gif) <!-- Replace with actual demo gif -->

---

## ✨ What This Project Does

- 🔍 Detects objects (e.g. people, cars, bottles) from webcam in real time
- 🚀 Uses YOLOv8n (nano model) for high-speed inference
- 🧠 Built in Python using Ultralytics' YOLOv8 API
- 💡 Easily modifiable to support video input, image input, or recording output

---

## 🔧 Built With

- [Ultralytics YOLOv8](https://docs.ultralytics.com/)
- [OpenCV](https://opencv.org/)
- Python 3.x
- NumPy

---

## 🚀 Quickstart

### 1️⃣ Clone the Repo

```bash
git clone https://github.com/YOUR_USERNAME/object-detection-laptop-camera.git
cd object-detection-laptop-camera
```

### 2️⃣ Set Up Virtual Environment

```bash
python -m venv venv
source venv/Scripts/activate  # On Git Bash
```

> Or, if you're using CMD:

```cmd
venv\Scripts\activate
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

Or manually:

```bash
pip install ultralytics opencv-python numpy
```

### 4️⃣ Run the App

```bash
python yolo_detect.py
```

> Press `q` to close the camera window.

---

## 📁 File Overview

```
object-detection-laptop-camera/
├── yolo_detect.py         # Main script running YOLOv8 on webcam
├── test_camera.py         # Simple webcam test script
├── requirements.txt       # Python packages
├── demo/                  # Folder for output GIFs/images
└── README.md              # This file
```

---

## 🧠 Applications

- Surveillance cameras
- Interactive AI projects
- Human detection for safety or automation
- Robotics and drone vision

---

## 👤 Author

**Tushar Dhulasawant**  
_Aerospace Engineer | Embedded Systems Developer | AI Enthusiast_

- 🔗 [LinkedIn](https://www.linkedin.com/in/tushar-dhulasawant)
- 📧 tushardhulasawant5@gmail.com

---

## 📄 License

MIT License – free to use and modify.
