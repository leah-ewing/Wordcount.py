# put your code here.
def wordcount(input):
    #input = open("test.txt")
    input_var = open(input)
    letter_counts = {}

    for line in input:
        line = line.split(' ')
        letter_counts[line] = letter_counts.get(line, 0) + 1

    return letter_counts

print(wordcount("test.txt"))

