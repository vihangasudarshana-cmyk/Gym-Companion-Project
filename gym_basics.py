print("Welcome to the Python")

'''my_name = "Vihanga"
target_bicep_curls = 10
print(f"My name is {my_name} and my target is {target_bicep_curls} reps")'''


"""
PLAN FOR TOMORROW:
1. Link this IntelliJ project to my GitHub.
2. Push my first 'gym_basics.py' code online!
3. Start building the actual 'Gym Companion' logic.
"""

'''favorite_exercise = input("What is your favorite exercise,bro? ")
print(f"Awesome! bro, {favorite_exercise} is beast of the movement.")'''

day_type = input("Is it a Gym day or Rest day bro? ")
if day_type == "Gym day":
    print("Let's go! Time to hit the weights and grow bro!")
elif day_type == "Rest day":
    print("Nice. Relax, recover, and stretch out today!")
else:
    print("Hmm, I don't recognize that day type, bro. Type 'Gym' or 'Rest'.")

push_day = ["Incline bench press" ,"Chest dips" ,"Shoulder press" ,"Lateral raises" ,"Triceps pushdown"]
print("\nHere is your current Push Day inventory, bro:")
for exercise in push_day:
    print(f"- {exercise}")