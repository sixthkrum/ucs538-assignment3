import sys
import os
import cv2

def convertVideoToBW(filename):
    captureStream = cv2.VideoCapture(filename)
    captureWidth = captureStream.get(cv2.CAP_PROP_FRAME_WIDTH)
    captureHeight = captureStream.get(cv2.CAP_PROP_FRAME_HEIGHT)
    captureSize = (int(captureWidth), int(captureHeight))
    captureFPS = captureStream.get(cv2.CAP_PROP_FPS)
    captureFourCC = int(captureStream.get(cv2.CAP_PROP_FOURCC))
    extIndex = filename.rindex('.')
    outputName = filename[ : extIndex] + '_converted' + filename[ extIndex : ]
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

    return outputName
