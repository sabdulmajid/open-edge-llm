import qdrant_client
from qdrant_client.models import PointStruct

client = qdrant_client.QdrantClient(':memory:')

# Example: insert a vector
def insert_vector(collection_name, vector, payload):
    client.upsert(
        collection_name=collection_name,
        points=[PointStruct(id=1, vector=vector, payload=payload)]
    )

if __name__ == "__main__":
    insert_vector('test_collection', [0.1, 0.2, 0.3], {'meta': 'example'})
