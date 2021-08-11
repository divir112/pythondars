greeting = 'hello, world'

char = [i for i in greeting]
print(char)
char1 = {i for i in greeting}
print(char1)
char2 = tuple(i for i in greeting if i == 'l')
print(char2)