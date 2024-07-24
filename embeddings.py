import torch
import torchvision
from sklearn.metrics.pairwise import cosine_similarity
from dbupdate import embdcompare



from sentence_transformers import SentenceTransformer 

model = SentenceTransformer('sentence-transformers/stsb-bert-base')

def sentencembd(veru):
    embeddings = model.encode(veru)
    #print(embeddings)
    return embeddings







