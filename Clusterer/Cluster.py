from random import *


def cluster(libraries):
    clusters = list()
    while len(libraries) > 0:
        cluster = list()
        for library in reversed(libraries):
            if libraries.index(library) == 0:
                continue
            if matches(libraries[0], library):
                cluster.append(library)
                libraries.remove(library)
        libraries.pop(0)
        clusters.append(cluster)
    return clusters


def matches(main, sub):
    print(main + " | " + sub)
    return randint(1, 100) > 50
