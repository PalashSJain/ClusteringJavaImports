import os

from CSVWorker.CSVReader import CSVReader
from Clusterer import Cluster
from CSVWorker.CSVWriter import CSVWriter as writer
from Main.Utils import Utils as Utils


def __main__():
    input_files = os.listdir("input")
    Utils.make_dirs(Utils.__OUTPUT_DIR__)

    for file_name in input_files:
        output_file = Utils.__OUTPUT_DIR__ + str(Utils.__THRESHOLD__) + "_" + file_name

        print("Reading file: " + file_name)
        reader = CSVReader()
        reader.read_file(Utils.__INPUT_DIR__ + file_name)
        libraries = reader.get_libraries()

        print("Starting to cluster...")
        clusters = Cluster.run(libraries)

        print("Writing output to: " + output_file)
        for cluster in clusters:
            for library in cluster:
                writer.println(library, output_file)
            writer.println("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~", output_file)

    print("Fin.")


__main__()
