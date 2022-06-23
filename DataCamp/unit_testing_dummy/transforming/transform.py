import re

def str_of_int_to_list(string):
    """ Convert a string containing a list to the list in the string.

    :params string: string to get the list from
    :return: the list written in the string. Return None if the list does not contain integers
    
    >>> str_to_list("[3, 6]")
    [3, 6]
    """
    temp = re.findall(r"\[(.*?)\]", string)  # gets what is contained in the string as a list with one element
    try:
        temp_separated = temp[0].split(",")  # split the string
    except IndexError:  # l'input ne contient pas de brackets
        print("Assurez-vous de bien rentrer une liste")
        return None
    try:
        res = [int(num) for num in temp_separated]
    except ValueError:  # the list contained in the string contains at least one non integer 
        print("Rentrez des int dans la liste")
        res = None
    finally:
        return res


tu = "[1000, 1282, 198, 37.5]"
str_of_int_to_list(tu)
r = input()
str_of_int_to_list(r)



