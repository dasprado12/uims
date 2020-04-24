# Table of Contents

1. [Contributing](#contributing)
2. [Setup](#setup)
3. [Run](#run)
4. [Run Tests](#run-tests)
5. [Run PEP8](#run-pep8)


## Contributing

1. Create a issue with a feature or bug.
2. Fork the project into your own repository and create a branch called ``dev_[feature]``, where *feature* is the name of the
  feature that you are working on.
3. Update the branch ``dev_[feature]`` and send commits with the number of
your issue at the message, e.g.:
  ```bash
  git commit -m "solves commit #5"
  ```
4. Run tests to check if everything is working fine:
  ```bash
  (venv) python setup.py test
  ```
4. After run the tests and passed all of them, push your modifications and
send a *PR* (Pull Resquest) to master.


## Setup

- Tools required:
  - [Python3.7](https://www.python.org/downloads/)
  - [MongoDB](https://docs.mongodb.com/manual/installation/)
  - [docker-compose](https://docs.docker.com/compose/install/#prerequisites)


- Using virtualenv and setuptools:

```bash
sudo service mongod start  # starts mongodb
python3 -m venv venv # creates python 3 virtual environment
source venv/bin/activate # starts python 3 virtual environment
(venv) pip install -e . # install UIoT dash_api app and its requirements
```

## Run

- Using setuptools:

```shell
(venv) dash_api # run as development server
```

## Run Tests

```bash
(venv) pytest # run all tests
```

## Run PEP8

```bash
(venv) pycodestyle dash_api # run linter to check PEP8 styling
```

## Authors

- Dayanne Fernandes:
  - Github : [@Dayof](https://github.com/Dayof)
  - E-mail : dayannefernandesc@gmail.com
- Thiago Araújo:
  - Github : [@Thiago-AS](https://github.com/Thiago-AS)
  - E-mail : thiago.silva@uiot.org
- Lucas Martins:
  - Github : [@lucasmauricio](https://github.com/lucasmauricio)
  - E-mail : lucas.martins@uiot.org
