import os, csv, datetime, time, pathlib, hashlib
from collections import namedtuple

import fileApps

if __name__ == '__main__':
    ######################################################
    # create a files data .csv file
    #timeStamp = time.strftime('%Y-%m-%dT%H:%M:%S',time.localtime())

    filesSource = r'C:\Users\mark_\Documents\BP-FirstDjangoApp\mysite'
    MetaSet = 'django'
    outputDir = r'j:\\temp'

    #filesSource = r'J:\eBooks-Topics'
    #MetaSet = 'file'

    userDocsPath = os.getenv('USERPROFILE') + r'\Documents'

    fileDataName = os.path.join(userDocsPath, MetaSet + r'-data.txt')
    errFileName = os.path.join(userDocsPath, MetaSet + r'-errs.txt')
    
    fileDataObj = open(fileDataName, 'w')
    errFileObj = open(errFileName, 'w')

    print('{:17} - {}'.format('MetaSet:',MetaSet))
    print('{:17} - {}'.format('start:', \
            str(time.strftime('%Y-%m-%dT%H:%M:%S'))))

    ######################################################
    # delete extraneous files
    # .txt, .gif, .jpeg, zero-length
    fileApps.pyFilesClean(filesSource,fileDataObj,errFileObj)
    #file_action.FileCullAttr(filesSource, flex1)
    #file_action.EmptyDirectories(filesSource)

    ######################################################
    # db overhead
    #dbConnectStr = r'postgresql+psycopg2:' \
    #            + r'//postgres:postgrespassword@localhost' \
    #            + r':5432/MYFILES'
    #engine = create_engine(dbConnectStr)
    ##engine.echo = True                 # db debugging switch
    #conn = engine.connect()
    #db_utility.createTables(engine)
    #dbFilesMeta = db_utility.ConnectExistingTables(conn)

    #######################################################
    # put the files metadata csv into the database
    #db_app.FileMetaCsv2Db(csvDataName,conn,dbFilesMeta,errFileObj)

    ######################################################
    # clean up
    #file_action.EmptyDirectories(filesSource)
    fileApps.EmptyDirCnt(filesSource)

    fileDataObj.close()
    errFileObj.close()
    print('{:17} - {}'.format('finished!', \
            str(time.strftime('%Y-%m-%dT%H:%M:%S'))))