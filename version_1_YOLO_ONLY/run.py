#!/usr/bin/env python3
"""
Version 1 (YOLO Only) - Startup Script
Auto-configures paths and launches the application
"""
import sys
import os

# Add current directory to path for relative imports
version_dir = os.path.dirname(os.path.abspath(__file__))
if version_dir not in sys.path:
    sys.path.insert(0, version_dir)

# Now run main
from main import main

if __name__ == "__main__":
    main()
