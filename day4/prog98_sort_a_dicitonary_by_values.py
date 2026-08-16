#Write program to sort dictionary by values
numbers = {'A':26,
           'B':25,
           'C':24,
           'D':23,
           'E':22,
           'F':19
}
items = list(numbers.items())
for i in range(len(items)):
    for j in range(i + 1, len(items)):
        if items[i][1] > items[j][1]:
            items[i],items[j] = items[j],items[i]
sorted_dictionary = dict(items)
print("Dictionary sorted by values:", sorted_dictionary)
