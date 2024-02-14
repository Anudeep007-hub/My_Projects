import random,time
avik_points,user_points = 0,0
m = ["rock","paper","scissors"]


print("Hi I am AVIK, I love to play this game are you ready :)")
user_name = input("Enter your name: ")
while True:
    computer_input = random.choice(m)
    user_input = input("choose one among rock/paper/scissors('q'-quit): ")
    if user_input.lower() == "rock":
        if computer_input == "rock":
            print("I too have choosen rock, it's a TIE!!!")
        elif computer_input == "paper":
            print("I have choosen paper, I won 😁😁😁")
            avik_points += 1
        elif computer_input == "scissors":
            print("I have choosen scissors,😒😒")
            user_points += 1

    elif user_input.lower() == "paper":
        if computer_input == "rock":
            print("I have choosen rock,😒😒")
            user_points += 1
        elif computer_input == "paper":
            print("I too have choosen paper, it's a TIE!!!")
        elif computer_input == "scissors":
            print("I have choosen scissors, I won 😁😁😁")
            avik_points += 1
    elif user_input.lower() == "scissors":
        if computer_input == "rock":
            print("I have choosen rock, I won 😁😁😁")
            avik_points += 1
        elif computer_input == "paper":
            print("I have choosen paper,😒😒")
            user_points += 1
        elif computer_input == "scissors":
            print("I too have choosen scissors, it's a tie")
    elif user_input.lower() == "q":
        break
            
    else:
        print("Type correctly!!!!")

print("The winner is ")
for i in range(3,0,-1):
    time.sleep(1)
    print(i)
time.sleep(1)

if user_points > avik_points:
    print(f"{user_name} with {user_points} points🥱🥱🥱")
    print(f"I got {avik_points} points")
elif user_points < avik_points:
    print(f"AVIK with {avik_points} points 😎😎😎😎😎")
    print(f"You got {user_points} points 😏😏😏😏😏😏😏😏")
elif user_points == avik_points:
    print("Match Tied 🤦‍♂️🤦‍♂️🤦‍♂️")


        
        
