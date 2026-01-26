def test_argtest01(cmd_opts):
    # print(cmd_opts.readline())
    assert cmd_opts.readline().index("Lab")


# pytest -v -s pytest_basics\test_argtests.py --cmdopt=PROD
# pytest -v -s pytest_basics\test_argtests.py --cmdopt=QA