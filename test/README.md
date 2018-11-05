# Testing sampler

If you have pytest and/or pytest-3, use these lines to test the basic sampler code.

   pytest -s > /tmp/pytest-s.out
   diff -I '^===' -I '^Current' test/pytest-s.out /tmp/pytest-s.out || echo "Output differences detected"

   pytest-3 -s > /tmp/pytest-s.out
   diff -I '^===' -I '^Current' test/pytest-s.out -I 'Python' /tmp/pytest-s.out  || echo "Output differences detected"

## Testing with coverage:

If python-coverage is installed you can also monitor test coverage

    pytest --cov

    # Look at missing coverage lines

    python-coverage html
    sensible-browser htmlcov/index.html
