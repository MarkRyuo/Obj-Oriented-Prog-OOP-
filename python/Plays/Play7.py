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


def _Name() :
    while True :
        _person = input(
            f"Please choose a number ({CHO_NUM1} or {CHO_NOM2}): "
            )
        if _person.isdigit() :
            _person = int(_person)
            if _person == 1 or _person == 2 :
                break
            else :
                print("Please choose the right number")
        else :
            print("Choose from the option")
    return _person 

def _process() :
    colname = _Name()
    if colname == 1 :
        _char = Character(_CHAR1["fname"], _CHAR1["fracta"])
        _char.speak()

def main():
    _process()

main()