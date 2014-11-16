def make_words_list(filename):
	f = open(filename, 'r')
	words = []
	while 1:
		line = f.readline()
		if not line:
			break
		if line[0] == ";":
			continue
		else:
			words.append(line[:-1])
	return words
		
if __name__ == "__main__":
	pos_words = make_words_list("positive-words.txt")
	neg_words = make_words_list("negative-words.txt")
	print pos_words