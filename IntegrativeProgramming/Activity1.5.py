"""
Input print: Apple Sharing
N students take K apples and distribute them among each other evenly.
The remaining (the indivisible) part remains in the basket.
How many apples will each single student get? How many apples will remain in the basket?
The program reads the numbers N and K. It should print the two answers for the questions above.
Example input
6
50
Example output
8
2
"""
students = int(input())
apples = int(input())

students_apples = apples // students
remain_apples = apples % students

print(int(students_apples))
print(int(remain_apples))