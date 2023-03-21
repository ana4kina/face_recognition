import os
import pickle
import sys
from config import pth_all_photo, w_os, pth_enc, pth_photo
import face_recognition
import shutil


def null_directory(name):
    print("         NULL_DIRECTORY          ")
    filename = os.path.basename(name)
    index = filename.index('.')
    dir_mkdir = pth_photo() + filename[:index]
    print("null_directory(): dir_mkdir: ", dir_mkdir)
    os.mkdir(dir_mkdir, mode=0o777, dir_fd=None)
    dest_path = pth_photo() + filename[:index]
    print("null_directory(): dest_path: ", dest_path)
    new_location = shutil.move(name, dest_path)
    print("null_directory(): new_location: ",  new_location)


def recognition(name, pth):         # name = /rect/... .jpg      pth = /people/data
    print("")
    print("         RECOGNITION         ")
    print("recognition(): name:", name)
    print("recognition(): pth:", pth)
    current = name
    another = False
    known_encodings = []
    face_img = face_recognition.load_image_file(current)
    face_enc = face_recognition.face_encodings(face_img)[0]
    known_encodings.append(face_enc)
    dir = os.listdir(pth)
    print("recognition(): dir: ", dir)  
    for (i, image) in enumerate(dir):       ####
        print("current: ", current)
        if len(dir) == 0:
            return another
        print(f"[* processing img {i + 1}/{len(dir)}")
        face_img = face_recognition.load_image_file(current)
        face_enc = face_recognition.face_encodings(face_img)[0]
        for item in range(0, len(known_encodings)):
            res = face_recognition.compare_faces([face_enc], known_encodings[item])
            if res[0]:
                known_encodings.append(face_enc)
                print("Same person!")
                another = True
                break   
            else:
                print("Another person!")
                another = False
                return another
        current = pth + w_os() + dir[i]
    print(f"Length {len(known_encodings)}")
    print("")
    return another

def train_model_by_img(name):
    print("")
    print("         TRAIN_MODEL_BY_IMG          ")
    images = os.listdir(pth_photo())
    print("train_model_by_img(): name: ", name)
    print("train_model_by_img(): images: ", images)
    if len(images) == 0:
        print("train_model_by_img(): was called null_directory: ")
        null_directory(name)
        return
    count = 0                          # номер директории из /photos
    filename = os.path.basename(name)  # имя файла из пути file.txt
    pth = pth_photo() + images[count]  # путь к каталогу в people/pth
    print("train_model_by_img(): filename: ", filename)
    print("train_model_by_img(): pth: ", pth)
    while (os.path.isfile(pth)) and (count < len(images)):
        count += 1
        pth = pth_photo() + images[count]
        print("train_model_by_img(): ''pth'' in while: ", pth)
    if count == len(images):
        null_directory(name)
        return
    while count < len(images):
        pth = pth_photo() + images[count]
        face = recognition(name, pth)
        if face:
            new_location = shutil.move(name, pth + w_os() + filename)
            print("new_location: ", new_location)
            return
        else:
            count += 1
    index = filename.index('.')
    path = pth_photo() + filename[:index] + w_os()
    os.mkdir(path, mode=0o777, dir_fd=None)
    dest_path = pth_photo() + filename[:index]
    print("")
    print("dest_path: ", dest_path)
    new_location = shutil.move(name, dest_path)
    print("here is new_location: ", new_location)