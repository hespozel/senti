# senti

##  Sentiment Classifier Platform for Sincere/Insincere Questions on Kaggle

The objective of this project was to develop a full stack sentiment classifier that would be used in real life situations.
This project contains a PROTOTYPE containing:the model development , and REST-API that make the model available to other applications
and a simple web application that permits to test the model and the REST-API.
Beeing a PROTOTYPE it still under development and is not intended to use in a production envinroment.

## Web Application

* [Web Application](https://github.com/hespozel/senti/edit/master/webapp)

The objective of this module is to make available to overall users the usage of the Machine Learning developed Model. It is a very simple Web application that allow the creation of a user credention that permits the submmission of questions. This questions will be not be answered !!!! But will be classified as Sincere (closes to o) or Insincere (closes to 1) accordling to the model developed.

The applications is developed in python 3.6 using [Flask](http://flask.pocoo.org/) framework .

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
* [Kaggle Insincere - Question Platform](https://www.kaggle.com/hespozel/testing-platform-choose-and-run/versions)

Also a local automated test was developed to test ipython notebooks( api and model load and run).
* [Model Testing](https://github.com/hespozel/senti/edit/master/tests)

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

3. In a new browser window, use the local http adress to access the application.

http://127.0.0.1:5000

1. WebApp Página Principal.

![Página Principal](https://github.com/hespozel/senti/blob/master/images/tela%20principal.PNG)

2. Web App Página de Registro

![Registro](https://github.com/hespozel/senti/blob/master/images/tela%20registro.PNG?raw=true)

3. Web App Página de Login

![Login](https://github.com/hespozel/senti/blob/master/images/tela%20login.PNG?raw=true)

4. Web App Página Principal - Usuário logado

![Principal com Usuário](https://github.com/hespozel/senti/blob/master/images/tela%20inicial%20usuario%20logado.PNG?raw=true)

5. Web App Página de Submissão e Classificação das Perguntas
![Teste](https://github.com/hespozel/senti/blob/master/images/tela%20de%20testes%20da%20api.PNG)
