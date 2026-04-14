name: str = input("Enter your name: ")
noun_a: str = input("Enter your noun: ")
verb_a: str = input("Enter your verb: ")
noun_b: str = input("Enter your noun: ")
verb_b: str = input("Enter your verb (past tense): ")
number_a: str = input("Enter a number: ")
number_b: str = input("Enter another number: ")


story: str = f"""
----------------------------------------------
this is a story about a story about {name}, a strong and beautiful {noun_a} who
loved to {verb_a}.
{name} once {verb_b} and won a {noun_b} as a prize.
Isn't that cooolll!
Today, {name} is {int(number_a) + int(number_b)} years old and has retired from all adventures.

and will shall continue on own next episode of life.

-----------------------------------------------
"""

print(story)