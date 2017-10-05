import Calculator


C = Calculator.calc()


def main():
    print('-------Simple Calculator--------')
    print('-------Press 1 for Addition')
    print('-------Press 2 for Subtraction')
    print('-------Press 3 for Multiplication')
    print('-------Press 4 for Division')
    print('-------Press 5 for Square Root')
    print('-------Press any other key to exit')

    try:
        choice = int(input('Enter Choice: '))

        if choice == 1:
            a = int(input('First number: '))
            b = int(input('Second number: '))

            C.add(a, b)

        elif choice == 2:
            a = int(input('First number: '))
            b = int(input('Second number: '))

            C.sub(a, b)

        elif choice == 3:
            a = int(input('First number: '))
            b = int(input('Second number: '))

            C.mult(a, b)

        elif choice == 4:
            a = int(input('First number: '))
            b = int(input('Second number: '))

            C.div(a, b)

        elif choice == 5:
            a = int(input('Number to square: '))

            C.square(a)

    except ValueError:
        print('Wrong value type. Try again.')
        exit()

    main()

main()
