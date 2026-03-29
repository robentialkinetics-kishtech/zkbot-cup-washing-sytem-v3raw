# Version 3: Raw Program Execution Only - Standalone Setup

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

- ✅ **Models** - Robot controller, sensors
- ✅ **UI** - PyQt5 interface with login, user mode, developer mode
- ✅ **Config** - Settings and calibration files
- ✅ **Data** - Storage, logging, programs
- ✅ **Utils** - Helpers and validators
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

## Features (Version 3 - Minimal)

- 🤖 **Robot Arm Control** - Move, position, and control the robot arm
- ⚙️ **Step-by-Step Program Execution** - Execute programs one step at a time
- 💾 **Data Logging** - Tracks cycles and errors
- 👤 **User Management** - Login system with roles (user, developer, admin)
- 🛠️ **Developer Mode** - Teach positions, manage programs, adjust settings
- 📍 **Position Tracking** - Monitor arm position and movement

## What's Removed ❌

- ❌ **YOLO Vision** - No cup detection system
- ❌ **DIDO Motor Control** - No automatic motor signal transmission
- ❌ **Auto Safety Checks** - No detection-based safety protocols

## Use Case

This version is ideal for:
- **Testing robot arm mechanics** without complexity
- **Validating program step execution** logic
- **Baseline performance** measurements
- **Manual motor operation** (external control)
- **Integration foundation** for adding features back

## Advantages ✅

- ✅ **Minimal dependencies** - Fastest startup
- ✅ **No camera required** - Run on any hardware
- ✅ **No ML overhead** - Pure mechanical testing
- ✅ **Simple debugging** - Easy to trace execution
- ✅ **Small footprint** - ~500MB vs 2GB+ for full version

## Troubleshooting

### ModuleNotFoundError: No module named 'pyserial'
```bash
pip install pyserial
```

### Robot connection failed
- Check COM port setting in `config/settings.json`
- Verify robot is powered and connected via serial
- Check serial cable connection
- Try different baud rates (default: 115200)

### Program execution halted
- Verify all positions are calibrated (use Developer Mode)
- Check program JSON syntax in `data/programs/`
- Review error log in `data/logs/error_log.json`
- Ensure robot has power and is responsive

## File Structure
```
version_3_RAW_ONLY/
├── main.py                    # Entry point
├── run.py                     # Standalone runner  
├── requirements.txt           # Python dependencies
├── config/                    # Settings & calibration
├── data/                      # Storage & programs
├── models/                    # Robot, sensors (core only)
├── ui/                        # PyQt5 interface
├── utils/                     # Helpers
├── workers/                   # Background threads
└── README.md                  # Documentation
```

## Running from a Different Folder

You can move this entire folder anywhere and it will work:
```bash
mv version_3_RAW_ONLY /path/to/new/location
cd /path/to/new/location/version_3_RAW_ONLY
python run.py
```

## Manual Motor Operation

Since this version has no automatic motor control, use:

**Via Developer Mode UI**:
1. Launch application
2. Login as developer / admin
3. Use "Control Panel" to manually activate motors

**Via Custom Programs**:
Create programs that only include G-code movements:
```json
{
  "steps": [
    {"step": 1, "cmd": "G00", "x": 0, "y": 0, "z": 0},
    {"step": 2, "cmd": "GRIPPER", "angle": 0},
    {"step": 3, "cmd": "PUMP_ON"},
    {"step": 4, "cmd": "WAIT", "pause": 2.0}
  ]
}
```

## System Requirements

- Python 3.8+
- PyQt5 5.15+
- PySerial 3.5+ (for robot communication)
- 256MB+ RAM

## Performance

| Operation | Time |
|-----------|------|
| Startup | ~2 seconds |
| Position Move | ~1 second (varies) |
| Program Load | ~100ms |
| Step Execution | ~50ms |

## Support

- See `VERSIONS_GUIDE.md` for comparison with other versions
- See `VALIDATION_REPORT.md` for validation details
- See `VERSION_INFO.md` for version-specific information

---

**Status**: ✅ Standalone & Independent  
**Last Updated**: 2026-03-22
