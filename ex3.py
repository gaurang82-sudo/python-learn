sentence = "hello i am a gaurang javiya dilipbhai"
char = {}
for i in sentence:
    if i in char:
        char[i] += 1
    else:
        char[i] = 1
char_short = sorted(char.items(), key=lambda key: key[1])
print(
    f"most repate charter is : {char_short[-1][0]} times of {char_short[-1][1]}")
