import csv
import os.path
import argparse


def get_most_elements(nums: list[str]) -> list[str]:
    """This function returns a list of the most common elements in a list"""
    lookup = dict()
    result = []
    for i in nums:
        if i in lookup:
            lookup[i] += 1
        else:
            lookup[i] = 1
    max_value = max(lookup.values())
    for key, value in lookup.items():
        if value == max_value:
            result.append(key)
    return result


def file_parser(filename: str):
    """This function returns a dictionary populated with the cookies for each day"""
    lookup = dict()
    with open(filename, 'r') as cookie_log:
        cookie_log_reader = csv.DictReader(cookie_log)
        line_count = 0
        for row in cookie_log_reader:
            if line_count == 0:
                continue
            get_cookie = row["cookie"]
            get_timestamp = row["timestamp"]
            get_day = get_timestamp.split("T")[0]
            if get_timestamp in lookup:
                lookup[get_day].append(get_cookie)
            else:
                lookup[get_day] = [get_cookie]
    return lookup


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument(dest='argument1', help="This is the filename")
    parser.add_argument('-d', '--date',
                        help='prefix for saved date ',
                        required=True)
    return parser.parse_args()


def main():
    args = parse_args()
    date = args.date
    filename = args.argument1

    # assert if the filename exists in the same folder as the program
    if os.path.exists(filename):
        lookup = file_parser(filename)
        most_elements = get_most_elements(lookup[date])
        return most_elements
    print("This file does not exist")


if __name__ == "__main__":
    main()
