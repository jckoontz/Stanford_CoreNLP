import io
import os
import sys
import gensim.models.word2vec as w2v 
from sklearn.decomposition import PCA
from sklearn.manifold import TSNE 	
from matplotlib import pyplot

'''
Program to train word embeddings using Gensim's word2vec
Ideal dimension size for words is 200-300, for character embeddings 50+ 
'''
class WordEmbeddings: 

	def read_file(self, txt): 	
		try: 
			f = io.open(txt, 'r', encoding='utf-8')
		except FileNotFoundError: 
			print('File not found')
		return f

	def sentence_tokenizer(self, file):
	    items = [line for line in file]
	    return items 

	def word_list(self, sentences): 
		return [sentence.split() for sentence in sentences]

	def word_2_vec(self, wordlist): 
	    token_count = sum([len(line) for line in wordlist])
	    print("The  corpus contains {0:,} tokens".format(token_count))
	    Embeddings = w2v.Word2Vec(wordlist, min_count=2, size=300, window=1, workers=15, sample=0.0001)
	    print("Embeddings vocabulary length:", len(Embeddings.wv.vocab))
	    if not os.path.exists("trained"):
	        os.makedirs("trained")
	    Embeddings.save(os.path.join("trained", "Spanglish.w2v"))

def main(): 
	we = WordEmbeddings()
	f = we.read_file('Spanglish_TextOnly.txt')
	sentences = we.sentence_tokenizer(f)
	wordlist = we.word_list(sentences)
	we.word_2_vec(wordlist)
	Embeddings = w2v.Word2Vec.load(os.path.join("trained", "Spanglish.w2v"))
	X = Embeddings[Embeddings.wv.vocab]
	pca = PCA(n_components=2)
	result = pca.fit_transform(X)
	pyplot.scatter(result[:, 0], result[:, 1])
	words = list(Embeddings.wv.vocab)
	for i, word in enumerate(words):
		pyplot.annotate(word, xy=(result[i, 0], result[i, 1]))
	pyplot.show()

if __name__ == '__main__':
	main()
