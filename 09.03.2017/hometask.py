
import logging
from argparse import ArgumentParser
from datetime import datetime, timedelta
from os import path, listdir

period = timedelta(days=12)
Date = "2017/03/12"
date_birthday = datetime.strptime(Date, "%Y/%m/%d")
if datetime.now().date() <date_birthday.date() < date_birthday.date() + period:
    print("yes")
else:
    print("no")



logging.basicConfig(filename='example.log', level=logging.DEBUG,
                    format='%(asctime)s %(message)s', datefmt='[%m/%d/%Y | %I:%M:%S | %p]')
logging.debug('(This is a debug message)')


parser = ArgumentParser()
parser.add_argument('-l', '--level', choices=['debug', 'info', 'warning', 'error', 'critical'],
                    help='Logging level', default='info')
args = parser.parse_args()




def convert(a):
    """Returns 'dd/mm/yy'.
    Works with string:
    >>> convert("2019 03 10")
    '03/10/19'
    """
    c = datetime.strptime(a,"%Y %m %d")
    return c.strftime("%x")

print(convert("2017 03 10"))


my_path = "."
dirs = listdir(my_path)

for file in dirs:
    if path.isdir(file):
        print(file)

print()

for file in dirs:
    if path.isfile(file):
        print(file)


