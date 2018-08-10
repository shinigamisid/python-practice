#program to check if a given three digit number is a palindrome

def palincheck(num):
    num = int(num)
    hun_num = (num // 100) * 100
    ten_num = (num // 10) * 10 - hun_num
    unit_num = num - hun_num - ten_num
    print(hun_num, ten_num, unit_num)
    inv_hun_num = hun_num // 100
    inv_unit_num = unit_num * 100
    inv_num = inv_hun_num + ten_num + inv_unit_num
    print("Inverted number: ", inv_num)
    if num == inv_num:
        print("Your number is a palindrome, huzzah!")
    else:
        print("Your number isn't a palindrome :(")
