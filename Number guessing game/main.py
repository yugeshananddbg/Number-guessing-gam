import random as r
print('''
Number Guessing game 
----------------------------------------------------------------

''')
a=int(input('Starting range :- '))
b=int(input('End range :- '))+1
Cnum= r.randrange(a,b)
count = 5

print("You have 5 chance to guess the number")
print("_____________________________________________________________________")
while count > 0:
    print('''
      Chance left :- {}''' .format(c,count))

    Unum= int(input("Guess the Number :- " ))
    if Unum==Cnum:
        print('''
        You have guess the number 
        Finally You won the game''')
        break
    elif Unum < Cnum:
        print("Your guessed Number : {} is too low".format(Unum))
        count= count-1

    else:
        print("Your guessed Number : {} is too High".format(Unum))
        count = count - 1


