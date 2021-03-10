output = []
for i in range(26):
    output.append(chr(i + 65))
key = []
print(output)
for i in range(26):
    key.append(int(i))
line = input()
print(key)
result = ''
for i in range(len(line)):
    index_char = output.index(line[i])
    result += str(key[index_char])
print(result)






