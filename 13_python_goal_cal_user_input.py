from datetime import datetime

user_input = input("Enter your goal with a deadline.... (Format: dd.mm.Y) \n")

split_input = user_input.split(":")
goal = split_input[0]
deadline = split_input[1]

deadline_date = datetime.strptime(deadline, "%d.%m.%Y")
current_date = datetime.today()

calculation = deadline_date - current_date
print(f"Dear user time remaining of your goal {goal} is {calculation.days} days.")

