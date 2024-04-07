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

while True:
print("            _ _                         _      ")
print("  /\  /\___| (_) ___  _ __     ___ __ _| | ___ ")
print(" / /_/ / _ \ | |/ _ \| '_ \   / __/ _` | |/ __|")
print("/ __  /  __/ | | (_) | | | | | (_| (_| | | (__ ")
print("\/ /_/ \___|_|_|\___/|_| |_|  \___\__,_|_|\___|")
print("choose operation: 1.+ 2.- 3.* 4./")

    wybor = input("choose operation number (1/2/3/4): ")

    if wybor in ('1', '2', '3', '4'):
        liczba1 = float(input("first number: "))
        liczba2 = float(input("second number: "))

        if wybor == '1':
            print("result:", dodawanie(liczba1, liczba2))
        elif wybor == '2':
            print("result:", odejmowanie(liczba1, liczba2))
        elif wybor == '3':
            print("result:", mnozenie(liczba1, liczba2))
        elif wybor == '4':
            print("result:", dzielenie(liczba1, liczba2))

        kontynuacja = input("want continue? (yes/no): ")
        if kontynuacja.lower() != 'yes':
            break
    else:
        print("AntiTroll-antycheat detected wrong number")
