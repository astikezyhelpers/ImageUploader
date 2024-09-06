# import csv
# import re

# def sanitize_filename(name):
#     """Sanitize the hotel and location names by replacing special characters and spaces."""
#     name = re.sub(r'[\\/*?:"<>|,]', "", name)  # Remove invalid characters
#     name = re.sub(r'\s+', "%20", name.strip())  # Replace spaces with %20
#     return name

# def remove_postal_codes(location):
#     """Remove postal codes and numeric values from the location string."""
#     return re.sub(r'\b\d+\b', '', location).strip()

# def extract_location(location):
#     """Extract the city from the full location string (e.g., '20150 Pattaya Central' -> 'Pattaya Central')."""
#     location_without_postal_code = remove_postal_codes(location)
#     location_parts = location_without_postal_code.split(',')
#     if len(location_parts) > 1:
#         return location_parts[-2].strip()
#     return location.strip()

# def generate_urls(hotel_name, location, num_images=6):
#     """Generates URLs for hotel images based on hotel name and extracted city location."""
#     base_url = "https://ik.imagekit.io/tg5wbt4yj/TreboundImages/ThailandImages/"
#     location_sanitized = sanitize_filename(location)
#     hotel_name_sanitized = sanitize_filename(hotel_name)
    
#     # Generate a list of URLs for the specified number of images
#     urls = []
#     for i in range(1, num_images + 1):
#         url = f"{base_url}{location_sanitized}/{hotel_name_sanitized}/image_{i}.jpg"
#         urls.append(url)
#     return urls

# # Open the input CSV file
# with open('hotel_input.csv', 'r', encoding='utf-8') as csvfile:
#     csvreader = csv.DictReader(csvfile)
    
#     # Open the output CSV file to write the results
#     with open('generated_hotel_image_urls.csv', 'w', newline='', encoding='utf-8') as outputfile:
#         csvwriter = csv.writer(outputfile)
        
#         # Write the header row
#         csvwriter.writerow(['HotelName', 'Location', 'ImageURL1', 'ImageURL2', 'ImageURL3', 'ImageURL4', 'ImageURL5', 'ImageURL6'])

#         # Iterate through each row in the input CSV
#         for row in csvreader:
#             hotel_name = row["HotelName"].strip()
#             full_location = row["Location"].strip()

#             # Extract city from the full location and remove postal codes
#             city_location = extract_location(full_location)

#             # Generate URLs for the hotel
#             urls = generate_urls(hotel_name, city_location)

#             # Write the hotel name, location, and generated URLs in separate columns
#             csvwriter.writerow([hotel_name, full_location] + urls)

# print("Generated URLs have been successfully written to generated_hotel_image_urls.csv")


import csv
import re

def sanitize_filename(name):
    """Sanitize the hotel and location names by replacing special characters and spaces, but preserve commas in hotel names."""
    # Preserve commas in hotel names but replace other invalid characters and spaces
    name = re.sub(r'[\\/*?:"<>|]', "", name)  # Remove invalid characters
    name = re.sub(r'\s+', "%20", name.strip())  # Replace spaces with %20
    return name

def remove_postal_codes(location):
    """Remove postal codes and numeric values from the location string."""
    return re.sub(r'\b\d+\b', '', location).strip()

def extract_location(location):
    """Extract the city from the full location string (e.g., '20150 Pattaya Central' -> 'Pattaya Central')."""
    location_without_postal_code = remove_postal_codes(location)
    location_parts = location_without_postal_code.split(',')
    if len(location_parts) > 1:
        return location_parts[-2].strip()
    return location.strip()

def generate_urls(hotel_name, location, num_images=6):
    """Generates URLs for hotel images based on hotel name and extracted city location."""
    base_url = "https://ik.imagekit.io/tg5wbt4yj/TreboundImages/IndonesiaImages/"
    location_sanitized = sanitize_filename(location)
    hotel_name_sanitized = sanitize_filename(hotel_name)
    
    # Generate a list of URLs for the specified number of images
    urls = []
    for i in range(1, num_images + 1):
        url = f"{base_url}{location_sanitized}/{hotel_name_sanitized}/image_{i}.jpg"
        urls.append(url)
    return urls

# Open the input CSV file
with open('hotel_input.csv', 'r', encoding='utf-8') as csvfile:
    csvreader = csv.DictReader(csvfile)
    
    # Open the output CSV file to write the results
    with open('generated_hotel_image_urls.csv', 'w', newline='', encoding='utf-8') as outputfile:
        csvwriter = csv.writer(outputfile)
        
        # Write the header row
        csvwriter.writerow(['HotelName', 'Location', 'ImageURL1', 'ImageURL2', 'ImageURL3', 'ImageURL4', 'ImageURL5', 'ImageURL6'])

        # Iterate through each row in the input CSV
        for row in csvreader:
            hotel_name = row["HotelName"].strip()
            full_location = row["Location"].strip()

            # Extract city from the full location and remove postal codes
            city_location = extract_location(full_location)

            # Generate URLs for the hotel
            urls = generate_urls(hotel_name, city_location)

            # Write the hotel name, location, and generated URLs in separate columns
            csvwriter.writerow([hotel_name, full_location] + urls)

print("Generated URLs have been successfully written to generated_hotel_image_urls.csv")
