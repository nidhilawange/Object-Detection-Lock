import cv2
import DanceVid.ml as ml
import json
import re

#Run from DanceVid folder (cd DanceVid)
#
def processVideo():
    #
    try:

        with open("./DanceVid/Output/metadata.json","r") as metadata: 
            files = json.load(metadata)
        if files:
            return files
    except FileNotFoundError as e:
        pass
    except json.decoder.JSONDecodeError as j:
        pass

    frameNr = 0
    #
    files = []
    capture = cv2.VideoCapture("./DanceVid/vid.mp4")
    while(True):
        success, frame = capture.read()
        print(frameNr)
        if not success:
            break
        if success:
            if (frameNr%30 == 0):
                cv2.imwrite(f'./DanceVid/Output/frame_{frameNr}.jpg', frame)
                #
                files.append(f'./DanceVid/Output/frame_{frameNr}.jpg')
        else:
            break
    
        frameNr = frameNr+1

    capture.release()
    #
    with open("./DanceVid/Output/metadata.json","w") as metadata: 
        json.dump(files,metadata)
    #
    return files
#
def processFrames(files: list[str])->None: 
    for file in files:
        #
        frameNum = [s for s in file.replace("_",".").split(".") if s.isdigit()][0]
        print(f'{ml.runVision(file)},{frameNum}')
        #

if (__name__ == "__main__"):
    files = processVideo()
    processFrames(files)




