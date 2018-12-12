# Sentiment Classifier Deployed as a REST API using Flask

* [Flask Restful Documentation]()
* [HTTPie Documentation](https://httpie.org/doc)
* [Data Source: Kaggle](https://www.kaggle.com/c/quora-insincere-questions-classification/data)
* [This code api.py](https://github.com/hespozel/senti/edit/master/api)
___

## Environment and steps to run api
1. Start a virtual environment and install requirements
2. Download binary model created in the competition kernel 
3. Download tokenizer model to code the submmited questions
4. Run "python3 api.py" which is the API application that will be deployed
5. Test the API


## File Structure
* senti/api
  * api.py: Flask API application
  * textproc.py: utility to prepare/tokenize the questions to be submmited to api
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


