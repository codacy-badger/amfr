import cv2

from facial_recog.app.config import recog_method
from facial_recog.app.db_util import all_subjects_for_class


def get_recognizer():
    if recog_method == 'lbph':
        face_recognizer = cv2.face.LBPHFaceRecognizer_create()
    elif recog_method == 'eigen':
        face_recognizer = cv2.face.EigenFaceRecognizer_create()
    else:
        face_recognizer = cv2.face.FisherFaceRecognizer_create()
    return face_recognizer


def get_class_subjects(class_id):
    return [i[0] for i in all_subjects_for_class(class_id)]
