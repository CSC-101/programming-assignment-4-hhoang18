import county_demographics
import sys
import build_data

full_data = build_data.get_data()

#def main():
 #   file = "input"/+sys.argv

def data_set():
    global data
    data = []
    try:
        data_file = open('county_demographics.data', 'r')
        for line in data_file:
            data.append(line.strip())
            return data
        print(f"Number of data entries: {len(data)}") #return number of data entries
    except FileNotFoundError:
        print("Error: file not found.")
        sys.exit(1)
#this function loads the full demographics data set and prints the number of entries
#the input is the county_demographics data file
#the output is an error message or a string that prints the number of entries
#the function takes in a data file and returns a string

def display():
    for county in data:
        print(f"{county['County']}, {county['State']}")
        print(f"  Population: {county['Population_2014']}")
        print("Education:")
        print(f"  >= High School: {county['Education.High School or Higher']}%")
        print(f"  >= Bachelor's Degree: {county['Education.Bachelors Degree or Higher']}%")
        print("Ethnicities:")
        print(f"  American Indian and Alaska Native: {county['Ethnicities.American Indian and Alaska Native Alone']}%")
        print(f"  Asian Alone: {county['Ethnicities.Asian Alone']}%")
        print(f"  Black Alone: {county['Ethnicities.Black Alone']}%")
        print(f"  Hispanic or Latino: {county['Ethnicities.Hispanic or Latino']}%")
        print(f"  Native Hawaiian and Other Pacific Islander Alone: "
              f"{county['Ethnicities.Native Hawaiian and Other Pacific Islander Alone']}%")
        print(f"  Two or More Races: {county['Ethnicities.Two or More Races']}%")
        print(f"  White Alone: {county['Ethnicities.White Alone']}%")
        print(f"  White Alone, not Hispanic or Latino: {county['Ethnicities.White Alone, not Hispanic or Latino']}%")
        print("Income:")
        print(f"  Below Poverty Level: {county['Income.Persons Below Poverty Level']}%")
#this function prints the county information for each county to the terminal
#the function uses the data from county_demographics
#the output is county information
#data is a txt file, and strings are returned

def filter_state(state):
    global data #state is the state abbreviation
    data = [input for input in data if input['State']==state]
    print(f"Filter: state == {state} ({len(data)} entries)")
#the function reduces the collection of counties to those with the matching state abbreviation
#if no county's state matches the abbreviation, the resulting collection will be empty
#the input is the county demographics data
#the output is the collection of counties that have the matching state abbreviation
#state is a data file and a string is returned

def filter_gt(field, number):
    global data
    data = [input for input in data if float(input[field] > number)]
    print(f"Filter: {field} gt {number} ({len(data)} entries)")
#the function's purpose is to reduce the collection of entries to those where the value in the specified field is
#greater than the specified number
#the inputs are a specified field and number
#the output is the collection of entries where the value in the specified field is greater than the specified number
#float
#a string is returned

def filter_lt(field, number):
    global data
    data = [input for input in data if float(input[field]) < number]
    print(f"Filter: {field} lt {number} ({len(data)} entries)")
#the function's purpose is to reduce to collection of entries to those where the value in the specified field is less
#than the specified number
#the inputs are a specified field and number
#the output is a collection of entries where the value in the specified field is less than the specified number
#the number is a float value
#a string is returned

def population_total():
    total = sum(float(input['2014 Population']) for input in data)
    print(f"2014 population: {total}")
#the function's purpose is to print the total 2014 population across all counties
#the input is 2014 populations
#the output is the total 2014 population across all counties
#the function uses float and returns a string

def population(field):
    total = sum(float(input[field])*float(input['2014 Population'])/100 for input in data)
    print(f"2014 {field} population: {total}")
#the function's purpose is to compute the 2014 subpopulation across all counties
#the input is 2014 populations
#the output is the total 2014 population
#a float value is used for the populations
#a string is returned

def percent(field):
    total_population = sum(float(input['2014 Population']) for input in data)
    field_population = sum(float(input[field])*float(input['2014 Population'])/100 for input in data)
    percentage = (field_population / total_population)*100
    print(f"2014 {field} percentage: {percentage}")
#the function's purpose is to print the percentage of the total population within the subpopulation as specified by
#a field
#the input is a float (population)
#the output is the percentage of the total population within the subpopulation
#the function uses float and returns a string

def error_handling():
    filename = 'county_demographics.data'
    try:
        with open(filename,'r') as file:
            lines = file.readlines()
            line_num = 1
            for line in lines:
                if not line:
                    line_num += 1
                    continue #skip the empty lines
                try:
                    section = line.split(':')
                    op = section[0]
                    if op == 'display':
                        display()
                    elif op == 'filter_state':
                        if len(section) == 2:
                            filter_state()
                        elif len(section) != 2:
                            raise ValueError("Malformed line.")
                    elif op == 'filter_gt':
                        if len(section) == 3:
                            filter_gt()
                        elif len(section) != 3:
                            raise ValueError("Malformed line.")
                    elif op == 'filter_lt':
                        if len(section) == 3:
                            filter_lt()
                        elif len(section) != 3:
                            raise ValueError("Malformed line.")
                    elif op == "population_total":
                        population_total()
                    elif op == "population":
                        if len(section) == 2:
                            population()
                        elif len(section) != 2:
                            raise ValueError("Malformed line.")
                    elif op == "percent":
                        if len(section) == 2:
                            percent()
                        elif len(section) != 2:
                            raise ValueError("Malformed line.")
                    else:
                        print(f"Error in line {line_num}")
                except ValueError:
                    print("Error: this line has a value that could not be converted.")
    except FileNotFoundError:
        print("Error: the file cannot be found.")
        sys.exit(1)
#this function is used for error handling e.g. a file cannot be opened or a value can't be converted
#the input is a file with county demographic data
#the output is a string stating an error
#the function uses a file and returns type string

def main():
    data_set()
    error_handling()

if __name__ == "__main__":
    main()





