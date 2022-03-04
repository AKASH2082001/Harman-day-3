vowels = "aeiou"
name = "any"
count = 0

for i in name:
    for j in vowels:
        if(i==j):
            count = count + 1
            print(count)