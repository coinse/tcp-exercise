from inspect import getmembers, isfunction
from importlib import import_module
from coverage import Coverage

import os
import sys
import glob
import json

import pytest

def get_test_methods(pytest_file, source_dir):
    """
    TODO
    [Hint] use inspect & importlib modules
    """
    return []


def get_test_method_result(target_filename, test_file, test_method_name):
    """
    TODO
    """
    return True, {}


def collect_tc_coverages(source_dir, target_file, test_dir):
    test_files = glob.glob(os.path.join(test_dir, "test_*.py"))
    test_results = {}
    test_traces = {}
    """
    TODO
    """
    
    return test_results, test_traces


if __name__ == "__main__":
    test_results, test_traces = collect_tc_coverages('examples/', 'mid.py', 'examples/')
    
    for test_name in test_results:
        print(f'{test_name}: {test_traces[test_name]["executed_lines"]} (Passed: {test_results[test_name]})')

    """
    Expected output:

    test_mid1: [2, 3, 4, 6, 7, 13] (Passed: True)
    test_mid2: [2, 3, 4, 5, 13] (Passed: True)
    test_mid3: [2, 3, 9, 10, 13] (Passed: True)
    test_mid4: [2, 3, 9, 11, 13] (Passed: True)
    test_mid5: [2, 3, 4, 6, 13] (Passed: True)
    test_mid6: [2, 3, 4, 6, 7, 13] (Passed: False)
    """