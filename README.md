<div align="center">

# 🎯 Real-Time Object Detection via IP Webcam

### Detect objects live using your phone as a camera — powered by YOLOv8

---

## 📌 Overview

This project streams live video from a **mobile phone camera** (via IP Webcam) and runs **real-time object detection** using the [YOLOv8n](https://docs.ultralytics.com/) model. It's optimized for speed — using frame skipping, resolution reduction, and a lightweight YOLO variant to maximize FPS on standard hardware.

> No fancy GPU required. Runs efficiently on a regular laptop.

---

## ✨ Features

- 📡 **Live phone camera stream** — uses IP Webcam app over Wi-Fi
- ⚡ **Optimized for performance** — frame skipping + lower resolution = higher FPS
- 🧠 **YOLOv8n model** — fastest and most lightweight YOLO variant
- 🖼️ **Annotated output** — bounding boxes and labels drawn in real time
- 🔧 **Simple setup** — only 3 dependencies

---

## 🛠️ Tech Stack

| Tool | Purpose |
|------|---------|
| [Ultralytics YOLOv8](https://github.com/ultralytics/ultralytics) | Object detection model |
| [OpenCV](https://opencv.org/) | Video capture & frame rendering |
| [IP Webcam (Android)](https://play.google.com/store/apps/details?id=com.pas.webcam) | Phone as IP camera |

---

## 📋 Requirements

- Python 3.8+
- An Android phone with the **IP Webcam** app installed
- Both your PC and phone on the **same Wi-Fi network**

---

## ⚙️ Installation

**1. Clone the repository**
```bash
git clone https://github.com/YOUR_USERNAME/Object_Detection.git
cd Object_Detection
```

**2. Install dependencies**
```bash
pip install ultralytics opencv-python
```

> The `yolov8n.pt` model file is included in the repo — no separate download needed.

---

## 🚀 Usage

**1. Start IP Webcam on your phone**
- Open the app → scroll down → tap **"Start Server"**
- Note the IP address shown on screen (e.g., `http://192.168.x.x:8080`)

**2. Update the stream URL in `object_detection.py`**
```python
url = "http://YOUR_PHONE_IP:8080/video"
```

**3. Run the script**
```bash
python object_detection.py
```

**4. Press `ESC` to quit**

---

## 📁 Project Structure

```
Object_Detection/
│
├── object_detection.py   # Main detection script
├── yolov8n.pt            # YOLOv8 nano model weights
└── README.md
```

---

## ⚡ Performance Tuning

The script is pre-configured with these optimizations:

| Setting | Value | Effect |
|--------|-------|--------|
| `frame_skip = 2` | Every 2nd frame | Doubles effective FPS |
| `imgsz = 320` | Inference resolution | Faster inference |
| `conf = 0.5` | Confidence threshold | Filters weak detections |
| Frame resize | 480×360 | Reduces processing load |

Tweak these values in `object_detection.py` to balance speed vs. accuracy for your hardware.

---

## 🔧 Troubleshooting

**❌ "Could not open IP camera"**
- Make sure the IP Webcam server is running on your phone
- Ensure both devices are on the same Wi-Fi network
- Double-check the URL in the script

**❌ Low FPS / laggy stream**
- Increase `frame_skip` (e.g., set to `3` or `4`)
- Reduce `imgsz` to `224`
- Move closer to your Wi-Fi router

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

---

<div align="center">
Made with ❤️ using Python & YOLOv8
</div>
