# CellPhonePlan

def main():
    monthlyPayment = 30
    lateCharge = 0.05
    timeSpent = int(input("Enter the amount of time spent on the phone: "))

    while True:
        if timeSpent <= 700 and timeSpent >= 0:
            print(f"Your monthly payment is {monthlyPayment}")
            break

        if timeSpent > 700:
            minutes = timeSpent - 700
            total = monthlyPayment + (lateCharge * minutes)
            print(f"Your bill's total is {total}")
            break
        elif timeSpent < 0:
            print("you entered a negative number")
            timeSpent = int(input("Enter the amount of time spent on the phone: "))

if __name__ == '__main__':
    main()