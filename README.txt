# Face Detection Project

This Python script utilizes OpenCV to enable real-time face detection using Haar cascade classifier.

## Installation

- Clone the repository or download the script.
- Install the dependencies by running:
  
pip install -r requirements.txt

## Usage

Simply run the script with the following command:

py Face_Detect.py

This will launch the video feed with real-time face detection.

## Features

- The script opens a video window displaying the live webcam feed.
- Detected faces in the video feed are highlighted by a yellow rectangle and red words.
- To exit the script, press Esc on the keyboard.

## Configuration

The script uses the `haarcascade_frontalface_default.xml` file for face detection. You can replace this file with a different cascade XML file for custom object detection. Note that the tree version is not used as it was found to work in a worse manner.

## License

This project is licensed under the MIT License. Please review the [LICENSE](LICENSE) file for more details.

## Contributing

Contributions are not needed as this is a closed project, created for practice and fun.

Feel free to reach out with any questions or feedback!
