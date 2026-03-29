# 🔥 Fire Alert Detection System

A real-time computer vision system for detecting:
- Fire
- Smoke
- Flames
- Cigarettes

## 🚀 Features
- Multi-model detection pipeline
- Smart cascade system (smoke → fire)
- Real-time webcam processing
- Alert system with cooldown
- Modular architecture

## 📁 Project Structure
Fire-Alert-Detection/
│
├── models/
│   ├── cigarettes/
│   │   └── cigarettes.pt
│   │
│   ├── fire/
│   │   └── fire.pt
│   │
│   ├── flames/
│   │   └── flames.pt
│   │
│   └── smoke/
│       └── smoke.pt
│
├── src/
│   ├── main.py
│   ├── pipeline.py
│   ├── detector.py
│   ├── tracker.py
│   ├── camera.py
│   ├── utils.py
│   ├── config.py
│   └── __init__.py  (optional)
│
├── outputs/
│   ├── logs/
│   ├── videos/
│   └── frames/
│
├── requirements.txt
├── README.md
├── .gitignore
└── main.py  (optional root runner)

## ⚙️ Setup

```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
