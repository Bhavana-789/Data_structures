def read_words(word):

    file = open("d:\\info.txt", "r")
    s = " "
    count = 1

    while s:
        s = file.readline()
        L = s.split()
        if word in L:
            print("Line number:", count, ":", s)

    count += 1


if __name__ == "__main__":
    word1 = input("Enter the word to search:")
    print(read_words(word1))
