import cv2
import os
from utils import createdir


def convert(vidcap, rpath=os.getcwd(), framerate=0.5):


    rpath = os.path.join(rpath, 'results')
    createdir(rpath)

    def getFrame(sec):
        vidcap.set(cv2.CAP_PROP_POS_MSEC, sec * 1000)
        hasFrames, image = vidcap.read()
        if hasFrames:
            img_name = str(count) + ".jpg"
            cv2.imwrite(os.path.join(rpath, img_name), image)  # save frame as JPG file
        return hasFrames

    sec = 0

    count = 0

    success = getFrame(sec)

    while success:
        count = count + 1
        sec = sec + framerate
        sec = round(sec, 2)
        success = getFrame(sec)