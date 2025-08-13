AI Face Detection & Recognition

A PyQt5-based application for real-time face detection and recognition using the 'face_recognition' library and OpenCV.

------------------------------------------------------------
Features
------------------------------------------------------------
- Detects and recognizes faces from a live camera feed.
- Loads known faces from a user-selected folder.
- Matches detected faces against known face encodings.
- Displays recognized names in real-time with bounding boxes.
- Supports .jpg, .jpeg, and .png image formats.

------------------------------------------------------------
Requirements
------------------------------------------------------------
Install the required dependencies:
    pip install opencv-python face_recognition numpy pillow PyQt5

Note: The 'face_recognition' library requires 'dlib' to be installed.
Follow the installation instructions for your OS from:
https://pypi.org/project/face-recognition/

------------------------------------------------------------
How to Run
------------------------------------------------------------
1. Save the script as Face_recognition.py.
2. Run it using:
       python Face_recognition.py
3. Click "Load Known Faces" to select a folder with labeled images.
4. Click "Start Camera" to begin face detection & recognition.
5. The app will display live camera feed with names of recognized faces.

------------------------------------------------------------
How It Works
------------------------------------------------------------
- Known faces are loaded and encoded into numerical vectors.
- The camera feed is processed frame-by-frame.
- Detected faces are compared to known encodings using Euclidean distance.
- Matches are displayed with bounding boxes and names.

------------------------------------------------------------
License
------------------------------------------------------------
This project is open-source and free to use for learning and personal projects.
