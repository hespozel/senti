import os
import subprocess
import tempfile
import nbformat


def _notebook_run(path):
    """Execute a notebook via nbconvert and collect output.
       :returns (parsed nb object, execution errors)
    """

    testdir = os.path.dirname(os.path.abspath(__file__))
    print ("Test Dir",testdir)
    dirname, __ = os.path.split(path)

    os.chdir(testdir)
    os.chdir(dirname)
    with tempfile.NamedTemporaryFile(suffix=".ipynb") as fout:
        args = ["jupyter","nbconvert", "--to", "notebook", "--execute",
          "--ExecutePreprocessor.timeout=60",
          "--output", fout.name, path]
    print (args)
    subprocess.check_call(args, stdout=subprocess.DEVNULL)

    #fout.seek(0)
    nb = nbformat.read(fout.name, nbformat.current_nbformat)

    errors = [output for cell in nb.cells if "outputs" in cell
                     for output in cell["outputs"]\
                     if output.output_type == "error"]

    return nb, errors
