class CSVWriter:

    def print(library, file_name):
        f = open(file_name, "a")
        f.write(library)
        f.close()

    def println(library, file_name):
        f = open(file_name, "a")
        library += "\n"
        f.write(library)
        f.close()