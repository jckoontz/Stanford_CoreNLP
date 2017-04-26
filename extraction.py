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

os.environ['STANFORD_PARSER'] = '//Users//Charles//Desktop//stanford-parser-full-2016-10-31'
os.environ['CLASSPATH'] = '//Users//Charles//Desktop//stanford-parser-full-2016-10-31'

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

#tree = list(parser.raw_parse("Yo he pagado al chico."))[0]
#tree = ParentedTree.convert(tree)
#print(tree)
#tree.pretty_print()



#text = sent_tokenize(text)
#tree = et.parse('input.txt.xml')
#root = tree.getroot()
#print(root.tag, root.attrib)
#rootd = root.find('dependent')
#print(rootd.tag, rootd.attrib)

#with open('inputtxt.xml', 'rt') as f:
    #tree = ElementTree.parse(f)



#for node in tree.iter():
 #   print (node.tag, node.attrib) 

#for child in root:
 #   print(child.tag, child.attrib)

#for elem in page(root): 
 #   dep = page.find('dep').text
  #  print(dep)

#for dep in root.iter('dep'):
 #   dep = dep.find('dep').text
  #  print(dep)
   # print(dependent.attrib)

#for elem in root.findall('governor'):
 #   print (elem.tag, elem.attrib)
#for dependencies in root.iter('dependencies'):
 #   print(dependencies.attrib)
  #  name = dependencies.get('dependencies')
   # print(name)
