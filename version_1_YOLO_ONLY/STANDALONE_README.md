# Version 1: YOLO Detection Only - Standalone Setup

This folder is a **fully independent, self-contained version** of the Cup Washing System.

## Quick Start

### Option 1: Using Python directly
```bash
python run.py
```

### Option 2: Using PowerShell with virtual environment  
```powershell
# Activate virtual environment (if you have one)
& ".\.venv\Scripts\Activate.ps1"

# Run the application
python run.py
```

### Option 3: Using main.py
```bash
python main.py
```

## What's Included ✅

- ✅ **Models** - Robot controller, vision system, sensors
- ✅ **UI** - PyQt5 interface with login, user mode, developer mode
- ✅ **Config** - Settings and calibration files
- ✅ **Data** - Storage, logging, programs
- ✅ **Utils** - Helpers and validators
- ✅ **YOLO Models** - Pre-trained YOLOv8 detection models
- ✅ **Requirements** - All dependencies listed in requirements.txt

## First Time Setup

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Run the Application
```bash
python run.py
```

## Features (Version 1)

- 🎥 **YOLO Cup Detection** - Detects cups using YOLOv8 with 0.85+ confidence
- 🤖 **Robot Arm Control** - Move, position, and control the robot
- ⚙️ **Program Execution** - Load and execute washing programs
- 💾 **Data Logging** - Tracks cycles, errors, and performance
- 👤 **User Management** - Login system with roles (user, developer, admin)
- 🛠️ **Developer Mode** - Teach positions, manage programs, adjust settings

## No DIDO Motor Control ❌

This version has **removed DIDO motor control** to isolate vision testing. The wash/rinse motors are **not controlled automatically** via D01/D03 signals.

If you need motor control, use **Version 2 (DIDO Only)**.

## Troubleshooting

### ModuleNotFoundError: No module named 'cv2'
```bash
pip install opencv-python
```

### ModuleNotFoundError: No module named 'ultralytics'
```bash
pip install ultralytics
```

### Camera not found
- Check camera permissions
- Try different camera indices (0, 1, 2) in the UI
- Verify camera is not in use by another application

### Cup detection failing
- Check lighting conditions
- Verify cup is visible in camera frame
- Lower confidence threshold in settings
- Ensure YOLO model file exists in `pt files/` or `runs/detect/train/weights/`

## File Structure
```
version_1_YOLO_ONLY/
├── main.py                    # Entry point
├── run.py                     # Standalone runner  
├── requirements.txt           # Python dependencies
├── config/                    # Settings & calibration
├── data/                      # Storage & programs
├── models/                    # Robot, vision, sensors
├── ui/                        # PyQt5 interface
├── utils/                     # Helpers
├── workers/                   # Background threads
├── pt files/                  # YOLO model weights
├── runs/                      # Training results
├── yolo dataset/              # Training data
└── README.md                  # Documentation
```

## Running from a Different Folder

You can move this entire folder anywhere and it will work:
```bash
mv version_1_YOLO_ONLY /path/to/new/location
cd /path/to/new/location/version_1_YOLO_ONLY
python run.py
```

## System Requirements

- Python 3.8+
- PyQt5 5.15+
- OpenCV 4.8+
- YOLO (ultralytics 8.1+)
- PySerial 3.5+ (for robot communication)
- 2GB+ RAM recommended

## Support

- See `VERSIONS_GUIDE.md` for comparison with other versions
- See `VALIDATION_REPORT.md` for validation details
- See `VERSION_INFO.md` for version-specific information

---

**Status**: ✅ Standalone & Independent  
**Last Updated**: 2026-03-22
