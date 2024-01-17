s=0
while True:
    
    answer = input("Which animal is known as the 'Ship of the Desert'")
    if answer == "camel":
        print("Correct!")
        s+=1
    else:
        print(f"The answer is 'camel', not {answer!r}")

    answer = input("How many days are there in a week? ")
    if answer == "7":
        print("Correct!")
        s+=1
    else:
        print(f"The answer is '7', not {answer!r}")

    answer = input("How many hours are there in a day? ")
    if answer == "24":
        print("Correct!")
        s+=1
    else:
        print(f"The answer is '24', not {answer!r}")

    answer = input("How many letters are there in the English alphabet? ")
    if answer == "26":
        print("Correct!")
        s+=1
    else:
        print(f"The answer is '26', not {answer!r}")

    answer = input("How many days are there in a year? ")
    if answer == "365":
        print("Correct!")
        s+=1
    else:
        print(f"The answer is '365', not {answer!r}")

    print('You got',s,'/',5)

    check_int=input("Do you want to try again: ").lower()
    if check_int=='no':
        print("Thank you for playing")
        break
    else:
        continue

