"""
test_do_motor_control.py
Test script for controlling wash and rinse motors via DO (Digital Output) pins

Usage:
    python test_do_motor_control.py
    
    Then follow the prompts to test various motor operations.
"""

import serial
import time
import sys

class MotorControlTester:
    """Test DO pin motor control"""
    
    def __init__(self, port: str = "COM3", baudrate: int = 9600):
        """
        Initialize motor controller tester
        
        Args:
            port: Serial port (e.g., COM3)
            baudrate: Serial baud rate (9600 for this protocol)
        """
        self.port = port
        self.baudrate = baudrate
        self.serial_conn = None
        self.connected = False
    
    def connect(self) -> bool:
        """Connect to arm controller"""
        try:
            self.serial_conn = serial.Serial(
                port=self.port,
                baudrate=self.baudrate,
                timeout=2.0,
                write_timeout=2.0
            )
            time.sleep(0.5)
            self.connected = True
            print(f"✓ Connected to {self.port} at {self.baudrate} baud")
            return True
        except serial.SerialException as e:
            print(f"❌ Connection failed: {e}")
            return False
    
    def disconnect(self) -> bool:
        """Disconnect from arm controller"""
        try:
            if self.serial_conn and self.serial_conn.is_open:
                self.serial_conn.close()
            self.connected = False
            print("✓ Disconnected")
            return True
        except Exception as e:
            print(f"❌ Disconnect error: {e}")
            return False
    
    def send_command(self, command: str, wait_response: bool = True) -> tuple:
        """
        Send command to arm controller
        
        Args:
            command: Command string (e.g., "0x550xAA G06 D0 S1 P0 0xAA0x55")
            wait_response: Whether to wait for response
        
        Returns:
            Tuple (success: bool, response: str)
        """
        if not self.connected:
            return False, "Not connected"
        
        try:
            # Send command as bytes
            cmd_bytes = command.encode('utf-8')
            self.serial_conn.write(cmd_bytes)
            print(f"📤 Sent: {command}")
            
            if not wait_response:
                return True, "Sent (no response expected)"
            
            # Wait for response
            time.sleep(0.1)
            response = self.serial_conn.read(100)
            response_str = response.decode('utf-8', errors='ignore').strip()
            print(f"📥 Response: {response_str}")
            
            return True, response_str
            
        except Exception as e:
            print(f"❌ Error: {e}")
            return False, str(e)
    
    def motor_on(self, do_port: int) -> tuple:
        """
        Turn ON a motor on specified DO port
        
        Args:
            do_port: DO port number (0=wash, 1=rinse, etc.)
        
        Returns:
            Tuple (success: bool, response: str)
        """
        cmd = f"0x550xAA G06 D{do_port} S1 P0 0xAA0x55"
        return self.send_command(cmd)
    
    def motor_off(self, do_port: int) -> tuple:
        """
        Turn OFF a motor on specified DO port
        
        Args:
            do_port: DO port number (0=wash, 1=rinse, etc.)
        
        Returns:
            Tuple (success: bool, response: str)
        """
        cmd = f"0x550xAA G06 D{do_port} S0 P0 0xAA0x55"
        return self.send_command(cmd)
    
    def wash_motor_on(self) -> tuple:
        """Turn ON wash station motor (DO0)"""
        print("\n🌊 WASH MOTOR ON")
        return self.motor_on(do_port=0)
    
    def wash_motor_off(self) -> tuple:
        """Turn OFF wash station motor (DO0)"""
        print("\n🌊 WASH MOTOR OFF")
        return self.motor_off(do_port=0)
    
    def rinse_motor_on(self) -> tuple:
        """Turn ON rinse station motor (DO1)"""
        print("\n💧 RINSE MOTOR ON")
        return self.motor_on(do_port=1)
    
    def rinse_motor_off(self) -> tuple:
        """Turn OFF rinse station motor (DO1)"""
        print("\n💧 RINSE MOTOR OFF")
        return self.motor_off(do_port=1)
    
    def test_single_motor(self, do_port: int, duration: int = 3) -> bool:
        """
        Test a single motor: ON -> wait -> OFF
        
        Args:
            do_port: DO port to test (0-5)
            duration: How long to run motor (seconds)
        
        Returns:
            True if successful
        """
        print(f"\n{'='*50}")
        print(f"Testing DO{do_port} Motor")
        print(f"{'='*50}")
        
        # Turn ON
        success, resp = self.motor_on(do_port)
        if not success:
            print(f"❌ Failed to turn ON DO{do_port}")
            return False
        
        print(f"⏱ Running for {duration} seconds...")
        time.sleep(duration)
        
        # Turn OFF
        success, resp = self.motor_off(do_port)
        if not success:
            print(f"❌ Failed to turn OFF DO{do_port}")
            return False
        
        print(f"✓ Test complete")
        return True
    
    def test_wash_cycle(self, wash_duration: int = 3, rinse_duration: int = 2) -> bool:
        """
        Test complete wash cycle: Wash -> Rinse
        
        Args:
            wash_duration: Wash motor duration (seconds)
            rinse_duration: Rinse motor duration (seconds)
        
        Returns:
            True if successful
        """
        print(f"\n{'='*50}")
        print("COMPLETE WASH CYCLE TEST")
        print(f"{'='*50}")
        
        # WASH STATION
        print(f"\n[STAGE 1] Wash Station ({wash_duration}s)")
        success, _ = self.wash_motor_on()
        if not success:
            return False
        
        time.sleep(wash_duration)
        self.wash_motor_off()
        
        # Pause between stations
        print("\n⏸ Transition period (1s)...")
        time.sleep(1)
        
        # RINSE STATION
        print(f"\n[STAGE 2] Rinse Station ({rinse_duration}s)")
        success, _ = self.rinse_motor_on()
        if not success:
            return False
        
        time.sleep(rinse_duration)
        self.rinse_motor_off()
        
        print("\n✓ Wash cycle complete!")
        return True
    
    def test_all_do_ports(self, test_duration: int = 2):
        """
        Test all available DO ports (0-5) one by one
        
        Args:
            test_duration: Duration to run each motor (seconds)
        """
        print(f"\n{'='*50}")
        print("TESTING ALL DO PORTS (0-5)")
        print(f"{'='*50}")
        
        for port in range(6):
            print(f"\n📍 Testing DO{port}...")
            success, resp = self.motor_on(port)
            
            if success:
                print(f"✓ DO{port} ON successful")
                time.sleep(test_duration)
                self.motor_off(port)
                print(f"✓ DO{port} OFF successful")
            else:
                print(f"⚠ DO{port} test failed: {resp}")
            
            time.sleep(0.5)  # Pause between tests
        
        print(f"\n{'='*50}")
        print("All DO port tests complete!")
        print(f"{'='*50}")


