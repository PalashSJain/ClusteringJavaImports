import os

import sys

from CSVWorker.CSVReader import CSVReader
from Clusterer import Cluster
from CSVWorker.CSVWriter import CSVWriter as writer
from Main.Utils import Utils as Utils
from threading import Thread


def __main__():
    input_files = os.listdir("input")
    Utils.make_dirs(Utils.__OUTPUT_DIR__)

    try:
        for file_name in input_files:
            t = Thread(target=execute, args=(file_name,))
            t.start()
            t.join()
    except:
        print("Error in starting thread.")

    print("Fin.")


def execute(file_name):
    output_file = Utils.__OUTPUT_DIR__ + "output_" + file_name
    print("Reading file: " + file_name)
    reader = CSVReader()
    reader.read_file(Utils.__INPUT_DIR__ + file_name)
    libraries = reader.get_libraries()

    print("Starting to cluster "+file_name+"...")
    clusters = Cluster.run(libraries)

    Utils.delete_file(output_file)
    print("Writing output to: " + output_file)
    write_clusters_to_output_file(clusters, output_file)


def write_clusters_to_output_file(clusters, output_file):
    for cluster in clusters:
        write_cluster_to_output_file(cluster, output_file)


def write_cluster_to_output_file(cluster, output_file):
    for library in cluster:
        writer.println(library, output_file)
    writer.println("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~", output_file)


__main__()
