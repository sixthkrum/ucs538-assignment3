import sys
import os
import cv2

def compressVideo(filename, compressionFraction):
    captureStream = cv2.VideoCapture(filename)
    captureWidth = captureStream.get(cv2.CAP_PROP_FRAME_WIDTH)
    captureHeight = captureStream.get(cv2.CAP_PROP_FRAME_HEIGHT)
    outputSize = (int(captureWidth / compressionFraction) , int(captureHeight / compressionFraction))
    captureFPS = captureStream.get(cv2.CAP_PROP_FPS)
    captureFourCC = int(captureStream.get(cv2.CAP_PROP_FOURCC))
    extIndex = filename.rindex('.')
    outputName = filename[ : extIndex] + '_compressed' + filename[ extIndex : ]
    outputStream = cv2.VideoWriter(outputName, captureFourCC, captureFPS, outputSize)

    while(True):
        ret, currentFrame = captureStream.read()

        if ret == True:
            compressedFrame = cv2.resize(currentFrame, outputSize)
            outputStream.write(compressedFrame)

        else:
            break


    captureStream.release()
    outputStream.release()
    cv2.destroyAllWindows()
    return outputName
