s = 'Hello World'
words = s.split()
res = ''
for word in words:
    reverse = word[::-1].title()
    res += reverse + ' '
print(res)

import sys
inputMatrix = []

for line in sys.stdin:
    #print(line)
    if line in ['\n','\r\n']:
        squareWindow = line
        break
    inputMatrix.append(line)
