import requests

import xlsxwriter

from decouple import config

from datetime import date, datetime

headers = {
    'x-app-id': config('APPLICATION_ID'), 
    'x-app-key': config('APPLICATION_KEY'),
    'Content-Type': 'application/json'
}

user_query = input("Calculate exercise (I ran 2 km and wight lifting 1 hour and 30 min stretching): \n")
user_gender = input("Enter your gender (eg: female/male):\n")
weight_kg = input("Enter your weight (eg: 92.5):\n")
height_cm = input("Enter your height (eg: 167): \n")
age = input("Enter your age: \n")

payload = {
    "query": user_query,
    "gender": user_gender,
    "weight_kg": float(weight_kg),
    "height_cm": float(height_cm),
    "age": int(age)
}

request = requests.post('https://trackapi.nutritionix.com/v2/natural/exercise', headers=headers, json=payload)

workbook = xlsxwriter.Workbook('exercise_tracking.xlsx')
worksheet = workbook.add_worksheet()
worksheet.write('A1', 'date')
worksheet.write('B1', 'duration')
worksheet.write('C1', 'calories')
worksheet.write('D1', 'met')
worksheet.write('E1', 'exercise')
worksheet.write('E1', 'exercise')
worksheet.write('E1', 'exercise')
worksheet.write('E1', 'exercise')
worksheet.write('E1', 'exercise')

i = 1

for data in request.json()['exercises']:
    i += 1
    worksheet.write(f"A{i}", datetime.now().strftime("%Y%m%d"))
    worksheet.write(f"B{i}", data['duration_min'])
    worksheet.write(f"C{i}", data['nf_calories'])
    worksheet.write(f"D{i}", data['met'])
    worksheet.write(f"E{i}", data['name'])

workbook.close()