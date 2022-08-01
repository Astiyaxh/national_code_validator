national_code = input("Enter your melicode: ")
flag = 0

def normal_melicode(national_code):
    sum , control_digit, validation = 0,0,0
    national_code = int(national_code)
    control_digit = national_code % 10
    national_code = int(national_code / 10)

    for i in range (2, 11, 1):
        sum += (national_code % 10) * i
        national_code = int(national_code / 10)
        
    validation = sum % 11
    if validation < 2 and validation >= 0 and control_digit == validation:
        print(validation," Your national code in valid")
    elif validation < 2 and validation >= 0 and control_digit != validation:
        print(validation," Your national code in Invalid")
    elif validation >= 2:
        if control_digit == 11 - validation:
            print(11 - validation," Your national code in valid")
        else:
            print(11 - validation," Your national code in Invalid")

def zfill_national_code(national_code):
    i, temp, j, control_digit, validation = 0, 0, 10, 0, 0
    control_digit = int(national_code[9])
    while i < (len(national_code)-1):
        temp = int(national_code[i]) * j 
        validation += temp
        i += 1
        j -= 1
        
    validation %= 11
    if validation < 2 and validation >= 0 and control_digit == validation:
        print(validation," Your national code in valid")
    elif validation < 2 and validation >= 0 and control_digit != validation:
        print(validation," Your national code in Invalid")
    elif validation >= 2:
        if control_digit == 11 - validation:
            print(11 - validation," Your national code in valid")
        else:
            print(11 - validation," Your national code in Invalid")
            

while flag == 0:
    if national_code == '1111111111' or national_code == '2222222222' or national_code == '3333333333' or national_code == '4444444444' or national_code == '5555555555' or national_code == '6666666666' or national_code == '7777777777' or national_code == '8888888888' or national_code == '9999999999' or national_code == '0000000000':
        national_code = input("Try again don't be cute with me\nEnter your melicode: ")
    if  (str(national_code[0]) == '0' and str(national_code[1]) == '0' and str(national_code[2] == '0')) or (str(national_code[0]) == '0' and str(national_code[1]) == '0') or (str(national_code[0]) == '0'):
        flag = 1
        zfill_national_code(national_code)
    elif len(national_code) < 10 or len(national_code) > 10:
        national_code = input("Try again your melicode must be 10 digit\nEnter your melicode: ")
    else:
        flag = 1
        normal_melicode(national_code)
