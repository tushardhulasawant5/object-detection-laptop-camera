# 🧠 Object Detection with Laptop Camera using YOLOv8

This project uses a **pre-trained YOLOv8 model** to perform real-time object detection through your laptop's webcam. It leverages **OpenCV** for video streaming and **Ultralytics' YOLOv8** for object inference.

---

## 📸 Demo

> Detecting objects in real-time from webcam:

![demo-gif](demo/demo.gif)  <!-- Replace this with your actual GIF or image path -->

---

## 🚀 Features

- Real-time webcam feed with object detection
- Lightweight YOLOv8n model for fast inference
- Frame-by-frame annotation using OpenCV
- Easily extendable to record output or detect custom classes

---

## 🛠️ Tech Stack

- Python
- OpenCV
- YOLOv8 (via Ultralytics)
- NumPy

---

## 🧪 Setup Instructions

1. Clone the repository:
   ```bash
   git clone https://github.com/YOUR_USERNAME/object-detection-laptop-camera.git
   cd object-detection-laptop-camera

   Step 2: Create and Activate Virtual Environment
bash
Copy
Edit
python -m venv venv
source venv/Scripts/activate  # For Windows Git Bash
On Windows Command Prompt (CMD), use:

cmd
Copy
Edit
venv\Scripts\activate
Step 3: Install Dependencies
bash
Copy
Edit
pip install -r requirements.txt
Or, if you don't have requirements.txt, run:

bash
Copy
Edit
pip install ultralytics opencv-python numpy
Step 4: Run the Detection Script
bash
Copy
Edit
python yolo_detect.py
Press q to exit the webcam window.

🗂️ Project Structure
csharp
Copy
Edit
object-detection-laptop-camera/
├── yolo_detect.py          # YOLOv8 detection using webcam
├── test_camera.py          # Simple webcam test
├── requirements.txt        # List of Python dependencies
├── demo/                   # Screenshots or output GIFs
├── .gitignore
└── README.md               # You're reading this!
📈 Example Use Cases
Smart surveillance systems

Interactive vision projects

Object tracking for drones/robots

Real-time analytics applications

👨‍💻 About the Author
Tushar Dhulasawant
Aerospace & Embedded Systems Engineer with a passion for AI, automation, and real-time systems.

🔗 LinkedIn Profile

📧 tushardhulasawant5@gmail.com

🪪 License
This project is open-source under the MIT License.
