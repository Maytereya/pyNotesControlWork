import uuid
from datetime import datetime


class Note:
    def __init__(self, id=str(uuid.uuid1())[0:2], name="text", content="text",
                 date=str(datetime.now().strftime("%d.%m.%Y %H:%M:%S"))):
        self.id = id
        self.name = name
        self.content = content
        self.date = date

    def get_id(self):
        return self.id

    def get_name(self):
        return self.name

    def get_content(self):
        return self.content

    def get_date(self):
        return self.date

    def set_id(self):
        self.id = str(uuid.uuid1())[0:2]

    def set_name(self, name):
        self.name = name

    def set_content(self, content):
        self.content = content

    def set_date(self):
        self.date = str(datetime.now().strftime("%d.%m.%Y %H:%M:%S"))

    def to_string(self):
        return self.id + ';' + self.name + ';' + self.content + ';' + self.date

    def info(self):
        return ('\n Название: ' + self.name + '\n Содержание:' +
                self.content + '\n Дата создания:' + self.date)
