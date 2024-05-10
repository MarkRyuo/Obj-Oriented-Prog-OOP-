import module 
from _Class import Character

# Global Variable
CHO_NUM1 = 1
CHO_NOM2 = 2  

# Import Module / 
# Create List 
# Loop / 
# OOP 

# Create Global Variable for module 

_CHAR1 = module.Char1 
_CHAR2 = module.Char2

_CHAR = Character(_CHAR1["fname"],_CHAR1["codename"],_CHAR1["fracta"])  # Nicole
_CHARR = Character(_CHAR2["fname"],_CHAR2["codename"],_CHAR2["fracta"]) # Moda


def _input1() : # Loop for input character 
    while True :
        _person = input(
            f"Please choose a number ({CHO_NUM1} or {CHO_NOM2}): "
            )
        if _person.isdigit() : # isdigit 
            _person = int(_person)
            if _person == 1 or _person == 2 :
                break
            else :
                print("Please choose the right number")
        else :
            print("Choose from the option")
    return _person 

def _process1() :
    colinput = _input1()
    if colinput == 1 :
        _CHAR.speak()
    elif colinput == 2 :
        _CHARR.speak()

def _input2():
    _talk1 = input("What is your name?: ")

def main():
    _process1()

main()