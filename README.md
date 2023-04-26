<h1> Welcome to the Ref2Vec eCommerce Demo! </h1>

Step 1: Initialize Weaviate by running these commands:

```bash
cd weaviate-init
docker-compose up -d
python3 create-schema.py
python3 upload-data.py
```

Step 2: Run the app

Now you are all set!

Navigate out of the `weaviate-init` folder like this and start the FastAPI app!
```bash
cd ..
uvicorn main:app --reload
```

The app is now running on `localhost:8000`
