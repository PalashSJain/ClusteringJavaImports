from CSVWorker.CSVReader import CSVReader
from CSVWorker.CSVWriter import CSVWriter as writer
from Main.Utils import Utils as Utils


def matches(main, sub):
    print(main + " | " + sub)
    return True


def __main__():
    reader = CSVReader("input.csv")
    reader.readFile()
    libraries = reader.getLibraries()

    cluster_no = 0

    while len(libraries) > 0:
        for library in reversed(libraries):
            if libraries.index(library) == 0:
                continue
            if matches(libraries[0], library):
                Utils.make_dirs()
                writer.println(library, Utils.__OUTPUT_DIR__ + str(cluster_no) + ".csv")
                libraries.remove(library)
        libraries.pop(0)
        cluster_no += 1


__main__()
