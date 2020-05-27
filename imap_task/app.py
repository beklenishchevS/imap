import argparse
from mailReader import MailReader
import readline

parser = argparse.ArgumentParser()

parser.add_argument("-s", nargs=1, required=True, help="адрес (или доменное имя) IMAP-сервера в формате адрес", dest="server")
parser.add_argument("-n", nargs="*", help="диапазон писем", dest="numbers")
parser.add_argument("--user", help="имя пользователя", dest="name")

args = parser.parse_args()
password = input()
if args.numbers is None:
    mr = MailReader(args.name, args.server[0], password)
elif len(args.numbers) == 1:
    mr = MailReader(args.name, args.server[0], password, int(args.name[0]))
else:
    mr = MailReader(args.name, args.server[0], password, int(args.name[0]), int(args.name[1]))
mr.print_info()
