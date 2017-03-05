import os,time, pathlib, shutil
from classes import AppUtil

def EmptyDirCnt(filesSource):
    print('{:17} - {}'.format('EmptyDirectories:', \
            str(time.strftime('%Y-%m-%dT%H:%M:%S'))))
    dirCnt = 0
    emptyDirCnt = 0
    for root, directories, filenames in os.walk(filesSource):
        for directory in directories:
            directoryPath = os.path.join(root, directory)
            if not os.path.exists(directoryPath):
                continue
            try:
                fileList = os.listdir(directoryPath)
            except Exception as other:
                print('problem: {}\nDirectory: {}'.format(other,directory))
                continue
            dirCnt =+ dirCnt + 1
            if len(fileList) == 0:
                try:
                    #os.rmdir(path)
                    emptyDirCnt += 1
                    pass
                except Exception as other:
                    print('problem: ', other)
                    #print('{} - {}'.format(len(fileList),directoryPath))
                    pass

    outputStr = "\ndirectory: {0:s}\ndirectories: {1:n}, empty directories: {2:n}\n"\
        .format(filesSource, dirCnt, emptyDirCnt)
    print(outputStr)
    return

def pyFilesClean(filesSource,fileDataObj,errFileObj):
    print('{:17} - {}'.format('fileApps:', \
            str(time.strftime('%Y-%m-%dT%H:%M:%S'))))
    aU = AppUtil()
    errStr = 'fileApps:fileDelete() {}'.format(aU.timeStamp())
    fileDataObj.write(errStr)
    errFileObj.write(errStr)

    scannedCnt = 0
    killCount = 0

    for root, directories, filenames in os.walk(filesSource):
        for directory in directories:
            directoryPath = os.path.join(root, directory)
            directoryPath = str(directoryPath).lower()
            if not os.path.exists(directoryPath):
                continue

            if directory == '__pycache__':
                fileDataObj.write(directoryPath + '\n')
                shutil.rmtree(directoryPath)
                killCount += 1

    outputStr = "\noutput file: {0:s}\ndirectories: {1:n}, kill count: {2:n}\n"\
        .format(fileDataObj.name, scannedCnt, killCount)
    print(outputStr)

    filesScannedCnt = 0
    killCount = 0
    for root, directories, filenames in os.walk(filesSource):
        #for directory in directories:
            #print (os.path.join(root, directory))
        for filename in filenames:
            fileNamePath = os.path.join(root, filename)

            if not os.path.exists(fileNamePath):
                continue

            print('.', end="", flush=True)
            if (filesScannedCnt %500 == 0):
                print('\n{:05d} - {}'.format(filesScannedCnt, \
                        str(time.strftime('%Y-%m-%dT%H:%M:%S'))))
            filesScannedCnt += 1
            
            killFlg = False
            fileNameExtension = pathlib.Path(fileNamePath).suffix
            fileNameExtension = fileNameExtension.lower()
            if filename.startswith('.'):
                killFlg = True
            elif fileNameExtension == ".pyc":
                killFlg = True
            elif fileNameExtension == ".pyo":
                killFlg = True

            if killFlg:
                killCount += 1
                fileDataObj.write(fileNamePath + '\n')
                os.unlink(fileNamePath)
                pass

                
    errFileObj.close()
    fileDataObj.close()
    outputStr = "\noutput file: {0:s}\nfiles scanned: {1:n}, kill count: {2:n}\n"\
        .format(fileDataObj.name, filesScannedCnt, killCount)
    print(outputStr)
    return





