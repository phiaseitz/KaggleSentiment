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

def count_sentiment(sentence, pos_words, neg_words):
	inv = ["not", "lack of"]
	plus = ["really","very","incredibly","ridiculously","fairly"]
	words = sentence.split()
	inv_on = 1
	count = 0
	plus_word = 0
	for word in words:
		if word in inv:
			inv_on = -1*inv_on
		elif word in plus:
			plus_word = 1
		elif word in pos_words:
			count += inv_on + plus_word
			plus_word = 0
		elif word in neg_words:
			count -= inv_on + plus_word
			plus_word = 0
	return count
		
if __name__ == "__main__":
	pos_words = make_words_list("positive-words.txt")
	neg_words = make_words_list("negative-words.txt")
	sentences = ["the quick brown fox jumped over the lazy dog",
				 "this movie was terrible",
				 "I really liked the acting style",
				 "Do not see this movie",
				 "It was not bad"]
	for sentence in sentences:
		print sentence, count_sentiment(sentence, pos_words, neg_words)