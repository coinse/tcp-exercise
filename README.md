# Test Prioritisation Exercise

We will implement a simple, additional greedy based Test Case Prioritisation (TCP) toolchain based on [coverage.py](https://coverage.readthedocs.io/en/coverage-5.5/) and [PyTest](https://docs.pytest.org/en/6.2.x/).

The included `sample.py` contains examples of:

1. How to invoke `coverage.py` from within Python script, and
2. How to execute PyTest test cases from within Python script.

However, to implement TCP, we need to figure out the following.

## Task 1: Get Individual Coverage of Each Test Case

Because we need the coverage of each indivudal test case (=test function, in PyTest terms). There are two related subgoals, which are:

- Identify all the test functions, and
- Execute each of the test functions individually, while recording coverage

Fill in `collect_tc_coverage.py` to achieve Task 1. Use the `mid.py` under `examples` directory as an example.

## Task 2: Generate test case execution sequence using greedy prioritisation

Once you collect individual coverage of each test case, you need to set the order between them. We will try additional greedy algorithm, i.e., choosing whichever test case that will increase the accumulated coverage by the maximum. Fill in `tcp.py` to achieve Task 2. Use the `mid.py` under `examples` directory as an example.