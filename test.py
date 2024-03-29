from gensim.models import word2vec
import logging
import gensim

model = gensim.models.Word2Vec.load('text.model')
#输出词向量
print(model.wv['sets'])
#输出最相关的词
res = model.wv.most_similar("economy",topn=10)
for item in res:
    print(item[0],item[1])
#输出两个词的相似度
sim = model.wv.similarity("economy","according")
print(sim)