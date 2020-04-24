from setuptools import setup, find_packages
import io
import re


with io.open('README.md', encoding='utf8') as readme:
    long_description = readme.read()


with io.open('./dash_api/__init__.py', encoding='utf8') as version_file:
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]",
                              version_file.read(), re.M)
    if version_match:
        version = version_match.group(1)
    else:
        raise RuntimeError("Unable to find version string.")


setup(
    name='dash_api',
    version=version,
    description='dash_api is a module of the UIoT middleware.',
    url='https://uiot.org/',
    long_description=long_description,
    author='Dayanne Fernandes, Lucas Martins, Thiago Araújo',
    author_email='dayannefernandesc@gmail.com, lucas.martins@uiot.org,\
                thiago.silva@uiot.org',
    packages=find_packages(exclude='tests'),
    install_requires=['flask', 'meinheld', 'pymongo', 'flask_pymongo',
                      'flask_marshmallow', 'itsdangerous', 'Jinja2',
                      'MarkupSafe', 'Werkzeug', 'ipdb', 'pytest',
                      'pycodestyle', 'pathlib', 'pyyaml', 'flask_cors',
                      'uwsgi', 'flask-swagger-ui', 'datetime', 'requests'],
    setup_requires=['pytest-runner'],
    entry_points={
        'console_scripts': [
            'dash_api = dash_api.__main__:start_server',
        ]
    },
    classifiers=[
        'Programming Language :: Python :: 3.7',
    ],
    tests_require=['pytest']
)
