# if condition

weather = "sunny"

if weather == "sunny": # if this line is true, the next line will be run
    print("enjoy the weather")

if weather != "rainy": # if this line is not true, the next line will be run
    print("weather is not rainy, enjoy while you can")

# greater than/less than

age = 17

if age < 18:
    print("you are not old enough to watch this movie")

# elif and else ensure all possibilities are met for the user

if age < 18:
    print("you are not old enough to watch this movie")
elif age >= 18:
    print("enjoy the movie")
else:
    print("there has been an error processing your age")