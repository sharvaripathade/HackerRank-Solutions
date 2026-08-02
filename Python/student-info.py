"""
Program: Student Information Collector
Author: Sharvari Pathade
Chapter: 02 - Getting Started with Python

Description:
This program collects information from the user
and displays it in a formatted manner.
"""

print("=" * 50)
print("      STUDENT INFORMATION COLLECTOR")
print("=" * 50)

# Taking input from the user
name = input("Enter your name: ")
age = input("Enter your age: ")
college = input("Enter your college: ")
language = input("Enter your favorite programming language: ")
dream_job = input("Enter your dream job: ")

print("\n" + "=" * 50)
print("         YOUR INFORMATION")
print("=" * 50)

print(f"👤 Name                 : {name}")
print(f"🎂 Age                  : {age}")
print(f"🏫 College              : {college}")
print(f"💻 Favorite Language    : {language}")
print(f"🎯 Dream Job            : {dream_job}")

print("=" * 50)
print("Thank you! Keep learning Python. 🚀")
print("=" * 50)