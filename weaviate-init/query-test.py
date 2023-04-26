import weaviate
import numpy as np

client = weaviate.Client("http://localhost:8080")

labelName = "wp05-gray_back"

query_str = """
{
Get {
  User (
    where: {
      path: ["id"]
      operator: Equal
      valueString: "%s"
    }
  ){
	 _additional {
    vector
    }
  }
 }
}
""" % labelName

results = client.query.raw(query_str)["data"]["Get"]["Product"][0]["_additional"]["vector"]
print(results)