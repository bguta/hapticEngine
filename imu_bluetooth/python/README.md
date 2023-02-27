### Bluetooth IMU Reader

This is starter code to communicate with bluetooth devices using python. Ensure that you have installed the required packages mentioned in the root directory's README.md before running these scripts.

## Getting Started

Upload and run ```imu_bluetooth.ino``` then run ```python3 sensor.py``` to start obtaining readings from the IMUs. If there are any errors, run ```python findBluetooth.py RFduino``` to search for the address that the RFduino sensor is sending out and make sure this is the same as the expected address within ```sensor.py```. If that also fails, run ```python3 scanner.py``` to search for all bluetooth devices that are emitting a signal nearby.