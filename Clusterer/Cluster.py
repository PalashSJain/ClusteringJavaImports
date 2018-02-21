from Main.Utils import Utils as Utils


def no_of_classes(library):
    return len(library.split("."))


def add_to_relevant_cluster(clusters, single_size_cluster):
    for single_cluster in single_size_cluster:
        isAdded = False
        for cluster in clusters:
            if isAdded:
                break
            for library in cluster:
                if isAdded:
                    break
                if library.endswith(single_cluster):
                    cluster.append(single_cluster)
                    isAdded = True
                    break


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

    add_to_relevant_cluster(clusters, single_size_cluster)
    clusters.append(single_size_cluster)
    return clusters


def has_min_matches(consecutive_matches_count, size):
    # for a given SIZE, it should have a minimum of CONSECUTIVE_MATCHES_COUNT to qualify as matching
    dict = {1: 1,
            2: 1,
            3: 2,
            4: 3,
            5: 3,
            6: 4,
            7: 5,
            8: 6,
            9: 7,
            10: 8,
            11: 9,
            12: 10,
            13: 11}
    return dict[size] <= consecutive_matches_count


def matches(f, o):
    first = f.split(".")
    other = o.split(".")
    size = len(first) if len(first) < len(other) else len(other)

    consecutive_matches_count = 0
    iF = 0
    iO = 0

    if Utils.is_ignore_word(first[iF]):
        iF += 1
    if Utils.is_ignore_word(other[iO]):
        iO += 1

    for i in range(size):
        if first[iF] == other[iO]:
            consecutive_matches_count += 1
            iF += 1
            iO += 1
        else:
            break

        if iF == size or iO == size:
            break
    # return (consecutive_matches_count * 100 / size) >= Utils.__THRESHOLD__
    return has_min_matches(consecutive_matches_count, size)
