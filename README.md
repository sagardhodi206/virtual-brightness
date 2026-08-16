# 💡 Virtual Brightness Control

A gesture-based computer vision application that allows users to **adjust their screen brightness using hand movements**.

The system uses a webcam to detect hand landmarks and converts the distance between fingers into a brightness level. This provides a simple **touch-free method of controlling display brightness**.

## 🌟 What This Project Does

Instead of using keyboard buttons or manually opening display settings, the user can control brightness with a natural hand gesture.

The hand is detected through the webcam, the required finger positions are tracked, and the measured distance is mapped to the available screen-brightness range.

## ⚡ Key Features

* 📷 Real-time webcam processing
* 🖐️ Hand landmark detection
* 📏 Finger-distance measurement
* 💡 Dynamic screen brightness adjustment
* 🔄 Continuous brightness updates
* 🖥️ Touch-free computer interaction
* 🤖 Computer Vision based control

## 🔬 Processing Flow

```text
Camera
   ↓
Video Frame Capture
   ↓
Hand Detection
   ↓
Hand Landmark Tracking
   ↓
Measure Finger Distance
   ↓
Convert Distance to Brightness
   ↓
Update Display Brightness
```

## 🧠 Working Principle

The application continuously observes the user's hand through the webcam.

After detecting the hand, the program tracks selected finger landmarks and calculates the distance between them.

The measured distance is converted into a brightness value.

```text
Fingers Closer
      ↓
Lower Brightness

Fingers Farther Apart
      ↓
Higher Brightness
```

This creates a smooth and interactive brightness-control experience.

## 🛠️ Technology Stack

| Tool                      | Usage                       |
| ------------------------- | --------------------------- |
| Python                    | Application logic           |
| OpenCV                    | Webcam and image processing |
| MediaPipe                 | Hand tracking               |
| Screen Brightness Library | Display brightness control  |

## 📦 Installation

Install the required Python packages:

```bash
pip install opencv-python mediapipe screen-brightness-control
```

## ▶️ Running the Project

Start the application using:

```bash
python app.py
```

Make sure your webcam is connected and working before starting the program.

Once the application starts, place your hand in front of the camera and perform the supported gesture.

## ✋ Gesture Interaction

| Hand Movement          | Result              |
| ---------------------- | ------------------- |
| 🤏 Fingers move closer | Decrease brightness |
| 🖐️ Fingers move apart | Increase brightness |

The brightness changes according to the detected finger distance.

## 📁 Project Structure

```text
virtual-brightness/
│
├── app.py
└── README.md
```

## 🎯 Use Cases

This project can be used as a demonstration of:

* Touchless computer control
* Gesture-based interfaces
* Human-Computer Interaction
* Computer Vision applications
* Accessibility-focused interfaces
* AI and Python projects

## 🚀 Future Improvements

Some possible extensions are:

* 🔊 Combine brightness and volume control
* 🌙 Automatic night-mode activation
* 🖥️ Brightness percentage display
* ✋ Support for additional gestures
* 💾 User-defined gesture settings
* 📊 Smoother brightness transitions

## 👨‍💻 Developer

**Sagar Dhodi**

AI & Computer Vision Project

---

⭐ **If you like this project, consider giving the repository a star!**

**Built with Python + Computer Vision + Hand Gestures.**