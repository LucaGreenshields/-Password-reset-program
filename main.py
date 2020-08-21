def get_new_password():
    get_password = input("Enter a new password. ")
    password = str(get_password)
    return(password)

def length_test (password):
    if len(password) > 8:
        return((True, None))
    else:
        return(False, "Password not long enough.")

def uppercase_letter_test (password):
    letters = set(password)
    upper = any(letter.isupper() for letter in letters)
    if upper == True:
        return((True, None))
    else:
        return(False, "No uppercase letters")



def lowercase_letter_test (password):
    letters = set(password)
    lower = any(letter.islower() for letter in letters)
    if lower == True:
        return((True, None))
    else:
        return(False, "No lowercase letters")

def check_list():
    clist = [length_test,
             uppercase_letter_test,
             lowercase_letter_test]
    return(clist)

def valid_new_password(failures):
    if len(failures) == 0:
        return("New password set")
    else:
        return("Not a vaild password the problems are:\n" + "\n".join(failures))



def main():
    #password = get_new_password()
    password = "lucaGreenshields"
    test_results = [ check(password) for check in check_list()]
    failures = [ result[1] for  result in test_results if result[0] == False]
    print(valid_new_password(failures))

main()
