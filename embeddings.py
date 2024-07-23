import torch
import torchvision



from sentence_transformers import SentenceTransformer 

model = SentenceTransformer('sentence-transformers/stsb-bert-base')

def sentencembd(veru):
    embeddings = model.encode(veru)
    return embeddings

