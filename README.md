Weaviate Virtual Store!

First Initialize Weaviate by running these commands:

```bash
cd weaviate-init
docker-compose up -d
python3 create-schema.py
python3 upload-data.py
```

Now you are al set!

Run the app with:
`uvicorn main:app --reload`

And visualize on `localhost:8000`