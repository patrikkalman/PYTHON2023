
import random

def generate_lotto_numbers(lotto_type):
    if lotto_type == 5:
        min_num, max_num, count = 1, 90, 5
    elif lotto_type == 6:
        min_num, max_num, count = 1, 45, 6
    elif lotto_type == "toto":
        min_num, max_num, count = 1, 90, 14
    elif lotto_type == "skandinav":
        min_num, max_num, count = 1, 35, 7
    else:
        return "Érvénytelen lottó típus. Válasszon 5, 6, toto vagy skandináv közül."

    numbers = generate_random_numbers(min_num, max_num, count)
    return numbers

def generate_random_numbers(min_num, max_num, count):
    return sorted(random.sample(range(min_num, max_num + 1), count))

def main():
    print("Szerencsejáték tipp generátor")
    print("Válasszon a következő lehetőségek közül:")
    print("1. 5-ös lottó")
    print("2. 6-os lottó")
    print("3. Toto")
    print("4. Skandináv lottó")
    print("0. Kilépés")

    while True:
        choice = input("Válasszon egy lehetőséget (1/2/3/4/0): ")

        if choice == "0":
            break
        elif choice in ["1", "2", "3", "4"]:
            lotto_type = int(choice) if choice != "3" else "toto"
            numbers = generate_lotto_numbers(lotto_type)
            print("A generált számok:", numbers)
        else:
            print("Érvénytelen választás. Válasszon 1, 2, 3, 4 vagy 0 közül.")

if __name__ == "__main__":
    main()
