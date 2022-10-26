# Test 18 --------------------------------------------------------------------- 
from random import randint


def cows_and_bulls():
    rnd_num = str(randint(1, 9)) + str(randint(1, 9)) + str(randint(1, 9)) + str(randint(1, 9))
    print(rnd_num)
    guess = ''
    guess_counter = 0
    while guess != rnd_num:
        guess_counter += 1
        guess = input("Enter a 4-digit number:\n")
        cow = 0
        bull = 0
        for index, number in enumerate(rnd_num):
            if number in guess:
                if number == guess[index]:
                    cow += 1
                else:
                    bull += 1
        print(f"{cow} cows, {bull} bulls.")
    return f'Game ended with {guess_counter} total guess.'


def main():
    print(cows_and_bulls())


if __name__ == "__main__":
    main()
