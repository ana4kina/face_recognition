import face_recognition
from config import pth_to_save, w_os
from PIL import Image, ImageDraw
from datetime import datetime
import cv2
import os
from training_model import train_model_by_img


def cut_face(pth_img, file):
    print("")
    print("         CUT_FACE            ")
    count = 0
    faces = face_recognition.load_image_file(pth_img)
    faces_locations = face_recognition.face_locations(faces)

    for faces_location in faces_locations:
        top, right, bottom, left = faces_location
        face_img = faces[top:bottom, left:right]
        pil_img = Image.fromarray(face_img)
        pth = pth_to_save() + datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "_" + file
        print("")
        print("cut_face(): pth: ", pth)
        pil_img.save(pth)
        train_model_by_img(pth)
        count += 1
    print(f"cut_face(): Found {count} face(s) in this photo")


def face_rec(name_file, file):
    print("")
    print("         FACE_REC            ")
    print(name_file)
    face_img = face_recognition.load_image_file(name_file)
    face_location = face_recognition.face_locations(face_img)  # для нескольких лиц

    print("face_rec(): face_location: ", face_location)
    print(f"face_rec(): Found {len(face_location)} face(s) in this photo")

    if not len(face_location):
        print("There aren't any faces :(")
        return 0
    pil_img = Image.fromarray(face_img)
    draw = ImageDraw.Draw(pil_img)

    for (top, right, bottom, left) in face_location:
        draw.rectangle(((left, top), (right, bottom)), outline=(255, 255, 0), width=4)
    new_photo = pth_to_save() + datetime.now().strftime("%Y-%m-%d-%H:%M:%S") + "_" + file
    pil_img.save(new_photo)
    del draw
    
    print("face_rec(): new_photo ", new_photo)
    file = os.path.basename(name_file)
    cut_face(new_photo, file)
    print("face_rec(): new_photo ", new_photo)
    return new_photo
    

def show_photo(name_file, file):
    new_photo = face_rec(name_file, file)
    if not new_photo:
        print("Sorry, there aren't any photos :(")
        return
    img = Image.open(new_photo)
    img.show()
