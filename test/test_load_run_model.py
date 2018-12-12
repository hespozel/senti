from notebookrun import _notebook_run


def test_load_run_model():
    nb, errors = _notebook_run('../notebook/model_load-run.ipynb')
    assert errors == []
