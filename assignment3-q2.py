import sys
import os
import cv2
import filetype

if len(sys.argv) != 3:
    print("Only enter filename and compression fraction (1 to 99) of video as argument:\n python convert.py <VideoFileName> <CompressionFraction")
    exit()

else:
    compressionFraction = int(sys.argv[2])
    if not compressionFraction >= 1 and compressionFraction <= 99:
        print("Compression fraction should be between 1 and 99")
        exit()

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
    outputSize = (int(captureWidth / compressionFraction) , int(captureHeight / compressionFraction))
    captureFPS = captureStream.get(cv2.CAP_PROP_FPS)
    captureFourCC = int(captureStream.get(cv2.CAP_PROP_FOURCC))
    outputName = "compressed_" + filename
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
