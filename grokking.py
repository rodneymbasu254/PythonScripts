import numpy as np
norms = np.sum(weights_0_1 * weights_0_1,axis=1)
norms.resize(norms.shape[0],1)
normed_weights = weights_0_1 * norms
def make_sent_vect(words):
      indices = list(map(lambda x:word2index[x],\
                filter(lambda x:x in word2index,words)))
      return np.mean(normed_weights[indices],axis=0)
reviews2vectors = list()
for review in tokens: 
      reviews2vectors.append(make_sent_vect(review))
reviews2vectors = np.array(reviews2vectors)
def most_similar_reviews(review):
      v = make_sent_vect(review)
      scores = Counter()
      for i,val in enumerate(reviews2vectors.dot(v)):
                   scores[i] = val
      most_similar = list()
      for idx,score in scores.most_common(3):
                          most_similar.append(raw_reviews[idx][0:40])
      return most_similar
most_similar_reviews(['boring','awful'])
['I am amazed at how boring this film',
 'This is truly one of the worst dep',
 'It just seemed to go on and on and']