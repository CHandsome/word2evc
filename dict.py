from gensim.models import word2vec
import logging
import gensim
import deal_file

texts = deal_file.get_content("trn")
# wath = deal_file.clear_comment(wath)
# print(wath)
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
content = ''.join(texts)
deal_file.creat_file(content)
# print(content)
sentences = word2vec.Text8Corpus('train_txt')
# print(sentences)
model = word2vec.Word2Vec(sentences, sg=1, size=20,  window=3,  min_count=1,  negative=3, sample=0.001, hs=1, workers=4)
model.save('text.model')
# print(model['man'])
# new_model = gensim.models.Word2Vec.load("text82.model")
# sim=new_model.wv.most_similar(positive=['greek', 'belief'], negative=['man'], topn=1)
# print(new_model['greek'])
