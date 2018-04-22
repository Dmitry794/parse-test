import openpyxl


class Writer:

    output_name = 'output.xlsx'

    def __init__(self, template, sheet):
        self.output = template
        self.workbook = openpyxl.load_workbook(template)
        self.sheet = self.workbook[sheet]

    def close(self):
        self.workbook.save(Writer.output_name)
        self.workbook.close()

    def write_sku(self, row, col, value):
        self.sheet.cell(row, col, value)
