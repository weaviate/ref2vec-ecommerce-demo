import weaviate

client = weaviate.Client("http://localhost:8080")

query_str="""
{
  Get {
    Product {
    _additional {
      vector
      }
    }
  }
}
"""

vector = client.query.raw(query_str)["data"]["Get"]["Product"][0]["_additional"]["vector"]
print(len(vector))