import os

def getFilesInDir(folder):
    entries = os.listdir(folder)
    fEntries = []
    for entry in entries:
        fEntries.append(folder +'/'+ entry)
    return fEntries