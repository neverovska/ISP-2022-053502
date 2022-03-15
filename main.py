import os
import re
import UserChoice
import Importing
import Methods


def main():
    filename = "/home/alcabens/2course/isp/text"
    if not os.path.exists(filename) or os.path.getsize(filename) == 0:
        print("Указанный файл не существует")
    else:
        text = Importing.get_words(filename)
        count_words = Methods.number_of_words(text)
        words_dict = Methods.words_dictionary(count_words)
        print("All words:")
        for word in words_dict:
            print(word.ljust(20), words_dict[word])
        print(f"Average number: {Methods.aver_number(text)}")
        print(f"Median: {Methods.median_number(text)}")
        print(f"Топ-K N-грам: {UserChoice.user_choice(text)}")


if __name__ == "__main__":
    main()