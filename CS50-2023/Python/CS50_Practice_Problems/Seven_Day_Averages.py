import csv
import requests


def main():
    # Read NYTimes Covid Database
    download = requests.get(
        "https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-states.csv"
    )
    decoded_content = download.content.decode("utf-8")
    file = decoded_content.splitlines()
    reader = csv.DictReader(file)

    # Construct 14 day lists of new cases for each states
    new_cases = calculate(reader)

    # Create a list to store selected states
    states = []
    print("Choose one or more states to view average COVID cases.")
    print("Press enter when done.\n")

    while True:
        state = input("State: ")
        if state in new_cases:
            states.append(state)
        if len(state) == 0:
            break

    print(f"\nSeven-Day Averages")


    # Print out 7-day averages for this week vs last week
    comparative_averages(new_cases, states)


# TODO: Create a dictionary to store 14 most recent days of new cases by state
def calculate(reader):
    new_cases = dict()
    previous_cases = dict()

    for row in reader:
        state = row['state']
        cases = int(row['cases'])

        if state not in previous_cases:
            previous_cases[state] = cases
            new_cases[state] = []
            new_cases[state].append(cases)

        else:
           case_current = previous_cases[state]
           if (cases - previous_cases[state]) > 0:
                previous_cases[state] = cases
                cases = (previous_cases[state] - case_current)
                if len(new_cases[state]) >= 14:
                    new_cases[state].pop(0)
                new_cases[state].append(cases)

    return new_cases


# TODO: Calculate and print out seven day average for given state
def comparative_averages(new_cases, states):


    for state in states:
        recent_cases = round(sum(new_cases[state][7:]))
        last_cases = round(sum(new_cases[state][:7]))
        recent_avg = int(recent_cases/7)
        
        percent = int(((recent_cases - last_cases) / last_cases) * 100)

        if percent > 0:
            msg = 'increase'
        else:
            msg = 'decrease'

        percent = abs(percent)

        print(f"{state} had a 7-day average of {recent_avg} and {msg} of {percent}%")


main()
