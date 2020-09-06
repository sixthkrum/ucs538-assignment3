import sys
import os
import cv2
import filetype

if len(sys.argv) != 2:
    print("Only enter filename of video as argument:\n python convert.py <VideoFileName>")
    exit()

else:
    filename = sys.argv[1]

    if not os.path.isfile('./' + filename):
        print("File does not exist")
        exit()

    if str(filetype.guess('./'+filename)).find('video') == -1:
        print("File is not a video")
        exit()

    captureStream = cv2.VideoCapture(filename)
    captureWidth = captureStream.get(cv2.CAP_PROP_FRAME_WIDTH)
    captureHeight = captureStream.get(cv2.CAP_PROP_FRAME_HEIGHT)
    captureSize = (int(captureWidth), int(captureHeight))
    captureFPS = captureStream.get(cv2.CAP_PROP_FPS)
    captureFourCC = int(captureStream.get(cv2.CAP_PROP_FOURCC))
    outputName = "converted_" + filename
    outputStream = cv2.VideoWriter(outputName, captureFourCC, captureFPS, captureSize, False)

    while(True):
        ret, currentFrame = captureStream.read()

        if ret == True:
            convertedFrame = cv2.cvtColor(currentFrame, cv2.COLOR_BGR2GRAY)
            outputStream.write(convertedFrame)

        else:
            break

    captureStream.release()
    outputStream.release()
    cv2.destroyAllWindows()
