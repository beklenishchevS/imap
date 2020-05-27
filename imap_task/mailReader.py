import imaplib
from mailParser import MailParser

class MailReader:
    def __init__(self, name, server, password, start=-1, finnish=-1):
        self.name = name
        self.server = server
        self.password = password
        self.start = start
        self.finish = finnish

    def print_info(self):
        mail = imaplib.IMAP4_SSL(self.server)
        mail.login(self.name, self.password)
        mail.select("inbox")
        result, data = mail.search(None, "ALL")
        ids = data[0]
        id_list = ids.split()
        if self.finish == -1:
            self.finish = len(id_list)
        if self.start == -1:
            self.start = 0
        for i in range(self.start+1, self.finish):
            try:
                latest_email_id = id_list[-i]
                result1, data = mail.fetch(latest_email_id, "(RFC822)")
                mp = MailParser(data[0][1].decode("utf-8"), data[0][0].decode("utf-8").split("{")[1][:-1])
                print(mp.generate_info())
            except Exception:
                continue