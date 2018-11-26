# -*- coding: utf-8 -*-
#
#
# def test_bar_fixture(testdir):
#     """Make sure that pytest accepts our fixture."""
#
#     # create a temporary pytest test module
#     testdir.makepyfile("""
#         def test_sth(bar):
#             assert bar == "europython2015"
#     """)
#
#     # run pytest with the following cmd args
#     result = testdir.runpytest(
#         '--foo=europython2015',
#         '-v'
#     )
#
#     # fnmatch_lines does an assertion internally
#     result.stdout.fnmatch_lines([
#         '*::test_sth PASSED*',
#     ])
#
#     # make sure that that we get a '0' exit code for the testsuite
#     assert result.ret == 0


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


# def test_tc_file_ini_setting(testdir):
#     testdir.makeini("""
#         [pytest]
#         addopts = --tc-file ~/pytest-testconfig/examples/example_cfg.ini
#     """)
#
#     testdir.makepyfile("""
#         import pytest
#
#         @pytest.fixture
#         def addopts_value(request):
#             return request.config.getini('addopts')
#
#         def test_tc_file_ini_setting(addopts_value):
#             assert addopts_value == ['--tc-file', '~/pytest-testconfig/examples/example_cfg.ini']
#     """)
#
#     result = testdir.runpytest('-v')
#
#     # fnmatch_lines does an assertion internally
#     result.stdout.fnmatch_lines([
#         '*::test_tc_file_ini_setting PASSED*',
#     ])
#
#     # make sure that that we get a '0' exit code for the testsuite
#     assert result.ret == 0
