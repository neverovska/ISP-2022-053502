import Methods


def user_choice(text):

    while True:
        answer = input("Желаете оставить K=10 и N=4 ? y/n\n")
        if answer == "y":
            list1 = Methods.n_grams(text, 10, 4)
            break
        elif answer == "n":
            while True:
                try:
                    k_str = input("Введите K: ")
                    k = int(k_str)
                    n_str = input("Введите N: ")
                    n = int(n_str)
                    if type(n) == int and type(k) == int and n > 0 and k > 0:
                        list1 = Methods.n_grams(text, k, n)
                        break
                except:
                    print("Некорректный ввод.\n")
            break
        else:
            print("Введите корректный символ! ")
    return list1