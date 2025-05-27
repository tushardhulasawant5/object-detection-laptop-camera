
# 🐾 Animal Detection Using YOLOv8 and Laptop Camera

This project detects **animals in real time** using your laptop's webcam and the YOLOv8 object detection model. It filters out all non-animal objects and highlights only animals such as dogs, cats, elephants, and birds.

---

## 📷 Demo Snapshot

> Real-time animal detection preview:

![demo](demo/demo.gif) <!-- Replace this with your own gif or screenshot -->

---

## 🧠 What It Detects

Only the following animals (based on COCO dataset classes):

- 🐶 Dog
- 🐱 Cat
- 🐴 Horse
- 🐑 Sheep
- 🐄 Cow
- 🐘 Elephant
- 🐻 Bear
- 🦓 Zebra
- 🦒 Giraffe
- 🐦 Bird

---

## ⚙️ Technologies Used

- Python 3.x
- OpenCV
- Ultralytics YOLOv8
- NumPy

---

## 🚀 How to Run

### Step 1: Clone the Repo

```bash
git clone https://github.com/YOUR_USERNAME/object-detection-laptop-camera.git
cd object-detection-laptop-camera
```

### Step 2: Set Up Virtual Environment

```bash
python -m venv venv
source venv/Scripts/activate  # For Git Bash
```

> On CMD:

```cmd
venv\Scripts\activate
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

> Or manually:

```bash
pip install ultralytics opencv-python numpy
```

### Step 4: Run the Detection Script

```bash
python yolo_detect.py
```

> Press `q` to quit the webcam window.

---

## 📁 Project Structure

```
object-detection-laptop-camera/
├── yolo_detect.py         # Animal-only YOLOv8 detection
├── test_camera.py         # Webcam test script
├── requirements.txt       # Dependencies
├── demo/                  # Screenshots or GIFs
└── README.md              # This file
```

---

## 📈 Use Cases

- Wildlife detection systems
- Smart pet monitoring
- Educational demos
- AI-powered surveillance in zoos or forests

---

## 👨‍💻 Author

**Tushar Dhulasawant**  
_Aerospace & Embedded Systems Engineer with passion for AI and real-time systems_

- 🔗 [LinkedIn](https://www.linkedin.com/in/tushar-dhulasawant)
- 📧 tushardhulasawant5@gmail.com

---

## 📄 License

This project is licensed under the MIT License.
