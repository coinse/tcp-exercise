import os
import sys
import glob
import json

import pytest

from coverage import Coverage

"""
Following example shows how to collect coverage for the entire test methods in given test file & parse JSON report generated from coverage.py

For more functionality, refer to https://coverage.readthedocs.io/


* Example test file path: `examples/test_mid.py`
* Example source code path: `examples/mid.py`
"""

test_files = ['examples/test_mid.py']
source_files = ['examples/mid.py']

cov = Coverage(source=["./examples"], omit=test_files)  # initialise coverage collector for target source directory
cov.erase()  # erase previously collected data

cov.start()  # start coverage collection

old_out = sys.stdout   # do not mess up stdout with coverage.py output
old_err = sys.stderr
sys.stdout = open(os.devnull, 'w')
sys.stderr = open(os.devnull, 'w') 

for test_file in test_files[:]:
    test_name = os.path.basename(test_file)
    test_name = os.path.splitext(test_name)[0]        
    pytest.main([f"{test_file}", "--cache-clear"])

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

print(coverage)