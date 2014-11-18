import opinion_lexicon_English.pos_neg_lists as pnl
import data.dataHandler as dataHandler
import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets, linear_model, cross_validation

def main():
	pos_words = pnl.make_words_list("opinion_lexicon_English/positive-words.txt")
	neg_words = pnl.make_words_list("opinion_lexicon_English/negative-words.txt")

	data = dataHandler.readPickle("data/pickles/train.p")

	data = data[1:-1]
	for index,line in enumerate(data):
		sentence = line[2]
		data[index].insert(3,pnl.count_sentiment(sentence, pos_words, neg_words))
		#print sentence, pnl.count_sentiment(sentence, pos_words, neg_words)

	calculated = [item[3] for item in data]
	actual = [item[4] for item in data]

	X = np.array(calculated, dtype = 'int_')
	Ones = np.ones((X.shape[0],))
	X = np.column_stack((Ones,X))
	#X = np.insert(X,0,1,axis=0)
	y = np.array(actual, dtype = 'int_')

	print X.shape
	print y.shape

	Xtrain, Xtest, ytrain, ytest = cross_validation.train_test_split(X,y, test_size = 0.33, random_state = 42)

	print Xtrain

	regr = linear_model.LinearRegression()
	regr.fit(Xtrain, ytrain)

	print('Coefficients: \n', regr.coef_)

	print("Residual sum of squares: %.2f" % np.mean((regr.predict(Xtest) - ytest) ** 2))
	# Explained variance score: 1 is perfect prediction
	print('Variance score: %.2f' % regr.score(Xtest, ytest))

if __name__ == "__main__":
	main()