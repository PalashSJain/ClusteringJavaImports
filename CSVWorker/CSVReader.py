def extractFirstColumn(line, __DELIMITER__=","):
    return line.replace("\n", "").split(__DELIMITER__)[0]


class CSVReader:

    def __init__(self):
        self.content = list()

    def read_file(self, file_name):
        with open(file_name) as f:
            for line in f:
                self.content.append(extractFirstColumn(line))

    def get_libraries(self):
        return self.content
