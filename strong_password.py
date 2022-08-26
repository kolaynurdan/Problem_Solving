#Louise joined a social networking site to stay in touch with her friends. The signup page required her to input a name and a password. However, the password must be strong. The website considers a password to be strong if it satisfies the following criteria:

#Its length is at least .
#It contains at least one digit.
#It contains at least one lowercase English character.
#It contains at least one uppercase English character.
#It contains at least one special character. The special characters are: !@#$%^&*()-+
#She typed a random string of length  in the password field but wasn't sure if it was strong. Given the string she typed, can you find the minimum number of characters she must add to make her password strong?

import sys

def minimumNumber(n, password):
    numbers = "0123456789"
    lower_case = "abcdefghijklmnopqrstuvwxyz"
    upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    special_characters = "!@#$%^&*()-+"
    
    n_bool = 1
    l_bool = 1
    u_bool = 1
    s_bool = 1
    for c in password:
        if c in numbers: n_bool = 0
        elif c in lower_case: l_bool = 0
        elif c in upper_case: u_bool = 0
        elif c in special_characters: s_bool = 0
    return max(6-n, n_bool + l_bool + u_bool + s_bool)

if __name__ == "__main__":
    n = int(input().strip())
    password = input().strip()
    answer = minimumNumber(n, password)
    print(answer)
