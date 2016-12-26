#readlines() will read each line in a list of lines include trailing newline
#read() will read whole file and splitlines by newline charact
f = open("testcase.txt", "r")
xs = f.read().split("\n")
f.close()
for x in range(10):
    print(xs[x])
