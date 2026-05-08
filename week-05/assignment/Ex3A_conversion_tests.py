# Description: This script tests various numeric conversion techniques
# Author: Jeremiah Goode

a = float(" 101.1 ").strip()
b = int('55')
c = str("402 Steven")
for c in range(3) : c = int(c)
d = str('Number 5 ').strip()

print(a, type(a))
print(b, type(b))
print(c, type(c))
print(d, type(d))