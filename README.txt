Face Detection Project

This is a Py Script that uses opencv to allow face detection in real-time using Haar cascade classifier.

There is a requirements.txt file that allow you to install the pre-requisites module

- Python 3.x
- opencv library (cv2)

Therefore:

- Clone the repo or download the script
- install the dependencies

The script does not need any special commands to run as the main function has allowed for easer use.
Therefore run with the following command:

py Face_Detect.py

This will launch the video feed with real time face detection.

The script will open a video window that will display the live webcam feed.
Faces deceted in the video feed will be highlghted by a yellow rectangle and red words.
To exit the script press Esc on the keyboard on the GUI.

Configuration:

The script uses the 'haarcascade_frontalface_default.xml' file for face detection. You can replace this file with a different cascade XML file for custom object detection.
Note that the tree version is not used as it was found to work in a worse manner.

License
This project is licensed under the MIT License. Please review the LICENSE file for more details.

Contributing:

They are not needed as this is a closed project, just for practice and fun.
