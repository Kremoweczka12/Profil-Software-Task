import sys
import time
import argparse
import dataReader


if __name__ == "__main__":
    arguments = sys.argv[1:]
    try:
        parser = argparse.ArgumentParser(description="Program for data parsing and reading.", exit_on_error=False)
        parser.add_argument("-ic", '--incorrect-emails', help='Use this to display incorect emails',
                            action='store_true')
        parser.add_argument("-s", '--search', type=str, metavar='',
                            help='Displays emails which contain given substring.')
        parser.add_argument("-gbd", '--group-by-domain', help='Groups emails and displays them',
                            action='store_true')
        parser.add_argument("-feil", '--find-emails-not-in-logs', type=str, metavar='',
                            help='Displays emails which do not occur in given logs file')
        args = parser.parse_args()
        if len(arguments) > 0:
            d = dataReader.DataReader()
            t = 0
            if args.incorrect_emails:
                d.showInvalid()
                t += 15
            if args.search is not None:
                d.search(args.search)
                t += 15
            if args.group_by_domain:
                d.groupByDomain()
                t += 15
            if args.find_emails_not_in_logs is not None:
                d.checkNotSent(args.find_emails_not_in_logs)
                t += 15
            print(100*"*", f"\nThis view will be active for {t} seconds")
            time.sleep(t)
        else:
            print("You gave program no arguments!")
    except argparse.ArgumentError as e:
        print(e)
    except argparse.ArgumentTypeError as e:
        print(e)
time.sleep(5)
