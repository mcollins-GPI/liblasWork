from liblas import file
import math
import numpy
import matplotlib.pyplot as plt

inputfile		= file.File('L109633_EB.las', mode='r')
outputfile		= open('outputfile.txt', 'w')
countIntervals	= range(0, 1000000000, 100000)
fileLength		= len(inputfile)

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

	
# masterClusterList = []
# for key, value in sortByIntensity(0, 2).iteritems():
	# # outputfile.write('%s, %s\n' % (key, value))
	# clusters = []
	# indicesToRemove = []
	# comparatorList = [] # create a comparison list
	# comparatorList.append(value.pop()) # take first comparison value
	# while len(value) > 0: # if there is only one value, it will never enter this loop
		# for comparator in comparatorList:
			# for index, position in enumerate(value): # iterate through the list to see if anything matches initial value
				# if math.sqrt((comparator[0] - position[0])**2 + (comparator[1] - position[1])**2 + (comparator[2] - position[2])**2) < 0.08333:
					# indicesToRemove.insert(0, index)
		# if len(indicesToRemove) > 0: # points were found close to the existing set
			# indicesToRemove = set(indicesToRemove) # remove duplicates
			# indicesToRemove = list(indicesToRemove) # remove duplicates
			# indicesToRemove.sort() # sort ascending
			# indicesToRemove.reverse() # sort descending
			# for indexToRemove in indicesToRemove:
				# comparatorList.append(value[indexToRemove])
				# del value[indexToRemove]
		# else: # no points were found close to the comparators
			# if len(comparatorList) > 5:
				# clusters.append(comparatorList)
			# comparatorList = [] # clear the comparison list
			# comparatorList.append(value.pop()) # take the next comparison value
		# indicesToRemove = []
	# if len(clusters) > 0:
		# masterClusterList.append(clusters)
		# outputfile.write('%s, %s\n' % (key, clusters))

# for clusters in masterClusterList:
	# for cluster in clusters:
		# print cluster
					
					
					
	# # destructibleList = value
	# # groupings = []
	# # while len(destructibleList) > 0:
		# # comparator = destructibleList.pop() # Grab the last value off the list.
		# # closePoints = [comparator]
		# # indicesToRemove = []
		# # while len(closePoints) > 0:
			# # foundPoints = []
			# # for point in closePoints:
				# # for index, position in enumerate(destructibleList): # Compare all remaining points to see if they are close
					# # if math.sqrt((comparator[0] - position[0])**2 + (comparator[1] - position[1])**2 + (comparator[2] - position[2])**2) < 0.08333:
						# # foundPoints.append(position)
						# # del destructibleList[indexToRemove]
			# # if len(foundPoints) > 0:
				# # closePoints.append(foundPoints)
			# # else:
				# # groupings.append(closePoints)
				# # closePoints = []
	# # if len(groupings) > 0:
		# # outputfile.write('%s, %s\n' % (key, groupings))

# getSubSet(0, 1041077.388, 2840809.409, 1041282.639, 2841084.66) # Highland Road & Route 6 SB
# getSubSet(0, 1041858.076, 2841306.202, 1041881.986, 2841330.932) # Highland Road & Route 6 NB
things, stuff = generateIntensityHistogram(100000, 1000, 2)

outputfile.close()