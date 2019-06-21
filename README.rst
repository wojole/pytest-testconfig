=================
pytest-testconfig
=================

.. image:: https://img.shields.io/pypi/v/pytest-testconfig.svg
    :target: https://pypi.org/project/pytest-testconfig
    :alt: PyPI version

.. image:: https://img.shields.io/pypi/pyversions/pytest-testconfig.svg
    :target: https://pypi.org/project/pytest-testconfig
    :alt: Python versions

.. image:: https://travis-ci.org/wojole/pytest-testconfig.svg?branch=master
    :target: https://travis-ci.org/wojole/pytest-testconfig
    :alt: See Build Status on Travis CI


Test configuration plugin for pytest.

Based on nose-testconfig by Jesse Noller. Rewritten for pytest by Wojciech Olejarz and Bartłomiej Skrobek.

----

This `pytest`_ plugin was generated with `Cookiecutter`_ along with `@hackebrot`_'s `cookiecutter-pytest-plugin`_ template.


Features
--------
pytest-testconfig is a plugin to the pytest test framework used for passing test-specific (or test-run specific) configuration data
to the tests being executed.

Currently configuration files in the following formats should be supported:

- YAML (via `PyYAML <http://pypi.python.org/pypi/PyYAML/>`_)
- INI (via `ConfigParser <http://docs.python.org/lib/module-ConfigParser.html>`_)
- Pure Python (via Exec)
- JSON (via `JSON <http://docs.python.org/library/json.html>`_)

The plugin is ``meant`` to be flexible, ergo the support of exec'ing arbitrary
python files as configuration files with no checks. The default format is
assumed to be ConfigParser ini-style format.

If multiple files are provided, the objects are merged. Later settings will
override earlier ones.

The plugin provides a method of overriding certain parameters from the command
line (assuming that the main "config" object is a dict) and can easily have
additional parsers added to it.

A configuration file may not be provided. In this case, the config object is an
emtpy dict. Any command line "overriding" paramters will be added to the dict.


Requirements
------------

requires pytest>=3.5.0


Installation
------------

You can install "pytest-testconfig" via `pip`_ from `PyPI`_::

    $ python3 -m pip install pytest-testconfig


Usage
-----

Tests can import the "config" singleton from testconfig::

    from pytest_testconfig import config

By default, YAML files parse into a nested dictionary, and ConfigParser ini
files are also collapsed into a nested dictionary for foo[bar][baz] style
access. Tests can obviously access configuration data by referencing the
relevant dictionary keys::

    from pytest_testconfig import config
    def test_foo():
        target_server_ip = config['servers']['webapp_ip']

``Warning``: Given this is just a dictionary singleton, tests can easily write
into the configuration. This means that your tests can write into the config
space and possibly alter it. This also means that threaded access into the
configuration can be interesting.

When using pure python configuration - obviously the "sky is the the limit" -
given that the configuration is loaded via an exec, you could potentially
modify pytest, the plugin, etc. However, if you do not export a config{} dict
as part of your python code, you obviously won't be able to import the
config object from testconfig.

When using YAML-style configuration, you get a lot of the power of pure python
without the danger of unprotected exec() - you can obviously use the pyaml
python-specific objects and all of the other YAML creamy goodness.

Defining a configuration file
-----------------------------

Simple ConfigParser style::

    [myapp_servers]
    main_server = 10.1.1.1
    secondary_server = 10.1.1.2

So your tests access the config options like this::

    from pytest_testconfig import config
    def test_foo():
        main_server = config['myapp_servers']['main_server']

YAML style configuration::
    myapp:
        servers:
            main_server: 10.1.1.1
            secondary_server: 10.1.1.2

And your tests can access it thus::

    from pytest_testconfig import config
    def test_foo():
        main_server = config['myapp']['servers']['main_server']

Python configuration file::

    import socket

    global config
    config = {}
    possible_main_servers = ['10.1.1.1', '10.1.1.2']

    for srv in possible_main_servers:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((srv, 80))
        except:
            continue
        s.close()
        config['main_server'] = srv
        break

And lo, the config is thus::

    from pytest_testconfig import config
    def test_foo():
        main_server = config['main_server']

If you need to put python code into your configuration, you either need to use
the python-config file faculties, or you need to use the !!python tags within
PyYAML/YAML - raw ini files no longer have any sort of eval magic.

Command line options
--------------------

After it is installed, the plugin adds the following command line flags to
pytest::

    --tc-file=TESTCONFIG  Configuration file to parse and pass to tests
                          [PY_TEST_CONFIG_FILE]
                          If this is specified multiple times, all files
                          will be parsed. In all formats except python,
                          previous contents are preserved and the configs
                          are merged.

    --tc-format=TESTCONFIGFORMAT  Test config file format, default is
                                  configparser ini format
                                  [PY_TEST_CONFIG_FILE_FORMAT]

    --tc=OVERRIDES        Option:Value specific overrides.

    --tc-exact            Optional: Do not explode periods in override keys to
                          individual keys within the config dict, instead treat
                          them as config[my.toplevel.key] ala sqlalchemy.url in
                          pylons.

Contributing
------------
Contributions are very welcome. Tests can be run with `tox`_, please ensure
the coverage at least stays the same before you submit a pull request.

License
-------

Distributed under the terms of the `Apache Software License 2.0`_ license, "pytest-testconfig" is free and open source software


Issues
------

If you encounter any problems, please `file an issue`_ along with a detailed description.

.. _`Cookiecutter`: https://github.com/audreyr/cookiecutter
.. _`@hackebrot`: https://github.com/hackebrot
.. _`MIT`: http://opensource.org/licenses/MIT
.. _`BSD-3`: http://opensource.org/licenses/BSD-3-Clause
.. _`GNU GPL v3.0`: http://www.gnu.org/licenses/gpl-3.0.txt
.. _`Apache Software License 2.0`: http://www.apache.org/licenses/LICENSE-2.0
.. _`cookiecutter-pytest-plugin`: https://github.com/pytest-dev/cookiecutter-pytest-plugin
.. _`file an issue`: https://github.com/wojole/pytest-testconfig/issues
.. _`pytest`: https://github.com/pytest-dev/pytest
.. _`tox`: https://tox.readthedocs.io/en/latest/
.. _`pip`: https://pypi.org/project/pip/
.. _`PyPI`: https://pypi.org/project
