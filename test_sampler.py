"""Run tests of sampler.generate_outputs() function based on test
specifications in tests.json.
TODO: add tests for sampling without replacement, count exceeding total, old_output_list, skipping samples.
"""

import pytest
import sampler
import json

testfile='tests.json'
testspecs = json.load(open(testfile, 'r'))['tests']

@pytest.mark.parametrize("testspec", testspecs)
def test_generate_outputs(testspec):
    "Compare generate_outputs() result using testspec data with expected value"

    data = testspec['data']
    _, new_output_list = sampler.generate_outputs(
        data['count'], True, 1, data['total'], data['seed'], 0)
    assert(new_output_list == testspec['expected'])
