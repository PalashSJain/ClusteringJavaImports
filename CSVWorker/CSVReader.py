def extractFirstColumn(line, __DELIMITER__=","):
    return line.replace("\n", "").split(__DELIMITER__)[0]


class CSVReader:

    def __init__(self, file_name):
        self.file_name = file_name

    def readFile(self):
        self.content = list()
        with open(self.file_name) as f:
            for line in f:
                self.content.append(extractFirstColumn(line))

    def getLibraries(self):
        return self.content
