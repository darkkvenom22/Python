# Write a program to read a csv file, read set of data, push the data to dict and then use the dict to print the data

# input csv file - Hermoine, Griffyndor
# dict values - { "name" : "Hermoine", "house" : "Griffyndor" }
# Printing output - Hermoine is in house Griffyndor

csv_file = "names.csv"

def main() :
    students = read_csv(csv_file)
    print_output(students)
    print_output_using_lambda(students)

def read_csv(csv_file) :
    students = []

    with open(csv_file) as file :
        for line in file :
            name, house = line.split(",")
            student = {"name" : name.strip(), "house" : house.strip()}
            students.append(student)
            #students.append({"name" : name.strip(), "house" : house.strip()})
    
    print(students)
    return students


# Sort on list of dict
# sorted(<list of dict>, key=<funct that returns the values of all the keys>, reverse=<True or False>)

# Write a fun to get the values of the keys
def get_value(student) :
    return student["house"]


def print_output(n) :
    for i in sorted(n, key=get_value, reverse = True) : # get the values of all the keys for each dict in the list
        print(f'{i["name"]} is in {i["house"]}')


# Using lambda functions

def print_output_using_lambda(n) :
    for i in sorted(n, key=lambda student: student["name"], reverse = True) :
        print(f"{i['name']} runs in {i['house']}")


if __name__ == "__main__" :
    main()