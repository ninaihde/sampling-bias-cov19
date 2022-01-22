import argparse
import csv
import json


def main():
    parser = argparse.ArgumentParser(description='A script that converts the JSON metadata from GISAID to a TSV file.')
    parser.add_argument('-t', '--tsv', type=str, default=None,
                        help='Location of resulting TSV file')
    parser.add_argument('-j', '--json', type=str, default=None,
                        help='Location of given GISAID json file')
    args = parser.parse_args()
    create_tsv(args.json, args.tsv)


def create_tsv(json_path, tsv_path):
    error_count = 0

    with open(json_path, 'r', encoding='utf-8') as json_file:
        with open(tsv_path, 'w') as tsv_file:
            for i, line in enumerate(json_file):
                # Read one key-value object per line
                obj = json.loads(line)

                # For first object, take keys as header for TSV
                if i == 0:
                    dw = csv.DictWriter(tsv_file, obj.keys(), delimiter='\t')
                    dw.writeheader()
                    i += 1

                try:
                    # For each object, append its values as new row to TSV
                    dw.writerow(obj)
                except UnicodeEncodeError:
                    # If UnicodeEncodeError occurs, count and ignore row
                    error_count += 1
                    continue

    print(f'{error_count} UnicodeEncodeErrors occured.')


if __name__ == '__main__':
    main()
