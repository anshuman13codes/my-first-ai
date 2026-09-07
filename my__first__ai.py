from colorama import Fore, Style, init
import datetime
import random

init(autoreset=True)

# --- Colourful Welcome ---
print(Fore.CYAN + Style.BRIGHT + """
  ____          _ _           ____          _ _          
 |  _ \   __ _ | | |__   ___ |  _ \   __ _ | | |__   ___ 
 | |_) | / _` || | '_ \ / _ \| |_) | / _` || | '_ \ / _ \\
 |  _ < | (_| || | | | |  __/|  _ < | (_| || | | | |  __/
 |_| \_\ \__,_||_|_| |_|\___||_| \_\ \__,_||_|_| |_|\___|
""")
print(Fore.YELLOW + "I am your first AI - Made for Microsoft Dream!\n")

name = input(Fore.WHITE + "What is your name? ")
print(Fore.GREEN + f"\nWow {name}! Nice to meet you!" + Style.RESET_ALL)

# --- Main Menu Loop ---
while True:
    print(Fore.MAGENTA + "\n--- What should I do? ---")
    print(Fore.WHITE + "1. Check Prime Number")
    print("2. Find Factorial")
    print("3. Print Table")
    print("4. Calculator")
    print("5. Tell me a Joke / Motivation")
    print("6. What is the time?")
    print("7. Exit AI")

    choice = input(Fore.YELLOW + "\nEnter your choice (1-7): ")

    if choice == '1':
        n = int(input("Enter number: "))
        is_prime = True
        if n < 2:
            is_prime = False
        else:
            for i in range(2, int(n**0.5)+1):
                if n % i == 0:
                    is_prime = False
                    break
        if is_prime:
            print(Fore.GREEN + f"{n} is PRIME! 🔥")
        else:
            print(Fore.RED + f"{n} is NOT prime.")

    elif choice == '2':
        n = int(input("Enter number for factorial: "))
        fact = 1
        for i in range(1, n+1):
            fact *= i
        print(Fore.CYAN + f"Factorial of {n} is {fact}")

    elif choice == '3':
        n = int(input("Which table you want? "))
        for i in range(1, 11):
            print(Fore.BLUE + f"{n} x {i} = {n*i}")

    elif choice == '4':
        a = float(input("First number: "))
        b = float(input("Second number: "))
        op = input("Operation (+, -, *, /): ")
        if op == '+': print(Fore.GREEN + f"Answer: {a+b}")
        elif op == '-': print(Fore.GREEN + f"Answer: {a-b}")
        elif op == '*': print(Fore.GREEN + f"Answer: {a*b}")
        elif op == '/': print(Fore.GREEN + f"Answer: {a/b}")
        else: print(Fore.RED + "Wrong operation")

    elif choice == '5':
        jokes = [
            "Why do programmers love Maths? Because it has no bugs, only features!",
            "You will definitely get into Microsoft - your logic is strong!",
            "Maths + Code = Google Job! Keep going!"
        ]
        print(Fore.YELLOW + random.choice(jokes))

    elif choice == '6':
        now = datetime.datetime.now()
        print(Fore.CYAN + f"Time is: {now.strftime('%H:%M:%S')}")

    elif choice == '7':
        print(Fore.CYAN + f"\nBye {name}! Radhe Radhe! See you tomorrow for Version 3 - Voice AI! 🙏")
        break

    else:
        print(Fore.RED + "Wrong choice, try again!")