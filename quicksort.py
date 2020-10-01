def quicksort(sequence: list, lower_bound: int, higher_bound: int) -> list:
    """
    Takes a list[int] and returns a sorted version of it
    https://en.wikipedia.org/wiki/Quicksort
    """""

    def partition(sequence: list, lower_bound: int, higher_bound: int) -> list:
        pivot = sequence[(higher_bound + lower_bound) // 2]

        lower_index = lower_bound - 1
        higher_index = higher_bound + 1

        while True:
            lower_index += 1
            while sequence[lower_index] < pivot:
                lower_index += 1

            higher_index -= 1
            while sequence[higher_index] > pivot:
                higher_index -= 1

            if lower_index >= higher_index:
                return higher_index

            sequence[lower_index], sequence[higher_index] = sequence[higher_index], sequence[lower_index]

    sorted_sequence = list(sequence)
    if lower_bound < higher_bound:
        p = partition(sorted_sequence, lower_bound, higher_bound)
        quicksort(sorted_sequence, lower_bound, p)
        quicksort(sorted_sequence, p + 1, higher_bound)

    return sorted_sequence


sequence = list(range(100, 0, -1))
print(sequence)
print(quicksort(sequence, 0, len(sequence) - 1))











heap = FibonacciHeap()
heap.insert() #...

[heap.delete_min()]






[]
[].append()
[].pop()

[1]
[1, 2].pop() == 2
[1].pop() == 1

[ ]
[1]
[1,  ]
[1, 2]

[1,  ]
last

for _ in :


[1, 2,  ,  ]
[1, 2, 3,  ]

[1, 2, 3,  ]
[1, 2, 3, 4]

[1, 2, 3, 4,  ,  ,  ,  ]
[1, 2, 3, 4,  ,  ,  ,  ]


1 = {
    value
    next = 2
}

2 = {
    value
    next = None
}

[index] !=
current = 1.next
current is not None

current.next #Crash



[1, 2, 1er, 4, 2nd]

len()
def len(tab):
    count = 0
    for element in tab:
        count += 1

    return count


def find(tab, value):
    for element in tab:
        if element == value:
            return element

    return None


def unique(tab):
    copy = []
    for element in tab:
        if element not in copy:
            copy.append(element)

    return copy


print([value * value for value in range(1, 10)])
print({value: value for value in range(1, 10)})
