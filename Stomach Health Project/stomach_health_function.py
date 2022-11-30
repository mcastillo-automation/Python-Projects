from stomach_survey_function import StomachSurvey

for day, farts in StomachSurvey.survey_results.items():
    if farts == 'No Data':
        print(f'No data for {day}')
    elif farts > 5:
        print(f'You ate too poorly on {day}. You farted {farts} times!')
    else:
        print(f'You did well on {day}')
print("In a week, we're going to follow up and see how you're doing")
