import csv

# Input and output file names
input_file = "/home/sushant-kumar/IIITH/2-2/PRECOG_RECRUITMENT/world-city-listing-table.csv"
output_file = "cities.txt"

# Read the input file and extract cities
cities = []
with open(input_file, mode="r", newline="", encoding="utf-8") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        if len(cities) < 500:
            cities.append(row["city"])
        else:
            break

# Write the city names to a text file
with open(output_file, mode="w", encoding="utf-8") as txtfile:
    for city in cities:
        txtfile.write(city + "\n")

print(f"Extracted the first 500 cities into {output_file}.")
