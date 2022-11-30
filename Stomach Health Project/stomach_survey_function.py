def stomach_survey():
    farts_in_a_week = {
        'Monday': 'No Data',
        'Tuesday': 'No Data',
        'Wednesday': 'No Data',
        'Thursday': 'No Data',
        'Friday': 'No Data',
        'Saturday': 'No Data',
        'Sunday': 'No Data'
    }
    while True:
        question = input('Do you mind answering the following survey? Please answer with: Yes or No\n').capitalize()
        if question == 'Yes':
            print('Thank you for your time. We appreciate your responses. If at any time you would like to exit, '
                  'please enter Exit.')
            for day in farts_in_a_week:
                while True:
                    try:
                        farts = input(f'How many farts did you have on {day}?\n')
                        exit_test = farts.capitalize()
                        if exit_test == 'Exit':
                            print('Thank you for your time. Exiting.')
                            return farts_in_a_week
                        else:
                            farts_int = int(farts)
                            if farts_int < 0:
                                print('Please enter in a non-negative value or Exit.')
                            else:
                                farts_in_a_week[day] = farts_int
                                break
                    except:
                        print('Please enter a valid value.')
            break
        elif question == 'No':
            print('We understand. Have a nice day!')
            break
        else:
            print("That's not a valid response. Please respond with Yes or No.")
    return farts_in_a_week


class StomachSurvey:
    survey_results = stomach_survey()
