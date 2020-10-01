def bubble_sort(sequence: list) -> list:
    """
    Takes a list[int] and returns a sorted version of it
    https://en.wikipedia.org/wiki/Bubble_sort
    """

    length = len(sequence)
    sorted_sequence = list(sequence)

    swapped = True
    while swapped:
        swapped = False # On le met à FAUX au début
        for i in range(1, length):
            if sorted_sequence[i - 1] > sorted_sequence[i]:
                # échange a et b
                # temp = a
                # a = b
                # b = temp
                # swap(a, b)
                sorted_sequence[i - 1], sorted_sequence[i] = sorted_sequence[i], sorted_sequence[i - 1]
                swapped = True

    return sorted_sequence


sequence = list(range(100, 0, -1))
print(sequence)
print(bubble_sort(sequence))
