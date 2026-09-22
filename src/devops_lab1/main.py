from lib import add, multiply, subtract


def main():
    x, y = 10, 5
    print(f"Сума {x} + {y} = {add(x, y)}")
    print(f"Добуток {x} * {y} = {multiply(x, y)}")
    print(f"Різниця {x} - {y} = {subtract(x, y)}")


if __name__ == "__main__":
    main()