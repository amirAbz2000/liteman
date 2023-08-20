def password_generator(min,max):
    import random
    cs = True
    ls = True
    n = True
    sy = True
    global basic_password
    random_length = random.randint(min,max)
    basic_password = ""
    strings = "abcdefghijklmnopqrstuvwxyz"
    numbers = "123456789"
    upper_strings = strings.upper()
    symbol = "!@#$%^&*(){}[]"
    list_character = [strings , numbers , upper_strings , symbol ]
    for i in range (1):
        basic_password += random.choice(strings)
        basic_password += random.choice(numbers)
        basic_password += random.choice(upper_strings)
        basic_password += random.choice(symbol)
        for j in range(random_length - 4):
            title = random.choice(list_character)
            basic_password += random.choice(title)


def length_checker(min , max):
    looper = True

    while looper :
         if (5 < min < 17 ) and (5 < max < 17 ) and ( min < max ) :
             looper = False
         else :
             print("maybe your number isn't  between 6-16 or your min isn't lower than max")
             min = int(input(" enter your minimum length "))
             max = int(input(" enter your maximum length "))

    basicpass= open("basic password generator .txt", "w")

    counter = 1
    for i in range (5):
        password_generator(min,max)
        basicpass.write(f"{counter})")
        basicpass.write(basic_password)
        basicpass.write("\n")
        counter += 1