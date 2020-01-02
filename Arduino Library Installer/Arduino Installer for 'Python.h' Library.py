try:
    print("Finding required Libraries...")

    #This function allows us to write to the errorLog.txt file.
    def writeToStatusLog(data,fileStatus = 'a'):
        f = open("Error Log.txt",fileStatus)
        f.write(data+"\n")
        f.close()

    #The first message is set to write mode rather than append mode so it clears data from the
    #last script. It will also create the file if it doesn't already exist due to the "+" flag
    writeToStatusLog("Importing Required Files",'w+')

    #Import all the libraries we will require for this installer to function
    import pip,os,sys,ctypes.wintypes,filecmp,shutil,time
    
    print("Installing Arduino Library...")
    writeToStatusLog("\nLocating Required Directories")
    
    #Get the user directory. I'll be honest, I don't actually know how this bit works,
    #i just got it off the internet and somehow it seems to work. No point reinventing the wheel!
    CSIDL_PERSONAL = 5
    SHGFP_TYPE_CURRENT = 0
    
    buf = ctypes.create_unicode_buffer(ctypes.wintypes.MAX_PATH)
    ctypes.windll.shell32.SHGetFolderPathW(None, CSIDL_PERSONAL, None, SHGFP_TYPE_CURRENT, buf)
    
    writeToStatusLog("Stripping Directory Data")
    
    #Strip the directory of strange characters, replace them, and strip the last directory pointer
    buf.value = buf.value.replace("\\","/")
    while (buf.value.endswith("/") == False):
        buf.value = buf.value[:-1]

    #Ok, now the tricky stuff is out of the way, we start finding the directories we need
    arduinoDestinationFolder = buf.value + "Documents/Arduino/libraries/"

    writeToStatusLog("Checking Directory Existance")
    
    #Does the directory already exist? If so, delete it and continue on
    if (os.path.exists(arduinoDestinationFolder + "Python/")):
        writeToStatusLog(" - Deleting File: " + arduinoDestinationFolder + "Python/")
        shutil.rmtree(arduinoDestinationFolder + "Python/")

    #We have the required directories and permissions to start installing the file
    sourceFile = os.getcwd().replace("\\","/") + "/Python.zip"

    writeToStatusLog("\nUnzipping Arduino Library")
    
    #Ok, so we know where we are putting the resulting file, as well as where the file is
    import zipfile

    fh = open(sourceFile, 'rb')
    z = zipfile.ZipFile(fh)
    for name in z.namelist():
        outpath = arduinoDestinationFolder
        writeToStatusLog("Extracting Arduino Library")
        z.extract(name, outpath)
    fh.close()
    
    writeToStatusLog("Finished Extracting Arduino Library")
    writeToStatusLog("\nSuccessfully Installed Arduino Library")
    print("\nSuccessfully Installed Arduino Python Library")

    #Delete the error log because no error occured.
    os.remove("Error Log.txt")

    #Pause for 3 seconds so the user can read the success message
    time.sleep(3)
    
except Exception as ex:
    f = open("Progress Log.txt",'a')
    f.write("\n\n\n" + str(ex))
    f.close()
    
    print("An error has occured. Please check the statusLog.txt file for more information")
