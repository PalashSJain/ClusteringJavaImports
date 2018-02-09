from Main.Utils import Utils as Utils


def no_of_classes(library):
    return len(library.split("."))


def run(libraries):
    clusters = list()
    single_size_cluster = set()

    while len(libraries) > 0:
        if no_of_classes(libraries[0]) == 1:
            single_size_cluster.add(libraries[0])
            libraries.remove(libraries[0])
            continue

        cluster = list()

        for other_library in reversed(libraries):
            if libraries.index(other_library) == 0:
                continue
            if no_of_classes(other_library) == 1:
                single_size_cluster.add(other_library)
                libraries.remove(other_library)
                continue
            elif matches(libraries[0], other_library):
                cluster.append(other_library)
                libraries.remove(other_library)

        cluster.append(libraries.pop(0))
        clusters.append(cluster)

    return clusters, single_size_cluster


def matches(f, o):
    first = f.split(".")
    other = o.split(".")
    size = len(first) if len(first) < len(other) else len(other)

    consecutive_matches_count = 0
    for i, j in range(size):
        if first[i] == other[j]:
            consecutive_matches_count += 1
        else:
            break
    return (consecutive_matches_count * 100 / size) >= Utils.__THRESHOLD__