def main():
    """Main test menu"""
    print("\n" + "="*60)
    print("🤖 ZKBot Arm - Motor Control (DO Pins) Test")
    print("="*60)
    
    # Get COM port
    port = input("\nEnter COM port (default: COM3): ").strip() or "COM3"
    
    # Initialize tester
    tester = MotorControlTester(port=port, baudrate=9600)
    
    # Connect
    if not tester.connect():
        print("❌ Failed to connect. Exiting.")
        return
    
    # Test menu
    while True:
        print("\n" + "-"*60)
        print("TEST MENU:")
        print("-"*60)
        print("1. Test DO0 (Wash Motor) - 3 seconds")
        print("2. Test DO1 (Rinse Motor) - 3 seconds")
        print("3. Test DO0 + DO1 (Wash Cycle) - 3s + 2s")
        print("4. Test ALL DO ports (0-5) - 2 seconds each")
        print("5. Quick ON/OFF toggle DO0")
        print("6. Quick ON/OFF toggle DO1")
        print("7. Custom DO port test")
        print("8. Exit")
        print("-"*60)
        
        choice = input("Select option (1-8): ").strip()
        
        if choice == "1":
            tester.test_single_motor(do_port=0, duration=3)
        
        elif choice == "2":
            tester.test_single_motor(do_port=1, duration=3)
        
        elif choice == "3":
            tester.test_wash_cycle(wash_duration=3, rinse_duration=2)
        
        elif choice == "4":
            test_duration = input("Duration per motor (seconds, default 2): ").strip()
            test_duration = int(test_duration) if test_duration.isdigit() else 2
            tester.test_all_do_ports(test_duration=test_duration)
        
        elif choice == "5":
            print("\nDO0 Quick Toggle:")
            tester.wash_motor_on()
            time.sleep(1)
            tester.wash_motor_off()
        
        elif choice == "6":
            print("\nDO1 Quick Toggle:")
            tester.rinse_motor_on()
            time.sleep(1)
            tester.rinse_motor_off()
        
        elif choice == "7":
            try:
                do_port = int(input("Enter DO port number (0-5): ").strip())
                duration = int(input("Enter duration (seconds): ").strip())
                
                if 0 <= do_port <= 5:
                    tester.test_single_motor(do_port=do_port, duration=duration)
                else:
                    print(f"❌ Invalid port: {do_port} (must be 0-5)")
            except ValueError:
                print("❌ Invalid input")
        
        elif choice == "8":
            print("\n👋 Exiting...")
            break
        
        else:
            print("❌ Invalid option")
    
    # Cleanup
    tester.disconnect()
    print("✓ Test complete")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n⚠ Test interrupted by user")
        sys.exit(0)
    except Exception as e:
        print(f"\n❌ Error: {e}")
        sys.exit(1)
