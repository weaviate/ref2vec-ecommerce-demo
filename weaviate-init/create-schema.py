import weaviate

client = weaviate.Client("http://localhost:8080")

schema = {
    "classes": [
    {
        "class": "Product",
        "description": "A product.",
        "moduleConfig": {
            "multi2vec-clip": {
                "imageFields": [
                    "image"
                ]
            }
        },
        "properties": [
            {
                "dataType": ["blob"],
                "name": "image",
                "description": "A product.",
            },
            {
                "dataType": ["text"],
                "moduleConfig": {
                    "multi2vec-clip": {
                        "skip": "True"
                    }
                },
                "name": "description",
                "description": "A description of the product.",
            },
            {
                "dataType": ["text"],
                "moduleConfig": {
                    "multi2vec-clip": {
                        "skip": "True"
                    }
                },
                "name": "imagePath",
                "description": "A product.",
            },
            {
                "dataType": ["text"],
                "moduleConfig": {
                    "multi2vec-clip": {
                        "skip": "True"
                    }
                },
                "name": "sku",
                "description": "A product.",
            },
            {
                "dataType": ["text"],
                "moduleConfig": {
                    "multi2vec-clip": {
                        "skip": "True"
                    }
                },
                "name": "category",
                "description": "A product category"
            },
            {
                "dataType": ["int"],
                "name": "price",
                "description": "A product.",
            },
            {
                "dataType": ["int"],
                "name": "qty",
                "description": "A product.",
            },
            {
                "dataType": ["int"],
                "name": "index",
                "description": "A product.",
            }
        ],
        "vectorIndexType": "hnsw",
        "vectorizer": "multi2vec-clip"
    },
    {
        "class": "User",
        "description": "A user of the platform.",
        "properties": [
            {
                "name": "sessionNumber",
                "description": "Deprecate soon.",
                "dataType": ["int"]
            },
            {
                "name": "likedItem",
                "description": "A product.",
                "dataType": ["Product"]
            }
        ],
        "moduleConfig": {
            "ref2vec-centroid": {
                "referenceProperties": ["likedItem"]
            }
        },
        "vectorizer": "ref2vec-centroid"
    }
]}

client.schema.create(schema)
