from Main.Utils import Utils as Utils


def cluster(libraries):
    clusters = list()

    while len(libraries) > 0:
        cluster = list()

        for other_library in reversed(libraries):
            if libraries.index(other_library) == 0:
                continue
            if matches(libraries[0], other_library):
                cluster.append(other_library)
                libraries.remove(other_library)

        cluster.append(libraries.pop(0))
        clusters.append(cluster)

    return clusters


def matches(f, o):
    first = f.split(".")
    other = o.split(".")
    size = len(first) if len(first) < len(other) else len(other)

    if size == 1:
        return first[len(first) - 1] == other[len(other) - 1]

    consecutive_matches_count = 0
    for i in range(size):
        if first[i] == other[i]:
            consecutive_matches_count += 1
        else:
            break
    return (consecutive_matches_count * 100 / size) >= Utils.__THRESHOLD__
