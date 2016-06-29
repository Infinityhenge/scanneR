import time
import os
import shutil

def machine():
    print("This will scan your entire system for a filetype and date of your chosing")
    fileIn = input("Input your system drive to scan(C:\\ is usually the default): ")
    filesOut = input("Where do you want to store your files(type 'default' to store to where program is located): ")
    searchtype = input("Month or day, (m/d/n); Type d to find files based on day, month and year or, "
                       "type m to find files based on only month and year, or n for no date filtering so m/d/n?: ")
    if not searchtype == "n":
        dateIn = input("Please input the date you want to scan for; For d type format as so: eg. 20 Apr 2016 and for m type"
                   "format as shown here: eg. Apr 2016 '--------USE CAPITAL LETTERS AS SHOWN FOR THE MONTHS AND USE THE"
                   " ABBREVIATED VERSIONS OF THEM: eg. June->Jun-----': ")

    filetype = input("Please input the filetype you want to copy: ")

    if filesOut == "default":
        filesOut = os.getcwd()

    def copyfile(file, fileIn, newpath, createdTime = None):
        createdTime1 = time.ctime(os.path.getctime(fileIn + "\\" + file))
        createdTime2 = createdTime1.replace("  ", " ").split(" ")
        createdTime3 = str(createdTime2[2]) + " " + str(createdTime2[1]) + " " + str(createdTime2[4])
        createdTime4 = str(createdTime2[1]) + " " + str(createdTime2[4])
        createdTime5 = "none"

        if createdTime is None:
            if searchtype == "d":
                copyfile(file, fileIn, newpath, createdTime3)
            elif searchtype == "m":
                copyfile(file, fileIn, newpath, createdTime4)
            elif searchtype == "n":
                copyfile(file, fileIn, newpath, createdTime5)

        else:
            if not createdTime == "none":
                if dateIn == createdTime:
                    print(file)
                    print("created: %s" % createdTime)
                    print(fileIn + "\\files from scanner and sorter\\" + file)
                    shutil.copy(fileIn + "\\" + file, newpath)
            elif createdTime == "none":
                print(file)
                print(fileIn + "\\files from scanner and sorter\\" + file)
                shutil.copy(fileIn + "\\" + file, newpath)


    def detectFile(file, fileIn, newpath):
        if file.endswith(filetype):
            copyfile(file, fileIn, newpath)


    def runDetectFile(fileIn):

        newpath = filesOut + "\\files from scanner and sorter\\"
        if not os.path.exists(newpath):
            os.makedirs(newpath)

        if fileIn != filesOut:
            try:
                for file in os.listdir(fileIn):
                    if os.path.isdir(fileIn + "\\" + file):
                        runDetectFile(fileIn + "\\" + file)
                    else:
                        detectFile(file, fileIn, newpath)
            except:
                pass



    runDetectFile(fileIn)
machine()