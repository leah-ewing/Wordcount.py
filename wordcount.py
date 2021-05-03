# put your code here.
def wordcount(input):
    #input = open("test.txt")
    input_var = open(input)
    letter_counts = {}

    for line in input_var:
        line = line.rstrip()
        line = line.split(' ')
        for word in line:
            letter_counts[word] = letter_counts.get(word, 0) + 1
            
    for word in letter_counts:
        print(word, letter_counts[word])
    return letter_counts

wordcount("test.txt")


