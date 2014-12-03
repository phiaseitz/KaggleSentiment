import nltk

def sentenceTree(sentence):
	text = nltk.word_tokenize(sentence)
	#print text
	tagged_text = nltk.pos_tag(text)
	tags = [tup[1] for tup in tagged_text]
	#print tags
	
	'''simple_grammar = nltk.parse_cfg("""
		S -> NP VP
		PP -> P NP
		NP -> Det N | Det N PP
		VP -> V NP | V PP
		Det -> 'DT'
		N -> 'NN'
		V -> 'VBZ'
		P -> 'PP'
		""")'''

	'''simple_grammar = nltk.parse_cfg("""
		G -> NP | Det | V | VP | P | PP | C | VP NP | VP PP | G C G | G P G | VP J
		VP -> NP V
		PP -> P NP
		NP -> 'NN' | 'PRP' | 'NNS' | J NP | Det NP | NP PP | 'WP'
		Det -> 'DT'
		V -> 'VBZ' | 'VB' | 'VBD' | 'VBG' | 'VBN' | 'VBP' | 'VBZ'
		P -> 'IN'
		C -> 'WP' | 'CC'
		J -> 'JJ'
		""")'''

	# Things we're ignoring: gerunds ('VBG')
	simple_grammar = nltk.parse_cfg("""
		G -> Sentence | Clause | Phrase | Fragment | Sentence Punct Sentence | G Punct | Sentence Punct Clause | Clause Punct Clause

		Sentence -> IndClause DepClause | DepClause IndClause | IndClause Punct DepClause | DepClause Punct IndClause | Sentence Punct
		Clause -> IndClause | DepClause | Phrase Phrase
		Phrase -> NounPhrase | AdvPhrase | VerbPhrase | PrepPhrase | GerPhrase | Phrase Punct
		Fragment -> Det | Adj | Adv | Noun | Verb | Prep | Conj | Ger | Pos

		IndClause -> NounPhrase VerbPhrase
		DepClause -> Conj IndClause
		NounPhrase -> Noun | Det NounPhrase | NounPhrase PrepPhrase | NounPhrase GerPhrase | NounPhrase Pos
		AdvPhrase -> Adj Adv | Adv Adj | Adv
		VerbPhrase -> Verb | HelpingVerb VerbPhrase | AdvPhrase VerbPhrase | VerbPhrase AdvPhrase | VerbPhrase PrepPhrase | VerbPhrase Adj | VerbPhrase NounPhrase
		PrepPhrase -> Prep NounPhrase
		GerPhrase -> Ger IndClause | Ger NounPhrase | Ger PrepPhrase

		Det -> 'DT'
		Adj -> 'JJ' | 'JJR' | 'JJS'
		Adv -> 'RB' | 'RBR' | 'RBS'
		Noun -> 'NN' | 'PRP' | 'PRP$' | 'NNS' | Adj Noun | Adj | 'WP' | 'WDT' | 'DT' | Adv | 'NNP' | 'CD' | Verb | Noun Noun
		Verb -> 'VBZ' | 'VB' | 'VBD' | 'VBN' | 'VBP'
		HelpingVerb -> 'MD'
		Prep -> 'IN' | 'RP' | 'TO'
		Conj -> 'WP' | 'CC' | 'IN'
		Ger -> 'VBG'
		Punct -> ',' | '.'
		Pos -> 'POS'
		""")

		# let verbs be nouns & nouns be verbs?

	parser = nltk.ChartParser(simple_grammar)
	try:
		tree = parser.parse(tags)
		if (tree == None):
			raise ValueError("Grammar doesn't include this structure.")
		else:
			pass
			#print "Tagged!"
			print tree
		return 1
	except ValueError, e:
		print e
		print "Can't tag."
		print sentence
		print tags
		return 0


def testParser(train, n):
	good = 0
	printed = 0
	for i in range(n):
		val = sentenceTree(train[i][2])
		good = good + val
		if printed < 10 and val == 0:
			print i
	return float(good)/n

