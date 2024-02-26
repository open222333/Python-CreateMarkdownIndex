from src.files import FilesParser
from argparse import ArgumentParser
from common_tool.src.logger import Log
from pprint import pprint
import json
import os

logger = Log('Main')

parser = ArgumentParser()
parser.add_argument('-p', '--path', help='指定路徑', required=True)
args = parser.parse_args()

if __name__ == '__main__':
    files = FilesParser.get_all_files(args.path, args.path, ['md'], add_abspath=False)

    # with open('test.json', 'w') as f:
    #     f.write(json.dumps(files, ensure_ascii=False))

    # pprint(files)

    for file in files:
        filename = os.path.basename(file)
        filename, _ = os.path.splitext(filename)
        print(filename)
