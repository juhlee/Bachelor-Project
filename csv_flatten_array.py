import numpy as np
import os
import cv2
import csv
import glob

'''
Objective
    - Take in augmented images, convert them into single-row vector
    - Stack the vectors as one big matrix, save as csv
'''

def read_image(folder):

    data_list = list()
    file_length = 0
    patient_folders = os.listdir(folder) #1, 2, .., 2643
    patient_sorted = sorted([int(i) for i in patient_folders])
    patient_sorted = [str(i) for i in patient_sorted]

    for patient in patient_sorted:

        image_list = sorted(os.listdir(folder + '/' + patient)) # 1_0090.png ...

        for image_name in image_list:
            img_path = folder + '/' + patient + '/' + image_name
            file_length += 1

            img_structure = image_name.split('_') # 1, 0090
            img = cv2.imread(img_path, 0)
            img = cv2.resize(img, (100, 100))
            img = str(list(img.flatten()))[1:-1] # slilcing for removal of list brackets
            print('id:', img_structure[0], 'img:', img_structure[1])

            append_chunk = (img_structure[0], img_structure[1], img)
            data_list.append(append_chunk)

    return data_list

def csv_writer(data_list):

    global final

    csv_file = open('patients_oriaug.csv', 'w')

    for item in data_list:
        csv_file.write(str(item[0]) + ',' + str(item[1]) + ',' + item[-1] + '\n')

    csv_file.close()

if __name__ == '__main__':
    augmented_folder = 'augmented'
    data_list = read_image(augmented_folder)
    csv_writer(data_list)
