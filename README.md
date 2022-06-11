# Spend Classifier POC using TheyBuyForYou data

Comparison of SVM, LSTM and Transformer-based classifier based on data from TheyBuyForYou.

See https://theybuyforyou.eu/ for background on TheyBuyForYou and http://data.tbfy.eu/ for information on the Knowledge Graph (KG) data that was created as part of TheyBuyForYou. The code and model in this repo are based on this TheyBuyForYou data.

This repo contains the following notebooks:
1. `1-prepare-tbfy-data`: Shows the code for preparing data from the raw Zenodo JSON dump (available from https://zenodo.org/record/5546616#.YXMoOZvTVH4). You will need to download the data from Zenodo if you want to replicate this step locally. You do not need to run this locally. The data has already been extracted from the JSON dump.
2. `2-prepare-train-test-split`: Convert the extracted data into one train/test set so that each test can easily use exactly the same source data
3. `3.1-svm-train-model`: Create model using Support Vector Machine (actually Scikit-Learn's LinearSVC: https://scikit-learn.org/stable/modules/generated/sklearn.svm.SVC.html)
4. `3.2-bilstm-train-model`: Create model using a Bidirectional LSTM (using Keras: https://keras.io/examples/nlp/bidirectional_lstm_imdb/)
5. `3.3-transformers-train-(fine-tune)-model`: Fine tune a model based on `distilbert-base-uncased` https://huggingface.co/distilbert-base-uncased with Huggingface Transformers
3. `4-test-tbfy-models`: Qualitative comparisons of the trained models on different input text


## Results

### Training/Validation Results

| Model Architecture| Duration | Validation Accuracy |GPU RAM|
|-------|----------|----------|-------|
|LinearSVC|0:02:18.461116|0.6339677891654466|n/a|
|Bi-LSTM|2:02:48.193593|0.7137|15829MiB|
|Transformer|8:47:47.526466|0.782414|11129MiB|

LinearSVC finished after 56 iterations, so more training would not help this one.

### Qualtitative tests

- **mobile app**: All 3 approaches did well
- **mobile billboard**: Transformer picked the most likely category. Others did not but, equally, had low confidence scores so in a production system they would probably have been a 'no match'
- **mobile office**: None of the 3 options did particularly well (with more training, it's likely that both the Bi-LTSM and the Transformer would get a better result, but LinearSVC had gone as far as it could)
- **mobile phone**: With the precise spelling of 'mobile phones' (plural) all 3 came up with a credible result. With slight spelling changes only Transformers kept producing a consistent result
- Examples using longer text. Curiously for some of these attempts the LinearSVC performed well. However overall the Transformer produces more consistent results as the text changes.

### Conclusion

Transformers takes a lot longer to fine-tune but the results are more consistent for this kind of use case.
