# python3


def compute_min_number_of_refills(d, m, stops):
    assert 1 <= d <= 10 ** 5
    assert 1 <= m <= 400
    assert 1 <= len(stops) <= 300
    assert 0 < stops[0] and all(stops[i] < stops[i + 1] for i in range(len(stops) - 1)) and stops[-1] < d

    if m > d:
        return 0

    for i in range(len(stops) - 1):
        if stops[i + 1] - stops[i] > m:
            return -1


    currentRefill = 0
    lastRefill = 0
    count = 0

    while currentRefill < len(stops):
        if stops[currentRefill] - lastRefill > m:
            lastRefill = stops[currentRefill - 1]
            count = count + 1

        if stops[currentRefill] - lastRefill == m:
            lastRefill = stops[currentRefill]
            count = count + 1

        if currentRefill == len(stops) - 1 and d - lastRefill > m:
            lastRefill = stops[-1]
            count = count + 1
        currentRefill = currentRefill + 1


    return count




if __name__ == '__main__':
    input_d = int(input())
    input_m = int(input())
    input_n = int(input())
    input_stops = list(map(int, input().split()))
    assert len(input_stops) == input_n

    print(compute_min_number_of_refills(input_d, input_m, input_stops))
