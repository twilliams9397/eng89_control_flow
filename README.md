# Control Flow with if, elif and else conditions
- control flow methods control flow of programme dependent of conditions
- syntax if variable - condition variable:
- condition can be equal to/not equal to:
```python
weather = "sunny"

if weather == "sunny": # if this line is true, the next line will be run
    print("enjoy the weather")
if weather != "rainy": # if this line is not true, the next line will be run
    print("weather is not rainy, enjoy while you can")
```
- condition can be greater than/less than:
```python
age = 17

if age < 18:
    print("you are not old enough to watch this movie")
```
- `elif` and `else` ensure all condition variables are dealt with
```python
age = 17

if age < 18:
    print("you are not old enough to watch this movie")
elif age >= 18:
    print("enjoy the movie")
else:
    print("there has been an error processing your age")
```
## Loops - for loops and while loops

- loops help us iterate through our data
- such as lists, dicts and sets etc
- syntax `for variable in data:`
```python
shopping_list = ["eggs", "apple", "milk", "bread", "butter"]

for items in shopping_list:
    print(items)
```
- this will print each item in the `shopping_list` variable
- for loops can be used together with `if` statements:
```python
shopping_list = ["eggs", "apple", "milk", "bread", "butter"]

for items in shopping_list:
    if items == "bread":
        break
    print(items)
```
- this above code will check the `if` statement for each variable in the list and execute the `break` function as soon as the condition is met, giving the below return:
```python
eggs
apple
milk
```
- loops can also iterate over dictionaries
- iterating over `data` in a dict will iterate over the keys
```python
student_data = {
    "student_name": "Tom",
    "course": "DevOps",
    "course_topics": 4,
    "topic_names": ["Business Week", "Python", "Virtualisation with Vagrant", "AWS Cloud"]
}

for data in student_data:
    print(data)
```
will return:
```python
student_name
course
course_topics
topic_names
```
- conditions in the values or keys can be checked with `if` statements
```python
for data in student_data.values():
    if data == "Tom":
        print(data)
```
will return:
```python
Tom
```
## While loops will leep iterating until a condition is met
- syntax `while condition for varaiable:`
- this below code will only run while the `num` variable is lower than 10
```python
num = 0

while num < 10:
    print(f"it's working --> {num}")
    num += 1
```
- it will return:
```python
"it's working --> 0"
"it's working --> 1"
"it's working --> 2"
"it's working --> 3"
"it's working --> 4"
"it's working --> 5"
"it's working --> 6"
"it's working --> 7"
"it's working --> 8"
"it's working --> 9"
```
- while loops can be broken with `if` statements:
```python
num = 0

while num < 10:
    print(f"it's working --> {num}")
    if num == 5:
        break
    num += 1
```
- the above code will exit the while loop when the `num` value reaches 5, so returns the above code up to (including) the "5" line.
- `while` loops can also take user input and check it against certain conditions:
```python
age = input("What is your age?  ")

while age.isdigit() != True:
    print("Please enter your age in digits.")
    age = input("What is your age?  ")
    if age.isdigit() == True:
        print(f"Your age is {age}")
        break
```
- the above code prompts the user for their age and checks if it is in `int` form with the `.isdigit()` function
- if the data is not in this format it prints the error message and re prompts the user and restarts the loop
- when the condition is met, the user's age is returned and the `while` loop is stopped with the `break`
- loops can also be ended without a `break` function
```python
user_prompt = True

while user_prompt:
    age = input("What is your age?  ")
    if age.isdigit() and int(age) < 150:
        print(f"Your age is {age}")
        user_prompt = False
    else:
        print("Please enter a valid age in digits under 150.")
```
- the above code will keep prompting the user until a valid age is input
- when a valid age is input the `user_prompt` is set to `False` and therefore the `while` condition is no longer met, so the loop does not continue