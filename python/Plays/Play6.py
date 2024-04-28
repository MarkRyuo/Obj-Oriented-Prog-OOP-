
_order = input("What is your order?: ")

while not _order :
    _order = input("What is your order?: ")

list_ = [
    "Americano",
    "Barako",
    "Mocha",
    "Latte"
]

for count in range(1, 4) :
    print(list_[count])

