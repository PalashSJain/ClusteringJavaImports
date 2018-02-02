from CSVWorker.CSVReader import CSVReader
from Clusterer import Cluster
from CSVWorker.CSVWriter import CSVWriter as writer
from Main.Utils import Utils as Utils


def __main__():
    reader = CSVReader("input.csv")
    reader.readFile()
    libraries = reader.getLibraries()

    clusters = Cluster.cluster(libraries)

    for cluster in clusters:
        Utils.make_dirs()
        for library in cluster:
            writer.println(library, Utils.__OUTPUT_DIR__ + str(clusters.index(cluster)) + ".csv")


__main__()
