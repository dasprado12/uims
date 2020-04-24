<p align="center">
  <img src="http://imgur.com/iQU8c9L.png"/>
  <h4 align="center">UIoT</h4>
  <p align="center">
    <img src="https://img.shields.io/badge/platform-macOS%20%7C%20Linux-lightgrey.svg"/>
  </p>
</p>

UIoT dash_api
----------

**UIoT** is an *Internet of Things* open middleware. Made to handle and store knowledge and be a layer for IoT applications and devices. **UIoT** is maintained by the [Universal Internet of Things](https://uiot.org) and the [University of Brasília](http://www.unb.br).

**dash_api** is a module of the UIoT middleware which is the layer between devices/applications and data. It is an acronym for *Data Interface Management System*.

Requirements
---
- Tools required:
  - [Python 3.7](https://www.python.org/downloads/)
  - [MongoDB](https://docs.mongodb.com/manual/installation/)
  - [Docker Compose](https://docs.docker.com/compose/install/#prerequisites)

Run
---
- Running using docker-compose:

```bash
docker-compose up
```
dash_api will use `/tmp/dash_api` as a Docker *bind mount* to store logs, and `/var/docker/data/mongodb` to store database data.

- Running using standalone dependencies:
```bash
sudo service mongod start  # starts mongodb
python3 -m venv venv  # creates python 3 virtual environment
source venv/bin/activate  # starts python 3 virtual environment
pip install -e .  # install UIoT dash_api app and its requirements
uwsgi --ini uwsgi.ini  # run UIoT dash_api app
```

Contributing
------------

You can <b>Contribute</b> on dash_api! Check the [Contributing Guide](CONTRIBUTING.md).

<br>
<br>
<img align="right" src="http://imgur.com/l5hOjj4.gif">
