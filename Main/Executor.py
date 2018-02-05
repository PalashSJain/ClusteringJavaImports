from CSVWorker.CSVReader import CSVReader
from Clusterer import Cluster
from CSVWorker.CSVWriter import CSVWriter as writer
from Main.Utils import Utils as Utils


def __main__():
    file_name = "AuthTests-MethodCalls-Sample2"
    reader = CSVReader()
    reader.read_file(file_name + ".csv")
    libraries = reader.get_libraries()

    clusters = Cluster.cluster(libraries)

    print(len(clusters))

    cluster_index = 0

    for cluster in clusters:
        Utils.make_dirs(Utils.__OUTPUT_DIR__)
        for library in cluster:
            writer.println(library, Utils.__OUTPUT_DIR__ + str(cluster_index) + ".csv")
            writer.println(library, file_name + "_output_" + str(Utils.__THRESHOLD__) + ".csv")
        writer.println("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~",
                       file_name + "_output_" + str(Utils.__THRESHOLD__) + ".csv")

        cluster_index += 1


__main__()
