# ☕ Cafe Vision – Plainsight OpenFilter Hackathon 2025  

**Real-time Productivity & Customer Flow Tracker for Coffee Shops**  
Built in 4 hours during the Plainsight × OpenFilter Computer Vision Hackathon.  

---

## 🎯 Overview
Cafe Vision uses **OpenFilter**, **YOLOv8**, and **OpenCV** to create an intelligent vision pipeline that tracks:  
- 🧑‍🍳 Barista productivity – how many coffees are made per shift  
- 👥 Customer engagement – how long each visitor stays  
- 🪑 Seat occupancy – live count of available tables  

All of this happens **in real time**, turning any webcam or CCTV feed into actionable analytics.

---

## 🧠 Concept Flow
```
Video Feed → YOLOv8 Detection → Object Tracking → Zone Logic → Overlay + Report
```

✅ **Employee activity** → counts each barista action  
✅ **Customer duration** → tracks entry / exit timestamps  
✅ **Occupancy stats** → outputs live JSON / CSV reports for dashboards  

---

## ⚙️ Tech Stack
| Layer | Tools |
|:--|:--|
| Computer Vision | OpenFilter (stub), OpenCV, YOLOv8 (Ultralytics) |
| ML / Inference | PyTorch (CPU build) |
| Utilities | NumPy, Pandas, Matplotlib |
| Reporting | CSV logger + console visualization |

---

## 🧩 Project Structure
```
Cafe_Vision/
│
├── cafe_vision.py           # main pipeline entry
├── openfilter_stub.py       # minimal OpenFilter-compatible interface
├── filters_camera.py        # video / webcam handler
├── filters_yolo_detect_track.py # YOLOv8 detection + Norfair tracking
├── filters_zone_logic.py    # line-crossing + in/out logic
├── filters_overlay.py       # bounding boxes + labels overlay
├── filters_reporter.py      # analytics + CSV report writer
├── cafe_events.csv          # sample output log
└── plainsight.mp4           # demo input video
```

---

## 🧰 Installation & Setup

### 1️⃣ Create Virtual Environment
```bash
python -m venv .venv
.venv\Scripts\activate      # on Windows
```

### 2️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

or manually:
```bash
pip install numpy opencv-python torch torchvision ultralytics shapely pandas
```

---

## ▶️ Usage

### 🔹 Run with video file
```bash
python cafe_vision.py --source plainsight.mp4
```

### 🔹 Run with webcam
```bash
python cafe_vision.py --source 0
```

### 🔹 Output
- Annotated video window  
- Live console metrics  
- `cafe_events.csv` → stores timestamps & counts  

---

## 🖼️ Sample Output Screenshots

![Sample Output 1](<img width="1920" height="1080" alt="OutputSS" src="https://github.com/user-attachments/assets/3e152ab3-9f7a-434c-92b1-7bf1f45a17fc" />)
![Sample Output 2](<img width="1920" height="1080" alt="SS2" src="https://github.com/user-attachments/assets/21051a5f-9f59-421f-ac11-aaac0b1a5318" />)

---

## 🧪 Hackathon Highlights
| Criteria | How We Met It |
|:--|:--|
| Creativity | Unique “employee × customer” dual tracking concept |
| Functionality | Live feed + output metrics + data export |
| Technical Implementation | YOLOv8 + OpenFilter-compatible pipeline |
| Problem Fit | Applicable to any retail / hospitality setup |
| Presentation | Clean demo video + chart summary |

---

## 🧾 Future Improvements
- Dashboard with real-time graphs (Plotly / Streamlit)  
- Cloud storage (AWS S3 + Lambda processing)  
- Employee analytics over time periods  
- Queue length / wait-time estimation  

---

## 👥 Team MI
**Agnel Salve** – pipeline design, OpenFilter integration, object tracking, analytics reporting, and final demo implementation.  
**Chinmay Sakhare** – presentation design, YOLO configuration, visualization assets, and final demo implementation.

---

## 🏁 Acknowledgments
- [Plainsight AI](https://plainsight.ai) – OpenFilter framework & hackathon support  
- [Ultralytics YOLOv8](https://github.com/ultralytics/ultralytics) – object detection  
- [OpenCV](https://opencv.org) – real-time video processing  

---

### 🌟 “Turning every cup of coffee into data.”  
#hackathon #plainsight #computer-vision #openfilter #yolov8 #python #ai #realtime-analytics #productivity-ai
