"""EX01 hello."""

"""
1. Print Hello
Example output:

What is your name? Mari
Hello, Mari! Enter a random number: 5
Great! Now enter a second random number: 4
5 + 4 is 9

"""
# ask for a name
name = input("What is your name? ")
# ask for first random number
num1 = int(input(f"Hello, {name}! Enter a random number: "))
# ask for second random number
num2 = int(input("Great! Now enter a second random number: "))
# print out sum
print(num1, "+", num2, "is", num1 + num2)
"""
2. Poem
Example output:

Roses are red,
violets are blue,
I love to code
And so will you!

"""
color = str(input("Enter a color: "))
objects = str(input("Enter objects: "))
activity = str(input("Enter an activity: "))

print(f"Roses are {color}, {objects} are blue, I love to {activity} And so will you!")

"""
3. GreetingsGreetingsGreetings
Example output:

Enter a greeting: Hello
Enter a recipient: world
How many times to repeat: 3
Hello world! Hello world! Hello world!

"""
greeting = str(input("Enter a greeting: "))
recipient = str(input("Enter a recipient: "))
repeat = int(input("How many times to repeat: "))

nice_greeting = (f"{greeting} {recipient}! ")
output = nice_greeting * repeat

print(output)
