from gensim.models import word2vec
import logging
import gensim
import deal_file

texts = deal_file.get_content("trn")

# 小语料库可以自行构建相应的sentences不需要创立新文件[[dog,cat],[yellow,black]]
# sentences = []
# for label in texts:
#     content = label.split()
#     sentences += [content]
    # print(content)
# print(sentences)

# 大量数据通过Text8Corpus等三种语料库格式构建，需要创建相应的总文件
content = ''.join(texts)
deal_file.creat_file(content)
sentences = word2vec.Text8Corpus('train_txt')#按照该语料库格式处理类似切词处理分割好中文则不行
# print(sentences)

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
model = word2vec.Word2Vec(sentences, sg=1, size=20,  window=3,  min_count=1,  negative=3, sample=0.001, hs=1, workers=4)
model.save('text.model')
# print(model['man'])
# new_model = gensim.models.Word2Vec.load("text82.model")
# sim=new_model.wv.most_similar(positive=['greek', 'belief'], negative=['man'], topn=1)
# print(new_model['greek'])
