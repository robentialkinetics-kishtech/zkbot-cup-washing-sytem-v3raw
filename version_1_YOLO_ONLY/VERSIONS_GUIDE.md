# Cup Washing System - Version Comparison Guide

## Overview
The project has been split into 3 distinct versions to enable reverse engineering and feature isolation. Each version removes specific components while maintaining a working system.

---

## 📊 Version Comparison Matrix

| Feature | Version 1 (YOLO) | Version 2 (DIDO) | Version 3 (Raw) | Original |
|---------|:-:|:-:|:-:|:-:|
| **YOLO Detection** | ✅ | ❌ | ❌ | ✅ |
| **DIDO Motor Control** | ❌ | ✅ | ❌ | ✅ |
| **Arm Movement** | ✅ | ✅ | ✅ | ✅ |
| **Camera System** | ✅ | ❌ | ❌ | ✅ |
| **Motor Signals** | ❌ | ✅ | ❌ | ✅ |
| **Cup Detection** | ✅ | ❌ | ❌ | ✅ |
| **Emergency Protocols** | Simplified | Full | None | Full |

---

## 🎯 Version Details

### **Version 1: YOLO Detection Only**
**Location**: `version_1_YOLO_ONLY/`

**What it does**:
- Full cup detection using YOLOv8
- Image capture and frame processing
- Stable detection counting
- Robot arm movement and positioning
- Basic wash/rinse timing

**What's removed**:
- ALL DIDO motor control methods
- Motor activation signals (D01, D03)
- Emergency motor stop procedures
- Motor signal handling in step execution

**Best for**:
- ✅ Testing YOLO accuracy and performance
- ✅ Vision system debugging
- ✅ Camera calibration
- ✅ Detection confidence tuning
- ✅ Frame rate optimization

**Dependencies**:
```
- ultralytics (YOLO)
- opencv-python (cv2)
- Camera hardware
```

---

### **Version 2: DIDO Motor Control Only**
**Location**: `version_2_DIDO_ONLY/`

**What it does**:
- Full DIDO motor control protocol
- Wash station motor activation (D01)
- Rinse station motor activation (D03)
- Emergency motor shutdown
- Robot arm movement and positioning
- Basic timing operations

**What's removed**:
- ALL YOLO vision/detection system
- Camera initialization
- Cup detection checkpoints
- Frame capture and processing
- Vision confidence thresholds

**Best for**:
- ✅ Testing motor control signals
- ✅ Wash/rinse station operation
- ✅ DIDO protocol verification
- ✅ Motor timing validation
- ✅ Emergency stop mechanism testing

**Dependencies**:
```
- serial (for robot communication)
- No camera required
- No ML dependencies
```

---

### **Version 3: Raw Program Execution**
**Location**: `version_3_RAW_ONLY/`

**What it does**:
- Basic robot arm control
- G-code/program step execution
- Gripper and pump control
- Position tracking
- Minimal error logging

**What's removed**:
- ALL YOLO detection system
- ALL DIDO motor control methods
- Emergency motor protocols
- Auto cup verification
- All intelligent automation

**Best for**:
- ✅ Baseline mechanical testing
- ✅ Program structure validation
- ✅ Robot connectivity verification
- ✅ Basic movement testing
- ✅ Foundation for custom implementations

**Limitations**:
- ⚠️ No automatic cup detection
- ⚠️ No motor control
- ⚠️ Manual verification required
- ⚠️ No safety checkpoints

---

## 🔄 Progression Strategy

### Testing Flow
```
Version 3 (Raw)
    ↓ (Add component)
Version 1 (YOLO) + Version 2 (DIDO)
    ↓ (Combine)
Original (Both YOLO + DIDO)
```

### Recommended Testing Order
1. **Start with Version 3** - Verify basic robot operation
2. **Test Version 1** - Validate YOLO detection accuracy
3. **Test Version 2** - Verify motor control signals
4. **Test Original** - Integrated system verification

---

## 📝 Key Differences in Code

