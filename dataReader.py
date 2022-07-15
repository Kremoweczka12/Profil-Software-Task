import email
import os


class DataReader:
    def __init__(self):
        self.logs = None
        self.emails = []
        for filename in os.listdir("emails"):
            if filename.endswith(".txt"):
                with open(os.path.join("emails", filename)) as file:
                    lines = file.readlines()
                    self.emails += [email.Email(line.rstrip()) for line in lines]

            elif filename.endswith(".csv"):
                with open(os.path.join("emails", filename)) as file:
                    lines = file.readlines()[1:]
                    self.emails += [email.Email(line.rstrip().split(";")[1]) for line in lines]

    def showInvalid(self):
        x = [e.fullAddress for e in self.emails if not e.validated]
        print(100 * "*", f"\nInvalid emails ({len(x)}):")
        for em in x:
            print("    ", em)

    def search(self, text):
        x = [e.fullAddress for e in self.emails if text in e.fullAddress and e.validated]
        x = list(set(x))
        print(100 * "*", f"\nFound emails with '{text}' in email ({len(x)}):")
        for em in x:
            print("    ", em)

    def groupByDomain(self):
        dic = {}
        x = []
        for element in self.emails:
            if element.validated and element.fullAddress not in x:
                if element.domain in dic.keys():
                    dic[element.domain].append(element.fullAddress)
                else:
                    dic[element.domain] = [element.fullAddress]
                x.append(element.fullAddress)
        print(100 * "*", "\n")
        for key in sorted(dic.keys()):
            print(f"Domain {key} ({len(dic[key])}):")
            for el in sorted(dic[key]):
                print("    ", el)

    def checkNotSent(self, path):
        x = []
        self.collectLogs(path)
        if self.logs != -1:
            for email in self.emails:
                if email.fullAddress not in self.logs and email.validated:
                    x.append(email.fullAddress)
            table = sorted(list(set(x)))
            print(100 * "*", f"\nEmails not sent ({len(table)}):")
            [print("    ", e) for e in table]

    def collectLogs(self, path):
        self.logs = []
        try:
            with open(path) as file:
                lines = file.readlines()
                for line in lines:
                    try:
                        x = line.rstrip()
                        first = x.find("'") + 1
                        second = len(x) - x[::-1].find("'") - 1
                        x = x[int(first): int(second)]
                        self.logs += [x]
                    except:
                        continue
        except Exception as e:
            self.logs = -1
            print(100 * "*", "\nINVALID LOG DIRECTION\FILE GIVEN AS AN ARGUMENT\n")
            print(e)
