import weaviate
import json
import argparse

client = weaviate.Client("http://localhost:8080")

result = client.backup.restore(
    backup_id="magento-data",
    backend='filesystem',
    wait_for_completion=True
)

print(json.dumps(result, indent=4))