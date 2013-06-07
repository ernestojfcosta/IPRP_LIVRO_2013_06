import os
import random
import cImage
import time

def searchFiles(path):
    dirList = os.listdir(path)
    
    filesList = []
    
    for fname in dirList:
        if os.path.isdir(fname):
            print "It's a directory: ",fname
            newList = searchFiles(path+"/"+fname)
            
            for i in range(len(newList)):
                filesList.append(fname+"/"+newList[i])
        else:
            sp = fname.rpartition(".")
            if len(sp) == 3:
                if sp[2] == "gif":
                    filesList.append(fname)
                    print "Image: ",fname
                else:
                    print "Not a image file: ",fname
            else:
                print "Wrong file name. Skipping..."
    
    random.shuffle(filesList)
    return filesList

def showImages(path, filesList, delay):
    print ""
    print "Going to show images...";
    print ""
    
    window = cImage.ImageWin("Imagem", 600,400)
    
    for i in range(len(filesList)):
        filePath = path+"/"+filesList[i]
        print "Path: ",filePath
        
        image = cImage.FileImage(filePath)
        
        image.draw(window)
        time.sleep(delay)

    window.exitOnClick()

if __name__ =='__main__':
    delay = 2
    path="/tempo/imagens"
    filesList = searchFiles(path)

    print ""
    print "Shuffled Files: ",filesList

    showImages(path, filesList, delay)
