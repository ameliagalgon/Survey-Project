import json

def findAverageAge(data):
    sum = 0
    for entry in data:
        sum += int(entry['age'])
    return sum / len(data)

def main():
    file = open("allanswers.json", "r")
    data = json.load(file)
    print("Analyzing data...")
    averageAge = findAverageAge(data)
    print("Average age: %d" %averageAge)

if __name__ == "__main__":
    main()
