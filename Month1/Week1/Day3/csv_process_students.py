# import csv
# # Open the input CSV for reading
# with open('student.csv', mode='r') as infile:
#     reader = csv.DictReader(infile)
#     # Prepare to write to output CSV
#     with open('output.csv', mode='w', newline='') as outfile:
#         writer = csv.writer(outfile)
#         # Write header for output
#         writer.writerow(['Name', 'Average'])
#         # Process each row
#         for row in reader:
#             # Calculate average of Maths, Science, English
#             avg = (float(row['Maths']) +
#                    float(row['Science']) + float(row['English'])) / 3
#             writer.writerow([row['Name'], avg])


import csv
with open("students.csv", mode='r') as infile:
    reader = csv.DictReader(infile)
    with open("output.csv", mode="w", newline='') as outfile:
        writer = csv.writer(outfile)
        writer.writerow(['Name', 'Average'])
        for row in reader:
            avg = (float(row['Maths']) +
                   float(row['Science']) + float(row['English'])) / 3
            writer.writerow([row['Name'], avg] )
        print(f" output written to output.csv")

Name,Average
Alice,85.0
Bob,68.33333333333333
Charlie,93.33333333333333

Name,Maths,Science,English
Alice,80,90,85
Bob,70,60,75
Charlie,95,85,100
