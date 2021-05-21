import random
import time

def four_random(omit=False, omit_number=0):
    random1 = random.randint(1, 2)
    if not omit:
        if random1 == 1:
            return random.randint(1, 2)
        elif random1 == 2:
            return random.randint(3, 4)
    elif omit:
        if random1 == 1:
            if omit_number == 1:
                return 2
            elif omit_number == 2:
                return 1
            return random.randint(1, 2)
        elif random1 == 2:
            if omit_number == 3:
                return 4
            elif omit_number == 4:
                return 3
            return random.randint(3, 4)


Main_Password = [0, 0, 0, 0]


def password(num=1):
    if num == 1:
        Main_Password[0] = four_random()
        password(2)
    elif num == 2:
        Main_Password[1] = four_random(True, Main_Password[0])
        password(3)
    elif num == 3:
        RandomList = []
        for i in range(1, 5):
            if i is not Main_Password[0] and i is not Main_Password[1]:
                RandomList.append(i)
        p = random.randint(1, 2)
        if p == 1:
            Main_Password[2] = RandomList[0]
        elif p == 2:
            Main_Password[2] = RandomList[1]
        password(4)
    elif num == 4:
        for i in range(1, 5):
            if i is not Main_Password[0] and i is not Main_Password[1] and i is not Main_Password[2]:
                Main_Password[3] = i
                return


password()


def Enter_Pass(i=1):

    if i == 1:
        try:
            inp = int(input("\nNumber1:- "))
        except:
            print("Please enter a number")
            Enter_Pass()
        if inp == Main_Password[0]:
            Enter_Pass(2)
        else:
            print("Failed XD")
            print("Password:- " + str(Main_Password))
            password()
            Enter_Pass()
    elif i == 2:
        try:
            inp = int(input("Number2:- "))
        except:
            print("Please enter a number")
            Enter_Pass(2)
        if inp == Main_Password[1]:
            Enter_Pass(3)
        else:
            print("Failed XD")
            print("Password:- " + str(Main_Password))
            password()
            Enter_Pass()
    elif i == 3:
        try:
            inp = int(input("Number3:- "))
        except:
            print("Please enter a number")
            Enter_Pass(3)
        if inp == Main_Password[2]:
            Enter_Pass(4)
        else:
            print("Failed XD")
            print("Password:- " + str(Main_Password))
            password()
            Enter_Pass()
    elif i == 4:
        try:
            inp = int(input("Number4:- "))
        except:
            print("Please enter a number")
            Enter_Pass(4)
        if inp == Main_Password[3]:

            print("YouPassed! \nNow do it again XD")
            time.sleep(1)
            password()
            Enter_Pass()
        else:
            print("Failed XD")
            print("Password:- " + str(Main_Password))
            password()
            Enter_Pass()

print("This is a game\n")
time.sleep(2)
print("Rules:- ")
time.sleep(2)
print("There is a 4 number password")
time.sleep(2)
print("You have to guess each number")
time.sleep(2)
print("Failing even one number will lead to the password being reset")
time.sleep(3)
print("The numbers can only be 1,2,3,4")
time.sleep(2)
print("And no number is repeated")
time.sleep(1.3)
print("\nGoodLuck NERD B)")

time.sleep(0.5)
Enter_Pass()
