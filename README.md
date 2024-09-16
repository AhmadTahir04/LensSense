# LensSense
LensSense is a Python application that uses camera input to train an SVM model to detect and respond to specific actions. This project leverages machine learning and computer vision techniques to classify and react to real-time camera feed.

## Features
- Captures real-time images from the camera for training and prediction.
- Trains a Support Vector Machine (SVM) model to classify specific actions based on camera input.
- Provides an interactive GUI for capturing images, training the model, and making predictions.
- Automatically resizes and preprocesses images for optimal model training and prediction accuracy.

## Getting Started

### Dependencies

- Python 3.x
- OpenCV
- scikit-learn
- Pillow
- NumPy
- Tkinter

### Setting up the environment

```bash
pip install opencv-python scikit-learn Pillow numpy
```

### Executing the Program

Run `main.py` to start:

```bash
python main.py
```

The application will open a GUI window that allows you to capture images for training, train the SVM model, and make predictions based on live camera input.

### Modules
- `main.py`: The entry point of the application, initializes and starts the GUI.
- `camera.py`: Manages the camera input and captures frames for training and prediction.
- `model.py`: Contains the SVM model, handles training and making predictions based on the camera input.
- `app.py`: The main control module for the GUI, providing user interaction for capturing images, training the model, and performing predictions.

### Authors

Ahmad Tahir

### Acknowledgments

Thanks to the creators of OpenCV and scikit-learn libraries for providing tools that made this project possible.
