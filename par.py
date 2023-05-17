import csv

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
