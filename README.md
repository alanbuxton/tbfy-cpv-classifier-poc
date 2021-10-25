# Spend Classifier POC using TheyBuyForYou data

Simple transformer-based classifier proof of concept based on data from TheyBuyForYou.

See https://theybuyforyou.eu/ for background on TheyBuyForYou and http://data.tbfy.eu/ for information on the Knowledge Graph (KG) data that was created as part of TheyBuyForYou. The code and model in this repo are based on this TheyBuyForYou data.

This repo contains 3 jupyter notebooks:
1. `1-prepare-tbfy-data`: Shows the code for preparing data from the raw Zenodo JSON dump (available from https://zenodo.org/record/5546616#.YXMoOZvTVH4). You will need to download the data from Zenodo if you want to replicate this step locally.
2. `2-fine-tune-tbfy-classifier`: Fine-tunes a base Distilbert model using the data prepared in step 1. Running this needs access to GPU.
3. `3-test-tbfy-model`: Run the fine-tuned model locally. This runs the existing model, though the model file itself is not included in the github repo as it is 257Mb in size (Github's limit is 100Mb)
