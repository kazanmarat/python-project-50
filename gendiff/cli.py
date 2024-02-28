import argparse


def collect_arguments():
    '''
    Collects and parses command line arguments for file comparison.

    Returns:
    - first_file: str, the path to the first file for comparison
    - second_file: str, the path to the second file for comparison
    - format: str, the format of the output (default: 'stylish')
    '''
    parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.',
        prog='gendiff')

    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument('-f', '--format', default='stylish',
                        help='set format of output')

    args = parser.parse_args()
    return args.first_file, args.second_file, args.format
