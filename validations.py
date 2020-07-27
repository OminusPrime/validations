#!/usr/bin/env python3


def vailidate_user(username, minlen):
    """Checks if the recieved username matches the required conditions."""
    if type(username) != str:
        raise TypeError("username must be a string")
    if minlen < 1:
        raise ValueError("minlen must be at least 1".)
        #if you already have the length of the username, there is no rease to perform
        #this next line
        #if len(username) < minlen:
            #return False
    if not username.isalnum():
        return False
    # Usernames can't begin with a number
    if username [0].isnumeric():
        return False
    return True

main()
"Have the user enter a new username; Pass the length of the parameter"
    user=input("Please enter a new username: ")
    user_length=len(user)
    vailidate_user(user, user_length)
