#Reference: https://realpython.com/face-detection-in-python-using-a-webcam/
#the above link was used to base this function of the face detection part of the code aswell as linking it to the haarcascade_frontalface_default.xml  

#to run use command: py Face_Detect.py haarcascade_frontalface_default.xml     
#py Face_Detect.py haarcascade_frontalface_alt_tree.xml     (worse detetcion thaN above)                                                                                                    
#------------------------------------------------------------------------------
#------------------------------------------------------------------------------
#Importing the modules needed

import cv2
import sys

#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------

def Face_Detector(faceCascade, video_feed):

    # Define the font for the message alerts
    font = cv2.FONT_HERSHEY_SIMPLEX
    font_scale = 1
    font_color = (0, 0, 255)  # Red color
    line_thickness = 2

    # Set the title of the video window
    cv2.namedWindow('Press Esc to exit', cv2.WINDOW_NORMAL)

    while video_feed.isOpened():
        # Capture frame-by-frame
        ret, frame = video_feed.read()

        if not ret:
            # If no frame is received, break out of the loop
            break

        # now we will process the frame or perform any desired operations
        #wanna convert the frame to grayscale
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        #---------------------------------------------------------------------------
        #---------------------------------------------------------------------------

        #detect faces in the grayscale frame
        faces = faceCascade.detectMultiScale(
            gray,
            scaleFactor=1.3,
            minNeighbors=5,
            minSize=(30, 30)
        )

        # Draw rectangles around the detected faces instead- visually more appealing
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (64, 224, 208), 2)
            cv2.putText(frame, 'Face Detected', (x, y - 10), font, font_scale, font_color, line_thickness)

            print('Face Detected')
            #displaying the resulting frame 
            cv2.imshow('Video GUI Face Detection ', frame)

        #-------------------------------------------------------------------------------------
        #------------------------------------------------------------------------------------

        if cv2.waitKey(1) == 27:  # Check for the 'esc' key press
            print('Terminating Face Detection')
            break

if __name__ == "__main__":

    '''
    # Check if the required command-line argument is provided
    if len(sys.argv) < 2:
        print("Please provide the path to the cascade XML file as a command-line argument!")
        sys.exit(1)   
    #cascPath = sys.argv[1]
    '''
    #creating the face cascade
    cascPath = "haarcascade_frontalface_default.xml"
    faceCascade = cv2.CascadeClassifier(cascPath)

    #setting the webcam on the device to be the default camera source 
    video_feed = cv2.VideoCapture(0)

    #call this face detector function 
    Face_Detector(faceCascade, video_feed)

    # Release the video capture object
    video_feed.release()
    #closing all OpenCV windows 
    cv2.destroyAllWindows()