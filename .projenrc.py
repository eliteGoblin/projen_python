from projen.python import PythonProject

project = PythonProject(
    author_email="frank.sun@art.com.au",
    author_name="Frank Sun",
    module_name="projen_python",
    name="projen_python",
    version="0.1.0",
    deps=["boto3==1.28.38", "typer==0.9.0", "python_dotenv==1.0.0", "pydantic==2.3.0"],
    dev_deps=[
        "black==23.7.0",
        "ipdb==0.13.13",
        "isort==5.12.0",
        "mypy==1.5.1",
        "pylint==2.17.5",
        "pytest==7.4.0",
        "pytest_cov==4.1.0",
        "pytest_randomly==3.15.0",
        "icecream==2.1.3",
    ],
)

project.synth()
