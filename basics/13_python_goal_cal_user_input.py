from datetime import datetime, date

user_input = input(f"Enter your goal with a deadline.... (eg, Python:{date.today().strftime('%d.%m.%Y')}) \n")

split_input = user_input.split(":")
goal = split_input[0]
deadline = split_input[1]
print(deadline)


deadline_date = datetime.strptime(deadline, "%d.%m.%Y")
current_date = datetime.today()

calculation = deadline_date - current_date
print(f"Dear user time remaining of your goal {goal} is {calculation.days} days.")

