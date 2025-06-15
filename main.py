import sys
from stats import number_of_words, number_of_letters, sorter


def main ():
    if not len(sys.argv) == 2:
        print ("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        print ("============ BOOKBOT ============")
        print (f"Analyzing book found at {sys.argv[1]} ...")
        print ("----------- Word Count ----------")
        print ("Found", number_of_words(sys.argv[1]), "total words")
        print ("-------- Character Count --------")
        letter_count = number_of_letters(sys.argv[1])
        sorted_letters = sorter(letter_count)
        for i in range (0, len(sorted_letters)):
            print (f"{sorted_letters[i]["char"]}: {sorted_letters[i]["num"]}")
        print ("============== END ===============")


main()