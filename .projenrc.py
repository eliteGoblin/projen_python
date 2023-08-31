from projen.python import PythonProject

project = PythonProject(
    author_email="frank.sun@art.com.au",
    author_name="Frank Sun",
    module_name="projen_python",
    name="projen_python",
    version="0.1.0",
    deps=["boto3", "typer", "python_dotenv", "pydantic"],
    dev_deps=[
        "black",
        "ipdb",
        "isort",
        "mypy",
        "pycodestyle",
        "pytest",
        "pytest_cov",
        "pytest_randomly",
        "tox",
        "twine",
    ],
)

project.synth()
