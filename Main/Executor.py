import os

import sys

from CSVWorker.CSVReader import CSVReader
from Clusterer import Cluster
from CSVWorker.CSVWriter import CSVWriter as writer
from Main.Utils import Utils as Utils


def __main__():
    setup()

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

        Utils.delete_file(output_file)
        print("Writing output to: " + output_file)
        for cluster in clusters:
            for library in cluster:
                writer.println(library, output_file)
            writer.println("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~", output_file)

    print("Fin.")


def setup():
    if len(sys.argv) == 2:
        try:
            print("Setting threshold to " + sys.argv[1])
            Utils.__THRESHOLD__ = int(sys.argv[1])
        except:
            print("Threshold set is not a number. Threshold set to default value of 75.")
            Utils.__THRESHOLD__ = 75
    else:
        print("Threshold value not passed. Threshold set to default value of 75.")
        Utils.__THRESHOLD__ = 75


__main__()
