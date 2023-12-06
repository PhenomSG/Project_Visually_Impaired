# Project Eyes
# Real-time Object Detection with TensorFlow Lite and Smart Object Detection System

## Overview

This project combines real-time object detection using a TensorFlow Lite model and a webcam with a Smart Object Detection System implemented on a Raspberry Pi. The TensorFlow Lite model detects objects in the webcam feed, while the Raspberry Pi system employs sensors to detect objects and provide real-time alerts, including fall detection and emergency notifications.

## TensorFlow Lite Object Detection

### Project Structure

- **VideoStream Class (`videostream.py`):**
  - Handles video streaming from the webcam in a separate processing thread.
  - Utilizes OpenCV to capture frames.

- **TensorFlow Lite Model Initialization (`object_detection.py`):**
  - Loads a TensorFlow Lite model specified through command line arguments.
  - Utilizes TensorFlow Lite interpreter for inference.
  
- **Object Detection Loop (`object_detection.py`):**
  - Captures frames from the webcam continuously.
  - Performs object detection using the loaded model.
  - Draws bounding boxes around detected objects on the frames.
  - Converts detected object names to speech using Google Text-to-Speech (`gTTS`) and plays the result using `mpg321`.
  - Displays frames per second (FPS) on the video stream.

- **Argument Parsing (`object_detection.py`):**
  - Parses command line arguments to customize script behavior.
  - Arguments include the model directory, model file, label map file, confidence threshold, webcam resolution, and Edge TPU usage.

### How to Run TensorFlow Lite Object Detection

1. **Install Dependencies:**
   ```bash
   pip install opencv-python numpy gtts
   pip install tflite-runtime
   ```

   If using the Coral Edge TPU, install the Edge TPU runtime:
   
   ```bash
   pip install tflite_runtime
   ```

2. **Prepare Model and Label Files:**
   - Ensure the presence of the TensorFlow Lite model file (`detect.tflite`) and the corresponding label map file (`labelmap.txt`) in the specified model directory (`Sample_TFLite_model`).

3. **Run the Script:**
   ```bash
   python object_detection.py --modeldir Sample_TFLite_model --graph detect.tflite --labels labelmap.txt --threshold 0.5 --resolution 640x480
   ```

   Adjust command line arguments based on your model file, label map file, and preferences.

4. **Interact with the Application:**
   - The script launches a window showing the webcam feed with real-time object detection results.
   - Press 'q' to exit the application.
   - Note: Ensure your webcam is connected and accessible. If using the Coral Edge TPU, make sure it is properly connected and recognized by your system.

## Smart Object Detection System with Fall Detection and Emergency Alert

### Overview

This project extends the capabilities of the Raspberry Pi by integrating various sensors for object detection and real-time alerts. The system includes a camera for object detection, ultrasonic sensors for proximity detection, a moisture sensor for detecting wet conditions, and a switch for emergency situations. Detected objects trigger announcements, and emergency alerts are sent via messaging.

### Components

#### Raspberry Pi Script (`user.py`)

##### Sensors and Devices Used:

1. **Ultrasonic Sensors:**
   - Three ultrasonic sensors for detecting distances in different directions (left, right, and front).
   - GPIO pins are utilized to trigger and receive signals from the sensors.

2. **Moisture Sensor:**
   - Detects moisture levels to identify wet conditions.
   - Connected to a GPIO pin for reading sensor data.

3. **Switch:**
   - A switch is used to detect emergency situations.
   - Connected to a GPIO pin for reading the switch state.

4. **Buzzer:**
   - An output device to generate emergency alerts.
   - Connected to a GPIO pin for activating the buzzer.

##### Object Detection and Announcement:

- The script captures data from ultrasonic sensors to measure distances in different directions.
- Moisture sensor and switch states are monitored to detect wet conditions and emergencies.
- Object detection using ultrasonic sensors triggers announcements and alerts.
- If a person falls down (detected through sensor values), an emergency message is sent using the Telegram API, and a buzzer is activated.

##### How to Run:

1. **Install Dependencies:**
   ```bash
   pip install RPi.GPIO spidev telepot
   ```

2. **Connect Sensors:**
   - Connect ultrasonic sensors, moisture sensor, and switch to the designated GPIO pins on the Raspberry Pi.

3. **Run the Script:**
   ```bash
   python user.py
   ```

   Ensure that the required sensors are connected, and the Raspberry Pi has internet access.

### Future Prospects

1. **Integration with AI Models:**
   - Incorporate AI models for more advanced object detection and classification.

2. **Enhanced Communication:**
   - Improve communication capabilities, such as sending alerts through various channels (SMS, email).

3. **Remote Monitoring:**
   - Enable remote monitoring and control through a web interface or mobile app.

4. **Machine Learning for Fall Detection:**
   - Train machine learning models specifically for fall detection using additional sensors or cameras.

5. **Integration with Smart Home Systems:**
   - Connect the system with smart home devices for seamless integration into existing smart home setups.

This combined Smart Object Detection System serves as a foundation for creating intelligent and responsive environments, enhancing safety and security. Feel free to customize and expand the project to meet specific requirements and explore new features and improvements.
