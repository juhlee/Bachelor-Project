# import necessary packages
import cv2
import numpy as np
from skimage import transform
import math

def flip(img, direction):
    ''' Flipping the image either horizontally, veritcally, or both.
    Args
        img: MRI image
        direction (int): option for direction of flipping.
                         0/1/2 = horizontal/vertical/both
    Returns
        flip_img : flipped MRI image
    '''

    # flip image horizontally
    flip_img = cv2.flip(img, direction)

    if not direction in range(0,3):
        flip_img = img # If a weird option given, give no effect

    return flip_img

def gaussian_noise(img, mean=0, std=0.1):
    ''' Adding gaussian noise to the image
    Args
        img : MRI image
        mean : pixel mean of image
        std : pixel standard deviation of image
    Returns
        gaussain_img : blurred MRI image
    '''
    # convert image to 1-channel
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    w, h = img.shape
    noise = np.zeros((w, h)) # initialize a noise filter.

    cv2.randu(noise, mean ,256) # set the noise filter with gaussian distr.

    gaus_img = img + np.array(std*noise, dtype=np.uint8)
    gaus_img = cv2.cvtColor(gaus_img, cv2.COLOR_GRAY2BGR)

    return gaus_img

def jittering(img, intensity=1):
    ''' Adding contrast to the image (1~4)
    Args
        image_path : path of the MRI image
    Returns
        contrast_img : MRI image with different contrast intensty
    '''

    clahe = cv2.createCLAHE(clipLimit=3.0, tileGridSize=(8,8))

    lab = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)  # convert from BGR to LAB color space
    l, a, b = cv2.split(lab)  # split on 3 different channels

    l2 = clahe.apply(l)  # apply CLAHE to the L-channel

    lab = cv2.merge((l2,a,b))  # merge channels
    img = cv2.cvtColor(lab, cv2.COLOR_LAB2BGR)  # convert from LAB to BGR

    return img

def scaling(img, x=1, y=1):
    ''' Affine transformation of image either in x or y direction.
    Args
        img : MRI image
    Returns
        scale_img : scaled MRI image
    '''
    # convert to 1-channel
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # apply re-scaling
    x2, y2 = img.shape[1]/x, img.shape[0]/y
    scale_img = cv2.resize(img, (x2,y2))

    # Keep the size of image constant by adding black regions
    scaling_canvas = np.zeros(img.shape, dtype=np.uint8)

    y_lim = int(min(y,1)*scale_img.shape[0])
    x_lim = int(min(x,1)*scale_img.shape[1])

    scaling_canvas[ : y_lim, : x_lim] = scale_img[ : y_lim, : x_lim]

    scale_img = scaling_canvas
    scale_img = cv2.cvtColor(scale_img, cv2.COLOR_GRAY2BGR)

    return scale_img

def gamma_correction(img, gamma=1.0, bright=True):
    ''' Adjust the gamma level of the picture
 s        img : MRI image
        gamma : gamma adjustment
    Returns
        gamma_img : MRI image with gamma adjustment
    '''
    value = gamma * 10
    img = img.astype("int16")

    if bright:
        img = img + value
    else:
        img = img - value

    img[img > 255] = 255
    img[img < 0] = 0

    img = img.astype("uint8")

    return img

def gaussian_blur(img, var=0.1):
    ''' Adding 'gaussian blur' to the image
    Args
        img : MRI image
        var : variance (intensity) of gaussian blur
    Returns
        blur_img : blurred MRI image
    '''
    sigma = var ** 0.5
    '''
    # kernel radius = 4 * sigma
    kernel_radius = int(math.ceil(4 * sigma))
    kernel = (kernel_radius, kernel_radius)
    print(kernel)

    blur_img = cv2.GaussianBlur(img, kernel, sigma, sigma, cv2.BORDER_DEFAULT)
    '''
    blur_img = cv2.GaussianBlur(img, (15, 15), sigma, sigma, cv2.BORDER_DEFAULT)

    return blur_img

def rotations(img, theta=10, scale = 1):
    ''' Rotation of the MRI image in a certain degrees
    Args
        img: MRI image
        theta: angle of rotation
        scale: degree of 'zooming in' to the image.
    Returns
        rotated_img : rotated MRI image
    '''

    # Find the center of the image
    (row, col) = img.shape[:2]
    img_center = (col / 2, row / 2)

    # Apply the rotation
    rot_matrix = cv2.getRotationMatrix2D(img_center, theta, scale)
    rotated_img = cv2.warpAffine(img, rot_matrix, (col, row), flags=cv2.INTER_LINEAR)

    return rotated_img

def shear(img, s=0.1):
    ''' Shearing of the MRI image represented by affine transformation
    Args:
        img: MRI image
        s : level of shearing [0.1 ~ 0.35]
    Returns
        shear_img : sheared MRI image
    '''

    rows,cols,ch = img.shape

    pts1 = np.float32([[50, 50],[200, 50],[50, 200]])
    pts2 = np.float32([[50 * s, 50 * s],[200, 50],[50, 200]])

    M = cv2.getAffineTransform(pts1,pts2)

    shear_img = cv2.warpAffine(img,M,(cols,rows))

    return shear_img

if __name__ == '__main__':

    img_name = '../../MRI_T2_COR_2019_02_20/1/1_0096.png'

    img = cv2.imread(img_name)
    hflip = flip(img, 0)
    vflip = flip(img, 1)
    gnoise = gaussian_noise(img, 0, 0.4)
    contrast = jittering(img)
    scalex = scaling(img, 2, 1)
    scaley = scaling(img, 1, 2)
    scalexy = scaling(img, 2,2)
    gcorrection = gamma_correction(img, 4, True)
    g_dark = gamma_correction(img, 4, False)
    gblur = gaussian_blur(img, 0.4)
    rot = rotations(img, 45, 1)
    sheared = shear(img, 0.35)

    list = [hflip, vflip, gnoise, contrast, scalex, scaley, gcorrection, g_dark, gblur, rot, sheared]

    for i, j in enumerate(list):
        cv2.imwrite('save' + str(i) + '.png', j)
