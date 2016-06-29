import time
import os
import shutil

def machine():
    print("INPUT 'default' TO SCAN THE DIRECTORY OF THE EXE/PY FILE THIS IS RUNNING FROM")
    fileIn = input("Please input a directory to copy the files of: ")
    searchtype = input("Month or day, (m/d); Type d to find files based on day, month and year or, "
                       "type m to find files based on only month and year, so m/d?: ")

    dateIn = input("Please input the date you want to scan for; For d type format as so: eg. 20 Apr 2016 and for m type"
                   "format as shown here: eg. Apr 2016 '--------USE CAPITAL LETTERS AS SHOWN FOR THE MONTHS AND USE THE"
                   " ABBREVIATED VERSIONS OF THEM: eg. June->Jun-----': ")

    def copyfile(file, directory, newpath, createdTime = None):
        createdTime1 = time.ctime(os.path.getctime(directory + "\\" + file))
        createdTime2 = createdTime1.replace("  ", " ").split(" ")
        createdTime3 = str(createdTime2[2]) + " " + str(createdTime2[1]) + " " + str(createdTime2[4])
        createdTime4 = str(createdTime2[1]) + " " + str(createdTime2[4])

        if createdTime is None:
            if searchtype == "d":
                copyfile(file, directory, newpath, createdTime3)
            elif searchtype == "m":
                copyfile(file, directory, newpath, createdTime4)
        else:
            if dateIn == createdTime:
                print(file)
                print("created: %s" % createdTime)
                print(directory + "\\files from scanner and sorter\\" + file)
                shutil.copy(directory + "\\" + file, newpath)

    def detectFile(file, directory, newpath):
        if file.endswith(".png"):
            copyfile(file, directory, newpath)
        elif file.endswith(".jpg"):
            copyfile(file, directory, newpath)
        elif file.endswith(".raw"):
            copyfile(file, directory, newpath)
        elif file.endswith(".jpeg"):
            copyfile(file, directory, newpath)
        elif file.endswith(".JPG"):
            copyfile(file, directory, newpath)


    def runDetectFile():
        if fileIn == "default":
            directory = os.getcwd()

            newpath = directory + "\\files from scanner and sorter\\"
            if not os.path.exists(newpath):
                os.makedirs(newpath)

            for file in os.listdir(directory):
                detectFile(file, directory, newpath)
        else:
            directory = fileIn

            newpath = directory + "\\files from scanner and sorter\\"
            if not os.path.exists(newpath):
                os.makedirs(newpath)

            for file in os.listdir(directory):
                detectFile(file, directory, newpath)

        newpath = directory + "\\files from scanner and sorter\\"
        if not os.path.exists(newpath):
            os.makedirs(newpath)
    runDetectFile()
machine()
