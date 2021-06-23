# # if condition
#
# weather = "sunny"
#
# if weather == "sunny": # if this line is true, the next line will be run
#     print("enjoy the weather")
#
# if weather != "rainy": # if this line is not true, the next line will be run
#     print("weather is not rainy, enjoy while you can")
#
# # greater than/less than
#
# age = 17
#
# if age < 18:
#     print("you are not old enough to watch this movie")
#
# # elif and else ensure all possibilities are met for the user
#
# if age < 18:
#     print("you are not old enough to watch this movie")
# elif age >= 18:
#     print("enjoy the movie")
# else:
#     print("there has been an error processing your age")

# for and while loops

# shopping_list = ["eggs", "apple", "milk", "bread", "butter"]
#
# for item in shopping_list:
#     print(item)

# adding if condition

# shopping_list = ["eggs", "apple", "milk", "bread", "butter"]
#
# for items in shopping_list:
#     if items == "bread":
#         break
#     print(items)

# using loops with dicts

# student_data = {
#     "student_name": "Tom",
#     "course": "DevOps",
#     "course_topics": 4,
#     "topic_names": ["Business Week", "Python", "Virtualisation with Vagrant", "AWS Cloud"]
# }
# # print(student_data)
#
# for data in student_data:
#     print(data)
#
# for data in student_data.values():
#     if data == "Tom":
#         print(data)

# while loops can be used to monitor data

# num = 0
#
# while num < 10:
#     print(f"it's working --> {num}")
#     num += 1

# num = 0
#
# while num < 10:
#     print(f"it's working --> {num}")
#     if num == 5:
#         break
#     num += 1

# Let's see how can we interact with our user in the Third Iteration
# prompt the user to input age and restrict to enter in digits only
# check if the data is in digits display it back to the user if not in digits prompt the user with message to enter in digits

# age = input("What is your age?  ")
#
# while age.isdigit() != True:
#     print("Please enter your age in digits.")
#     age = input("What is your age?  ")
#     if age.isdigit() == True:
#         print(f"Your age is {age}")
#         break

# end loop without break function

user_prompt = True

while user_prompt:
    age = input("What is your age?  ")
    if age.isdigit() and int(age) < 150:
        print(f"Your age is {age}")
        user_prompt = False
    else:
        print("Please enter a valid age in digits under 150.")