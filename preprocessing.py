import cv2
import numpy as np
from skimage import transform
import math
import os
from data_augmentation import * # Import all augmentation methods
from matplotlib import pyplot as plt

folder = '../MRI_T2_COR_2019_02_20'
savefolder = 'augmented'

try:
    os.mkdir(savefolder)
except:
    pass

def import_file(folder):

    sub_folders = sorted(os.listdir(folder)) # 1, 2, ..., 2300

    for sub_folder in sub_folders:

        sub_folder_path = folder + '/' + sub_folder
        savefolder2 = savefolder + '/' + sub_folder

        if not os.path.exists(savefolder2):
            os.mkdir(savefolder2)

        image_names = sorted(os.listdir(sub_folder_path))
        # 'MRI_T2_COR_2019_02_20/1/1_0096.png'

        try:
            for image_name in image_names:

                img = cv2.imread(sub_folder_path + '/' + image_name)
                img = cv2.resize(img, (256, 256))
                print(image_name)

                # Randomly apply augmentation methods
                if np.random.rand() < 0.5:
                    img = flip(img, 0)
                if np.random.rand() < 0.5:
                    img = flip(img, 1)
                if np.random.rand() < 0.5:
                    img = flip(img, 1)
                if np.random.rand() < 0.5:
                    img = gaussian_noise(img)
                if np.random.rand() < 0.5:
                    img = jittering(img)
                if np.random.rand() < 0.5:
                    img = scaling(img)
                if np.random.rand() < 0.5:
                    img = gamma_correction(img)
                if np.random.rand() < 0.5:
                    img = gaussian_blur(img)
                if np.random.rand() < 0.5:
                    img = rotations(img)
                if np.random.rand() < 0.5:
                    img = shear(img)

                cv2.imwrite(os.path.join(savefolder2, image_name), img)

        except:
            pass

print(import_file(folder))
