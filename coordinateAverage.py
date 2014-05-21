from liblas import file
import os
import numpy as np

inputLocation	= './'
outputfile		= open('outputfile.txt', 'w')

def listFiles(dir):
    rootdir = dir
    for root, subFolders, files in os.walk(rootdir):
        for file in files:
            yield os.path.join(root, file)
    return

for foundFile in listFiles(inputLocation):
	if (foundFile.split('.')[-1] == 'las'):
		print foundFile
		inputfile = file.File(foundFile, mode='r')
		xAverage = []; yAverage = []; zAverage = []
		for row in range(0, 10):
			xAverage.append(inputfile[row].x)
			yAverage.append(inputfile[row].y)
			zAverage.append(inputfile[row].z)
		outputfile.write('%s\t\t\t%s, %s, %s\n' % (foundFile, np.mean(xAverage), np.mean(yAverage), np.mean(zAverage)))

outputfile.close()