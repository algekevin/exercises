import fileinput
import itertools

# Challenge 323[E]
# Take all combinations of 3 numbers and retrieve the ones that add up to 0.


class sumThrees:
    def __init__(self):
        for line in fileinput.input('sumThreesNums.txt'):
            print(line)

            arr = list( map(int, line.split(' ')) )            # We know the numbers are formatted this way.
            combos = tuple(itertools.combinations(arr, 3))     # Get triplets without replacement(no dupes)
                                                               # But still dupes in output if dupe numbers exist

            sums = []
            for i in combos:
                if sum(i) == 0:         # Checking sum of the tuple combinations from above.
                    sums.append(i)      # If sum of tuple is 0, add tuple to sums array.

            print('number of 3sums: ', len(sums))
            print('3sums: ')
            for trip in sums:
                print(*trip)            # *trip to print the tuples in an easier to read format.
            print()


sumThrees()