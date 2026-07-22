import csv
import fileinput
from optparse import OptionParser

widths = [
    ('uri', 30),
    ('type', 30),
    ('tenantId', 30),
    ('env', 30),
    ('', 30),
    ('name', 60),
    ('address', 55),
    ('pobox', 55),
    ('city', 30),
    ('state', 30),
    ('zip', 18),
    ('country', 30),
    ('phone', 20)
]

fixed_format = ''.join([('%%(%s)-%d.%ds' % (x[0], x[1], x[1])) if x[0] != '' else ' ' * x[1] for x in widths])
empty_dict = dict([(x[0], '') for x in widths if x[0] != ''])

parser = OptionParser(usage="fwf -f filename.csv")
parser.add_option("-f", "--file", dest="filename",
                  help="file with CSV records", metavar="FILE")

(options, args) = parser.parse_args()


def merge_two_dicts(x, y):
    z = x.copy()
    z.update(y)
    return z


def process(reader):
    csvreader = csv.reader(reader)
    headers = next(csvreader)
    for row in csvreader:
        print(fixed_format % merge_two_dicts(empty_dict, dict(zip(headers, row))))


if options.filename:
    with open(options.filename) as csvfile:
        process(csvfile)
else:
    process(fileinput.input())
