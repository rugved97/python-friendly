import csv


def average(array):
    sum = 0
    if not array:
        return
    for val in array:
        sum += val
    return sum / len(array)


# with open('nyc_weather.csv') as csv_file:
#     csvreader = csv.reader(csv_file, delimiter=',')
#     values = []
#     line_count = 0
#     for row in csvreader:
#         if line_count == 0:
#             print(row)
#             line_count += 1
#         else:
#             values.append(int(row[1]))
#
#     print(average(values[0:7]))
#     print(max(values))


with open("nyc_weather.csv", "r") as f:
    weather = {}
    for line in f:
        tokens = line.split(',')
        try:
            key = tokens[0]
            value = int(tokens[1])
            weather[key] = value
        except:
            print("Invalid temperature.Ignore the row")

    print(weather['Jan 9'])
    print(weather['Jan 4'])

# The operators 'in' and 'not in' test for membership. x in s evaluates to True if x is a member of s,
# in tests for the existence of a key in a dict:
with open('poem.txt') as file:
    word_dict = {}
    for line in file:
        tokens = line.split(' ')
        for word in tokens:
            if word in word_dict:
                word_dict[word] += 1
            else:
                word_dict[word] = 1

    print(word_dict)
