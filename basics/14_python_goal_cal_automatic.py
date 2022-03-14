from datetime import datetime

goal_date = "30.03.2022"

current_date = datetime.today()

deadline_date = datetime.strptime(goal_date, "%d.%m.%Y")

calculation = deadline_date - current_date

print(f"Dear user, time remaining of your goal Python is {calculation.days} days.")