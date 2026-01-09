"""
An email validator checks whether an email follows basic rules, not whether it actually exists.
"""

import re
def email_vaildator(email_id):
    pattern=re.compile(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')
    return re.match(pattern,email_id) is not None


if __name__=="__main__":
    email_id=input("enter your email id:")
    email_vaildator(email_id)
    if email_vaildator(email_id):
        print("vaild email")
    else:
        print("invaild email try again")    