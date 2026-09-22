
# GYM TRACKER - PYTHON DICTIONARY PRACTICE
# ==========================================


print("Welcome to the Gym Tracker!")

# my_name = "Vihanga"
# target_bicep_curls = 10
# print(f"My name is {my_name} and my target is {target_bicep_curls} reps")

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

while True:
    day_type = input("\nWhat's the plan today, bro? (Push / Pull / Leg / Cardio / Core / Rest): ").strip().lower()
    if day_type == "exit" or day_type == "quit":
        print("Catch you later, bro! Go crush your goals today! 💪🔥")
        break
    elif day_type == "add":
        new_day = input("Enter the name of the new routine (e.g., Arms):").strip().lower()
        exercises_raw = input("Enter the name of the exercise (e.g., Bicep Curls, Skull crushers) :")
        new_exercises = [ex.strip() for ex in exercises_raw.split(",") if ex.strip()]

        if new_day in workout_database:

            workout_database[new_day].extend(new_exercises)
            print(f"Updated {new_day.upper()}! Added {len(new_exercises)} new exercise(s) to your existing list.")
        else:
            workout_database[new_day] = new_exercises
            print(f"Boom! {new_day.upper()} routine has been added to your database!")

    else:
        display_workout(day_type, workout_database)

