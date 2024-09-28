math = int(input("What was your math score: "))
english = int(input("What was your English score: "))
science = int(input("What was your science score? "))
history = int(input("What was your history score? "))

combined_score = math + english + science + history
average_percentage = (combined_score / 400) * 100

print("Your average percentage is:", average_percentage)