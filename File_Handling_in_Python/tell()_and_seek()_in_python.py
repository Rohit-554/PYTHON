f = open("E:\\My Codes\\Python Codes\\April 2021\\30-04-2021\\file1.txt", "r")
print(f.tell())
print(f.readline())
print(f.tell())
f.seek(0)
print(f.readline())