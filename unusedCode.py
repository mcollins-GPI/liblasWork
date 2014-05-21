		# for variable in vars():
			# if variable in memoryCheck.keys():
				# if len(memoryCheck[variable]) == 1:
					# memoryCheck[variable].append(sys.getsizeof(variable))
				# else:
					# memoryCheck[variable][1] = sys.getsizeof(variable)
			# else:
				# memoryCheck[variable] = [sys.getsizeof(variable)]
	# for key, values in memoryCheck.iteritems():
		# outputfile.write('%s, %s\n' % (key, values))
		
		
# intensities = zip(*[inputfile[row] for row in range(0, 100)])
# weights, pos = zip(*[map(float,d.split()) for d in data.strip().splitlines()])
	
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
# things, stuff = generateIntensityHistogram(100000, 1000, 2)