class Email:
    def __init__(self, text):
        self.fullAddress = text
        self.validated = False
        self.domain = ''
        self.validation()

    def validation(self):
        """there is only one @
length of the part before the @ is at least 1
length of the part between @  and . is at least 1
length of the part after the last . is at least 1 and at most 4 and contains only letters and/or digits"""
        try:
            self.findDomain()
            d = self.fullAddress[::-1]
            d = d.find(".") != -1 and 1 <= len(d[:d.find(".")]) < 5
            self.validated = len(self.domain) != 0 and self.fullAddress.count("@") == 1 and self.fullAddress[0] != "@" \
                             and len(self.domain[:self.domain.find(".")]) >= 1 and d
        except Exception as e:
            print(e)
            self.validated = False

    def findDomain(self):
        a = self.fullAddress.find("@")
        if a != -1:
            self.domain = self.fullAddress[a + 1:]
        else:
            self.domain = ''
