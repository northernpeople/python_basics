#! /usr/bin/env python

import sys

# strings

print 1, 2, 3
print "*" * 10
"".isalpha()
print "_".join(['1', '2', '3'])

text = "%d piggies ate %s" % (3, "grass and grains")
print text


# functions

def repeat(s, exclaim):
    result = s * 3
    if exclaim:
        result = result + "!!!"
    return result


def main():
    print "hello there", repeat(sys.argv[1], True)


# hack to simulate main method invokation
if __name__ == '__main__':
    main()




