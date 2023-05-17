import csv
from collections import Counter

# Open the "allpro" file in read mode
with open('allpro', 'r') as file:
    # Read the content of the file
    content = file.read()

    # Split the content into individual entries
    entries = content.split('\n\n')

    # Create a new CSV file to write the parsed data
    with open('parsed_data.csv', 'w', newline='') as output_file:
        # Create a CSV writer object
        csv_writer = csv.writer(output_file)

        # Write the header row to the CSV file
        csv_writer.writerow(['Company', 'Address', 'City', 'State', 'Zip Code', 'Phone'])

        # Create a list to store occurrences with the same name that occur only once or twice
        occurrences_once_twice = []

        # Create a Counter to keep track of occurrences of each company
        company_counter = Counter()

        # Iterate over each entry
        for entry in entries:
            # Split the entry into lines
            lines = entry.split('\n')

            # Extract the relevant data from the entry
            if len(lines) >= 3:
                company = lines[0].strip()
                address = lines[1].strip()
                city_state_zip = lines[2].strip()
                phone = lines[-1].replace('Phone:', '').strip()

                # Split the city, state, and zip code
                city, state_zip = city_state_zip.rsplit(' ', 1)
                state, zipcode = state_zip[:2], state_zip[2:]

                # Write the parsed data to the CSV file
                csv_writer.writerow([company, address, city, state, zipcode, phone])

                # Increment the count for the company
                company_counter[company] += 1

        # Find occurrences that occur only once or twice
        for company, count in company_counter.items():
            if count <=2:
                occurrences_once_twice.append(company)

    # Create a CSV file to write the occurrences that occur only once or twice
    with open('one-and-two-allpro-loc.csv', 'w', newline='') as occurrences_file:
        # Create a CSV writer object for the occurrences file
        csv_writer_occurrences = csv.writer(occurrences_file)

        # Write the header row to the occurrences file
        csv_writer_occurrences.writerow(['Company', 'Address', 'City', 'State', 'Zip Code', 'Phone'])

        # Write the occurrences to the occurrences file
        for entry in entries:
            # Split the entry into lines
            lines = entry.split('\n')

            # Extract the relevant data from the entry
            if len(lines) >= 3:
                company = lines[0].strip()
                address = lines[1].strip()
                city_state_zip = lines[2].strip()
                phone = lines[-1].replace('Phone:', '').strip()

                # Split the city, state, and zip code
                city, state_zip = city_state_zip.rsplit(' ', 1)
                state, zipcode = state_zip[:2], state_zip[2:]

                # Check if the company occurs only once or twice
                if company in occurrences_once_twice:
                    # Write the occurrence to the occurrences file
                    csv_writer_occurrences.writerow([company, address, city, state, zipcode, phone])
