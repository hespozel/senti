# senti

##  Sentiment Classifier Platform for Sincere/Insincere Questions on Kaggle

The objective of this project was to develop a full stack sentiment classifier that would be used in real life situations.
This project contains a PROTOTYPE containing:the model development , and REST-API that make the model available to other applications
and a simple web application that permits to test the model and the REST-API.
Beeing a PROTOTYPE it still under development and is not intended to use in a production envinroment.

All project was based in a Kaggle Competition - Quora Insincere Questions Classification. This is a kernel only competition, that only allows the development code under Kaggle´s kernel environment.

* [Kaggle Competion](https://www.kaggle.com/c/quora-insincere-questions-classification)
* [Model Development](https://github.com/hespozel/senti/edit/master/notebook)
* [REST API](https://github.com/hespozel/senti/edit/master/api)
* [Web Application](https://github.com/hespozel/senti/edit/master/webapp)
* [Model Testing](https://github.com/hespozel/senti/edit/master/test)
* [Web Application and API Testing](https://github.com/hespozel/senti/edit/master/webapp/tests)
___

## Model Development

* [Model Development Kaggle](https://www.kaggle.com/hespozel/testing-platform-choose-and-run/versions)
* [Model Development Local](https://github.com/hespozel/senti/edit/master/notebook)

The model development was all developed under Kaggle´s kernel environment. This was the most challenge and time consuming effort. The model development was created to help me with real data for my master at PUC.  The objective of my master is to evaluate different deep learning approaches to process natural language in sentiment analysys.

This module was designed to run multiple deep learning architectures/models , over different evaluations methods with different embeddings and fully parametrizable, allowing you to record and compare results

## REST-API

* [REST API](https://github.com/hespozel/senti/edit/master/api)

This objective of this module was to make available developed machine-learning models. This api allows the consumption of complex machine learning systems in a simple way. This module uses a downloaded binary ML model developed in a Kaggle kernel.   

## Web Application

* [Web Application](https://github.com/hespozel/senti/edit/master/webapp)

The objective of this module is to make available to overall users the usage of the Machine Learning developed Model. It is a very simple Web application that allow the creation of a user credention that permits the submmission of questions. This questions will be not be answered !!!! But will be classified as Sincere (closes to o) or Insincere (closes to 1) accordling to the model developed.

The applications is developed in python 33.6 using [Flask]http://flask.pocoo.org/ microframework .

## File Structure
* senti/api
  * api.py: Flask API application
  * textproc.py: utility to prepare/tokenize the questions to be submitted to api
* senti/model
   * model.hdf5: 
     * Machine learning model saved in Kaggles Kernel - 
     * Run senti/notebook/model_development.ipynb in Kaggle and Download it from output tab (easier)
     * or build a local environment to run this notebook
   * tokenizer.pickle:
     * Run senti/notebook/model_development.ipynb in Kaggle as a kernel and download it from output tab
* senti/test : *.py
  * automated tests to run ipynb notebooks to verify api and model load/run 
* senti/input:
   * train and test csv files from Kaggle
* senti/ notebook:
   * model_development.ipynb - create and save the model/tokenizer to be used in api
   * model_load-run.ipynb - test load and run the model created by model_development.ipynb
   * rest_api - tests the api running

## Testing Model Development

Lastest versions of the model development notebooks are available under kernels kaggle and can be access here:
*[Kaggle Insincere - Question Platform](https://www.kaggle.com/hespozel/testing-platform-choose-and-run/versions)

Also a local automated test was developed to test ipython notebooks( api and model load and run).
*[Model Testing](https://github.com/hespozel/senti/edit/master/tests)

## Testing Web Applications and API Testing

* [Web Application and API Testing](https://github.com/hespozel/senti/edit/master/webapp/tests)

* Unit and Functional Tests were developed to test the Web Application. The [pytest](https://docs.pytest.org/en/latest/) platform was used to create the tests.

## Testing the API
1. Activate virtual environment created
```bash
source vsenti/bin/activate
```
2. Run the Flask API locally for testing. Go to directory with `api.py`.
```bash
python3 senti/api/api.py
```
3. In a new terminal window, use HTTPie to make a GET request at the URL of the API.

```bash
http http://127.0.0.1:5001/?query=="Dos this question is sincere or unsincere ?"
```
4. Example of successful output.

```bash
HTTP/1.0 200 OK
Content-Length: 57
Content-Type: application/json
Date: Wed, 12 Dec 2018 11:23:27 GMT
Server: Werkzeug/0.14.1 Python/3.6.7

{
    "confidence": 0.038,
    "prediction": "Sincere"

```
## Testing WebApp

0. Activate the API -Steps above.

1. Activate virtual environment created
```bash
source vsenti/bin/activate
```
2. Run the Webapp locally for testing. Go to directory with `webapp`.
```bash
./runapi.sh
```
3. In a new browsere window, use the local http adress to access the application.

http://127.0.0.1:5000

4. Example of successful output.

![Webapp Main Page](https://github.com/hespozel/senti/blob/master/images/tela%20principal.PNG)
