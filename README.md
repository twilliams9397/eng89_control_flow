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
if age < 18:
    print("you are not old enough to watch this movie")
elif age >= 18:
    print("enjoy the movie")
else:
    print("there has been an error processing your age")
```
## Loops - for loops and while loops
