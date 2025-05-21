import faiss
import numpy as np

def build_faiss_index(vectors):
    dim = vectors.shape[1]
    index = faiss.IndexFlatL2(dim)
    index.add(vectors)
    return index

def search(index, query_vector, k=5):
    D, I = index.search(query_vector, k)
    return I

if __name__ == "__main__":
    vectors = np.random.rand(100, 128).astype('float32')
    index = build_faiss_index(vectors)
    query = np.random.rand(1, 128).astype('float32')
    print(search(index, query))
