
list_ = [
    "Americano",
    "Barako",
    "Mocha",
    "Latte"
]

_display = input("Display the menu?: (Yes/No): ")

while not _display :
    _display = input("Display the menu?: (Yes/No)")

_display = _display.lower()

if _display == "yes" :
    for count in range(0, 4) :
        print(list_[count])
elif _display == "no" :
    exit()
else :
    print(f"{_display} is not ")


_order = input("What is your order?: ")

while not _order :
    _order = input("What is your order?: ")

if _order in list_ :
    print(f"Your order is {_order}")
else :
    print(f"{_order} is not on the list of coffee")








