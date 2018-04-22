from src.manager import Manager

TEMPLATE = '../template.xlsx'
INPUT = '../pages'

if __name__ == '__main__':
    manager = Manager(TEMPLATE, INPUT)
    manager.start()
