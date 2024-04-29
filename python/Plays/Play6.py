
list_ = [
    "Americano",
    "Barako",
    "Mocha",
    "Latte"
]

for count in range(0, 4) :
    print(list_[count])

_order = input("What is your order?: ")

while not _order :
    _order = input("What is your order?: ")

if _order in list_ :
    print(f"Your order is {_order}")
else :
    print(f"{_order} is not on the list of coffee")

