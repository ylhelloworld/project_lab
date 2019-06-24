from collections import defaultdict
from gensim import corpora
from gensim import models
from gensim.models import Word2Vec

raw_corpus = ["Human machine interface for lab abc computer applications",
             "A survey of user opinion of computer system response time",
             "The EPS user interface management system",
             "System and human system engineering testing of EPS",              
             "Relation of user perceived response time to error measurement",
             "The generation of random binary unordered trees",
             "The intersection graph of paths in trees",
             "Graph minors IV Widths of trees and well quasi ordering",
             "Graph minors A survey"]
 
##移除虚词 
stoplist = set('for a of the and to in'.split(' '))
texts = [[word for word in document.lower().split() if word not in stoplist]
          for document in raw_corpus]

 
#移除只出现一次的单词
frequency = defaultdict(int)
for text in texts:
    for token in text:
        frequency[token] += 1

precessed_corpus = [[token for token in text if frequency[token] > 1] for text in texts]

print(precessed_corpus)

#向量化
dictionary = corpora.Dictionary(precessed_corpus)
print(dictionary)
print(dictionary.token2id)

#对“human computer interaction”向量化,结果（ID，出现的次数）
new_doc = "human computer interaction"
new_vec = dictionary.doc2bow(new_doc.lower().split())
print(new_vec)

## 统计每一个单词
bow_corpus = [dictionary.doc2bow(text) for text in precessed_corpus]
print(bow_corpus)

## TF-IDF（term frequency–inverse document frequency） 一个词在文件中的重要程度
## TF词频(Term Frequency)，IDF逆向文件频率(Inverse Document Frequency)
tfidf = models.TfidfModel(bow_corpus)
string = "system minors"
string_bow = dictionary.doc2bow(string.lower().split())
string_tfidf = tfidf[string_bow]
print(string_bow)
print(string_tfidf)


##计算相似度
#word2vec_model = Word2Vec.load('data/model/word2vec_gensim')
#word2vec_model.most_similar('woman')

vec=Word2Vec(precessed_corpus, min_count=1)
sim=vec.most_similar("human")
print(sim)
print("ok")