<h1> Welcome to the Ref2Vec eCommerce Demo! </h1>

Step 1: Download the images!

Download base64_images for upload - https://drive.google.com/file/d/1TDohvh6vyC6Ugd2NlrfhkAvwPfpjnBg3/view?usp=sharing

Put this folder in `weaviate-init`

Download images for showing the images locally - https://drive.google.com/file/d/1Vp0tg_6_qb1sezf-c-S1lHbmxy5EZ-de/view?usp=sharing

Put this folder in `static`

Step 2: Now Initialize Weaviate by running these commands:

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
