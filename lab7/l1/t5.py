#25341a05l1 vinay

def celsius_to_fahrenheit(c):
    return (c * 9 / 5) + 32


def fahrenheit_to_celsius(f):
    return (f - 32) * 5 / 9


while True:
    print("\n1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    print("3. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        c = float(input("Enter temperature in Celsius: "))
        print("Fahrenheit =", celsius_to_fahrenheit(c))

    elif choice == 2:
        f = float(input("Enter temperature in Fahrenheit: "))
        print("Celsius =", fahrenheit_to_celsius(f))

    elif choice == 3:
        print("Exiting...")
        break

    else:
        print("Invalid choice")

'''output :
1. Celsius to Fahrenheit
2. Fahrenheit to Celsius
3. Exit
Enter your choice: 1
Enter temperature in Celsius: 25
Fahrenheit = 77.0

1. Celsius to Fahrenheit
2. Fahrenheit to Celsius
3. Exit
Enter your choice: 2
Enter temperature in Fahrenheit: 98.6
Celsius = 37.0

1. Celsius to Fahrenheit
2. Fahrenheit to Celsius
3. Exit
Enter your choice: 3
Exiting...
'''