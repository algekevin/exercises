import math
import fileinput

# Print list of numbers starting at 1, up to whatever the third number is in the input.
# Replace numbers divisible by the first number input with F, and numbers divisible by the second input with B.
# If the number is divisible by both, replace it with FB.
# ie: first line of inputs from fizzText is 3 5 10
# Output should be: 1 2 F 4 B F 7 8 F B
# There should be no trailing spaces in each line.

class FizzBuzz:
    def textCaller(self):
        for line in fileinput.input('fizzText.txt'):
            print(line, end=' ')
            self.replacer(line)
            print()
        print(fileinput.filename())

    def replacer(self,line):
        list = line.split()
        print(list)

        for x in range(1, int(list[2])+1):
            print(x, end=' ')
        print()

        for x in range(1, int(list[2])+1):
            if (x % int(list[0]) == 0) & (x % int(list[1]) == 0):
                x = 'FB'
            elif x % int(list[0]) == 0:
                x = 'F'
            elif x % int(list[1]) == 0:
                x = 'B'
            print(x, end=' ')


FizzBuzz().textCaller()