import io

"""Utility class to build language models, namely character ngrams"""

class LanguageModel:
    
     def read_file(self, txt):
         try:
             f = io.open(txt, 'r', encoding='utf-8')
         except FileNotFoundError:
             print('File not found')
         return f

     """Tokenizes space delimited sentences of format: Instance Label
     @Returns: a list of tokenized sentences
     @Params: text file in abovementioned format
     """
     def sentence_tokenizer(self, txt): 
          sentences = [line.split() for line in txt]
          i = 0
          x = []
          y = []
          for i in range(len(sentences)): 
               x.append(sentences[i][0])
               y.append(sentences[i][1])
               i += 1
          x = [line.lower() for line in x]
          return x

     """Generate character bigrams 
     @Returns: List of character bigrams
     @Params: list of sentence or word tokens"""
     def ngram(text,grams):  
          model=[]  
          count=0  
          for token in text[:len(x)-grams+1]:  
               model.append(text[count:count+grams])  
               count=count+1  
          return model

def main(): 
     ng = LanguageModel()
     f = ng.read_file("Data/Spanglish.txt")
     sentences = ng.sentence_tokenizer(f)
     #for sent in sentences: 
      #    print(sent)
    # bigrams = ng.bigram(sentences)
     ngrams_clean = []
     bigrams = []
     for i in range(len(sentences)): 
          ngrams_clean.append(ng.bigram(sentences[i], 2))
          st = " ".join(ngrams_clean[i])
          bigrams.append(st) 
     for bg in bigrams: 
          print(bg)

if __name__ == "__main__":
     main()

        
