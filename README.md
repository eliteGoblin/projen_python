# Python projen example

Run app

```sh
# generated with projen 0.73.2
source .env/bin/activate
python main.py main --name=Frank --age=18 --vip --lang=Man
# Hello, Frank VIP! You are 18 years old.
```


Run CI script

```bash
./scripts/ci/ci
```

# Init your own project

```sh
projen --version
# 0.73.2
mkdir {YOUR PROJECT NAME}  && cd {YOUR PROJECT NAME}
projen new python
# copy .projenrc.py to your project
projen # update requirements
```

Optional

```sh
# Add git pre commit hook
ln -s -f ../../git-hooks/pre-commit .git/hooks/pre-commit
```


Features

*  Porjen
*  Typer
*  dotenv
*  Pytest
*  Pylint


