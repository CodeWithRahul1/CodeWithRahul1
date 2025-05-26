def method(intervals):
    if not intervals:
        return []

    intervals.sort(key=lambda i: i[0])
    output = [intervals[0]]  # initialize with the first interval

    for start, end in intervals[1:]:
        last_end = output[-1][1]
        if start <= last_end:
            output[-1][1] = max(last_end, end)
        else:
            output.append([start, end])

    return output

# Example
intervals = [[1, 3], [8, 10], [15, 18], [2, 6]]
print(method(intervals))
