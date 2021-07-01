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
    ordered = []
    covered_lines = set()

    remaining = list(test_traces.keys())
    
    while len(remaining) > 0:
        max_added = 0
        next_test = None
        # find the test in remaining that can increase the size of covered_lines the most
        for test in remaining:
            added = len(set(test_traces[test]["executed_lines"]) - covered_lines)
            if added > max_added:
                max_added = added 
                next_test = test

        if next_test:
            remaining.remove(next_test)
            ordered.append(next_test)
            covered_lines = covered_lines.union(set(test_traces[next_test]["executed_lines"]))
        else:
            covered_lines = set()
            print("reset")            
    
    return ordered


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