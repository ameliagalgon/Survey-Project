import json
surveys = []

questions = ["What is your name? ", "What is your age? "]
keys = ["name", "age"]

answer = "yes"
while answer.lower() == 'yes':
    responses = {}
    for i in range(len(questions)):
        response = input(questions[i])
        responses[keys[i]] = response
    surveys.append(responses)
    print("Thank you for your response!\n")
    answer = input("Would you like to take a survey? ")


# Add all of your old data to your surveys list
file = open("allanswers.json", "r")
olddata = json.load(file)
surveys.extend(olddata)
file.close()



# Write the surveys into the file
# Using a loop to format the file so that a human can read it much more easily
file = open("allanswers.json", "w") #Open the file with write access

file.write('[\n')
index = 0
for survey in surveys:
    if(index < len(surveys) - 1):
        json.dump(survey, file)
        file.write(',\n')
    else:
        json.dump(survey, file)
        file.write('\n')
    index += 1

file.write(']')
file.close()
