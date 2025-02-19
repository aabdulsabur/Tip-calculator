'''
lets work on a tip calculator.
it should as customers
1. the total amount of their bill
2. ask for tip percentage
3. calculate tip and add to bill
4. ask for number of people sharing bill
5. divide bill equally
'''

def main():
    # collect bill details
    while True:
        try:
            billAmount = float(input('Enter bill amount: $ '))
            tipPercent = float(input('Enter tip percentage (10, 20, 30, etc.): % '))
            break
        except ValueError:
            print("Invalid input. Please enter a numeric value. ")

    # Calculate tip and add to bill
    tipAmount = (tipPercent / 100) * billAmount
    netBill = tipAmount + billAmount
    print(f"Total amount to pay is $ {netBill:.2f}")

    splitBill = input('Do you want to split the bill? (Enter 1 for Yes): ')
    print("\n==========================")
    if splitBill == '1':
        while True:
            try:
                grpCount = int(input('Enter number of people to split bill (1, 2, 3, etc.): '))
                break
            except ValueError:
                print('Enter a valid number or 1 to continue')

        splittedBill = shareBill(netBill, grpCount)
        print(f'Each person to pay $ {splittedBill:.2f}')

    else:
        print(f"Total amount to pay: {netBill:.2f}")

def shareBill(bill: float, grpCount: int) -> float:
    return bill / grpCount


if __name__ == "__main__":
    main()