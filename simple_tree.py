import nltk

def sentenceTree(sentence):
	text = nltk.word_tokenize(sentence)
	tagged_text = nltk.pos_tag(text)
	tags = [tup[1] for tup in tagged_text]
	
	simple_grammar = nltk.parse_cfg("""
		S -> NP VP
		PP -> P NP
		NP -> Det N | Det N PP
		VP -> V NP | V PP
		Det -> 'DT'
		N -> 'NN'
		V -> 'VBZ'
		P -> 'PP' | 'IN'
		""")
	parser = nltk.ChartParser(simple_grammar)

	tree = parser.parse(tags)

	print tree