import cv2
import dlib
from imutils import face_utils, rotate_bound
#from tryOn import calculate_inclination

class VideoCamera(object):
    def __init__(self):
        # Using OpenCV to capture from device 0. If you have trouble capturing
        # from a webcam, comment the line below out and use a video file
        # instead.
        self.video = cv2.VideoCapture(0)
        # If you decide to use video.mp4, you must have this file in the folder
        # as the main.py.
        # self.video = cv2.VideoCapture('video.mp4')
    
    def __del__(self):
        self.video.release()
    
    def get_frame(self):
        success, image = self.video.read()
        # We are using Motion JPEG, but OpenCV defaults to capture raw images,
        # so we must encode it into JPEG in order to correctly display the
        # video stream.

        # detector = dlib.get_frontal_face_detector()
        # model = "data/shape_predictor_68_face_landmarks.dat"
        # predictor = dlib.shape_predictor(model)

        # gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        # faces = detector(gray, 0)

        # for face in faces: 
        #     (x,y,w,h) = (face.left(), face.top(), face.width(), face.height())

        #     shape = predictor(gray, face)
        #     shape = face_utils.shape_to_np(shape)
        #     incl = calculate_inclination(shape[17], shape[26]) #inclination based on eyebrows

        #     # condition to see if mouth is open
        #     is_mouth_open = (shape[66][1] -shape[62][1]) >= 10 #y coordiantes of landmark points of lips

        ret, jpeg = cv2.imencode('.jpg', image)
        return jpeg.tobytes()