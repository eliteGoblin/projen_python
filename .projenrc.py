from projen.python import PythonProject

project = PythonProject(
    author_email="frank.sun@art.com.au",
    author_name="Frank Sun",
    module_name="projen_python",
    name="projen_python",
    version="0.1.0",
)

project.synth()