import base64


class MailParser:

    def __init__(self, text, size):
        self.text = text.split("\n")
        self.from_ = ""
        self.date = ""
        self.to = ""
        self.subject = ""
        self.size = size
        self.parse_mail(self.text)

    def parse_mail(self, mail):
        for line in mail:
            line = line.rstrip()
            if line.startswith("From:"):
                from_name = self.encode_B64(line.split(' ')[1])
                a = from_name
                self.from_ = a
                continue
            if line.startswith("Date:"):
                self.date = line[6:]
                continue
            if line.startswith("To:"):
                to = line.split(" ")
                try:
                    self.to = to[2]
                except Exception:
                    self.to = to[1]
                continue
            if line.startswith("Subject:"):
                sub = line.split(" ")[1]
                self.subject = self.encode_B64(sub)
                continue

    def generate_info(self):
        return f"{self.to} {self.from_} {self.subject} {self.date} {self.size}"

    def encode_B64(self, line):
        line = line.split("?")
        res = base64.b64decode(line[3]).decode(line[1])
        return res




