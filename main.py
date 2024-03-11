import csv


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    with open("city-of-seattle-2012-expenditures-dollars.csv") as csvfile:
        reader = csv.reader(csvfile)

        dictionary = {}
        for row in reader:
            try:
                if row[0] not in dictionary.keys() and row[0] != "Department" and row[0] != "":
                    dictionary[row[0]] = 0

                if row[0] in dictionary.keys() and row[3] != "null":
                    dictionary[row[0]] = dictionary[row[0]] + int(row[3])
            except ValueError:
                continue

    padding = '.' * 20
    for key in dictionary.keys():
        value = "$" + str(dictionary[key]) + ".00"
        print("{:.10} {:^}".format(key + padding, value))




