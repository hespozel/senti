# senti Notebooks

##  Sentiment Classifier Platform for Sincere/Insincere Questions on Kaggle

The objective of this project was to develop a full stack sentiment classifier that would be used in real life situations.
This project contains a PROTOTYPE containing:the model development , and REST-API that make the model available to other applications
and a simple web application that permits to test the model and the REST-API.
Beeing a PROTOTYPE it still under development and is not intended to use in a production envinroment.

All project was based in a Kaggle Competition - Quora Insincere Questions Classification. This is a kernel only competition, that only allows the development code under Kaggle´s kernel environment.

* [Kaggle Competion](https://www.kaggle.com/c/quora-insincere-questions-classification)
__

## Model Development

* [Model Development Kaggle](https://www.kaggle.com/hespozel/testing-platform-choose-and-run/versions)

The model development was all developed under Kaggle´s kernel environment. This was the most challenge and time consuming effort. The model development was created to help me with real data for my master at PUC.  
The objective of my master is to evaluate different deep learning approaches to process natural language in sentiment analysys.
This module was designed to run multiple deep learning architectures/models , over different evaluations methods with different embeddings and fully parametrizable, allowing you to record and compare results

Just fork this kernel and play around.You can select:

1) Run one or multiple models from 19 models implemented. Each Model has a unique architecture
2) For each model select the rate between train and validation sets.
3) Select normal or Stratified k-fold implementation. Select the k splits.
4) Select evaluataion methods. Stantard Fit, Manual Controlled Fits, Early Stop, CLR
5) Select batch size, epochs etc.
6) Select what Embedding to use. Use one, the combination of one or more, or the concatenation of one or more.
7) For each model define the number of hidden layers, metrics, optimization etc.
8) Pre process or not the dataset with many options to select.

At the end one table is generated with the results for each model and the blended result for all models

https://github.com/hespozel/senti/blob/master/notebook/images/modelresults.PNG?raw=true
