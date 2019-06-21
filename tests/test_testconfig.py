# -*- coding: utf-8 -*-
import os


def test_tc_file_from_ini(testdir):
    """Test for parsing configuration from ini file."""

    testdir_path = os.getcwd()

    # create a temporary ini configuration file
    testdir.makefile(".ini", example_cfg="""
    # INI
    [myapp_servers1]
    main_server = 10.1.1.1
    secondary_server = 10.1.1.5
    """)

    testdir.makepyfile(
        """
        from pytest_testconfig import config

        def test_foo():

            target_server_ip = config['myapp_servers1']['main_server']
            assert target_server_ip == '10.1.1.1'
    """
    )

    # run pytest with the following cmd args
    result = testdir.runpytest(
        '--tc-file={}/example_cfg.ini'.format(testdir_path),
        '-v'
    )

    # fnmatch_lines does an assertion internally
    result.stdout.fnmatch_lines([
        '*test_tc_file_from_ini.py::test_foo PASSED*',
    ])

    # make sure that that we get a '0' exit code for the testsuite
    assert result.ret == 0


def test_tc_file_from_json(testdir):
    """Test for parsing configuration from json file."""

    testdir_path = os.getcwd()
    # create a temporary json configuration file
    testdir.makefile(".json", example_cfg="""{
    "myapp2": {
                 "servers": {
                                "main_server": "10.1.1.1",
                                "secondary_server": "10.1.1.1"
                            }
             }
    }
    """)

    testdir.makepyfile(
        """
        from pytest_testconfig import config

        def test_foo():

            target_server_ip = config['myapp2']['servers']['main_server']
            assert target_server_ip == '10.1.1.1'
    """
    )

    # run pytest with the following cmd args
    result = testdir.runpytest(
        '--tc-file={}/example_cfg.json'.format(testdir_path),
        '--tc-format=json',
        '-v'
    )

    # fnmatch_lines does an assertion internally
    result.stdout.fnmatch_lines([
        '*test_tc_file_from_json.py::test_foo PASSED*',
    ])

    # make sure that that we get a '0' exit code for the testsuite
    assert result.ret == 0


def test_tc_file_from_yaml(testdir):
    """Test for parsing configuration from yaml file."""

    testdir_path = os.getcwd()
    # create a temporary yaml configuration file
    testdir.makefile(".yaml", example_cfg="""
    # YAML
    myapp3:
        servers:
            main_server: 10.1.1.1
            secondary_server: 10.1.1.2
    """)

    testdir.makepyfile(
        """
        from pytest_testconfig import config

        def test_foo():

            target_server_ip = config['myapp3']['servers']['main_server']
            assert target_server_ip == '10.1.1.1'
    """
    )

    # run pytest with the following cmd args
    result = testdir.runpytest(
        '--tc-file={}/example_cfg.yaml'.format(testdir_path),
        '--tc-format=yaml',
        '-v'
    )

    # fnmatch_lines does an assertion internally
    result.stdout.fnmatch_lines([
        '*test_tc_file_from_yaml.py::test_foo PASSED*',
    ])

    # make sure that that we get a '0' exit code for the testsuite
    assert result.ret == 0


def test_tc_override(testdir):
    """Test for overriding configuration."""

    testdir.makepyfile(
        """
        from pytest_testconfig import config

        def test_foo():
            target_server_ip = config['myapp_servers4']['secondary_server']
            assert target_server_ip == '10.1.1.1'
    """
    )

    # run pytest with the following cmd args
    result = testdir.runpytest(
        '--tc=myapp_servers4.secondary_server:10.1.1.1',
        '-v',
        '-s'
    )

    # fnmatch_lines does an assertion internally
    result.stdout.fnmatch_lines([
        '*test_tc_override.py::test_foo PASSED*',
    ])

    # make sure that that we get a '0' exit code for the testsuite
    assert result.ret == 0


def test_tc_exact_override(testdir):
    """Test for overriding configuration with exact option."""

    testdir.makepyfile(
        """
        from pytest_testconfig import config

        def test_foo():
            target_server_ip = config['myapp_servers.secondary_server']
            assert target_server_ip == '10.1.1.1'
    """
    )

    # run pytest with the following cmd args
    result = testdir.runpytest(
        '--tc=myapp_servers.secondary_server:10.1.1.1',
        '--tc-exact',
        '-v'
    )

    # fnmatch_lines does an assertion internally
    result.stdout.fnmatch_lines([
        '*test_tc_exact_override.py::test_foo PASSED*',
    ])

    # make sure that that we get a '0' exit code for the testsuite
    assert result.ret == 0


def test_tc_file_from_python(testdir):
    """Test for parsing configuration from python file."""

    testdir_path = os.getcwd()
    # create a temporary py configuration file
    testdir.makefile(".py", example_cfg="""
    global config
    config = {
        'myapp5': {
            'servers': {
                'main_server': '.'.join(('10', '1', '1', '1',)),
            }
        }
    }
    """)

    testdir.makepyfile(
        """
        from pytest_testconfig import config

        def test_foo():

            target_server_ip = config['myapp5']['servers']['main_server']
            assert target_server_ip == '10.1.1.1'
    """
    )

    # run pytest with the following cmd args
    result = testdir.runpytest(
        '--tc-file={}/example_cfg.py'.format(testdir_path),
        '--tc-format=python',
        '-v'
    )

    # fnmatch_lines does an assertion internally
    result.stdout.fnmatch_lines([
        '*test_tc_file_from_python.py::test_foo PASSED*',
    ])

    # make sure that that we get a '0' exit code for the testsuite
    assert result.ret == 0


def test_help_message(testdir):
    result = testdir.runpytest(
        '--help',
    )
    # fnmatch_lines does an assertion internally
    result.stdout.fnmatch_lines([
        'test-config:',
        '  --tc-file=TESTCONFIG  Configuration file to parse and pass to tests',
        '                        [PY_TEST_CONFIG_FILE]',
        '  --tc-file-encoding=TESTCONFIGENCODING',
        '                        Test config file encoding, default is utf-8',
        '                        [PY_TEST_CONFIG_FILE_ENCODING]',
        '  --tc-format=TESTCONFIGFORMAT',
        '                        Test config file format, default is configparser ini',
        '                        format [PY_TEST_CONFIG_FILE_FORMAT]',
        '  --tc=OVERRIDES        Option:Value specific overrides.',
        '  --tc-exact            Optional: Do not explode periods in override keys to',
        '                        individual keys within the config dict, instead treat',
        '                        them as config[my.toplevel.key] ala sqlalchemy.url in',
        '                        pylons',
    ])
