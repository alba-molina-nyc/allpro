import csv
import re
from collections import Counter


def parse_data(data):
    company_name = data[0].strip()

    address_line = data[1].strip()
    street_match = re.search(r'^\d+\s+(.*)$', address_line)
    street_address = street_match.group(1) if street_match else ""

    city_state_zip = data[2].strip()
    city_match = re.search(r'(.+),', city_state_zip)
    city = city_match.group(1) if city_match else ""

    state_zip = re.search(r'(\w{2})\s+(\d{5})', city_state_zip)
    state = state_zip.group(1) if state_zip else ""
    zip_code = state_zip.group(2) if state_zip else ""

    phone_match = re.search(r'Phone:\s+([\d-]+)', data[3])
    phone_number = phone_match.group(1) if phone_match else ""

    return [company_name, street_address, city, state, zip_code, phone_number]

# Example usage:
data_sets = [
    [
        "BERMUDA PAINT COMPANY, LTD.",
        "9 WATLINGTON ROAD",
        "DEVONSHIRE DVBX BM DV06",
        "Phone: 441-236-4662"
    ],
    # Add more data sets here
]

parsed_data_list = []
for data_set in data_sets:
    parsed_data = parse_data(data_set)
    parsed_data_list.append(parsed_data)

# Specify the desired CSV file path
csv_file_path = "parsed_data.csv"

# Write the parsed data to the CSV file
with open(csv_file_path, "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Company Name", "Street Address", "City", "State", "Zip Code", "Phone Number"])  # Write header
    writer.writerows(parsed_data_list)  # Write data rows

print(f"Parsed data has been saved to {csv_file_path}.")

company_names = []  # Create an empty list to store company names

company_name_counts = Counter(company_names)


# Print the counts of each company name
for company_name, count in company_name_counts.items():
    print(f"{company_name}: {count} occurrences")

print(f"Parsed data has been saved to {csv_file_path}.")