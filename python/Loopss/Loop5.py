
even_numbers = {
    "2",
    "4",
    "6",
    "8",
    "10",
    "16"
}

def Loop() :
    input1 = input("Enter a number: ")
    if input1.isdigit():
        input1 = int(input1)
        for i in range(even_numbers) :
            input1[i]
            print(input1)


Loop()
