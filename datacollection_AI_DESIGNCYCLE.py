import csv

# Define the data fields
fields = ['Name', 'Age', 'Favorite_Color']

# Data collection (simulated user input)
data = []
for i in range(3):
    print(f"\nCollecting data for user {i+1}")
    name = input("Enter your name: ")
    age = input("Enter your age: ")
    color = input("Enter your favorite color: ")
    data.append([name, age, color])

# Save data to a CSV file
filename = 'D:\PUNIT_NAMDEO\collected_data.csv'
with open(filename, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(fields)
    writer.writerows(data)

print(f"\nData successfully saved to {filename}")
