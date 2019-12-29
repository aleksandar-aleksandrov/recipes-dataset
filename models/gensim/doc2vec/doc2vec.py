from pathlib import Path
from gensim.models.doc2vec import Doc2Vec, TaggedDocument
from nltk.tokenize import word_tokenize
import nltk

nltk.download('punkt')

main_path = Path(__file__).absolute().parents[3].joinpath('data/processed/docs')
common_texts = []

for i in range(10):
    new_path = main_path.joinpath(f'doc{i}/doc{i}.txt')
    with new_path.open('r+') as f:
        common_texts.append(f.read())

print(common_texts)

documents = [TaggedDocument(doc, [i]) for i, doc in enumerate(common_texts)]

max_epochs = 10
vec_size = 20
alpha = 0.025

model = Doc2Vec(size=vec_size,
                alpha=alpha,
                min_alpha=0.00025,
                min_count=1,
                dm=1)

model.build_vocab(documents)

for epoch in range(max_epochs):
    print('iteration {0}'.format(epoch))
    model.train(documents,
                total_examples=model.corpus_count,
                epochs=model.iter)
    # decrease the learning rate
    model.alpha -= 0.0002
    # fix the learning rate, no decay
    model.min_alpha = model.alpha

model.save("d2v.model")
print(model.vocabulary.raw_vocab)
#l = model.wv.most_similar_cosmul(positive=["beans", "ham"])
#print(l)

test_data = word_tokenize("I love chatbots".lower())
print(test_data)
v1 = model.infer_vector(test_data)
print("V1_infer", v1)
sims = model.docvecs.most_similar([v1], topn=len(model.docvecs))
print(sims)

for label, index in [('MOST', 0), ('MEDIAN', len(sims)//2), ('LEAST', len(sims) - 1)]:
    print(u'%s %s: «%s»\n' % (label, sims[index], ' '.join(documents[sims[index][0]].words)))
