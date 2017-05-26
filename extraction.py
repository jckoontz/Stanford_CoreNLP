from nltk.parse import stanford
from nltk.parse.stanford import StanfordParser
from nltk.tree import ParentedTree, Tree
from nltk import word_tokenize
from nltk import sent_tokenize
import json
import os
import operator
import sys
import codecs

os.environ['STANFORD_PARSER'] = 'Add Path'
os.environ['CLASSPATH'] = 'Add Path'

parser = StanfordParser()

with open('nytimes.txt') as f: 
    text = f.read().decode('utf-8')

text = sent_tokenize(text)
print(text)

sent_list = []
for sent in text:
    sent_list.append(sent)
    print(sent)
    print("---" * 30)

for sent in sent_list: 
    sent = list(parser.raw_parse(sent))[0]
    sent = ParentedTree.convert(sent)
    print(sent)

