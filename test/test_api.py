from  notebookrun import _notebook_run



def test_restapi():
    nb, errors = _notebook_run('../notebook/rest_api.ipynb')
    assert errors == []


