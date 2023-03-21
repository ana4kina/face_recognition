import os
from sys import platform


def pth_model():
    if platform == "linux" or platform == "linux2":
        face_model = os.path.abspath(os.curdir) + '/models/frontalface_default.xml'
    elif platform == "win32":
        face_model = os.path.abspath(os.curdir) + '\models\frontalface_default.xml'
    return face_model


def w_os():
    if platform == "linux" or platform == "linux2":
        return '/'
    elif platform == "win32":
        return '\\'


def pth_photo():
    if platform == "linux" or platform == "linux2":
        pth = os.path.abspath(os.curdir) + '/photos/people/'
    elif platform == "win32":
        pth = os.path.abspath(os.curdir) + '\photos\people\\'
    return pth


def pth_all_photo():
    if platform == "linux" or platform == "linux2":
        pth = os.path.abspath(os.curdir) + '/photos/'
    elif platform == "win32":
        pth = os.path.abspath(os.curdir) + '\photos\\'
    return pth


def pth_to_save():
    if platform == "linux" or platform == "linux2":
        pth = os.path.abspath(os.curdir) + '/photos/rectangle_photos/'
    elif platform == "win32":
        pth = os.path.abspath(os.curdir) + '\photos\rectangle_photos\\'
    return pth


def pth_only_faces():
    if platform == "linux" or platform == "linux2":
        pth = os.path.abspath(os.curdir) + '/photos/faces/'
    elif platform == "win32":
        pth = os.path.abspath(os.curdir) + '\photos\faces\\'
    return pth


def pth_enc():
    if platform == "linux" or platform == "linux2":
        pth = os.path.abspath(os.curdir) + '/photos/encodings/'
    elif platform == "win32":
        pth = os.path.abspath(os.curdir) + '\photos\encodings\\'
    return pth