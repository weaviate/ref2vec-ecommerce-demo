import weaviate
import json
import argparse

w1 = weaviate.Client("http://localhost:8080")

result = w1.backup.create(
    backup_id="magento-data",
    backend='filesystem',
)

print(json.dumps(result, indent=4))