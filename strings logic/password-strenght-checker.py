
def pass_strenght_checker(password):
    """
    Docstring for pass_strenght_checker
    A password is considered strong if it has:
    1.Minimum length (usually ≥ 8)
    
    2.At least one lowercase letter
    
    3.At least one uppercase letter
    
    4.At least one digit
    
    5.At least one special character(@ # $ % & ! etc.)
    """
    if len(password)<8:
        return "password must be atleast lenght of 8"   

    has_digit=False
    has_upper=False
    has_lower=False
    has_special=False
    special_chars="!@#$%^&*~"


    for ch in password:
        if ch.isdigit():
            has_digit=True
        elif ch.isupper():
            has_upper=True
        elif ch.islower():
            has_lower = True
        elif ch in special_chars:
            has_special = True

    if has_lower and has_digit and has_special and has_upper:
        return "strong password"
    elif has_digit and has_special and has_upper:
        return "medium : add lowercase"
    elif has_lower and has_special and has_upper:
        return "medium : add digit"
    elif has_lower and has_special and has_digit:
        return "medium : add uppercase"
    elif has_lower and has_digit and has_upper:
        return "medium : add special char"
    else:
        return "Medium: Add uppercase, digit, and special character"    







if __name__=="__main__":
    print(pass_strenght_checker.__doc__)
    password=input("Enter your password:")
    print(pass_strenght_checker(password))