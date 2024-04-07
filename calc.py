def dodawanie(a, b):
    return a + b

def odejmowanie(a, b):
    return a - b

def mnozenie(a, b):
    return a * b

def dzielenie(a, b):
    if b == 0:
        return "you cant divide by zero!"
    else:
        return a / b

print("Welcome, in calculator made by Helion")
print("Choose operation:")
print("1. +")
print("2. -")
print("3. *")
print("4. /")

wybor = input("Choose operation (1/2/3/4): ")

if wybor in ('1', '2', '3', '4'):
    liczba1 = float(input("Give first number: "))
    liczba2 = float(input("Give second number: "))

    if wybor == '1':
        print("Result:", dodawanie(liczba1, liczba2))
    elif wybor == '2':
        print("Result:", odejmowanie(liczba1, liczba2))
    elif wybor == '3':
        print("Result:", mnozenie(liczba1, liczba2))
    elif wybor == '4':
        print("Result:", dzielenie(liczba1, liczba2))

kontynuacja = input("Want continue? (yes/no): ")
        if kontynuacja.lower() != 'yes':
            break

else:
    print("damn, choose correct number")
