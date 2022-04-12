# Song Popularity and Decade Prediction

Group Members:

Öykü Irmak Hatipoğlu   
Elif Gamze Güliter  
Elif Kurtay  
Atakan Dönmez  
Cansu Moran  

Click [here](https://drive.google.com/drive/folders/1xQ9Wj0LY5du2JYC1NSBrVUxKGqVO9E_D?usp=sharing) to access the data used in the project

In this project, we performed two different classification tasks on song lyrics. First, we classified song lyrics into decades to observe what kind of distinction the song lyrics have in different decades, for example 70s, 80s or 90s. The second classification task we performed was whether that song is popular in a particular decade or not. We used different text vectorization techniques with two models to perform these classification tasks: Recurrent Neural Network(RNN) and Multinomial Naive Bayes model.

RNN is a class of artificial neural networks that is popular in text classification tasks. It
processes sequence input by iterating through the elements and passes the outputs from one timestep to their input on the next timestep. In our project we used RNN with Long Short-Term Memory (LSTM). Naive Bayes is a probabilistic classifier based on applying Bayes’ Theorem with independent assumptions between the features. In our project, we used a Multinomial Naive Bayes classifier.

RNN with the LSTM model achieved 33% accuracy on period classification and 73% accuracy on popularity classification(70s popularity classification) on our test set with the GloVe word vectorization technique whereas it achieved 32% accuracy on period classification and 69% accuracy on popularity classification(90s popularity classification) on our test set with the Word2Vec word vectorization technique. The Multinomial Naive Bayes classifier, on the other hand, achieved approximately 38% accuracy on period classification and 71% on popularity prediction (70s popularity classification).
