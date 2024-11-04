from random import randint,choice,shuffle
letter_lower = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
letter_upper = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
number= ['1','2','3','4','5','6','7','8','9','0']
symbols = ['!','@','#','$','%','^','&','*']

nr_letters = randint(2,4)
nr_symbols = randint(2,4)
nr_number = randint(1,2)

password_list = []
password_letters = [choice(letter_lower) for _ in range(nr_letters) ]
password_number = [choice(number) for _ in range(nr_number)]
password_symbol = [choice(symbols) for _ in range(nr_symbols)]

password_list = password_letters + password_number + password_symbol
shuffle(password_list)
password = "".join(password_list)
print(password)




