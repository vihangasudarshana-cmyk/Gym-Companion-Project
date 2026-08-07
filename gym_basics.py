# ==========================================
# GYM TRACKER - PYTHON DICTIONARY PRACTICE
# ==========================================


print("Welcome to the Gym Tracker!")

# my_name = "Vihanga"
# target_bicep_curls = 10
# print(f"My name is {my_name} and my target is {target_bicep_curls} reps")
#
#
#
# favorite_exercise = input("What is your favorite exercise,bro? ")
# print(f"Awesome! bro, {favorite_exercise} is beast of the movement.")
#
#  if day_type == "push":
#     print("\nHere is your current Push Day inventory, bro:")
#     for exercise in push_day:
#         print(exercise)
#
# elif day_type == "pull":
#     print("\nPull day! Time to smash that back and biceps, bro!")
#     for exercise in pull_day:
#         print(exercise)
#
# elif day_type == "leg":
#     print("\nLeg day! Never skip it. Time for deep squats and power!")
#     for exercise in leg_day:
#         print(exercise)
#
# elif day_type == "rest":
#     print("\nNice. Relax, recover, and grow today! Here is your checklist, bro:")
#     for exercise in rest_day:
#         print(exercise)


workout_database = {
"push" : ["Incline bench press" ,"Chest dips" ,"Shoulder press" ,"Lateral raises" ,"Triceps pushdown"],
"pull" : ["Barbell Rows", "Lat Pulldown", "Single Arm Dumbbell Rows", "Face Pulls", "Barbell Curls","Hammer Curls"],
"leg" : ["Barbell Back Squat", "Romanian Deadlift", "Leg Extensions", "Leg Curl","Calf raises "],
"rest" : ["Do light activities or active stretching", "Drink 3-4L of pure water",
            "Hit your protein targets", "Get 8+ hours sleep"],
"cardio" : ["Cycling on Millennium Greenway", "Treadmill run", "Jump rope"]
}
workout_database["core"] = ["Plank", "Hanging Leg Raises", "Ab Wheel"]   #add new routine
workout_database["rest"] = ["Active recovery walk", "Hydrate", "8+ hours sleep"]   #update
workout_database["push"].append("Cable Flyes")

def display_workout(selected_day, database):   #Takes the day typed by the user and prints the routine from the database.
    if selected_day in database:
        print(f"\nAwesome! Here is your routine for {selected_day.upper()}, bro:")

        for activity in database[selected_day]:
            print(f"- {activity}")
    else:
        print("\nHmm, I don't recognise that routine, bro. Make sure to type Push, Pull, Leg, Cardio, Core, or Rest!")

day_type = input("What's the plan today, bro? (Push / Pull / Leg / Cardio / Core / Rest): ").strip().lower()

display_workout(day_type, workout_database)