### Robot.py Changes
```python
# Version 1 & 3: REMOVED
def motor_control(self, do_port: int, state: bool)
def wash_motor_on()
def wash_motor_off()
def rinse_motor_on()
def rinse_motor_off()
def emergency_stop_motors()

# Version 2 & Original: PRESENT
[All motor control methods intact]
```

### Controller.py Changes
```python
# Version 2 & 3: REMOVED
from models.vision import VisionSystem
self.vision = VisionSystem(model_path=...)
def detect_cup_before_pickup(...)
self.vision.start_camera()

# Version 1 & 3: REMOVED (in controller.py)
self.robot.wash_motor_on()
self.robot.rinse_motor_on()
detection_checkpoints verification

# Version 2: REMOVED
detect_cup_before_pickup() calls
```

---

## 🛠 Switching Between Versions

### To test a different version:
```powershell
# Copy the version folder content to replace your working directory
# OR point your IDE to the version folder directly

# Make sure dependencies are installed
pip install -r version_X_*/requirements.txt
```

### Environment Variables
Each version uses the same config files:
- `config/settings.json` - Robot settings
- `config/calibration.json` - Position values
- These can be shared across versions

---

## 📊 File Sizes Comparison

```
Version 1 (YOLO):     ~850 KB (includes YOLO model)
Version 2 (DIDO):     ~450 KB (no vision models needed)
Version 3 (Raw):      ~400 KB (minimal dependencies)
Original:             ~900 KB (complete system)
```

---

## ✅ Testing Checklist

### Version 1 (YOLO Only)
- [ ] Camera connects successfully
- [ ] Cup appears in detected frames
- [ ] Detection confidence > 0.85
- [ ] Stable detection achieves 3+ consecutive frames
- [ ] Detection timeout works correctly
- [ ] Robot arm moves to positions

### Version 2 (DIDO Only)
- [ ] Robot connects to motor controller
- [ ] D01 (wash motor) activates/deactivates
- [ ] D03 (rinse motor) activates/deactivates
- [ ] Motor signals transmit correctly
- [ ] Emergency stop works
- [ ] Program steps 7, 9, 11, 13 execute

### Version 3 (Raw)
- [ ] Robot connects successfully
- [ ] Homing sequence completes
- [ ] Position-to-position movement works
- [ ] Linear movement works
- [ ] Gripper opens/closes
- [ ] Programs load and execute steps

---

## 🐛 Troubleshooting

### If Version 1 (YOLO) fails:
- Check camera connection
- Verify YOLO model file exists
- Check lighting conditions
- Verify cup is in camera frame
- Lower confidence threshold if needed

### If Version 2 (DIDO) fails:
- Check robot serial connection
- Verify motor controller is powered
- Check D01 and D03 pin connections
- Test emergency stop button manually
- Verify G06 command syntax

### If Version 3 (Raw) fails:
- Verify COM port and baudrate
- Check robot is connected
- Ensure E-stop is released
- Verify positions are calibrated
- Check G-code syntax in programs

---

## 📦 Dependencies Summary

**All Versions**:
- PyQt5 (UI)
- pyserial (Robot communication)

**Version 1 Added**:
- ultralytics (YOLO)
- opencv-python (cv2)
- numpy

**Version 2 & 3**:
- Only base dependencies

---

## 🎓 Learning Value

This multi-version approach allows:
1. **Isolation Testing** - Test each subsystem independently
2. **Performance Profiling** - Measure individual component impact
3. **Debugging** - Narrow down issues to specific systems
4. **Feature Development** - Build features starting from raw base
5. **Integration Testing** - Combine components systematically

---

## 📌 Notes

- All versions use the same robot arm controller (ZKBotController)
- Configuration files are interchangeable
- Calibration data is shared
- Motor control timing is preserved in Version 2
- YOLO model files are only needed in Version 1 and Original

---

**Created**: 2026-03-20
**Status**: All versions ready for testing
**Original**: Both YOLO + DIDO (saved separately)
