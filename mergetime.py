def merge_times(avail):
    i = 0
    while i < len(avail) - 1:
        if avail[i][1] >= avail[i + 1][0]:
            avail[i][1] = max(avail[i + 1][1], avail[i][1])
            del avail[i + 1]
        else:
            i += 1
    return avail
