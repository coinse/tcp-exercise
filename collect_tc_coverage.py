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
    sys.path.append(source_dir)

    test_name = os.path.splitext(pytest_file)[0]
    test_name = test_name.replace("/", ".")
    module = import_module(test_name)
    return getmembers(module, isfunction)


def get_test_method_result(target_filename, test_file, test_method_name):
    """
    TODO: measure coverage for test_method_name
    """

    source_files = [target_filename]

    cov = Coverage(source=["./examples"], omit=[test_file])  # initialise coverage collector for target source directory
    cov.erase()  # erase previously collected data

    cov.start()  # start coverage collection

    old_out = sys.stdout   # do not mess up stdout with coverage.py output
    old_err = sys.stderr
    sys.stdout = open(os.devnull, 'w')
    sys.stderr = open(os.devnull, 'w') 

    test_name = os.path.basename(test_file)
    test_name = os.path.splitext(test_name)[0]
    
    ret = pytest.main([f"{test_file}::{test_method_name}", "--cache-clear"])


    cov.stop()  # stop coverage collection
    sys.stdout = old_out
    sys.stderr = old_err

    # save and load JSON report of coverage collection
    tmp_filename = "tmp_total_cov.json"

    cov.json_report(morfs=source_files, outfile=tmp_filename)

    json_str = "".join(open(tmp_filename, "r").readlines())
    decoder = json.JSONDecoder()        
    coverage = decoder.decode(json_str)
    os.remove(tmp_filename)

    return ret == pytest.ExitCode.OK, coverage["files"][target_filename]


def collect_tc_coverages(source_dir, target_file, test_dir):
    test_files = glob.glob(os.path.join(test_dir, "test_*.py"))
    test_results = {}
    test_traces = {}
    """
    TODO
    """
    for test_file in test_files:
        test_methods = get_test_methods(test_file, source_dir)

        for member in test_methods:
            test_name = member[0]

            result, coverage = get_test_method_result(target_file, test_file, test_name)

            test_results[test_name] = result
            test_traces[test_name] = coverage
    
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