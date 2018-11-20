
f = open("text.txt", "rU")
for line in f:
    print len(line)
    for i in range(0, len(line)):
        print '*',
    print

f.close()