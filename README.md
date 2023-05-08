<h1> Welcome to the Ref2Vec eCommerce Demo! </h1>

For more info, check out our blog post announcing ref2vec! - https://weaviate.io/blog/ref2vec-centroid

<h2>Step 1: Download the images!</h2>

Download base64_images for upload - https://drive.google.com/file/d/1TDohvh6vyC6Ugd2NlrfhkAvwPfpjnBg3/view?usp=sharing

Put this folder in `weaviate-init`

Download images for showing the images locally - https://drive.google.com/file/d/1Vp0tg_6_qb1sezf-c-S1lHbmxy5EZ-de/view?usp=sharing

Put this folder in `static`

<h2>Step 2: Install all the requirements:</h2>

Use the `requirements.txt` file to install all packages as follows: 

```bash
python -m pip install -r requirements.txt
```

Optionally, you can accomplish this by creating a seperate conda environment: 

```bash
conda create -n ref2vec python=3.9
conda activate ref2vec
python -m pip install -r requirements.txt
```

<h2>Step 3: Now Initialize Weaviate by running these commands:</h2>

```bash
cd weaviate-init
docker-compose up -d
python3 create-schema.py
python3 upload-data.py
```

<h2>Step 4: Run the app</h2>

Now you are all set!

Navigate out of the `weaviate-init` folder like this and start the FastAPI app!
```bash
cd ..
uvicorn main:app --reload
```

The app is now running on `localhost:8000`
