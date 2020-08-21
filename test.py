def get_new_password():
    get_password = input("Enter a new password. ")
    password = str(get_password)
    return(password)

def length_test (password):
    if len(password) > 8:
        return((True, None))
    else:
        return(False, "Password not long enough.")

##def Valid_password_mixed_case(password):
    #letters = set(password)

    #lower = any(letter.islower() for letter in letters)
    #upper = any(letter.isupper() for letter in letters)
    #if not upper:
        #print("Password does not conatin any uppercase letters")

    #if not lower:
        #print("Password does not conatin any lowercase letters")

#def check_password():
    #password = get_new_password()
    #if length_test(password) and \
        #Valid_password_mixed_case(password):

        #print("Congratulations! This password is valid")

##check_password()
#password = "lucaGreenshields"


print(get_new_password)
#print(length_test(password))
