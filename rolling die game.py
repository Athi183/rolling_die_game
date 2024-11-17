import random
print("\tHii!!!!What do I call you??\n")
name=input("Your Name please...\t")
print("Hello "+name+" !!!!Let's Begin\n")
number=int(input("Before playing, tell me how many times you wanna roll the die:"))
count=0
for i in range(number):
    ch=input("Do you want to roll the die ->(y/n):")
    if ch=='y':
        first=random.randint(1,6)
        second=random.randint(1,6)
        print(f'({first}, {second})') #formatted type of print statement
        count+=1
        print(count," Roll")
    elif ch=='n':
        print("Thank you for playing")
        break
    else:
        print("Invalid choice")
