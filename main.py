import cv2
import os
import sys
from download import download
from vidtoimg import convert


def main():
    vid_path = download(sys.argv[1]) #accepts output path (cwd is default) and link, creates a 'download' dir, downloads video and returns path of video.

    #'https://www.youtube.com/watch?v=uPz9x4zNP4o'

    for vid in os.listdir(vid_path):
        vidcap = cv2.VideoCapture(os.path.join(vid_path,vid))

        convert(vidcap)


if __name__ == '__main__':
    main()