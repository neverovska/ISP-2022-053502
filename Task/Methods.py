import re


def number_of_words(text):
    text = text.replace(".", "").replace("?", "").replace("!", "")
    words = text.split()
    words.sort()
    return words


def aver_number(text):
    number = 0
    words = len(number_of_words(text))
    for char in text:
        if char == "." or char == "!" or char == "?":
            number = number+1
    number = words//number
    return number


def median_number(text):
    text = text.replace(". ", ".").replace("! ", "!").replace("? ", "?")
    sentences = re.split("[.!?]", text)
    sentences.remove('')
    words_dict_median = dict()
    for word in sentences:
        words_dict_median[word] = 1
        for char in word:
            if char == " " and word in words_dict_median:
                words_dict_median[word] = words_dict_median[word] + 1
    median_array = sorted(words_dict_median.values())
    if len(median_array) % 2 == 1:
        median = median_array[round(len(median_array)/2)]
    else:
        median = (median_array[len(median_array)//2-1]+median_array[len(median_array)//2])/2
    print(median_array)
    return median


def words_dictionary(words):
    words_dict = dict()
    for word in words:
        if word in words_dict:
            words_dict[word] = words_dict[word] + 1
        else:
            words_dict[word] = 1
    return words_dict


def n_grams(text, k, n):
    text = text.replace(" ", "").replace(".", "").replace("!", "").replace("?", "")
    dict_grams = dict()
    i = 0
    while i < len(text)-n:
        j = 1
        key = text[i]
        while j < n:
            key += text[i+j]
            j += 1
        i += 1
        if key in dict_grams:
            dict_grams[key] = dict_grams[key] + 1
        else:
            dict_grams[key] = 1

    res = sorted(dict_grams.items(), key=lambda item: item[1], reverse=True)
    i = 0
    top_list = list()
    while i < k:
        top_list.append(res[i])
        i += 1
    return top_list