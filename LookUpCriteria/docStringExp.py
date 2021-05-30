"""nametest
    - ask user for enter the Username (suname and name)
    - each letter does have a value
    - calculate the checksum of the name and returns it as int value

    tipp:
        special signs wil be represented by normal signs like: ae, oe, ue, ss

    attributes:
        name: ALFBECK
        date: 12.04.2021
        version: 0.0.1
"""
import pandas as pd

# create skript letter database
letter_list = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
clean_dict = {"ä":"ae", "ö":"oe", "ü":"ue", "ß":"ss"}
letter_dict = {}

for letter in letter_list:
    letter_dict[letter] = letter_list.index(letter)

 

def clean_userinput(text:str, conversion_dict: dict, before=None) -> str:
    """Userinput cleaning
    Translate words from a text using a conversion dictionary

    source: https://stackoverflow.com/questions/14156473/can-you-write-a-str-replace-using-dictionary-values-in-python
    
    Arguments:
        text: the userinput
        conversion_dict: the conversion dictionary u need to define as dict first
        before: a function to transform the input e.g. str.lower, str.upper ...
        (by default it will to a lowercase)

    Test:
        * length of result string must be 2
        * unguilty sign
    """
    # if empty:
    if not text:
        return text

    # preliminary transformation:
    before = before or str.lower
    t = before(text)
    for key, value in conversion_dict.items():
        t = t.replace(key, value)
    return t

   

def get_name_from_userinput() -> tuple:
    """get userinput
        ask user for name type-in and returns a tuple with name and suname

        param:
            nothing

        return:
            suname, name as tuple

        test:
            * is userinput string?
            * is userinput empty?
    """
    user_input = input("suname and name in format:[Suname Name]:")
    user_input = clean_userinput(user_input, clean_dict)
    #print("DEBUG::", user_input)
    my_suname, my_name = str(user_input.split()[0]).lower(), str(user_input.split()[-1]).lower()
    return my_suname, my_name



def calc_name_value(name:str) -> int:
    """calc name value
        calculate value of a name

        param:
            name(str): name for calculation

        return:
            sum of name calculation

        test:
            * check if letter exist and is in dictionary
            * check if value is correct calculated
            * what happens if we have more guilty signs inside the name?
    """
    calculation = 0
    try:
        for letter in name:
            calculation += letter_dict[letter]

    except Exception as general_error:
        print("sth. went horrible wrong:" + str(general_error))

    finally:
        return calculation



if __name__ == "__main__":
    # routine here
    my_suname, my_name = get_name_from_userinput()
    your_name_weight = calc_name_value(my_name) + calc_name_value(my_suname)
    print("your name value is: ", str(your_name_weight))
    print("divided with 2 is:", str(your_name_weight/2))
