"""Run tests of sampler function.

Test based on the test specifications in tests.json, and with some standard
input to main()

TODO: add tests for sampling without replacement, count exceeding total,
      old_output_list, skipping samples.

TODO: check the output generated against expected output, ignoring timestamps,
cleanly in portable Python.
Note the shell code in README.md checks much of this, but not the test_sampler.out
files from the saving results to file option.
"""


import sys
import io
import pytest
import json

import sampler

# FIXME: resolve bizarre error using pytest-3 rather than pytest in cleaner way....
# This doesn't seem to be a problem with non-pytest use of the code.
if not 'generate_outputs' in dir(sampler):
    from sampler import sampler

testfile='test/tests.json'
testspecs = json.load(open(testfile, 'r'))['tests']

@pytest.mark.parametrize("testspec", testspecs)
def test_generate_outputs(testspec):
    "Compare generate_outputs() result using testspec data with expected value"

    data = testspec['data']
    _, new_output_list = sampler.generate_outputs(
        data['count'], True, 1, data['total'], data['seed'], 0)
    assert(new_output_list == testspec['expected'])


# Various values to thest as the standard input to the program
stdin_tests = [
    u"test\nseed\n\n1\n1000\ny\nn\n10\n\n",
    u"test\nseed\n\n1\n1000\nn\nn\n10\n\n",
    u"test\nseed\n\n1\n1000\ny\ny\n10\n10\n\n",
    u"test\nseed\n\n1\n1000\ny\nn\n10\n/tmp/test_sampler.out\n"
    u"test\nseed\n\n1\n1000\ny\ny\n10\n10\n/tmp/test_sampler.out\n",
    u"test\nseed\n\n1\n1000\nn\ny\n10\n10\n/tmp/test_sampler.out\n"
]

@pytest.mark.parametrize("stdin_text", stdin_tests)
def test_main(stdin_text):
    """Test most of the command-line invocation code by feeding the given
    stdin_text thru the code starting with main()
    """

    sys.stdin = io.StringIO(stdin_text)
    sampler.main()
