#Crimson Publisher

Crimson Publisher is an tool for online publishing. Crimson Publisher is based on open source django framework.

## Requirements

* Django 1.7 or later
* Python 3.3 or later

There are no known issues with python 2.7.

## How to install

If you are familiar with django, you can skip this section.

Use pip to install the dependencies. You can run the following command from the root directory of application.

pip install -r requirement.txt

## Configuration

All settings and configurations are listed in publisher/settings.py and publisher/config.py. The recomended way to
override a value in settings.py or config.py is to redeclare it in publisher/settings.py or publisher/config.py.