from liblas import file as lasfile
import sys
import math
import numpy
import bisect
import time
import matplotlib.pyplot as plt

def getMinMaxValues(currentValue, minValue, maxValue):
	if minValue != None && maxValue != None:
		if currentValue > maxValue:
			maxValue = currentValue
		elif currentValue < minValue:
			minValue = currentValue
	else:
		minValue = currentValue
		maxValue = currentValue
	return minValue, maxValue
def sortByIntensity(maxRows, roundTo):
	counter			= 0
	intensityDict	= {}
	if maxRows == 0: maxRows = fileLength - 1
	for row in range(0, maxRows):
		intensityValue = inputfile[row].intensity
		position = (round(inputfile[row].x, roundTo), round(inputfile[row].y, roundTo), round(inputfile[row].z, roundTo))
		if intensityValue in intensityDict.keys():
			intensityDict[intensityValue].append(position)
		else: intensityDict[intensityValue] = [position]
		counter += 1
	return intensityDict, maxRows
def sortByPosition(maxRows, roundTo):
	counter			= 0
	xDict			= {}
	for row in range(0, maxRows):
		if inputfile[row].intensity > 0:
			xValue = round(inputfile[row].x, roundTo)
			yValue = round(inputfile[row].y, roundTo)
			pointIntensity = inputfile[row].intensity
			if xValue in xDict.keys():
				if yValue in xDict[xValue].keys():
					xDict[xValue][yValue].append(pointIntensity)
				else:
					xDict[xValue][yValue] = [pointIntensity]
			else:
				xDict[xValue] = {}
				xDict[xValue][yValue] = [pointIntensity]
	return xDict
def sortByElevation(maxRows, roundTo):
	counter			= 0
	xDict			= {}
	for row in range(0, maxRows):
		if inputfile[row].intensity > 0:
			xValue = round(inputfile[row].x, roundTo)
			yValue = round(inputfile[row].y, roundTo)
			pointIntensity = inputfile[row].intensity
			if xValue in xDict.keys():
				if yValue in xDict[xValue].keys():
					xDict[xValue][yValue].append(pointIntensity)
				else:
					xDict[xValue][yValue] = [pointIntensity]
			else:
				xDict[xValue] = {}
				xDict[xValue][yValue] = [pointIntensity]
	return xDict
def getSubSet(maxRows, xMin, yMin, xMax, yMax):
	if maxRows == 0: maxRows = fileLength - 1
	for row in range(0, maxRows):
		if row in countIntervals: print str(row) + ' rows completed!'
		pointIntensity = inputfile[row].intensity
		if pointIntensity < 0:
			xValue = inputfile[row].x
			if xValue > xMin and xValue < xMax:
				yValue = inputfile[row].y
				if yValue > yMin and yValue < yMax:
					outputfile.write('%s, %s, %s, %s\n' % (xValue, yValue, inputfile[row].z, pointIntensity))
def generateIntensityHistogram(maxRows, binSize, roundTo):
	intensityDict, maxRows	= sortByIntensity(maxRows, roundTo)
	print 'Intensity Dictionary created succesfully with ' + str(maxRows) + ' rows!'
	minIntensity			= min(intensityDict.keys())
	maxIntensity			= max(intensityDict.keys())
	histogramBins			= range(minIntensity, maxIntensity + binSize, binSize)
	# freq, histogramBins	= numpy.histogram(intensityDict.keys(), histogramBins)
	intensityArray			= []
	for key, value in intensityDict.iteritems():
		for count in range(0, len(value)): intensityArray.append(key)
	plt.hist(intensityArray, histogramBins, histtype='bar')
	print 'Histogram data processed. Launching GUI to display results!'
	plt.show()
	return intensityDict, histogramBins
def generateIntensityHistogramReducedMemory(maxRows, binSize, roundTo):
	memoryCheck = {}
	intensityArray = [0]
	intensityCountArray = [0]
	if maxRows == 0: maxRows = fileLength - 1
	for row in range(0, maxRows):
		tempIntensity = inputfile[row].intensity
		minValue, maxValue = getMinMaxValues(currentValue, minValue, maxValue)
		while tempIntensity > max(intensityArray):
			intensityArray.append(max(intensityArray) + binSize)
			intensityCountArray.append(0)
		while tempIntensity < min(intensityArray):
			intensityArray.insert(0, min(intensityArray) - binSize)
			intensityCountArray.insert(0, 0)
		intensityCountArray[bisect.bisect_left(intensityArray, tempIntensity)] += 1
	return intensityArray, intensityCountArray

start_time			= time.time()	
inputfile			= lasfile.File('L109633_EB.las', mode = 'r')
outputfile			= open('outputfile.txt', 'w')
bins, frequencies	= generateIntensityHistogramReducedMemory(1000000, 1000, 3)
outputfile.write('Histogram Bins: %s\n' % (bins))
outputfile.write('Bin Frequencies: %s\n' % (frequencies))
outputfile.close()
print time.time() - start_time, "seconds to execute!"