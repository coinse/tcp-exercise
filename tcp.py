import argparse
from collect_tc_coverage import collect_tc_coverages

def get_failure_found_order(test_seq, test_results):
    failure_index = []
    for i, test_name in enumerate(test_seq):
        if test_results[test_name] == False:
            failure_index.append(i+1)

    return failure_index

def greedy_prioritise(test_traces):
    """
    TODO
    [Hint] Construct sequence of test names by choosing next test case that maximises # unseen executed lines
    """
    return []


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Test Case Prioritisation')
    parser.add_argument("-s", "--source_dir", default='examples/',
                        help='the directory that contains Python source files')
    parser.add_argument("-f", "--target_file", default='mid.py',
                        help='the name of a target file to measure coverage')
    parser.add_argument('-t', "--test_dir", default='examples/',
                        help='the directory that contains PyTest test files (test_*.py)')

    args = parser.parse_args()

    test_results, test_traces = collect_tc_coverages(args.source_dir, args.target_file, args.test_dir)
    test_seq = greedy_prioritise(test_traces)

    print(test_seq)
    # Expected greedy sequence: 1 -> 6 -> 2 -> 3 -> 4 -> 5
    
    assert get_failure_found_order(test_seq, test_results) <= 2