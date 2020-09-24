# Use words.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
a=fh.read()
a=a.upper()
a=a.rstrip()
print(a)
