To run the scripts:

If you are running on your device and not the Google Colab, make sure you import all the required packages.

In RNN scripts, find the line:
train = pd.read_csv('BALANCED.csv') # change to the dataset file
and change the file name/path to the dataset you want to use. 


If you are running RNN GloVe scripts for the first time, uncomment:

#!wget http://nlp.stanford.edu/data/glove.6B.zip 
#!unzip glove*.zip

And run these commands. Running these commands once should be enough, therefore recomment these lines after you run them.


If you are running RNN Word2Vec scripts for the first time, uncomment:

#wv = api.load('word2vec-google-news-300')
#wv.save_word2vec_format('model.bin', binary=True)

And run these commands. Running these commands once should be enough, therefore recomment 