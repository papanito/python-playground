import re

file = open("example1.txt", "r")
string = file.read()
m = re.search('(?<=Label:) {0,2}(\w+)', string)

print m.group(1)