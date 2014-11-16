import pickle


# TSV handlers
def readTsv(tsvSource):
	f = open(tsvSource, 'r')
	s = f.read()
	f.close()

	# parse
	lines = s.split('\n')
	
	for i,line in enumerate(lines):
		lines[i] = line.split('\t')

	return lines


# Pickle handlers
def makePickle(tsvSource, pickleTarget):
	parsed = readTsv(tsvSource)
	pickle.dump(parsed, open(pickleTarget, 'w'))


def readPickle(pickleSource):
	return pickle.load(open(pickleSource, 'r'))


# Specific train/test data loaders
def loadTrain():
	return readPickle('pickles/train.p')

def loadTest():
	return readPickle('pickles/test.p')