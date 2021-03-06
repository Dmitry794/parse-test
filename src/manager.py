import openpyxl
import os
from .parser import Parser
from .writer import Writer


class Manager:

    def __init__(self, template, input_path):
        self.template = template
        self.input_path = input_path
        self.data_columns = self.get_columns()
        self.files = self.find_files()

    def start(self):
        print('start')
        print(self.data_columns)
        self.process()

    def get_columns(self):
        book = openpyxl.load_workbook(self.template)
        sheet = book['data']
        columns = {}
        i = 1
        while True:
            cell = sheet.cell(1, i)
            if cell.value is not None:
                columns[cell.value] = i
                i += 1
            else:
                break
        book.close()
        return columns

    def find_files(self):
        return os.listdir(self.input_path)

    def process(self):
        writer = Writer(self.template, 'data')
        for file in self.files:

            dir_path = os.path.abspath(self.input_path)
            with open(os.path.join(dir_path, file)) as f:
                parser = Parser(f.read())
                writer.write_sku(self.files.index(file)+2, self.data_columns['sku'], parser.get_sku())

        writer.close()