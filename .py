import re

def parse_data(data):
    company_name_match = re.search(r'^([^-\n]+)', data)
    company_name = company_name_match.group(1).strip() if company_name_match else ""

    address_line = data.split("\n")[1].strip()
    street_match = re.search(r'^\d+\s+(.*)$', address_line)
    street_address = street_match.group(1).strip() if street_match else ""

    city_state_zip = data.split("\n")[2].strip()
    city_match = re.search(r'([^,]+),', city_state_zip)
    city = city_match.group(1).strip() if city_match else ""
    state_zip = re.search(r'(\w{2})\s+(\d{5})', city_state_zip)
    state = state_zip.group(1) if state_zip else ""
    zip_code = state_zip.group(2) if state_zip else ""

    phone_match = re.search(r'Phone:\s+([\d-]+)', data)
    phone_number = phone_match.group(1) if phone_match else ""

    parsed_data = {
        "Company Name": company_name,
        "Street Address": street_address,
        "City": city,
        "State": state,
        "Zip Code": zip_code,
        "Phone Number": phone_number
    }

    return parsed_data

# Example usage:
data_set = """
BERMUDA PAINT COMPANY, LTD.
9 WATLINGTON ROAD
DEVONSHIRE DVBX BM DV06
Phone: 441-236-4662
"""

parsed_data = parse_data(data_set)
print(parsed_data)
